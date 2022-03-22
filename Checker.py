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


def get_valid_translation_data():
    print(welcome_sentence)
    for (index, element) in enumerate(supported_languages):
        print("{}. {}".format(str(index + 1), element))

    source_language_index = get_valid_input([str(i) for i in range(1, len(supported_languages) + 1)],
                                            choose_source_language).lower()
    source_language = supported_languages[int(source_language_index) - 1]

    target_language_index = get_valid_input([str(i) for i in range(1, len(supported_languages) + 1)],
                                            choose_target_language).lower()
    target_language = supported_languages[int(target_language_index) - 1]

    print(ask_for_word)
    word = input().lower()

    return source_language, target_language, word


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
