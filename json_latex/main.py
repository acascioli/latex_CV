import os
import pathlib as plib
import shutil
import subprocess
import sys
import locale

from dotenv import load_dotenv

from templates.certificates import certificates
from templates.education import education
from templates.languages import languages
from templates.personal_information import P_I
from templates.presentations import presentations
from templates.publications import publications
from templates.skills import skills
from templates.summary import summary
from templates.work import work
from templates.honors import honors

load_dotenv()

variant = None
# variant = "Bosch"
# variant = "it"

json_path = os.getenv("JSON_PATH")
base_path = plib.Path(__file__).parents[0]
templates_path = plib.Path(base_path, "templates")
resume_path = plib.Path(base_path, "resume")
file_path = plib.Path(base_path, "resume.tex")


# Run pdflatex to compile the LaTeX file
def run_pdflatex(tex_file):
    try:
        # Execute the pdflatex command
        subprocess.run(["xelatex", file_path], check=True)
        print(f"Successfully compiled {tex_file} to PDF.")
    except subprocess.CalledProcessError as e:
        print(
            f"Error: pdflatex failed with error code {e.returncode}", file=sys.stderr)


if variant:
    # data_path = plib.Path(base_path, "cv_data_" + variant)
    data_path = plib.Path(json_path + variant)
    file_path_new = plib.Path(base_path, "resume_" + variant + ".tex")
    shutil.copy(file_path, file_path_new)
    print(f"File copied from {file_path} to {file_path_new}")
    file_path = file_path_new
else:
    data_path = [plib.Path(json_path, "en"), plib.Path(json_path, "it")]

if isinstance(data_path, list):
    for i, d in enumerate(data_path):
        if i == 1:
            variant = "it"
            # Set locale to Italian
            locale.setlocale(locale.LC_TIME, "it_IT.UTF-8")
        else:
            variant = "en"
        P_I(resume_path, d, variant)
        summary(resume_path, d, variant)
        work(resume_path, d, variant)
        skills(resume_path, d, variant)
        certificates(resume_path, d, variant)
        education(resume_path, d, variant)
        publications(resume_path, d, variant)
        presentations(resume_path, d, variant)
        languages(resume_path, d, variant)
        honors(resume_path, d, variant)
        file_path_new = plib.Path(base_path, "resume_" + variant + ".tex")
        # Check if the file already exists
        if not file_path_new.exists():
            shutil.copy(file_path, file_path_new)
            print(f"File copied to {file_path_new}")
        else:
            print(f"File {file_path_new} already exists. Copy skipped.")
        file_path = file_path_new

        run_pdflatex("output_cv")
else:
    P_I(resume_path, data_path)
    summary(resume_path, data_path)
    work(resume_path, data_path)
    skills(resume_path, data_path)
    certificates(resume_path, data_path)
    education(resume_path, data_path)
    publications(resume_path, data_path)
    presentations(resume_path, data_path)
    languages(resume_path, data_path)
    honors(resume_path, d, variant)

    # Save the rendered templates to a final LaTeX file
    # with open("output_cv.tex", "w") as f:
    #     f.write(education_tex)
    # Call the function
    run_pdflatex("output_cv.tex")
