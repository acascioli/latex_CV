import json
import pathlib as plib

SECTION_TITLES = {
    "en": "Summary",
    "it": "Sommario",
    "de": "Kurzprofil",
}


def summary(resume_path, data_path, lan="en"):
    # Load JSON data from your file
    with open(plib.Path(data_path, "summary.json")) as f:
        data = json.load(f)

    title = SECTION_TITLES.get(lan, SECTION_TITLES["en"])
    tex = [
        f"\\cvsection{{{title}}}",
        "\\begin{cvparagraph}",
        data["summary"],
        "\end{cvparagraph}",
    ]
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "summary.tex"), "w") as f:
        f.write("\n\n".join(tex))
