#!/usr/bin/env python

from mimetypes import init
import boto3
from botocore.exceptions import ClientError

SENDER = "Trading Alerts <souvikmaji94+aws@gmail.com>"
RECIPIENT = "souvikmaji94@gmail.com"
CHARSET = "UTF-8"


class Notifier:
    def __init__(self) -> None:
        # Create a new SES resource and specify a region.
        self.client = boto3.client('ses')

    def notify(self, header, content):
        self.send_email(header, content)

    def send_email(self, subject, body):
        try:
            #Provide the contents of the email.
            response = self.client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': CHARSET,
                            'Data': body,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': subject,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])