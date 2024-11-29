import argostranslate.package
import argostranslate.translate

argostranslate.package.install_from_path("./argosModels/translate-lv_en-1_9.argosmodel")
argostranslate.package.install_from_path("./argosModels/translate-en_lv-1_9.argosmodel")

def en2lv(text):
    return argostranslate.translate.translate(text, "en", "lv")

def lv2en(text):
    return argostranslate.translate.translate(text, "lv", "en")
