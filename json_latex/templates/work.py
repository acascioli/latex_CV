import json
import pathlib as plib
from datetime import datetime

SECTION_TITLES = {
    "en": "Work Experience",
    "it": "Esperienza",
    "de": "Berufserfahrung",
}

PRESENT_LABEL = {
    "en": "Present",
    "it": "Presente",
    "de": "Aktuell",
}


def work(resume_path, data_path, lan="en"):
    # Load JSON data from your file
    with open(plib.Path(data_path, "work.json")) as f:
        data = json.load(f)

    title = SECTION_TITLES.get(lan, SECTION_TITLES["en"])
    present_label = PRESENT_LABEL.get(lan, PRESENT_LABEL["en"])
    tex_1 = [
        f"\\cvsection{{{title}}}\n",
        "\\begin{cventries}\n",
    ]
    tex_2 = []
    for work_item in data["work"]:
        tex_2.append("\cventry")
        tex_2.append("{{{job_title}}}".format(job_title=work_item["position"]))
        if work_item["url"]:
            tex_2.append(
                "{{\href{{{url}}}{{{company}}}}}".format(
                    url=work_item["url"], company=work_item["name"]
                )
            )
        else:
            tex_2.append("{{{company}}}".format(company=work_item["name"]))
        tex_2.append("{{{location}}}".format(location=work_item["location"]))

        if work_item["startDate"]:
            date_obj = datetime.strptime(work_item["startDate"], "%Y-%m-%d")
            startDate = date_obj.strftime("%b. %Y")
        else:
            startDate = present_label
        if work_item["endDate"]:
            date_obj = datetime.strptime(work_item["endDate"], "%Y-%m-%d")
            endDate = date_obj.strftime("%b. %Y")
        else:
            endDate = present_label
        tex_2.append(
            "{{{startDate} - {endDate}}}".format(
                startDate=startDate, endDate=endDate)
        )

        tex_2.append("{\\begin{cvitems}")
        for task in work_item["responsibilities"]:
            tex_2.append("\item {{{task}}}".format(task=task))

        tex_2.append("\end{cvitems}}\n")

    tex_3 = [
        "\end{cventries}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "experience.tex"), "w") as f:
        f.write("\n".join(tex))
