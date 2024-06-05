from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
apikey = os.getenv("NVIDIANIM_API_KEY")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = apikey
)

completion = client.chat.completions.create(
  model="meta/llama3-70b-instruct",
  messages=[{"role":"user","content":"Provide me an article on machine learning"}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True 
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

