from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re

# make a GET request to the server
response = requests.get("https://codeexercise.com/50-top-javascript-multiple-choice-questions-and-answers/")

# extract the text to create a readable html document
html = response.text

# use the html parser to create the soup object
soup = BeautifulSoup(html, 'html.parser')

# grab the desired tags
ordered_lists = soup.select("ol li p")

# save the desired text to a file so that I don't need to continually make the get requests
with open("quiz_questions.txt", "w") as questions_raw:
    questions_raw.write(str(ordered_lists))

with open("quiz_questions.txt", "r") as questions_raw:
    qw = questions_raw.read()


rm_p_tags = qw.replace("<p>", "{")
rm_p_close_tags = rm_p_tags.replace("</p>", "")
rm_br_tags = rm_p_close_tags.replace(r"<br/>", "")
rm_newlines = rm_br_tags.replace("\n", "', \n")
a_choice = rm_newlines.replace("A.", "A:")
b_choice = a_choice.replace("B.", "B:")
c_choice = b_choice.replace("C.", "C:")
d_choice = c_choice.replace("D.", "D:")
rm_commas = re.sub(r",\s{", "}{", d_choice)
finish_object = rm_commas.replace(" \n", ",")
beg_quotes = rm_commas.replace(": ", ": '")
q_object = beg_quotes.replace("{", "{question: '")
sub_final = q_object.replace(" \n", "")
final = sub_final.replace("}", "'}, ")
pprint(final)
with open("formatted_question.txt", "w") as fq:
    fq.write(final)





