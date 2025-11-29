# AWS Bedrock Setup Guide

## 1. Create an AWS Account
If you don't have one, sign up at [aws.amazon.com](https://aws.amazon.com/).

## 2. Enable Bedrock Model Access
Amazon Bedrock requires you to explicitly request access to models.

1.  Log in to the AWS Console and navigate to **Amazon Bedrock**.
2.  In the left navigation pane, select **Model access**.
3.  Click **Manage model access**.
4.  Select the following models:
    *   **Anthropic**: Claude 3 Sonnet (or Claude 3.5 Sonnet if available)
    *   **Amazon**: Titan Text G1 - Express
    *   **Amazon**: Titan Image Generator G1
    *   **Amazon**: Titan Embeddings V2
5.  Click **Request model access**. Access is usually granted immediately or within a few minutes.

## 3. Configure IAM Permissions
Ensure your IAM user or role has the necessary permissions to invoke Bedrock models.

Attach the `AmazonBedrockFullAccess` policy for unrestricted access during development, or create a custom policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockInvoke",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "*"
        }
    ]
}
```

## 4. Troubleshooting
*   **Access Denied**: Double-check that you have requested model access in the specific region you are using (e.g., us-east-1 or us-west-2).
*   **Throttling**: If you hit rate limits, implement exponential backoff (included in the starter client).
