from datetime import date
from nsepy.live import isworkingday

def isTodayWorkingDay():
    return isworkingday(date.today())


def createSuccessResponse(msg):
    return {
            'statusCode': 200,
            'body': json.dumps(msg)
        }
