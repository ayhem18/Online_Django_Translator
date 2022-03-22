import Checker as Ch
import actualTranslator as T

ask_for_language = \
    'Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into ' \
    'French: '
ask_for_word = "Type the word you want to translate:"


def first_stage_implementation():
    valid_languages = {"fr", "en"}
    language = Ch.get_valid_input(valid_languages, ask_for_language)
    print(ask_for_word)
    word = input()
    print('You chose "{}" as the language to translate "{}" to.'.format(language, word))


def second_stage_implementation():
    valid_languages = {"fr", "en"}
    destination = Ch.get_valid_input(valid_languages, ask_for_language)
    print(ask_for_word)
    word = input()
    print('You chose "{}" as the language to translate "{}" to.'.format(destination, word))

    if destination == 'fr':
        source = 'en'
    else:
        source = 'fr'
    T.translate(source, destination, word)


if __name__ == "__main__":
    second_stage_implementation()
