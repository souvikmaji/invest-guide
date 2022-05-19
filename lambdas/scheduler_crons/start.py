import datetime
import logging
import json
import boto3
from datetime import date
from nsepy.live import isworkingday

region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))
    if isworkingday(date.today()) == False:
        return createSuccessResponse("holiday")
        
    stopped = getStoppedInstances()
    if len(stopped) > 0:
        i = ec2.start_instances(InstanceIds=stopped)
        return createSuccessResponse('started your instances: ' + str(i))
    else:
        return createSuccessResponse('already running')

def getStoppedInstances():
    stopped = []
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
               'shutting-down', 'terminated', 'stopping', 'stopped'
            ],
        }
    ])
    
    for instance in response['InstanceStatuses']:
            stopped.append(instance['InstanceId'])
    
    return stopped
    
def createSuccessResponse(msg):
    return {
            'statusCode': 200,
            'body': json.dumps(msg)
        }
