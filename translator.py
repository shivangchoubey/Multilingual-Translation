from googletrans import Translator  

translator = Translator()

def translate_text(text, target_lang):
    """Translates text to the target language."""
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"

