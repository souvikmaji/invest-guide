import logging
import boto3
from util import getInstanceIds, isHoliday, createSuccessResponse

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
patch_all()


def handler(event, context):
    if isHoliday():
        return createSuccessResponse("holiday")
        
    stopped = getStoppedInstances()
    if len(stopped) > 0:
        i = ec2.start_instances(InstanceIds=stopped)
        return createSuccessResponse('started your instances: ' + str(i))
    else:
        return createSuccessResponse('already running')

def getStoppedInstances():
    return getInstanceIds(ec2, ['shutting-down', 'terminated', 'stopping', 'stopped'])