import requests
from bs4 import BeautifulSoup
import re 

# Define the URL of the website you want to scrape
def find_item(item_name):
    print(item_name)
    url = ('https://lordofthemysteries.fandom.com/wiki/'+item_name)

    # Send a GET request to the website and store the response in a variable
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    start = soup.find("span", id="Appearance")
    end = soup.find("span", id="References")
    s = soup.find(start)
    e = soup.find(end)
    soup = soup.prettify()

    text = soup[s:e]
    words = re.findall(r'<p>([^<>]*)</p>', text)
    # for i in words:
    #     text = text.replace(i, "")
    # words = re.findall(r'</([^<>]*)>', text)
    # for i in words:
    #     text = text.replace(i, "")
    # words = re.findall(r'<([a-zA-Z0-9_]*)>', text)
    # for i in words:
    #     text = text.replace(i, "")
    #     words = re.findall(r'</([a-zA-Z0-9_]*)>', text)
    # for i in words:
    #     text = text.replace(i, "")
    # print(text)

    # Appearance = (words[1]).replace("\n", "")
    # History = (words[2]).replace("\n", "")
    # Strengths = words[3].replace("\n", "")
    # Negative_effects = words[4].replace("\n", "")

    # print (f'''
    # `Appearance`: {Appearance}
    # `History`: {History}
    # `Strengths`: {Strengths}
    # `Negative_effects`: {Negative_effects}
    # ''')
    print(words)

find_item("Death_Knell")