import json
import pathlib as plib


def summary(resume_path, data_path):
    # Load JSON data from your file
    with open(plib.Path(data_path, "summary.json")) as f:
        data = json.load(f)

    tex = [
        "\cvsection{Summary}",
        "\\begin{cvparagraph}",
        data["summary"],
        "\end{cvparagraph}",
    ]
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "summary.tex"), "w") as f:
        f.write("\n\n".join(tex))
