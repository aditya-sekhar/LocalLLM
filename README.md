# Running LLM Locally Using Transformers

This guide explains how to run the Language Learning Model (LLM) locally using the Transformers library. We will use Google's GEMMA 2B model as an example.

## Prerequisites

- Python 3.6 or higher
- Transformers library

You can install the Transformers library using pip:

```bash
pip install transformers
```

##  Hugging Face Login
Some models require you to be logged in to Hugging Face. You can do that using the cli

```bash
% huggingface-cli login  
```

To get your Hugging Face API token:

* Go to the Hugging Face website and log in to your account.
* Go to the Hugging Face website and log in to your account.
* Click on your profile picture in the top right corner.
* Click on Settings.
* Your token will be visible under the 'API tokens' section.

## Understanding the Terms

* Tokenizer: This is a component that converts the input text into a format that the model can understand. In the context of transformer models, this usually means converting the text into a sequence of numerical values, each representing a specific word or character.

* Model: This is the actual machine learning model that has been trained to perform a specific task. In this case, the task is language learning.

* Pipeline: This is a high-level abstraction provided by the Transformers library that simplifies the process of using a model. It automatically takes care of tokenization and running the model, so you can use the model with just a few lines of code.