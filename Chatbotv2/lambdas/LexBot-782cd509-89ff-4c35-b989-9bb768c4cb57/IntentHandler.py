import json
import boto3
import re
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def intent_handler(event, intentName):
    area_list = ["Brooklyn","Manhattan","Queens"]
    content=None
    contentError=None
    slot_error=None
    
    
    if intentName == "GreetIntent":
        logger.info("In the greeting Intent")
        print("This is Done " + intentName)
        content ="Hi! How Can I help you?"
        response = {
            "dialogAction": {
                "type": "ElicitIntent",
                "message": {
                    "contentType": "PlainText",
                    "content": content
                }
            }
        }
        return response

    elif intentName == "ThankYouIntent":
        logger.info("In the Thank you Intent")
        content="You are welcome!"
        response = {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState":"Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": content
                }
            }
        }
    


    elif intentName == "DiningSuggestionIntent":
        dinning = event['currentIntent']['slots']['dinning']
        area = event['currentIntent']['slots']['area']
        phone = event['currentIntent']['slots']['phone']
        cuisine = event['currentIntent']['slots']['cuisine']
        people = event['currentIntent']['slots']['people']
        time = event['currentIntent']['slots']['time']
        date = event['currentIntent']['slots']['date']
        #All the Slots
        
        
        
        if area!= None:
            logger.info("Area is "+area)
            contentError= area_validator(area,area_list)
            slot_error="area"
            logger.info("The content Error"+str(contentError))
        if phone!=None:
            contentError= number_validator(phone)
            logger.info("Previous phone "+str(phone))
            if contentError == None:
                if len(phone) == 11:
                    logger.info("The number is of 11:"+ phone)
                    phone = "+" + phone
                elif "+1" not in phone:
                    phone = "+1" + phone
            logger.info("updated phone :"+str(phone))
            slot_error="phone"
        
        if contentError!=None:
            
            if slot_error == "area":
                area = None
            elif slot_error == "phone":
                phone = None
            response = {
                    "sessionAttributes": { 
                            "dinning":dinning,
                            "area":area,
                            "phone":phone,
                            "cuisine":cuisine,
                            "people":people,
                            "time":time,
                            "date":date,
                            "errorMessage":contentError
                            },
                    "dialogAction": {
                        "type": "ElicitSlot",
                        "message":{
                            "contentType":"PlainText",
                            "content":contentError
                        },
                        "intentName":intentName,
                        "slotToElicit":slot_error,
                        "slots": {
                            "dinning":dinning,
                            "area":area,
                            "phone":phone,
                            "cuisine":cuisine,
                            "people":people,
                            "time":time,
                            "date":date
                            
                            }
                        
                    }
                }
        else:
            response = {
                        "sessionAttributes": { 
                                "dinning":dinning,
                                "area":area,
                                "phone":phone,
                                "cuisine":cuisine,
                                "people":people,
                                "time":time,
                                "date":date,
                                "errorMessage":""
                                },
                        "dialogAction": {
                            "type": "Delegate",
                            "slots": {
                                "dinning":dinning,
                                "area":area,
                                "phone":phone,
                                "cuisine":cuisine,
                                "people":people,
                                "time":time,
                                "date":date
                                
                                }
                            
                        }
                    }
                
    logger.info("Returning the response"+str(response))

    return response


def area_validator(area,area_list):
    if area in area_list:
        
        logger.info("Okay! Finding in "+area+" ! Which type of Cuisine would you like to have?")
    else:
        slot_error="area"
        return "Please choose area from the following list \n"+str(area_list)


def number_validator(phone):
    
    prog = re.compile("^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$")

    if prog.match(phone):
        logger.info("Phone is validated! ")
        #return "Okay! Your number " + phone + " is stored!"
    
    else:
        slot_error="phone"
        logger.info("Phone is not validated")
        return "Please enter a Valid Phone Number e.g. +12345688967"
        


