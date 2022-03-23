from multipledispatch import dispatch
import actualTranslator as T
import ArgsParser as Ap

supported_languages = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
                       "dutch", "polish", "portuguese", "romanian", "russian", "turkish"]

welcome_sentence = "Hello, welcome to the translator. Translator supports:"

choose_source_language = "Type the number of your language:"

choose_target_language = "Type the number of language you want to translate to:"

ask_for_word = "Type the word you want to translate:"

display_limit = 5

failed_connection_msg = "Something wrong with your internet connection"

unsupported_language_msg = "Sorry, the program doesn't support {}"

unexpected_word_msg = "Sorry, unable to find {}"


def get_valid_input(valid_input_set, prompt_message=None):
    is_valid = False
    user_input = ""
    while not is_valid:
        if prompt_message is not None:
            print(prompt_message)
        user_input = input()
        is_valid = user_input in valid_input_set

    return user_input


# this method returns a tuple of three elements
# index of the source language(str), index of the target language(str)
# the word to be translated
def get_valid_translation_data():
    print(welcome_sentence)
    for (index, element) in enumerate(supported_languages):
        print("{}. {}".format(str(index + 1), element))

    source_language_index = get_valid_input([str(i) for i in range(1, len(supported_languages) + 1)],
                                            choose_source_language).lower()
    target_language_index = get_valid_input([str(i) for i in range(0, len(supported_languages) + 1)],
                                            choose_target_language).lower()

    print(ask_for_word)
    word = input().lower()

    return source_language_index, target_language_index, word


# given a list of words (translations) and list of examples, this function creates a string
# representing how these two lists should be displayed on the console as well as written to a file
@dispatch(str, list, list, str, int)
def print_words_examples(content, words, examples, target_lang, display_number=display_limit):
    new_content = content
    new_content += "{} Translations:".format(target_lang.capitalize()) + "\n"
    for i in range(min(display_number, len(words))):
        new_content += words[i] + "\n"
    new_content += "\n"
    limit = min(display_number * 2, len(examples))
    new_content += "{} Example{}:".format(target_lang.capitalize(), "" if limit <= 2 else "s") + "\n"
    for i in range(0, limit, 2):
        new_content += examples[i] + "\n"
        new_content += examples[i + 1] + "\n"
        new_content += "\n"
    new_content += "\n"
    return new_content


# this function extracts the returned translations and examples from the website
# and append them to the argument "content". content is later to be displayed to the console
@dispatch(str, str, str, str, int)
def translate_display(content, source_lang, target_lang, word, display_number):
    try:
        words, examples = T.translate(source_lang, target_lang, word)
        assert words is not None and examples is not None
        return print_words_examples(content, words, examples, target_lang,
                                    display_number)
    except AssertionError:
        pass


# this function handles the different scenarios:
# one to one translation or one to all translations
@dispatch(str, str, str)
def deliver_user_request(source_lang, target_lang, word):
    try:
        content = ""
        if target_lang == Ap.all_languages_arg:
            for language in supported_languages:
                if language != source_lang:
                    content = \
                        translate_display(content, source_lang, language, word, 1)
        else:
            content = translate_display(content, source_lang, target_lang, word, display_limit)

        assert content

        print(content)
        with open("{}.txt".format(word), "a", encoding="utf-8") as write_file:
            write_file.write(content)
    except:
        pass
