from googletrans import Translator


def tarjimon(xabar):
    trans = Translator()
    language = trans.detect(xabar).lang
    if language == 'uz':
        return trans.translate(xabar, "en").text
    elif language == 'en':
        return trans.translate(xabar, "uz").text