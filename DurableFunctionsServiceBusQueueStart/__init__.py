import logging

import azure.functions as func
import azure.durable_functions as df

async def main(msg: func.ServiceBusMessage, starter: str):
    messageText = msg.get_body().decode('utf-8')
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 messageText)

    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("OptimizationOrchestrator", None, messageText)

    logging.info(f"Started orchestration with ID = '{instance_id}'.")