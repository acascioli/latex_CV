import json
import pathlib as plib


def P_I(resume_path, data_path):
    # Load JSON data from your file
    with open(plib.Path(data_path, "general.json")) as f:
        data = json.load(f)

    # tex = """\\name{Alessandro}{Cascioli}
    # \position{Energy Engineer{\enskip\cdotp\enskip}PhD}
    # \\address{Viale Aleardi 6, Terni, Umbria, 05100, Italy}

    # \mobile{(+39) 348 5637707}
    # \email{alessandro.cascioli@protonmail.com}
    # \googlescholar{Jg8dwfUAAAAJ&hl}{}"""

    tex = [
        "\\name{{{name}}}{{{surname}}}".format(
            name=data["basics"]["name"], surname=data["basics"]["surname"]
        ),
        "\\position{{{label_1}{{\\enskip\\cdotp\\enskip}}{label_2}}}".format(
            label_1=data["basics"]["label_1"], label_2=data["basics"]["label_2"]
        ),
        "\\address{{{address}, {city}, {region}, {postalCode}, {nation}}}".format(
            address=data["basics"]["location"]["address"],
            city=data["basics"]["location"]["city"],
            region=data["basics"]["location"]["region"],
            postalCode=data["basics"]["location"]["postalCode"],
            nation=data["basics"]["location"]["nation"],
        ),
        "\mobile{{{mobile}}}".format(mobile=data["basics"]["phone"]),
        "\email{{{email}}}".format(email=data["basics"]["email"]),
        "\googlescholar{{{googlescholar}}}{{}}".format(
            googlescholar=data["profiles"][1]["id"]
        ),
    ]

    # Save the rendered templates to a final LaTeX file
    with open(plib.Path(resume_path, "personal_information.tex"), "w") as f:
        f.write("\n".join(tex))
