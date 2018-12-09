import json
import boto3

def lambda_handler(event, context):
    lex = boto3.client('lex-runtime')
    response = lex.post_text(
    botName='searchImage',
    botAlias="searchImageBot",
    userId="dhruv",
    inputText="Show me dog and cat"
    )
    return "Hi"
