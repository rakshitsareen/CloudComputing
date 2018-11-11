import boto3
import json

import IntentHandler
import FulfillmentHandler

def request_handler(event, context):
    print("Recieved Request"+str(event))
    currentIntent = event['currentIntent']['name']
    invocationSource = event['invocationSource']
    if invocationSource == "DialogCodeHook":
        response = IntentHandler.intent_handler(event, currentIntent)
    elif invocationSource == "FulfillmentCodeHook":
        print("In the FulfillmentCodeHook stage")
        status = FulfillmentHandler.push_to_sqs(event)
        
        response = {
            "dialogAction": {
                "type": "ElicitIntent",
                "message": {
                    "contentType": "PlainText",
                    "content": "You’re all set. Expect my recommendations shortly! Have a good day."
                }
            }
        }
    
    return response
