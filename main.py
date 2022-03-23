import sys
import Checker as Ch
import actualTranslator as T
import ArgsParser as Ap


def final_application():
    args = sys.argv
    if len(args) == 4:
        src_lang = args[1]
        tar_lang = args[2]
        word = args[3]
        try:
            assert src_lang in Ch.supported_languages
            try:
                assert tar_lang in Ch.supported_languages or tar_lang == Ap.all_languages_arg

                try:
                    Ch.deliver_user_request(src_lang, tar_lang, word)
                except:
                    print(Ch.unexpected_word_msg.format(word))

            except AssertionError:
                print(Ch.unsupported_language_msg.format(tar_lang))

        except AssertionError:
            print(Ch.unsupported_language_msg.format(src_lang))


if __name__ == "__main__":
    final_application()
