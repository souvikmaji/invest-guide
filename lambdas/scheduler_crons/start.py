import logging
import boto3
from util import isTodayWorkingDay, createSuccessResponse

region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):
    if isTodayWorkingDay():
        return createSuccessResponse("holiday")
        
    stopped = getStoppedInstances()
    if len(stopped) > 0:
        i = ec2.start_instances(InstanceIds=stopped)
        return createSuccessResponse('started your instances: ' + str(i))
    else:
        return createSuccessResponse('already running')

def getStoppedInstances():
    stopped = []
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
               'shutting-down', 'terminated', 'stopping', 'stopped'
            ],
        }
    ])
    
    for instance in response['InstanceStatuses']:
            stopped.append(instance['InstanceId'])
    
    return stopped