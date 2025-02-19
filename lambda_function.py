import boto3

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    response = ssm.start_automation_execution(
        DocumentName='ssm-automation-document',
        Parameters={
            'SourceAmiId': ['ami-12345678'],
            'InstanceType': ['t2.micro']
        }
    )
    return response
