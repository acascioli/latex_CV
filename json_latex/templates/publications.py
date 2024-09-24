import json
import pathlib as plib
from datetime import datetime


def publications(resume_path, data_path):
    # Load JSON data from your file
    with open(plib.Path(data_path, "publications.json")) as f:
        data = json.load(f)
    tex_1 = [
        "\cvsection{Publications}\n",
        "\\begin{cventries}\n",
    ]
    tex_2 = []
    for ed in data["publications"]:
        tex_2.append("\cventry")
        authors = []
        for author in ed["authors"].split(", "):
            if author == "A. Cascioli":
                authors.append("\\textbf{A. Cascioli}")
            else:
                authors.append(author)
        tex_2.append("{{{authors}}}".format(authors=", ".join(authors)))
        tex_2.append("{{{journal}}}".format(journal=ed["journal"]))
        tex_2.append("{}")
        date_obj = datetime.strptime(ed["date"], "%Y-%m-%d")
        date = date_obj.strftime("%Y")
        tex_2.append("{{{date}}}".format(date=date))

        tex_2.append("{\\begin{cvitems}")
        tex_2.append("\item {{{title}}}".format(title=ed["title"]))
        if ed["doi"]:
            tex_2.append("\item {{DOI: \href{{{DOI}}}{{{DOI}}}}}".format(DOI=ed["doi"]))

        tex_2.append("\end{cvitems}}\n")

    tex_3 = [
        "\end{cventries}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "publications.tex"), "w") as f:
        f.write("\n".join(tex))
