from app.models.answers_model import Answers
from pika.adapters.blocking_connection import BlockingChannel

class AnswerService:
    """
    Class responsible for handling the sending of answer messages 
    through a RabbitMQ communication channel.

    Methods:
    --------
    send_message_worker(channel: BlockingChannel, answers: Answers):
        Sends a message to the consumer with the answers serialized in JSON format.
    """
    
    @staticmethod
    def send_message_worker(channel: BlockingChannel, answers: Answers):
        """
        Sends a message to the consumer with the answer data.
        
        This method publishes a message to the 'answers' queue in RabbitMQ. The message
        contains the answer data serialized in JSON format, using the `model_dump_json` 
        method of the `Answers` class.

        Parameters:
        -----------
        channel (BlockingChannel): The communication channel with RabbitMQ used to 
                                   send the message. This channel is expected to be 
                                   of type `BlockingChannel` from the `pika` library.
                                   
        answers (Answers): An instance of the `Answers` class that holds the 
                           data to be sent to the consumer. The data is serialized 
                           using the `model_dump_json` method into JSON format.
        
        """
        channel.basic_publish(
            exchange="",
            routing_key="answers",
            body=answers.model_dump_json()
        )
        print("[x] Sent result to consumer")
