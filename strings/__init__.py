import os
import yaml

languages = {}
languages_present = {}

# Inisialisasi bahasa Indonesia sebagai default
default_lang = "id"

# Pastikan file default ada
default_path = f"./strings/langs/{default_lang}.yml"
if not os.path.exists(default_path):
    raise FileNotFoundError(f"File bahasa default '{default_path}' tidak ditemukan.")

languages[default_lang] = yaml.safe_load(open(default_path, encoding="utf8"))
languages_present[default_lang] = languages[default_lang]["name"]

# Inisialisasi bahasa lain
for filename in os.listdir(r"./strings/langs/"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == default_lang:
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        # Lengkapi key yang belum ada dengan default
        for item in languages[default_lang]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages[default_lang][item]
        try:
            languages_present[language_name] = languages[language_name]["name"]
        except Exception:
            print(f"Ada masalah pada file bahasa: {filename}")
            exit()

def get_string(lang: str):
    # Fallback ke default jika lang tidak ditemukan
    return languages.get(lang, languages[default_lang])
