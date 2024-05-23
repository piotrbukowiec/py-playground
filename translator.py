from dotenv import load_dotenv
from deepl import Translator, DeepLException, AuthorizationException
from typing import Union
from os import getenv

load_dotenv()


# api_key = getenv('DEEPL_API_KEY')
#
# try:
#     if not api_key:
#         raise ValueError('Api key must not be empty')
#     translator = Translator(api_key)
# except ValueError as err:
#     print(err.args)
# except AuthorizationException:
#     print('Invalid api key')
def get_translator():
    try:
        api_key = getenv('DEEPL_API_KEY')
        if not api_key:
            raise ValueError('Api key must not be empty')
        translator = Translator(api_key)
        return translator
    except ValueError:
        print('Api key must not be empty')
    # except AuthorizationException:
    #     print('Invalid api key')

def get_target_lang_codes():
    target_lang_codes = get_translator().get_target_languages()
    return target_lang_codes

def translate_text(text: str, target_lang_code: str) -> Union[str, None]:
    try:
        translator = get_translator()
        translated_text = translator.translate_text(text, target_lang=target_lang_code).text
        return str(translated_text)
    except DeepLException:
        print('Invalid target language code')
        return