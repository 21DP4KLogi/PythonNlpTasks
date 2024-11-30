import re

text = "@John: Šis ir lielisks produkts!!! 👏👏👏 Vai ne? http://example.com"

print(text)

step1 = re.sub(r"(https?://)?\w*\.[a-zA-Z]{2,}", r"", text)  # Remove URLs
step2 = re.sub(r"[#@]", "", step1)  # Remove unneeded symbols
step3 = re.sub(r"([^a-zA-Z0-9_\s]){2,}", r"\1", step2)  # Remove duplicate symbols
step4 = step3.lower()  # Lowercased

print(step4)
