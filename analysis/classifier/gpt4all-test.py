# python3 -m venv venv
# source venv/bin/Activate
# https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/python/README.md
# deactivate

# TODO:
# is this the LLM best model?
# is there a GPU version available?
# how to engineer the prompt to only include true/false?
# how does it perform on the raw tweets?

import sqlite3
import pandas as pd
from gpt4all import GPT4All
# from nomic.gpt4all import GPT4AllGPU
# import torch
# from transformers import LlamaTokenizer

# read in all the previously flagged tweets
con = sqlite3.connect("data/tweets.db")
tweets = pd.read_sql_query("SELECT * FROM tweets LIMIT 10", con)

# gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")
gptj = GPT4All("ggml-vicuna-13b-1.1-q4_2")
# gptj = GPT4AllGPU("ggml-vicuna-13b-1.1-q4_2")

def extract_resp(resp):
    return resp['choices'][0]['message']['content']

def determine_if_hate(tweet):
    base_prompt = "I need your assistance in identifying hate speech for an academic paper. Respond 'true' if a message is hate speech and 'false' otherwise. You can only response 'true' or 'false'. Here is the message: "
    prompt = base_prompt + tweet
    messages = [{"role": "user", "content": prompt}]
    resp = gptj.chat_completion(messages)
    is_hate_speech = extract_resp(resp)
    return(is_hate_speech)

determine_if_hate(tweets.text[0])

results = tweets.head(100).text.apply(determine_if_hate)
