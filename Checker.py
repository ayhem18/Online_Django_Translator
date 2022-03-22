from multipledispatch import dispatch
import actualTranslator as T

supported_languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese",
                       "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]

welcome_sentence = "Hello, welcome to the translator. Translator supports:"

choose_source_language = "Type the number of your language:"

choose_target_language = "Type the number of language you want to translate to:"

ask_for_word = "Type the word you want to translate:"

display_limit = 5


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


@dispatch(str, str, str)
def print_words_examples(words, examples, destination_language):
    print()
    print("{} Translations:".format(destination_language))
    for i in range(min(display_limit, len(words))):
        print(words[i])

    print()
    print("{} Examples:".format(destination_language))
    for i in range(0, min(display_limit * 2, len(examples)), 2):
        print(examples[i])
        print(examples[i + 1])
        print()


@dispatch(list, list, str, int, str)
def print_words_examples(words, examples, target_lang, display_number=display_limit, file_name=None):
    words_string = "\n"
    words_string += "{} Translations:".format(target_lang) + "\n"

    for i in range(min(display_number, len(words))):
        words_string += words[i] + "\n"

    examples_string = "\n"
    examples_string += "{} Examples:".format(target_lang) + "\n"
    for i in range(0, min(display_number * 2, len(examples)), 2):
        examples_string += examples[i] + "\n"
        examples_string += examples[i + 1] + "\n"
        examples_string += "\n"

    print(words_string)
    print(examples_string)

    if file_name is not None:
        with open(file_name, "a") as write_file:
            write_file.write(words_string)
            write_file.write(examples_string)


@dispatch(int, int, str)
def translate_display(source_lang_index, target_lang_index, word):
    words, examples = T.translate(supported_languages[source_lang_index - 1],
                                  supported_languages[target_lang_index - 1], word)
    print_words_examples(words, examples, supported_languages[int(target_lang_index) - 1].capitalize(),
                         1, "{}.txt".format(word))


def deliver_user_request():
    source_lang_index, target_lang_index, word = get_valid_translation_data()
    if int(target_lang_index) == 0:
        for i in range(len(supported_languages)):
            if i != int(source_lang_index):
                translate_display(int(source_lang_index), i + 1, word)
    else:
        translate_display(int(source_lang_index), int(target_lang_index), word)
