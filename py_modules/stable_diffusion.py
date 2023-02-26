#imports
from cmd import PROMPT
import sys
import replicate
from dotenv import load_dotenv
import os

#loading the dotenv file
load_dotenv()

# PROMPT = sys.argv[1]

REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
print(REPLICATE_API_TOKEN)

# client = replicate.Client(api_token=REPLICATE_API_TOKEN)
# model = client.models.get("stability-ai/stable-diffusion")
# image_urls = model.predict(prompt=PROMPT)
# print(image_urls)