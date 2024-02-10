from datetime import datetime

def handler(event, context):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        'statusCode': 200,
        'body': f'A hora atual é: {current_time}'
    }