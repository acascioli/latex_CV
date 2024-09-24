import json
import pathlib as plib
from datetime import datetime


def work(resume_path, data_path):
    # Load JSON data from your file
    with open(plib.Path(data_path, "work.json")) as f:
        data = json.load(f)

    tex_1 = [
        "\cvsection{Work Experience}\n",
        "\\begin{cventries}\n",
    ]
    tex_2 = []
    for work in data["work"]:
        tex_2.append("\cventry")
        tex_2.append("{{{job_title}}}".format(job_title=work["position"]))
        if work["url"]:
            tex_2.append(
                "{{\href{{{url}}}{{{company}}}}}".format(
                    url=work["url"], company=work["name"]
                )
            )
        else:
            tex_2.append("{{{company}}}".format(company=work["name"]))
        tex_2.append("{{{location}}}".format(location=work["location"]))

        if work["startDate"]:
            date_obj = datetime.strptime(work["startDate"], "%Y-%m-%d")
            startDate = date_obj.strftime("%b. %Y")
        else:
            startDate = "Present"
        if work["endDate"]:
            date_obj = datetime.strptime(work["endDate"], "%Y-%m-%d")
            endDate = date_obj.strftime("%b. %Y")
        else:
            endDate = "Present"
        tex_2.append(
            "{{{startDate} - {endDate}}}".format(startDate=startDate, endDate=endDate)
        )

        tex_2.append("{\\begin{cvitems}")
        for task in work["responsibilities"]:
            tex_2.append("\item {{{task}}}".format(task=task))

        tex_2.append("\end{cvitems}}\n")

    tex_3 = [
        "\end{cventries}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "experience.tex"), "w") as f:
        f.write("\n".join(tex))
