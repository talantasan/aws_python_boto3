import boto3, os

sqs_url = os.environ["SQS_QUEUE_URL"]
# Create SQS client
sqs = boto3.client('sqs')


queue_url = f'{sqs_url}'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'Author'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Chyngyz Aitmatov'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])