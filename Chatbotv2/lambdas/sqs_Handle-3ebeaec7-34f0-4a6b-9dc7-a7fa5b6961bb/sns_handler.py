import logging
import boto3

# Initialize logger and set log level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SNS client for Ireland region
session = boto3.Session(
    region_name="us-east-1"
)
sns_client = session.client('sns')

def send_message(phonenumber, suggestions):
    # suggestions = ["Chipotle","MCD","x1","x2","x3"] #Separate these and add it to Message.
    result = " "
    for s in suggestions:
        result = result + "\n " + s
    message = "Here are your Top 5 Suggestions : " + result
    
    print (message)
    
    response = sns_client.publish(
        Message = message,
        PhoneNumber =  phonenumber, 
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': 'DHRUV'
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Promotional'
            }
        },
        
    )
    
    logger.info(response)
    return 'OK'