import os
import json
import urllib3
import boto3
from botocore.exceptions import ClientError

# Defaults
ENDPOINT_URL = os.environ.get("ENDPOINT_URL", "https://api.anthropic.com/v1/complete")
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL","claude-2")
API_KEY_SECRET_NAME = "gic-hackathon-anthropic-api-key"

def get_secret(secret_name):
    print("Getting API key from Secrets Manager")
    secrets_client = boto3.client('secretsmanager')
    try:
        response = secrets_client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    api_key = response['SecretString']
    return api_key

def call_llm(parameters, prompt):
    api_key = get_secret(API_KEY_SECRET_NAME)
    data = parameters
    data["prompt"] = prompt

    # set API headers with API key
    headers = {
        "anthropic-version": "2023-06-01", 
        "x-api-key": api_key,
        "content-type": "application/json",
        "accept": "application/json"
    }
    http = urllib3.PoolManager()
    try:
        response = http.request(
            "POST",
            ENDPOINT_URL,
            body=json.dumps(data),
            headers=headers
        )
        if response.status != 200:
            raise Exception(f"Error: {response.status} - {response.data}")
        # print(response.data)
        generated_text = json.loads(response.data)["completion"].strip()
        return generated_text
    except Exception as err:
        print(err)
        raise


# set model params
model_params = {
    "model": "claude-2",
    "temperature": 0,
    "max_tokens_to_sample": 128
}
question = "Where is Singapore?"
# prompt template for Anthropic - see this page for more info: 
# https://docs.anthropic.com/claude/docs/constructing-a-prompt#use-the-correct-format
prompt = f"\n\nHuman: {question}\n\nAssistant:"

generated_text = call_llm(model_params, prompt)
print(f"Prompt: {prompt}")
print(json.dumps(generated_text))
