from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Your code using transformers
# For example, you can initialize a pipeline for text generation, sentiment analysis, etc.
nlp_pipeline = pipeline("sentiment-analysis")
result = nlp_pipeline("I love using transformers!")

print(result)
