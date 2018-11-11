import json
import boto3
import dynamo_handler
import yelp_handler
import sqs_handler
import sns_handler



def lambda_handler(event, context):
    api_key="-5dBnE7ZnbVw1RshcBve1t-Ayg00nnw4PEMj-in726bQM4jODmHTgdUKIEQXzKKgq4hrainJdwniItyA5tZOFg71e9yrEDuqa-tDoxlPpxxzFtQ20Jlr6AcSXRDlW3Yx"
    queue_url = 'https://sqs.us-east-1.amazonaws.com/459331344268/SQS_Queue'
    slot_list,message_list = sqs_handler.message_handle(queue_url)
    if slot_list == "False":
        print("The Queue is Empty")
        return "Queue is Empty"
    print("The slot list is "+str(slot_list))
    
    suggestions = []
    count = 0
    for element in slot_list:
        print("The element is "+str(element))
        suggestions = yelp_handler.get_info_yelp(element, api_key)
        request_number = str(element['phone']) +"/" +str(element['date']) +"/" +str(element['time']) 
        print("The element is "+str(element) + "and request_number: "+str(request_number))
        
        #Insert in to Dynamo DB
        dynamo_handler.insert_into_table(suggestions, message_list[count], request_number)
        
        # # #Send SNS with Suggestions
        phone_number = str(element['phone'])
        restaurant_suggestions = []
        for i in suggestions:
            restaurant_suggestions.append(i['restaurant_name'])
            
        sns_handler.send_message(phone_number,restaurant_suggestions)
        
        
    
        
    
    
    return "Hello"

