import Checker as Ch
import actualTranslator as T
import ArgsParser as Ap


def stage_4_implementation():
    source_lang, target_lang, word = Ch.get_valid_translation_data()
    words, examples = T.translate(source_lang, target_lang, word)
    Ch.print_words_examples(words, examples, target_lang.capitalize())


def stage_5_implementation():
    src, tar, word = Ch.get_valid_translation_data()
    Ch.deliver_user_request(int(src), int(tar), word)


def app_with_command_line():
    parser = Ap.app_arg_parser()
    args = parser.parse_args()
    src_lang = args.src_lang
    tar_lang = args.tar_lang
    word = args.word
    Ch.deliver_user_request(src_lang, tar_lang, word)


if __name__ == "__main__":
    app_with_command_line()

