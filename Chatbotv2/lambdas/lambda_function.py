import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    cognito = boto3.client('cognito-idp')
    access_token = event["access_token"]
    resp = cognito.get_user(
    AccessToken=access_token
    )
    print("The cog "+str(resp))
   
    
    userattr = resp['UserAttributes']
    email = ''
    for val in userattr:
        if val['Name'] == 'email':
            email = val['Value']
    
    print('The Cog email == ' + email)
    email = email.replace('@','_')
    lex = boto3.client('lex-runtime')
    response = lex.post_text(
    botName='OrderFood',
    botAlias='assignment_two',
    userId=email,
    inputText=event["Message"]
    )
    
    #print("The userId sending "+str(userId))
    print("The response from lex is "+str(response))
    print("The request is "+str(event))
    
    return response['message']
