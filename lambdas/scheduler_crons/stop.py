import boto3
import json
import logging

region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, context):
    i = ec2.stop_instances(InstanceIds=getRunningInstances())
    res = 'stopped your instances: ' + str(i)
    
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }

def getRunningInstances():
    running = []
    response = ec2.describe_instance_status(Filters=[
        {
            'Name': 'tag:trading',
            'Values': [
                'live',
            ],
        },
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ],
        }
    ],)
    for instance in response['InstanceStatuses']:
            running.append(instance['InstanceId'])
    
    return running