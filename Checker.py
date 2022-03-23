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


@dispatch(str, list, list, str, int)
def print_words_examples(content, words, examples, target_lang, display_number=display_limit):
    new_content = content
    new_content += "{} Translations:".format(target_lang) + "\n"
    for i in range(min(display_number, len(words))):
        new_content += words[i] + "\n"
    new_content += "\n"

    new_content += "{} Examples:".format(target_lang) + "\n"
    for i in range(0, min(display_number * 2, len(examples)), 2):
        new_content += examples[i] + "\n"
        new_content += examples[i + 1] + "\n"
        new_content += "\n"
    new_content += "\n"
    # if file_name is not None:
    #     with open(file_name, "a") as write_file:
    #         write_file.write(content)
    #         write_file.write(content)
    return new_content


@dispatch(str, int, int, str, int)
def translate_display(content, source_lang_index, target_lang_index, word, display_number):
    words, examples = T.translate(supported_languages[source_lang_index - 1],
                                  supported_languages[target_lang_index - 1], word)
    return print_words_examples(content, words, examples, supported_languages[int(target_lang_index) - 1].capitalize(),
                                display_number)


def deliver_user_request():
    source_lang_index, target_lang_index, word = get_valid_translation_data()
    content = ""
    if int(target_lang_index) == 0:
        for i in range(len(supported_languages)):
            if i != int(source_lang_index) - 1:
                content = \
                    translate_display(content, int(source_lang_index), i + 1, word, 1)
    else:
        content = translate_display(content, int(source_lang_index), int(target_lang_index), word, display_limit)
    print(content)

    with open("{}.txt".format(word), "a") as write_file:
        write_file.write(content)
