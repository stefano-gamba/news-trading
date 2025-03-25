# Define a class to process the data with a large language model using openai api
# It should filter the news by importance for the event in the world and rephrase them

import pandas as pd
import re
import random
import time
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class LLMNewsProcesser:
    def __init__(self, data):
        self.data = data
        self.news = []
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.model.eval()

    def process(self):
        for row in self.data:
            news = row[1]
            news = re.sub(r'\s+', ' ', news)
            news = re.sub(r'\n', ' ', news)
            news = news.strip()
            news = news[:1024]
            self.news.append(news)
    
    def rephrase(self):
        rephrased_news = []
        for news in self.news:
            input_ids = self.tokenizer.encode(news, return_tensors='pt')
            output = self.model.generate(input_ids, max_length=1024, num_return_sequences=1, temperature=0.7)
            rephrased_news.append(self.tokenizer.decode(output[0], skip_special_tokens=True))
            time.sleep(random.randint(1, 5))
        
        return rephrased_news
    
    def save(self, filename):
        df = pd.DataFrame(self.data, columns=['Rank', 'Name', 'Net Worth', 'Age', 'Country', 'Source'])
        df['News'] = self.news
        df['Rephrased News'] = self.rephrased_news
        df.to_csv(filename, index=False)
    
        return df