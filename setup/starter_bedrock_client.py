import boto3
import json
import time
from botocore.exceptions import ClientError

class BedrockClient:
    def __init__(self, region_name="us-east-1"):
        """
        Initialize the Bedrock runtime client.
        Ensure you have configured AWS credentials via `aws configure` or environment variables.
        """
        self.bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name=region_name
        )

    def generate_text(self, prompt, model_id="anthropic.claude-3-sonnet-20240229-v1:0", max_tokens=1000):
        """
        Generate text using the Bedrock Converse API.
        """
        messages = [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ]

        try:
            response = self.bedrock_runtime.converse(
                modelId=model_id,
                messages=messages,
                inferenceConfig={"maxTokens": max_tokens}
            )
            
            return response['output']['message']['content'][0]['text']

        except ClientError as e:
            print(f"Error invoking model: {e}")
            return None

    def generate_embedding(self, text, model_id="amazon.titan-embed-text-v2:0"):
        """
        Generate embeddings using Amazon Titan Embeddings V2.
        """
        body = json.dumps({
            "inputText": text
        })

        try:
            response = self.bedrock_runtime.invoke_model(
                body=body,
                modelId=model_id,
                accept="application/json",
                contentType="application/json"
            )

            response_body = json.loads(response.get("body").read())
            return response_body.get("embedding")

        except ClientError as e:
            print(f"Error generating embedding: {e}")
            return None

if __name__ == "__main__":
    # Example Usage
    client = BedrockClient()
    
    print("--- Testing Text Generation ---")
    response = client.generate_text("Hello, Santa! How are the reindeer?")
    if response:
        print(f"Response: {response}\n")
    else:
        print("Failed to generate text. Check your credentials and model access.\n")

    print("--- Testing Embeddings ---")
    embedding = client.generate_embedding("Christmas tree")
    if embedding:
        print(f"Generated embedding vector of length: {len(embedding)}")
    else:
        print("Failed to generate embedding.")
