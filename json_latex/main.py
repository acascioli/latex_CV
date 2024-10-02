import json
import pathlib as plib
import subprocess
import sys
from templates.personal_information import P_I
from templates.summary import summary
from templates.work import work
from templates.skills import skills
from templates.certificates import certificates
from templates.education import education
from templates.publications import publications
from templates.languages import languages
import shutil

variant = None
variant = "Bosch"

base_path = plib.Path(__file__).parents[0]
templates_path = plib.Path(base_path, "templates")
resume_path = plib.Path(base_path, "resume")
file_path = plib.Path(base_path, "resume.tex")

if variant:
    data_path = plib.Path(base_path, "cv_data_" + variant)
    file_path_new = plib.Path(base_path, "resume_" + variant + ".tex")
    shutil.copy(file_path, file_path_new)
    print(f"File copied from {file_path} to {file_path_new}")
    file_path = file_path_new
else:
    data_path = plib.Path(base_path, "cv_data")


P_I(resume_path, data_path)
summary(resume_path, data_path)
work(resume_path, data_path)
skills(resume_path, data_path)
certificates(resume_path, data_path)
education(resume_path, data_path)
publications(resume_path, data_path)
languages(resume_path, data_path)

# Save the rendered templates to a final LaTeX file
# with open("output_cv.tex", "w") as f:
#     f.write(education_tex)


# Run pdflatex to compile the LaTeX file
def run_pdflatex(tex_file):
    try:
        # Execute the pdflatex command
        subprocess.run(["xelatex", file_path], check=True)
        print(f"Successfully compiled {tex_file} to PDF.")
    except subprocess.CalledProcessError as e:
        print(f"Error: pdflatex failed with error code {e.returncode}", file=sys.stderr)


# Call the function
run_pdflatex("output_cv.tex")
