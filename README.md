# json-to-latex-template-resume

Uses Jinja2 template injection to convert my JSON-formatted resume into a nice looking "Overleaf Jake"-inspired resume.

This allows me to edit JSON instead of directly editing my eyesore of a .tex file.

## Usage

```bash
python generate_resume.py resume.json resume_template.tex resume.tex
```

## Schema for resume.json

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "contact": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "github": {
          "type": "string"
        },
        "linkedin": {
          "type": "string"
        }
      },
      "required": [
        "location",
        "email",
        "github",
        "linkedin"
      ]
    },
    "education": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "institution": {
              "type": "string"
            },
            "location": {
              "type": "string"
            },
            "degree": {
              "type": "string"
            },
            "graduationDate": {
              "type": "string"
            },
            "relevantCourses": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "institution",
            "location",
            "degree",
            "graduationDate",
            "relevantCourses"
          ]
        },
        {
          "type": "object",
          "properties": {
            "institution": {
              "type": "string"
            },
            "location": {
              "type": "string"
            },
            "degree": {
              "type": "string"
            },
            "graduationDate": {
              "type": "string"
            },
            "relevantCourses": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "institution",
            "location",
            "degree",
            "graduationDate",
            "relevantCourses"
          ]
        }
      ]
    },
    "experience": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "organization": {
              "type": "string"
            },
            "location": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "dates": {
              "type": "string"
            },
            "achievements": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "organization",
            "location",
            "title",
            "dates",
            "achievements"
          ]
        }
      ]
    },
    "projects": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "url": {
              "type": "string"
            },
            "technologies": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "details": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "name",
            "url",
            "technologies",
            "details"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "url": {
              "type": "string"
            },
            "technologies": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "details": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "name",
            "url",
            "technologies",
            "details"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "url": {
              "type": "string"
            },
            "technologies": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "details": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "name",
            "url",
            "technologies",
            "details"
          ]
        }
      ]
    },
    "technicalSkills": {
      "type": "object",
      "properties": {
        "languages": {
          "type": "array",
          "items": [
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            }
          ]
        },
        "frameworksAndLibraries": {
          "type": "array",
          "items": [
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            }
          ]
        },
        "tools": {
          "type": "array",
          "items": [
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            }
          ]
        }
      },
      "required": [
        "languages",
        "frameworksAndLibraries",
        "tools"
      ]
    },
    "certifications": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "issuer": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "date": {
              "type": "string"
            }
          },
          "required": [
            "issuer",
            "name",
            "date"
          ]
        }
      ]
    }
  },
  "required": [
    "name",
    "contact",
    "education",
    "experience",
    "projects",
    "technicalSkills",
    "certifications"
  ]
}
```
