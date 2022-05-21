import requests
from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://codeexercise.com/50-top-javascript-multiple-choice-questions-and-answers/")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
ordered_lists = soup.select("ol")
pprint(ordered_lists)