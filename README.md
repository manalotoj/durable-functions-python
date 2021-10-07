# durable-functions-python
Simple scaffolding for a durable functions orchestration using Python.

## Why Durable Functions?
DF provides an easy way to chain function calls (as well as other patterns) without having to wire intermediate queues. Since it is stateful, it will provide automatic retry of failed execution.

## Key Components
To follow are the key compoents.

### Starter Functions
Orchestrator functions cannot be invoked directly. They are invoked via regular azure functions using a trigger of choice:
- Http Trigger: DurableFunctionsHttpStart
- Service Bus Queue Trigger: durableFunctionsServiceBusQueueStart

### OptmizationOrchestrator
An example DF *Orchestrator function* that can chain DF *Activity function* calls. An Orchestrator function has a corresponding context that can be used to pass parameters via its input object. The orchestrator is used to implement a sequential process as a chain of activity functions. Azure functions running in a consumption plan have a maximum execition time of 10 minutes making decomposition into multiple activity functions advantageous for long running processes.

### Activity Functions
PrepareData, Optimize, and PersistOutput are example *Activity Functions*.
