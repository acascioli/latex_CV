import json
import pathlib as plib


def languages(resume_path, data_path):
    # Load JSON data from your file
    with open(plib.Path(data_path, "languages.json")) as f:
        data = json.load(f)
    tex_1 = [
        "\cvsection{Skills}\n",
        "\\begin{cvskills}\n",
    ]
    tex_2 = []
    for language in data["languages"]:
        tex_2.append("\cvskill")
        tex_2.append("{{{language}}}".format(language=language["language"]))
        tex_2.append("{{{fluency}}}".format(fluency=language["fluency"]))

    tex_3 = [
        "\end{cvskills}",
    ]

    tex = tex_1 + tex_2 + tex_3
    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "languages.tex"), "w") as f:
        f.write("\n".join(tex))
