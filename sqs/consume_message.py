import boto3, os

sqs_queue_name = os.environ['QUEUE_NAME']
sqs = boto3.resource("sqs")
queue = sqs.get_queue_by_name(QueueName=f"{sqs_queue_name}")


def process_message(message_body):
    print(f"processing message: {sqs_message}")
    # do what you want with the message here
    pass


if __name__ == "__main__":
    while True:
        messages = sqs_queue.receive_messages()
        for message in messages:
            process_message(message.body)
            message.delete()