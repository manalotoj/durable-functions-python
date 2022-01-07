import logging
import json
from opencensus.extension.azure.functions import OpenCensusExtension
from opencensus.trace import config_integration

config_integration.trace_integrations(['requests'])
OpenCensusExtension.configure()

def get_case_id_from_json_string(message):
    json_object = json.loads(message)
    case_id = json_object['caseId']
    return case_id

def get_case_id_from_object(message):
    case_id = message['caseId']
    return case_id

def log_info(message, event_id, description):
    logging.info()