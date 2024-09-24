import json
import pathlib as plib
from datetime import datetime


def honors(resume_path, data_path):
    # Load JSON data from your file
    with open(plib.Path(data_path, "honors.json")) as f:
        data = json.load(f)
    tex_1 = [
        "\cvsection{Honors \& Awards}\n",
        "\cvsubsection{International Awards}\n",
        "\\begin{cvhonors}\n",
    ]
    tex_2 = []
    for honor in data["international"]:
        tex_2.append("\cvhonor")
        tex_2.append("{{{award}}}".format(award=honor["award"]))
        tex_2.append("{{{issuer}}}".format(issuer=honor["issuer"]))
        tex_2.append("{{{location}}}".format(location=honor["location"]))
        date_obj = datetime.strptime(honor["date"], "%Y-%m-%d")
        date = date_obj.strftime("%Y")
        tex_2.append("{{{date}}}".format(date=date))

    tex_3 = [
        "\end{cvhonors}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "honors.tex"), "w") as f:
        f.write("\n".join(tex))
