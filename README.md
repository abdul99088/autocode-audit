# AutoCode Audit: Multi-Agent Software Engineering Guard & Security Scanner

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![AI Model](https://img.shields.io/badge/AI-Gemini%203.6%20Flash-orange.svg)](https://deepmind.google/technologies/gemini/)
[![Agile Framework](https://img.shields.io/badge/Agile-Scrum-green.svg)](https://www.atlassian.com/software/jira)

**AutoCode Audit** is an agentic static application security testing (SAST) tool built to automate code security reviews. It combines deterministic Abstract Syntax Tree (AST) metadata parsing with Google Gemini 3.6 Flash reasoning to spot critical software vulnerabilities, evaluate operational severity, and output refactored, production-ready code fixes.

---

## Key Features

* **Deterministic AST Code Analysis:** Extracts code structure, import statements, function definitions, and variable calls prior to AI processing using Python's built-in `ast` module.
* **Grounded AI Security Analysis:** Combines AST structural metadata with raw source code snippets to reduce LLM hallucinations and yield consistent vulnerability detection[cite: 1].
* **CWE Vulnerability Classification:** Identifies standard security flaws, such as OS Command Injection (CWE-78) and Hardcoded Sensitive Credentials (CWE-798)[cite: 1].
* **Automated Code Refactoring:** Provides refactored Python snippets implementing safe logging, environment variable extraction, and secure process execution[cite: 1].
* **Agile Jira Traceability:** Engineered around a strict Scrum workflow with smart commit integration referencing Jira keys (`SCRUM-13` through `SCRUM-20`)[cite: 1].

---

## Repository Structure

```text
autocode-audit/
├── src/
│   ├── ast_parser.py          # AST extraction and metadata node parsing
│   └── security_agent.py      # Gemini 3.6 Flash agent node & reasoning
├── main.py                    # Core pipeline driver script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
