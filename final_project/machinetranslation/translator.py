import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-04-21',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translates from english to french
    """
    if english_text != "":
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return translation['translations'][0].get('translation')
    return ""

def french_to_english(french_text):
    """
    Translate from french to english
    """
    if french_text != "":
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return translation['translations'][0].get('translation')
    return ""