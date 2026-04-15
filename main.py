from deep_translator import GoogleTranslator

def translate_to_english(text: str) -> str:
    translator = GoogleTranslator(source='auto', target='en')
    return translator.translate(text)

# Example usage
texts = [
    "Aanrijding Letsel",
    "Vz Rijdt Achterop",
    "Vz Tegemoetk Op Rijbaan Tp",
    "Verzekerde Rijdt Achterop Tegenpartij",
    "Vz Rijdt Tegen Opstal",
    "Aanrijding Met Voertuig",
    "Verz. Veranderde Van Rijstrook",
    "Vz Rijdt Achterop",
    "Verzekerde Verleent Geen Voorrang",
    "Achteroprijden",
    "Verzekerde Rijdt Achterop Tegenpartij",
    "Auto Aanrijding Geen Voorrang",
    "Onduidelijke/Geen Lezing",
    "A.Geen Afst. Bewaard Op Rechte Weg",
    "Vz Rijdt Achterop",
    "Vz Verleent Geen Voorrang",
    "Vz Verleent Geen Voorrang",
    "Vz Verandert Van Richting",
    "Verz Verliet Uitrit",
    "Letselschade",
    "Aanrijding Met Voertuig",
    "Letselschade",
    "Tp Op Vz Na Vz Op Voorganger",
    "Vz Verleent Geen Voorrang",
    "Vz Verleent Geen Voorrang",
    "Geen Voorrang Verleend",
    "Links/Rechts Afslaan",
    "Tgp. Stond Stil",
    "Aanrijding Met Voertuig",
    "Vz Rijdt Achterop"
]

for t in texts:
    translated = translate_to_english(t)
    print(f"Original: {t}")
    print(f"English : {translated}\n")