import boto3

def lambda_handler(event, context):
    client = boto3.client('ssm')
    
    response = client.start_automation_execution(
        DocumentName="ssm_automation",
        Parameters={"InstanceId": ["i-xxxxxxxxxxxxxxxx"]}
    )

    return response
