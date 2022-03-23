import argparse
import Checker as Ch

description = "This program translates any word from and to any " \
              "language in our list"
all_languages_arg = "all"
help_arg = "Please make sure to choose one of the supported languages"


# this method creates am argparse.ArgumentParser object that might be used to parse
# the command line arguments passed to the application
def app_arg_parser():
    supported_languages_extended = ["all"]
    for lang in Ch.supported_languages:
        supported_languages_extended.append(lang)

    parser = argparse.ArgumentParser(description=description)
    # add the first argument: source language
    parser.add_argument("src_lang", choices=Ch.supported_languages, help=help_arg)
    # add the second argument: target language
    parser.add_argument("tar_lang", choices=supported_languages_extended, help=help_arg)
    # add the third argument: the word to translate
    parser.add_argument("word")

    return parser
