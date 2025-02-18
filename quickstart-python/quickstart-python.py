import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize client with MakeHub API
client = OpenAI(
    api_key=os.getenv("MAKEHUB_API_KEY"),  # Replace with your MakeHub API key or use environment variable
    base_url="https://api.makehub.ai/v1"
)

# Set performance requirements for arbitrage
extra_query_params = {
    "min_throughput": "150",  # Minimum 150 tokens/sec
    "max_latency": "1000"    # Maximum 1000ms response time
}

# Call the API
response = client.chat.completions.create(
    model="meta/Llama-3.3-70B-Instruct-fp16",  # Example model
    messages=[{"role": "user", "content": "Hello, world!"}],
    extra_query=extra_query_params  # Arbitrages across providers
)

# Print the response
print(response.choices[0].message.content)