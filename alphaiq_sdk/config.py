import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    HOST_URL = os.getenv("HOST_URL", 'https://eofipoxzab.execute-api.us-east-1.amazonaws.com/v1')


config = Config()
