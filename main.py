import Checker as Ch
import actualTranslator as T


def stage_4_implementation():
    source_lang, target_lang, word = Ch.get_valid_translation_data()
    words, examples = T.translate(source_lang, target_lang, word)
    Ch.print_words_examples(words, examples, target_lang.capitalize())


if __name__ == "__main__":
    Ch.deliver_user_request()
