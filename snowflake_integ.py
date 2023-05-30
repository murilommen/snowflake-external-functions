import json
import pandas as pd
import whylogs as why


def lambda_handler(event, context):
    statusCode = 200
    snowflake_json_string = ''
    
    try:
        body = json.loads(event['body'])
        data = body['data']
        
        data_to_profile = pd.DataFrame(data, columns = ["data_index", "x", "y"])
        data_to_profile.set_index("data_index")
        result_set = why.log(data_to_profile)
            
        serialized_profile = result_set.view().serialize()
        
        profile_to_return = { 'data': serialized_profile }
        snowflake_json_string = json.dumps(profile_to_return)
        
    except Exception as e:
        statusCode = 400
        snowflake_json_string = json.dumps({'data': f'Error with exception: {str(e)}'})
    
    
    return {
        'statusCode': statusCode,
        'headers': {'Content-Type': 'application/json'},
        'body': snowflake_json_string
    }
