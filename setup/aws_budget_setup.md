# AWS Budget Setup Guide

GenAI experiments can incur costs. Setting up a budget is crucial to avoid surprises.

## Cost Estimates
For the 25-day challenge, assuming moderate usage:

*   **Bedrock (Claude 3 Sonnet)**: ~$5.00 - $15.00 (depending on token usage)
*   **Bedrock (Titan Image)**: ~$1.00 - $3.00
*   **Lambda/S3/DynamoDB**: Free Tier eligible (usually < $1.00)

**Total Estimated Cost**: $10.00 - $20.00

## Setting Up a Budget

1.  Log in to the AWS Console and search for **AWS Budgets**.
2.  Click **Create budget**.
3.  Select **Use a template (simplified)** and choose **Zero spend budget** (to be alerted immediately) or **Monthly cost budget**.
4.  For **Monthly cost budget**:
    *   Enter your budgeted amount (e.g., $20.00).
    *   Give it a name like "SleighRideBudget".
5.  Under **Email recipients**, enter your email address to receive alerts when actual or forecasted spend exceeds your threshold.
6.  Click **Create budget**.

## Cost Optimization Tips
*   **Use smaller models**: Use Titan Text or Claude Haiku for testing logic before switching to Sonnet.
*   **Clean up resources**: Delete unused S3 buckets and OpenSearch collections when finished.
*   **Monitor daily**: Check the Billing Dashboard periodically.
