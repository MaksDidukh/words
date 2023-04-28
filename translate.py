import six
from google.cloud import translate_v2 as translate

translate_client = translate.Client()
result = translate_client.translate("text", target_language="russian")
print(u"Text: {}".format(result["input"]))
print(u"Translation: {}".format(result["translatedText"]))
print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
