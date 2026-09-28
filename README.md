# AutoCode Audit: Multi-Agent Software Engineering Guard & Security Scanner

**AutoCode Audit** is an agentic static application security testing (SAST) tool built to automate code security reviews. It combines deterministic Abstract Syntax Tree (AST) metadata parsing with Google Gemini 3.6 Flash reasoning to spot critical software vulnerabilities, evaluate operational severity, and output refactored, production-ready code fixes.

## Table of Contents

1. [Project Overview & Key Features](#1-project-overview--key-features)

2. [Team & Scrum Allocations](#2-team--scrum-allocations)

3. [System Architecture & Design](#3-system-architecture--design)

4. [Getting Started & Usage](#4-getting-started--usage)

5. [Assignment 1 (P-1) Deliverables](#5-assignment-1-p-1-deliverables)

6. [Assignment 2 (P-2) Execution & Traceability](#6-assignment-2-p-2-execution--traceability)

7. [Assignment 3 (P-3) Final Engineering Report](#7-assignment-3-p-3-final-engineering-report)

8. [Assignment 4 (P-4) Demo & Viva Prep Guide](#8-assignment-4-p-4-demo--viva-prep-guide)

## 1. Project Overview & Key Features

### Overview

*AutoCode Audit* acts as an intelligent software guardrail during the development process. By parsing raw Python source code into an Abstract Syntax Tree (AST) before feeding structural metadata to an advanced LLM (Gemini 3.6 Flash), the system eliminates common AI hallucinations and grounds security findings in exact code constructs.

### Key Features

* **Deterministic AST Code Analysis:** Extracts code structure, import statements, function definitions, and variable calls prior to AI processing using Python's built-in `ast` module.

* **Grounded AI Security Analysis:** Combines AST structural metadata with raw source code snippets to yield consistent vulnerability detection.

* **CWE Vulnerability Classification:** Identifies standard security flaws, such as OS Command Injection (CWE-78) and Hardcoded Sensitive Credentials (CWE-798).

* **Automated Code Refactoring:** Provides refactored Python snippets implementing safe logging, environment variable extraction, and secure process execution.

* **Agile Jira Traceability:** Engineered around a strict Scrum workflow with smart commit integration referencing Jira keys (`SCRUM-13` through `SCRUM-20`).

## 2. Team & Scrum Allocations

| **Team Member** | **Role** | **Assigned Jira Keys** | **Core Deliverables** | 
| **Abdul Vassay** | Scrum Master / Lead | `SCRUM-13`, `SCRUM-17` | Repository Scaffolding & API Config | 
| **Atif Qayyum** | Core Developer | `SCRUM-14`, `SCRUM-18` | AST Parser Architecture & Code Implementation | 
| **Hassan Bin Ikram** | AI / Security Lead | `SCRUM-15`, `SCRUM-19` | Gemini Agent Integration & Prompt Engineering | 
| **Hashir Mansoor** | QA / Systems Integration | `SCRUM-16`, `SCRUM-20` | Driver Script Integration & Pipeline Specs | 

## 3. System Architecture & Design

### Repository Structure

```
autocode-audit/
├── src/
│   ├── ast_parser.py          # AST extraction and metadata node parsing
│   └── security_agent.py      # Gemini 3.6 Flash agent node & reasoning
├── main.py                    # Core pipeline driver script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

```

### High-Level Data Flow

```
[ Raw Python Code ]
        │
        ▼
┌──────────────────────────────┐
│  ast_parser.py               │
│  - Parses Syntax Tree        │
│  - Extracts Metadata         │
└──────────────┬───────────────┘
               │ (Metadata + Source Code)
               ▼
┌──────────────────────────────┐
│  security_agent.py           │
│  - Gemini 3.6 Flash Node     │
│  - Multi-Model Fallback      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  main.py (Driver Script)    │
│  - Displays Audit Findings   │
│  - Shows Refactored Code     │
└──────────────────────────────┘

```

## 4. Getting Started & Usage

### 1. Clone the Repository

```
git clone https://github.com/abdul99088/autocode-audit.git
cd autocode-audit

```

### 2. Install Dependencies

```
pip install -r requirements.txt

```

### 3. Configure API Key

Set your Google Gemini API key as an environment variable:

* **Windows (PowerShell):**

  ```
  $env:GEMINI_API_KEY="your-gemini-api-key-here"
  
  ```

* **Linux / macOS:**

  ```
  export GEMINI_API_KEY="your-gemini-api-key-here"
  
  ```

### 4. Run the Pipeline

Execute the main driver script to trigger AST parsing and the Gemini Security Agent:

```
python main.py

```

## 5. Assignment 1 (P-1) Deliverables

* **Project Title:** AutoCode Audit: Multi-Agent Software Engineering Guard & Security Scanner

* **Jira Board:** `AutoCode Audit CEP`

* **GitHub Repository:** `https://github.com/abdul99088/autocode-audit`

* **API Connection Validation:** Verified successful authentication and inference with `gemini-3.6-flash`.

## 6. Assignment 2 (P-2) Execution & Traceability

### Backlog & Work Items

* **Sprint 0 (`SCRUM-13` – `SCRUM-16`):** Project setup, environment configuration, AST design, and driver architecture.

* **Sprint 1 (`SCRUM-17` – `SCRUM-20`):** Core code implementation, AST parser module, security scanner agent, and main execution integration.

### Git Smart Commit Pattern

All commits are linked directly to Jira tasks using ticket keys:

```
git commit -m "SCRUM-18 SCRUM-19: Updated main execution print statements to match Jira tickets"
git push origin main

```

## 7. Assignment 3 (P-3) Final Engineering Report

### 1. Functional Requirements (FR)

* **FR-1:** Parse Python source code snippets into AST trees (`ast_parser.py`).

* **FR-2:** Pass structural AST metadata and raw code to Gemini 3.6 Flash for automated vulnerability detection (`security_agent.py`).

* **FR-3:** Classify security flaws according to CWE standards (e.g., CWE-78, CWE-798).

* **FR-4:** Output refactored Python code snippets resolving identified flaws.

### 2. Non-Functional Requirements (NFR)

* **NFR-1:** Multi-model fallback handling for API throttling.

* **NFR-2:** 100% commit-to-issue traceability via Jira keys.

* **NFR-3:** Execution time under 5 seconds per single-file scan.

## 8. Assignment 4 (P-4) Demo & Viva Prep Guide

### Demo Script (3-5 Minutes)

1. **Introduction:** State the project title and purpose (Agentic SAST tool combining AST + LLM).

2. **Terminal Execution:** Run `python main.py`. Highlight the AST parser output followed by the Gemini Security Agent report.

3. **Agile Evidence:** Display the completed Jira List View (`SCRUM-13` to `SCRUM-20`) and GitHub commit log.

### Viva Role Defense

* **Abdul Vassay (Scrum Master / Lead):** Focus on project scaffolding, environment variables, and fallback handling strategy.

* **Atif Qayyum (Core Developer):** Explain why AST metadata is essential for grounding LLM prompts and eliminating hallucinations.

* **Hassan Bin Ikram (AI Lead):** Detail prompt engineering techniques, section header enforcement, and CWE taxonomy classification.

* **Hashir Mansoor (QA / Integration):** Discuss `main.py` pipeline orchestration and Smart Commit git integration.
