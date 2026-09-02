"""
Crypto Research Copilot

Research-only agent prototype.
This module creates a structured research plan from a project name.

It does NOT:
- execute trades
- manage funds
- connect to financial accounts
- provide investment advice
"""

from dataclasses import dataclass, asdict
from typing import List
import json


@dataclass
class ResearchPlan:
    project: str
    objective: str
    research_areas: List[str]
    verification_checks: List[str]
    open_questions: List[str]


def create_research_plan(project_name: str) -> ResearchPlan:
    project = project_name.strip()

    if not project:
        raise ValueError("Project name cannot be empty.")

    objective = (
        f"Create a structured research plan for {project}, "
        "identify important research areas, and highlight "
        "information that should be independently verified."
    )

    research_areas = [
        "Problem & Purpose",
        "Technology",
        "Development & Maintenance",
        "Core Features",
        "Documentation & Primary Sources",
        "Limitations & Risks",
    ]

    verification_checks = [
        "Check official documentation and primary sources.",
        "Compare important claims with independent information.",
        "Review development activity where applicable.",
        "Identify limitations and unresolved questions.",
        "Separate verified facts from assumptions.",
    ]

    open_questions = [
        "What information is still missing?",
        "Which claims require additional verification?",
        "Which assumptions should be tested?",
    ]

    return ResearchPlan(
        project=project,
        objective=objective,
        research_areas=research_areas,
        verification_checks=verification_checks,
        open_questions=open_questions,
    )


def create_report(project_name: str) -> str:
    plan = create_research_plan(project_name)

    report = f"""
# Research Report: {plan.project}

## Research Objective

{plan.objective}

## Key Research Areas

"""

    for area in plan.research_areas:
        report += f"- {area}\n"

    report += """
## Verification Checklist

"""

    for check in plan.verification_checks:
        report += f"- {check}\n"

    report += """
## Open Questions

"""

    for question in plan.open_questions:
        report += f"- {question}\n"

    report += """
## Prototype Notice

This is an informational research prototype.
It does not execute trades, manage funds, connect financial
accounts, or provide investment advice.

Important claims should be independently verified using
reliable primary and independent sources.
"""

    return report


def create_json_report(project_name: str) -> str:
    plan = create_research_plan(project_name)
    return json.dumps(asdict(plan), indent=2)


if __name__ == "__main__":
    print("Crypto Research Copilot")
    print("Research-only prototype")
    print()

    project = input("Enter project name: ").strip()

    try:
        print(create_report(project))
    except ValueError as error:
        print(f"Error: {error}")
