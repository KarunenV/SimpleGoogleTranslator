from deep_translator import GoogleTranslator

def translate_to_english(text: str) -> str:
    translator = GoogleTranslator(source='auto', target='en')
    return translator.translate(text)

# Example usage
texts = [
    "Bonjour tout le monde",
    "Hola, ¿cómo estás?",
    "今日はいい天気ですね",
    "Aanrijding Letsel"
    "Bestelauto (BES)"
]

for t in texts:
    translated = translate_to_english(t)
    print(f"Original: {t}")
    print(f"English : {translated}\n")