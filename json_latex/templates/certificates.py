import json
import pathlib as plib
from datetime import datetime

SECTION_TITLES = {
    "en": "Certificates",
    "it": "Certificati",
    "de": "Zertifikate",
}


def certificates(resume_path, data_path, lan="en"):
    # Load JSON data from your file
    with open(plib.Path(data_path, "certificates.json")) as f:
        data = json.load(f)

    title = SECTION_TITLES.get(lan, SECTION_TITLES["en"])
    tex_1 = [
        f"\\cvsection{{{title}}}\n",
        "\\begin{cvhonors}\n",
    ]
    tex_2 = []
    for certificate in data["certificates"]:
        tex_2.append("\cvhonor")
        tex_2.append("{{{name}}}".format(name=certificate["name"]))
        tex_2.append("{}")
        tex_2.append("{{{issuer}}}".format(issuer=certificate["issuer"]))
        date_obj = datetime.strptime(certificate["date"], "%Y-%m-%d")
        date = date_obj.strftime("%Y")
        tex_2.append("{{{date}}}".format(date=date))

    tex_3 = [
        "\end{cvhonors}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "certificates.tex"), "w") as f:
        f.write("\n".join(tex))
