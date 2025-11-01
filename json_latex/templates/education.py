import json
import pathlib as plib
from datetime import datetime

SECTION_TITLES = {
    "en": "Education",
    "it": "Formazione",
    "de": "Ausbildung",
}

PRESENT_LABEL = {
    "en": "Present",
    "it": "Presente",
    "de": "Aktuell",
}


def education(resume_path, data_path, lan="en"):
    # Load JSON data from your file
    with open(plib.Path(data_path, "education.json")) as f:
        data = json.load(f)

    title = SECTION_TITLES.get(lan, SECTION_TITLES["en"])
    present_label = PRESENT_LABEL.get(lan, PRESENT_LABEL["en"])
    tex_1 = [
        f"\\cvsection{{{title}}}\n",
        "\\begin{cventries}\n",
    ]
    tex_2 = []
    for ed in data["education"]:
        tex_2.append("\cventry")
        tex_2.append("{{{position}}}".format(position=ed["area"]))
        if ed["url"]:
            tex_2.append(
                "{{\href{{{url}}}{{{institution}}}}}".format(
                    url=ed["url"], institution=ed["institution"]
                )
            )
        else:
            tex_2.append("{{{institution}}}".format(
                institution=ed["institution"]))
        tex_2.append("{{{location}}}".format(location=ed["location"]))

        if ed["startDate"]:
            date_obj = datetime.strptime(ed["startDate"], "%Y-%m-%d")
            startDate = date_obj.strftime("%b. %Y")
        else:
            startDate = present_label
        if ed["endDate"]:
            date_obj = datetime.strptime(ed["endDate"], "%Y-%m-%d")
            endDate = date_obj.strftime("%b. %Y")
        else:
            endDate = present_label
        tex_2.append(
            "{{{startDate} - {endDate}}}".format(
                startDate=startDate, endDate=endDate)
        )

        tex_2.append("{\\begin{cvitems}")
        for task in ed["responsibilities"]:
            tex_2.append("\item {{{task}}}".format(task=task))

        tex_2.append("\end{cvitems}}\n")

    tex_3 = [
        "\end{cventries}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "education.tex"), "w") as f:
        f.write("\n".join(tex))
