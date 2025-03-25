# Define a web scraper class to scrape the data from the website

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re   # Regular expression
import time
import random

class Scraper:
    def __init__(self, url):
        self.url = url
        self.data = []
    
    def scrape(self):
        # Send a request to the website
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table in the website
        table = soup.find('table')
        
        # Find all rows in the table
        rows = table.find_all('tr')
        
        # Extract the data from the rows
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            self.data.append([ele for ele in cols if ele])
        
        # Remove the first row (header)
        self.data = self.data[1:]
        
        return self.data
    
    def save(self, filename):
        # Save the data to a csv file
        df = pd.DataFrame(self.data, columns=['Rank', 'Name', 'Net Worth', 'Age', 'Country', 'Source'])
        df.to_csv(filename, index=False)
        
        return df