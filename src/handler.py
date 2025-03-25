# Define a class to handle the data processing and scraping

import pandas as pd
import re
import random 

from src.llm_news_processer import LLMNewsProcesser
from src.scraper import Scraper 

class Handler:
    def __init__(self, url):
        self.url = url
        self.data = []
        self.news = []
        self.rephrased_news = []

    def scrape_data(self):
        scraper = Scraper(self.url)
        self.data = scraper.scrape()

    def process_data(self):
        processer = LLMNewsProcesser(self.data)
        processer.process()
        self.news = processer.news

    def rephrase_news(self):
        processer = LLMNewsProcesser(self.news)
        self.rephrased_news = processer.rephrase()

    def save_data(self, filename):
        processer = LLMNewsProcesser(self.data)
        df = processer.save(filename)
        return df
    
    def save_news(self, filename):
        processer = LLMNewsProcesser(self.news)
        df = processer.save(filename)
        return df
    
    def save_rephrased_news(self, filename):
        processer = LLMNewsProcesser(self.rephrased_news)
        df = processer.save(filename)
        return df
    
    def run(self):
        self.scrape_data()
        self.process_data()
        self.rephrase_news()
        self.save_data('data.csv')
        self.save_news('news.csv')
        self.save_rephrased_news('rephrased_news.csv')

    # Define the main function to run the handler
    def main():
        url = 'https://www.forbes.com/real-time-billionaires/#6d5b4e7d251c'
        handler = Handler(url)
        handler.run()
    
    if __name__ == '__main__':
        main()