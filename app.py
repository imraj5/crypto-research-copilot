"""
Crypto Research Copilot
Starter project for an AI research agent.

This version does NOT execute trades or handle funds.
"""

def create_research_report(project_name):
    return f"""
# Research Report: {project_name}

## Overview
Research information about {project_name} and organize
the important facts into a clear report.

## Key Things to Research
- What does the project do?
- What technology does it use?
- Who develops or maintains it?
- What are its main features?
- What information can be independently verified?

## Things to Verify
- Official documentation
- Project claims
- Development activity
- Important risks or limitations

## Open Questions
- What information is still missing?
- Which claims need additional verification?

## Important Note
This is an informational research tool.
It does not provide investment advice and does not execute trades.
"""


if __name__ == "__main__":
    project = input("Enter project name: ")
    print(create_research_report(project))
