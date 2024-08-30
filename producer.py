import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello RabbitMQ!'
    )

    print("Messages Sended!")
    connection.close()

def CreateUser():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='user-created')

    channel.basic_publish(
        exchange='',
        routing_key='user-created',
        body='{"Name": "Pepito Perez","Age": 12,"Email": "pepito@email.com"}'
    )

    print("Messages Sended!")
    connection.close()

if __name__ == '__main__':
    CreateUser()