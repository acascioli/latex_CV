import json
import pathlib as plib
import subprocess
import sys
from templates.personal_information import P_I
from templates.summary import summary
from templates.work import work
from templates.skills import skills

base_path = plib.Path(__file__).parents[0]
templates_path = plib.Path(base_path, "templates")
data_path = plib.Path(base_path, "cv_data")
resume_path = plib.Path(base_path, "resume")


P_I(resume_path, data_path)
summary(resume_path, data_path)
work(resume_path, data_path)
skills(resume_path, data_path)

# Save the rendered templates to a final LaTeX file
# with open("output_cv.tex", "w") as f:
#     f.write(education_tex)


# Run pdflatex to compile the LaTeX file
def run_pdflatex(tex_file):
    try:
        # Execute the pdflatex command
        subprocess.run(["xelatex", "resume.tex"], check=True)
        print(f"Successfully compiled {tex_file} to PDF.")
    except subprocess.CalledProcessError as e:
        print(f"Error: pdflatex failed with error code {e.returncode}", file=sys.stderr)


# Call the function
run_pdflatex("output_cv.tex")
