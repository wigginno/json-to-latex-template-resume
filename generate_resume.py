#!/usr/bin/env python3
"""
Render a LaTeX résumé from JSON using the Jinja2 template above.

Usage
-----
python generate_resume.py resume.json resume_template.tex resume.tex
"""
import sys
import json
import collections
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from jsonschema import Draft4Validator, ValidationError


def tex_escape(text: str) -> str:
    """Escape LaTeX‐special characters in arbitrary text."""
    replace_map = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
    }
    # Also convert plain hyphen-minus surrounded by spaces into \- for dash
    text = re.sub(r" - ", r" \\- ", text)
    return "".join(replace_map.get(c, c) for c in text)


def group_education(edu_list):
    """Group consecutive education entries by institution/location."""
    grouped = collections.OrderedDict()
    for edu in edu_list:
        key = (edu["institution"], edu["location"])
        grouped.setdefault(key, []).append(edu)
    schools = []
    for (institution, location), degrees in grouped.items():
        schools.append(
            {
                "institution": institution,
                "location": location,
                "degrees": degrees,
            }
        )
    return schools


def main(json_path: str, template_path: str, output_path: str):
    data = json.loads(Path(json_path).read_text())

    with open("resume_schema.json", "r") as f:
        schema = json.load(f)
    Draft4Validator(schema).validate(data)

    # Pre‑compute grouped education
    data["schools"] = group_education(data["education"])

    # Configure Jinja2
    env = Environment(
        loader=FileSystemLoader(Path(template_path).parent or "."),
        autoescape=select_autoescape(enabled_extensions=()),
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}",
        comment_start_string="{/**",
        comment_end_string="**/}",
    )
    env.filters["tex"] = tex_escape

    template = env.get_template(Path(template_path).name)
    rendered = template.render(**data)

    # Post-process: remove extra spaces right after opening brace or before closing brace
    rendered = re.sub(r'\{\s+', '{', rendered)
    rendered = re.sub(r'\s+\}', '}', rendered)

    Path(output_path).write_text(rendered)
    print(f"Wrote → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_resume.py resume.json resume_template.tex resume.tex")
        sys.exit(1)
    main(*sys.argv[1:])
