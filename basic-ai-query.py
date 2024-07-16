import os
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

response = client.chat.completions.create(
    model="35turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who invented the car"}
    ]
)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)