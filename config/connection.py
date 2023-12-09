import boto3
from dotenv import load_dotenv
from os import getenv

load_dotenv()

sns_client = boto3.client("sns", aws_access_key_id = getenv("AWS_ACCESS_KEY_ID"), aws_session_token = getenv("AWS_SESSION_TOKEN"),
                          aws_secret_access_key = getenv("AWS_SECRET_ACCESS_KEY"), region_name = getenv("AWS_REGION"))

s3_client = boto3.client("s3", aws_access_key_id = getenv("AWS_ACCESS_KEY_ID"), aws_session_token = getenv("AWS_SESSION_TOKEN"),
                          aws_secret_access_key = getenv("AWS_SECRET_ACCESS_KEY"), region_name = getenv("AWS_REGION"))

dynamo_client = boto3.resource("dynamodb", aws_access_key_id = getenv("AWS_ACCESS_KEY_ID"), aws_session_token = getenv("AWS_SESSION_TOKEN"),
                          aws_secret_access_key = getenv("AWS_SECRET_ACCESS_KEY"), region_name = getenv("AWS_REGION"))