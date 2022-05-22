import boto3
import logging
from util import isTodayWorkingDay, createSuccessResponse


region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, context):
    if isTodayWorkingDay():
        return createSuccessResponse("holiday")

    i = ec2.stop_instances(InstanceIds=getRunningInstances())
    return createSuccessResponse('stopped your instances: ' + str(i))

def getRunningInstances():
    running = []
    response = ec2.describe_instances(Filters=[
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