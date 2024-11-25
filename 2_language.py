from langdetect import detect

texts = [
    "Šodien ir saulaina diena", # Latvian
    "Today is a sunny day", # English
    "Сегодня солнечный день", # Russian
    "Šudiņ saulaina dīna", # Lithuanian
    "Täna on päikesepaisteline päev", # Estonian
    "Šiandien saulėta diena", # Latgalian
    "Сьогодні сонячний день", # Ukrainian
    "Heute ist ein sonniger Tag", # German
    "Σήμερα είναι μια ηλιόλουστη μέρα", # Greek
    "I dag er en solrik dag", # Norwegian
    "I dag er en solskinsdag", # Danish
        ]

i = 1
for string in texts:
    print(str(i) + ': "' + string + '" - ' + detect(string))
    i += 1

print("""
Mistakes:
#2 is not Somali
#6 is Latgalian
#10 is Norwegian and #11 is Danish
      """)
