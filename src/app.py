import json

def donate(event, _):
    http_response = {
        "statusCode": 200,
        "body": json.dumps({"result":"success!"})
    }
    return http_response