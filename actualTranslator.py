import requests
from bs4 import BeautifulSoup


# The computer needs to represent itself as a certain user-agent to ensure connection establishment
import Checker

headers = {'User-Agent': 'Mozilla/5.0'}
# the general form of the website's url
website_basic_url = "https://context.reverso.net/translation/{}-{}/{}"

# output formalities
successful_connection = "{} OK"

beautifulSoup_parser_arg = "html.parser"

# values used to parse the website
literal_translations_id = "translations-content"
examples_id = "examples-content"


# return the customized url used to establish a connection with the website
def create_url(user_language_1, user_language_2, word):
    return website_basic_url.format(user_language_1.lower(),
                                    user_language_2.lower(), word)


# this method establishes successful connection with the site
# and return the corresponding response object
def establish_connection(url):
    # create a response object, make sure to pass the corresponding headers
    return requests.get(url, headers=headers)


# after inspecting the site, the literal translations are included in a div
# with an id = "translations-content". The search should be according to this data
def find_literal_translations(soup):
    links = soup.find("div", {"id": literal_translations_id}).findAll('a')
    return [link.text.strip() for link in links]


# after inspecting the site, the examples are included in a section element
# with id = "examples-content". the text is included in inner 'span' elements
def find_examples(soup):
    examples = soup.findAll("section", {"id": examples_id})
    for example in examples:
        expressions = example.findAll('span', {"class": "text"})
        return [expression.text.strip() for expression in expressions]


# a method that gather all the logic and provide a translation
# to the user
def translate(user_language1, user_language2, word):
    url = create_url(user_language1, user_language2, word)
    try:
        response = establish_connection(url)
        assert response is not None
        soup = BeautifulSoup(response.content, beautifulSoup_parser_arg)
        return find_literal_translations(soup), find_examples(soup)

    # except statement to cover the case of failed connection: response is None
    except AssertionError:
        print(Checker.failed_connection_msg)
        return None, None
    # except statement to cover the case of unexpected word to translate: exception raised by
    # find_literal_translations function
    except:
        print(Checker.unexpected_word_msg.format(word))
        return None, None
