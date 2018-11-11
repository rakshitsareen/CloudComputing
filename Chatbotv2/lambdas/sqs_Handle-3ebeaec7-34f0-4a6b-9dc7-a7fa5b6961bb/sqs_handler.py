import boto3




def message_handle(queue_url):
# Create SQS client

    sqs = boto3.client('sqs')

    

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=10,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )
    
    print("Response from SQS Handler"+str(response))
    if 'Messages' not in response:
        return "False","False"
    
    print("Response from SQS Handler"+str(response))
    messages = response['Messages'] #Array of Messages
    
    hmap = {}
    rhandle = {}
    message_list = []
    
    for i in range(len(messages)):
        print("the i is "+str(i)+"the range is "+str(range))
        id = messages[i]['MessageId']
        hmap[id] = messages[i]['MessageAttributes']
        print("The STRUCT")
        rhandle[id] = messages[i]['ReceiptHandle'] # collecting all reciept handles, so as to delete later
        message_list.append(messages[i])
        
    counter = 0
    output = []
    for k,v in hmap.items():
        details = {}
        dinning = v['dinning']['StringValue']
        details['dining'] = v['dinning']['StringValue']
        area = v['area']['StringValue']
        details['area'] = area
        phone = v['phone']['StringValue']
        details['phone'] = phone
        cuisine = v['cuisine']['StringValue']
        details['cuisine'] = cuisine
        people = v['people']['StringValue']
        details['people'] = people
        time = v['time']['StringValue']
        details['time'] = time
        date = v['date']['StringValue']
        details['date'] = date
        output.append(details)
        print("the output from sqs "+ str(output))
        print("And the details for 1 mess"+str(details))
        
        
    
    
    for k,v in rhandle.items():
        # Delete received messages from queue
        print(v)
        res_del = sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=v
        )
        print('Received and deleted message handle: %s' %v)

    return output,message_list