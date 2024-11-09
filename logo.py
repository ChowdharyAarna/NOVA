from openai import OpenAI
client = OpenAI(api_key="sk-oDj6r8Ox2aQCQfBmxPh2IQ",base_url="https://nova-litellm-proxy.onrender.com")

response = client.images.generate(
  model="dall-e-3",
  prompt="We are a company called EasyEats that helps find local food options for all sorts of dietary restrictions. Make a simple, eye-catching, and circular logo for our company. Can you make the main theme green colors and include leaves. Make the subcaption easy food for everyone.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)