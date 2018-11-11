import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def push_to_sqs(event):
    dinning = event['currentIntent']['slots']['dinning']
    area = event['currentIntent']['slots']['area']
    phone = event['currentIntent']['slots']['phone']
    cuisine = event['currentIntent']['slots']['cuisine']
    people = event['currentIntent']['slots']['people']
    time = event['currentIntent']['slots']['time']
    date = event['currentIntent']['slots']['date']
    
    sqs = boto3.client('sqs')

    queue_url = 'https://sqs.us-east-1.amazonaws.com/459331344268/SQS_Queue'
    
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=0,
        MessageAttributes={
            'dinning': {
                'DataType': 'String',
                'StringValue': dinning
            },
            'area': {
                'DataType': 'String',
                'StringValue': area
            },
            'phone': {
                'DataType': 'String',
                'StringValue': phone
            },
            'cuisine': {
                'DataType': 'String',
                'StringValue': cuisine
            },
            'people': {
                'DataType': 'String',
                'StringValue': people
            },
            'time': {
                'DataType': 'String',
                'StringValue': time
            },
            'date': {
                'DataType': 'String',
                'StringValue': date
            }
        },
        MessageBody=(
            'DHRUV ARORA IS HERE! Values about the user!'
        )
    )
    logger.info("SQS sent! "+str(response))

    return True