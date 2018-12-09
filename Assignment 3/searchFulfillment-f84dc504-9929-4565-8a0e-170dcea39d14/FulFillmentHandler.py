import requests
import json

def fulfillment_handler(event, context):
    print("Recieved Request"+str(event))
    currentIntent = event['currentIntent']['name']
    invocationSource = event['invocationSource']
    
    if invocationSource == "FulfillmentCodeHook":
        print("In the FulfillmentCodeHook stage")
        
        key1 = event['currentIntent']['slots']['queryone']
        key2 = event['currentIntent']['slots']['querytwo']
        
        if key1 == None:
            querytext = "Key2="+key2
        elif key2 == None:
            querytext = "Key1="+key1
        else:
            querytext = "Key1="+key1+"&"+"Key2="+key2
            
       
        API_ENDPOINT="https://vxp5rjw27b.execute-api.us-east-1.amazonaws.com/dev/search?"+querytext
        r = requests.get(url = API_ENDPOINT)
        
        byte_json = r.content
        
        json_string = byte_json.decode('utf8').replace("'", '"')
        json_object = json.loads(json_string)
       
        responseArray = []
        for i in json_object["Results"]:
            j = json.loads(i)
            json_object = {}
            json_object['imageUrl'] = "https://s3.amazonaws.com/" + j["bucket"] + "/" + j["key"]
            responseArray.append(json_object)
            
        print (responseArray)
        
        response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState":"Fulfilled",
            "message": {
                    "contentType": "PlainText",
                    "content": "Here are your results .. "
                },
            "responseCard": {
                "version": "2",
                "contentType": "application/vnd.amazonaws.card.generic",
                "genericAttachments": responseArray
            }
        }
    }
            
            
       
    return response