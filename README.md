AutoCode Audit: Multi-Agent Software Engineering Guard & Security ScannerAutoCode Audit is an agentic static application security testing (SAST) tool built to automate code security reviews. It combines deterministic Abstract Syntax Tree (AST) metadata parsing with Google Gemini 3.6 Flash reasoning to spot critical software vulnerabilities, evaluate operational severity, and output refactored, production-ready code fixes.   Key FeaturesDeterministic AST Code Analysis: Extracts code structure, import statements, function definitions, and variable calls prior to AI processing using Python's built-in ast module.   Grounded AI Security Analysis: Combines AST structural metadata with raw source code snippets to reduce LLM hallucinations and yield consistent vulnerability detection.   CWE Vulnerability Classification: Identifies standard security flaws, such as OS Command Injection (CWE-78) and Hardcoded Sensitive Credentials (CWE-798).   Automated Code Refactoring: Provides refactored Python snippets implementing safe logging, environment variable extraction, and secure process execution.   Agile Jira Traceability: Engineered around a strict Scrum workflow with smart commit integration referencing Jira keys (SCRUM-13 through SCRUM-20).   Repository StructurePlaintextautocode-audit/
├── src/
│   ├── ast_parser.py          # AST extraction and metadata node parsing
│   └── security_agent.py      # Gemini 3.6 Flash agent node & reasoning
├── main.py                    # Core pipeline driver script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
Tech Stack & PrerequisitesLanguage: Python 3.10+AI Model: Google Gemini 3.6 Flash (google-generativeai)   Agile & PM Tools: Jira Software, GitHub Smart Commits   Getting Started1. Clone the RepositoryBashgit clone https://github.com/abdul99088/autocode-audit.git
cd autocode-audit
2. Install DependenciesBashpip install -r requirements.txt
3. Configure API KeySet your Google Gemini API key as an environment variable:Windows (PowerShell):PowerShell$env:GEMINI_API_KEY="your-gemini-api-key-here"
Linux/macOS:Bashexport GEMINI_API_KEY="your-gemini-api-key-here"
4. Run the PipelineExecute the main driver script to trigger AST parsing and the Gemini Security Agent:   Bashpython main.py
Example Execution OutputPlaintext=== Running AST Parser (SCRUM-18) ===
AST Analysis Result: {'status': 'success', 'functions_found': ['check_user'], 'imports_found': ['os']}

=== Running Gemini Security Agent Node (SCRUM-19) ===
Querying Gemini 3.6 Flash model... please wait...
Successfully generated using gemini-3.6-flash.

--- Security Agent Final Output ---

### 1. Architectural & Safety Risks Found
* OS Command Injection (CWE-78)
  - Risk: os.system() executes shell commands via unescaped string formatting.
* Hardcoded Sensitive Credentials (CWE-798)
  - Risk: API keys stored directly in source code.

### 2. Severity Rating
CRITICAL / HIGH

### 3. Recommended Code Refactoring
```python
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_user(user_input: str) -> None:
    api_key = os.getenv("API_KEY")
    logger.info("Checking user: %s", user_input)
Team & Scrum AllocationsTeam MemberRoleAssigned Jira KeysCore DeliverablesAbdul Vassay   Scrum Master / Lead   SCRUM-13, SCRUM-17   Repository Scaffolding & API Config   Atif Qayyum   Core Developer   SCRUM-14, SCRUM-18   AST Parser Architecture & Code Implementation   Hassan Bin Ikram   AI / Security Lead   SCRUM-15, SCRUM-19   Gemini Agent Integration & Prompt Engineering   Hashir Mansoor   QA / Systems Integration   SCRUM-16, SCRUM-20   Driver Script Integration & Pipeline Specs
