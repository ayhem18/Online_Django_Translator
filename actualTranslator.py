import requests
from bs4 import BeautifulSoup
import re


user_site_map = {"en": "english", "fr": "french"}

# The computer needs to represent itself as a certain user-agent to ensure connection establishment
headers = {'User-Agent': 'Mozilla/5.0'}
# the general form of the website's url
website_basic_url = "https://context.reverso.net/translation/{}-{}/{}"

# output formalities
successful_connection = "{} OK"

beautifulSoup_parser_arg = "html.parser"

# values used to parse the website
literal_translations_id = "translations-content"
examples_id = "examples-content"


def create_url(user_language_1, user_language_2, word):
    site_language_1 = user_site_map[user_language_1]
    site_language_2 = user_site_map[user_language_2]
    return website_basic_url.format(site_language_1, site_language_2, word)


# this method establishes successful connection with the site
# and return the corresponding response object
def establish_connection(url):
    # create a response object, make sure to pass the corresponding headers
    response = requests.get(url, headers=headers)

    while not response:
        response = requests.get(url, headers)
    print(successful_connection.format(str(response.status_code)))
    return response


# after inspecting the site, the literal translations are included in a div
# with an id = "translations-content". The search should be according to this data
def find_literal_translations(soup):
    links = soup.find("div", {"id": literal_translations_id}).findAll('a')
    print([link.text.strip() for link in links])


# after inspecting the site, the examples are included in a section element
# with id = "examples-content". the text is included in inner 'span' elements
def find_examples(soup):
    examples = soup.findAll("section", {"id": examples_id})
    for example in examples:
        expressions = example.findAll('span', {"class": "text"})
        print([expression.text.strip() for expression in expressions])


# a method that gather all the logic and provide a translation
# to the user
def translate(user_language1, user_language2, word):
    url = create_url(user_language1, user_language2, word)
    response = establish_connection(url)
    print("Translations")
    soup = BeautifulSoup(response.content, beautifulSoup_parser_arg)
    find_literal_translations(soup)
    find_examples(soup)
