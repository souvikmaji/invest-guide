from datetime import date
from nsepy.live import isworkingday
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def isHoliday():
    return not isworkingday(date.today())

def getInstanceIds(ec2, states):
    ids = []
    response = ec2.describe_instances(Filters=[
        {
            'Name': 'tag:trading',
            'Values': [
                'live',
            ],
        },
        {
            'Name': 'instance-state-name',
            'Values': states,
        }
    ])
    logger.info(response)
    
    for instance in response['Reservations'][0]['Instances']:
            ids.append(instance['InstanceId'])
    
    return ids

def createSuccessResponse(msg):
    return {
            'statusCode': 200,
            'body': json.dumps(msg)
        }
