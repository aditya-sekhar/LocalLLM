from transformers import pipeline
import warnings
import tensorflow as tf

question = "My name is Lewis and I like to"
model_list = ['EleutherAI/gpt-neo-1.3B', 'microsoft/phi-2']

for model in model_list:
    nlp = pipeline('text-generation', model=model)
    print("\n" + "-"*50)
    output = nlp(question)
    print(f"Model: {model}")
    print(f"Output: {output[0]['generated_text']}")
    print("\n" + "-"*50)