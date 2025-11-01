import json
import pathlib as plib
from datetime import datetime

SECTION_TITLES = {
    "en": "Conferences and Seminars",
    "it": "Conferenze",
    "de": "Konferenzen und Seminare",
}


def presentations(resume_path, data_path, lan="en"):
    # Load JSON data from your file
    with open(plib.Path(data_path, "presentations.json")) as f:
        data = json.load(f)

    title = SECTION_TITLES.get(lan, SECTION_TITLES["en"])
    tex_1 = [
        f"\\cvsection{{{title}}}\n",
        "\\begin{cventries}\n",
    ]
    tex_2 = []
    for ed in data["presentations"]:
        tex_2.append("\cventry")
        tex_2.append("{{{type}}}".format(type=ed["type"]))
        tex_2.append("{{{conference}}}".format(conference=ed["conference"]))
        tex_2.append("{{{location}}}".format(location=ed["location"]))
        date_obj = datetime.strptime(ed["startDate"], "%Y-%m-%d")
        startDate = date_obj.strftime("%Y-%m-%d")
        date_obj = datetime.strptime(ed["endDate"], "%Y-%m-%d")
        endDate = date_obj.strftime("%Y-%m-%d")
        tex_2.append(
            "{{{startDate} - {endDate}}}".format(
                endDate=endDate, startDate=startDate)
        )

        tex_2.append("{\\vspace{-4.0mm}")
        tex_2.append("\\begin{justify}")
        tex_2.append("\\begin{itemize}[leftmargin=0ex, nosep, noitemsep]")
        tex_2.append("\setlength{\parskip}{0pt}")
        tex_2.append("\\renewcommand{\labelitemi}{\\bullet}")
        tex_2.append("{{{title}}}".format(title=ed["title"]))
        tex_2.append("\end{itemize}")
        tex_2.append("\end{justify}}")

    tex_3 = [
        "\end{cventries}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "presentations.tex"), "w") as f:
        f.write("\n".join(tex))
