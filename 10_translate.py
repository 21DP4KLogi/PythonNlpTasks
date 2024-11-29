import argostranslate.package
import argostranslate.translate

from_code = "lv"
to_code = "en"

argostranslate.package.install_from_path("./argosModels/translate-lv_en-1_9.argosmodel")
argostranslate.package.install_from_path("./argosModels/translate-en_lv-1_9.argosmodel")

print(argostranslate.translate.translate("Labdien! Kā jums klājas?", from_code, to_code))
print(argostranslate.translate.translate("Es šodien lasīju interesantu grāmatu.", from_code, to_code))

# Source:
# https://github.com/argosopentech/argos-translate#python
