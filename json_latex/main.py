import os
import pathlib as plib
import shutil
import subprocess
import sys
import locale

from dotenv import load_dotenv
from templates.certificates import certificates
from templates.education import education
from templates.honors import honors
from templates.languages import languages
from templates.personal_information import P_I
from templates.presentations import presentations
from templates.publications import publications
from templates.skills import skills
from templates.summary import summary
from templates.work import work

load_dotenv()

variant_override = None
# variant_override = "Bosch"
# variant_override = "it"
# variant_override = "de"

LANGUAGE_CONFIG = {
    "en": {"locale": "en_US.UTF-8"},
    "it": {"locale": "it_IT.UTF-8"},
    "de": {"locale": "de_DE.UTF-8"},
}
DEFAULT_LANGUAGES = tuple(LANGUAGE_CONFIG.keys())

json_path = os.getenv("JSON_PATH")
print(json_path)
base_path = plib.Path(__file__).parents[0]
resume_path = plib.Path(base_path, "resume")
file_path = plib.Path(base_path, "resume.tex")


# Run pdflatex to compile the LaTeX file
def run_pdflatex(tex_file):
    try:
        # Execute the pdflatex command
        subprocess.run(["xelatex", str(tex_file)], check=True)
        print(f"Successfully compiled {tex_file} to PDF.")
    except subprocess.CalledProcessError as e:
        print(f"Error: pdflatex failed with error code {e.returncode}", file=sys.stderr)


if variant_override:
    variant_plan = [(variant_override, plib.Path(json_path, variant_override))]
else:
    variant_plan = [(lang, plib.Path(json_path, lang)) for lang in DEFAULT_LANGUAGES]

for variant, data_dir in variant_plan:
    locale_name = LANGUAGE_CONFIG.get(variant, {}).get("locale")
    if locale_name:
        try:
            locale.setlocale(locale.LC_TIME, locale_name)
        except locale.Error:
            locale.setlocale(locale.LC_TIME, "")
    else:
        locale.setlocale(locale.LC_TIME, "")

    P_I(resume_path, data_dir, variant)
    summary(resume_path, data_dir, variant)
    work(resume_path, data_dir, variant)
    skills(resume_path, data_dir, variant)
    certificates(resume_path, data_dir, variant)
    education(resume_path, data_dir, variant)
    publications(resume_path, data_dir, variant)
    presentations(resume_path, data_dir, variant)
    languages(resume_path, data_dir, variant)
    honors(resume_path, data_dir, variant)

    file_path_new = plib.Path(base_path, f"resume_{variant}.tex")
    if not file_path_new.exists():
        shutil.copy(file_path, file_path_new)
        print(f"File copied to {file_path_new}")
    else:
        print(f"File {file_path_new} already exists. Copy skipped.")
    file_path = file_path_new

    run_pdflatex(file_path)
