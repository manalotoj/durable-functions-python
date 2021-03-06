# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):    
    rawInput = context.get_input()
    logging.info(f"orchestrator input data: {rawInput}")

    try:
        case_id = get_case_id(rawInput)        
        loInput = yield context.call_activity('PrepareData', rawInput)
        output = yield context.call_activity('Optimize', loInput)
        yield context.call_activity('PersistOutput', output)

        # delete service bus message here
        
        return [output]
    except Exception as _:
            return "something bad happened"
main = df.Orchestrator.create(orchestrator_function)

def get_case_id(json_string):
    json_object = json.loads(json_string)
    case_id = json_object['caseId']
    return case_id