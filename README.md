# Anthropic Completions API Sample Code

This repository includes a sample Python code to call [Anthropic's Completions API](https://docs.anthropic.com/claude/reference/complete_post) and generate a response from the chosen Large Language Model (LLM).

The sample code uses python urllib3 HTTP client to make the API calls, without using any additional libraries. There are other options too, such as using [Anthropic's Client SDK](https://github.com/anthropics/anthropic-sdk-python) or other open-source libraries such as [Langchain](https://python.langchain.com/docs/integrations/chat/anthropic).

Note that Anthropic API key is needed to interact with Anthropic's LLMs. The API key should be stored securely and should not be stored in the repository. The sample code provided retrieves the API key from AWS Secrets Manager, as such you would need to create a secret in AWS Secrets Manager (you may change the secret name in Line 10).