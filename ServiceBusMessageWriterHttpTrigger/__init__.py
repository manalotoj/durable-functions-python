import logging
import json
from os import environ
import azure.functions as func

from opencensus.extension.azure.functions import OpenCensusExtension
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger('opencensus')
if (logger.hasHandlers()):
    logger.handlers.clear()
    
logger.addHandler(
    AzureLogHandler(
        connection_string=f'InstrumentationKey={environ["APPINSIGHTS_INSTRUMENTATIONKEY"]}')
    )

OpenCensusExtension.configure()

def main(req: func.HttpRequest, msg: func.Out[str], context: func.Context) -> func.HttpResponse:

    
    
    logger.info("message received")
    input_msg = req.get_json()


    msg.set(json.dumps(input_msg))

    properties = {
        'custom_dimensions': {
            'caseId': input_msg['caseId'],
            'key_2': 'value_2'
        }
    }
    logger.warning("spot", extra=properties)

    return 'OK'
