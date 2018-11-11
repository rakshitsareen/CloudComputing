import boto3

#table_name, details
def insert_into_table(suggestion, message, request_number):
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')

    table = dynamodb.Table('diningBotSuggestions')

    title = "The Big New Movie"
    year = 2015

    response = table.put_item(
        Item={
            'requestid': request_number,
            'suggestions': suggestion,
            'sqsMessage': message,
            "status": "fulfillied"
        }
    )
    
    # resp2 = table.get_item(
    #     Key={
    #         'request_number': 2
    #     })
    
    print("Item added! Response is"+str(response))
    #print("Get  is"+str(resp2))
    