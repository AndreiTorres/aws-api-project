from connection import sns_client
from dotenv import load_dotenv
from os import getenv

load_dotenv()

response = sns_client.subscribe(
    TopicArn = "arn:aws:sns:us-east-1:581050077128:calificaciones",
    Protocol = "email",
    Endpoint = getenv("EMAIL"),
    ReturnSubscriptionArn = True
)

print(response)

