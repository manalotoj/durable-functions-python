import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
  
    logging.info(req.get_json())
    input_msg = req.get_json()

    msg.set(json.dumps(input_msg))

    return 'OK'
