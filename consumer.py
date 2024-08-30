import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f"Message Received From: {method.routing_key} With Meesage: {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages ...')
    channel.start_consuming()

def SendMessageCreatedUser():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='user-created')

    def callback(ch, method, properties, body):
        print(f"Message Received From: {method.routing_key} With Meesage: {body}")
        print(f"Sending Email ...")

    channel.basic_consume(queue='user-created', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages ...')
    channel.start_consuming()

if __name__ == '__main__':
    SendMessageCreatedUser()