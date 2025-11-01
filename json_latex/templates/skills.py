import json
import pathlib as plib

SECTION_TITLES = {
    "en": "Skills",
    "it": "Competenze",
    "de": "Kompetenzen",
}


def skills(resume_path, data_path, lan="en"):
    # Load JSON data from your file
    with open(plib.Path(data_path, "skills.json")) as f:
        data = json.load(f)
    title = SECTION_TITLES.get(lan, SECTION_TITLES["en"])
    tex_1 = [
        f"\\cvsection{{{title}}}\n",
        "\\begin{cvskills}\n",
    ]
    tex_2 = []
    for skill in data["skills"]:
        tex_2.append("\cvskill")
        tex_2.append("{{{category}}}".format(category=list(skill.keys())[0]))
        tex_2.append(
            "{{{skills_list}}}".format(
                skills_list=", ".join(list(skill.values())[0]))
        )

    tex_3 = [
        "\end{cvskills}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "skills.tex"), "w") as f:
        f.write("\n".join(tex))
