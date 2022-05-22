import boto3
import logging
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

    i = ec2.stop_instances(InstanceIds=getRunningInstances())
    return createSuccessResponse('stopped your instances: ' + str(i))

def getRunningInstances():
    return getInstanceIds(ec2, [ 'running'])