# AI Agent Guidelines for IA342 (Data Visualization)

This file serves as the definitive, repository-level source of truth for any AI Agents (e.g., Antigravity, CodeX, Copilot) operating within the JMU-Data/IA342 project.

## 1. Canonical Repository Boundary
- **Public Course Content**: This repository (JMU-Data/IA342) is strictly a **PUBLIC course-content and course-presentation repository**.
- **Scope**: Allowed content includes syllabus, schedule, lecture materials, slides, Tableau exercises, ArcGIS exercises, labs, assignments, visualization examples, public/sample datasets, student onboarding, and GitHub Pages content.
- **Out of Scope (Privacy Boundary)**: This repository must **NEVER** contain:
  - Student PII (personally identifiable information)
  - Student emails, names, or rosters
  - Student grades or submissions
  - API credentials, tokens, or secrets
  - Private student repositories
  - Grading scripts or LMS administration tools
  - Canvas automation or private instructor infrastructure/operational data
- *Note: Private grading, student management, LMS automation, and instructor-only tooling belong outside this public repository (e.g., in xbwei/jmu-teaching-coding). Do not describe how private systems are implemented here.*

## 2. Role Assignments
### Antigravity (Primary Agent)
- **Role**: Primary agent for IA342.
- **Responsibilities**: Manage public course materials, repository organization, and PR management.
- **Permissions**: Can create branches, modify files, run local validations, and create Pull Requests.
- **Restrictions**:
  - **NO DIRECT PUSH TO main**.
  - **NEVER AUTO-MERGE** any Pull Request.

### Other Agents (e.g., Codex)
- Do not proactively execute tasks unless explicitly authorized by the Owner.
- **IA342 does not require automatic Codex review** for Pull Requests.

### Owner (Instructor)
- The Owner retains the final review authority and merge decision for all changes.

## 3. Strict Pull Request (PR) Workflow
All substantive changes must follow this PR workflow:
1. main branch
2. → Create new branch
3. → Implementation
4. → Local / Self-Validation
5. → Create Pull Request
6. → Wait for Checks
7. → Owner Review
8. → Owner Merge Decision

- **Self-Audit**: Before creating any PR, agents must perform a security/privacy self-audit to ensure no sensitive data or private scripts are included.
- **PR Body Requirements**: Every PR must document:
  - Scope of changes
  - Files changed
  - Validation performed
  - Security/privacy self-audit confirmation
  - Known limitations
  - Owner decision status (Ready for Review)
- Agents are not permitted to infer merge authorization just because status checks are green.

## 4. Course Identity (Context for AI)
- **IA342 is a Data Visualization course**.
- **Core Topics**: Data Visualization, Business Intelligence, Visual Analytics, Tableau, ArcGIS, Dashboards, and Data Storytelling.
- **Not a Software Engineering Course**: This is not a coding-heavy software development course. Do not introduce heavy database engineering (Cloud SQL, MongoDB), heavy Python automation workflows, API development, or software architecture topics here.

## 5. Multi-device / Fresh Clone Bootstrap
Because the Owner operates across multiple devices (personal and school computers), this repository must be self-describing from GitHub alone.
- **Authoritative Source**: The remote GitHub repository and tracked files are the only source of truth. Local project memory, chat history, uncommitted code, and machine-local auth (.env) are NOT authoritative.
- **Fresh Clone Routine**: Upon initiating work on a new device or fresh clone, Antigravity MUST:
  1. Confirm the repository and remote.
  2. Run git fetch --all --prune.
  3. Inspect the current branch and git status.
  4. Read AGENTS.md and README.md.
  5. Inspect relevant open Issues, open PRs, and recent merged PRs to rebuild context.
  6. Resume an exact remote PR branch if work is ongoing, or start a new branch from the current remote main.
  7. Bootstrap using ONLY tracked configuration/lock files.
  8. Request only the absolute minimum Owner-side machine-local auth/setup when credentials are missing.
- **Independence**: Keep IA342 self-contained. Do not depend on a local IA340 or jmu-teaching-coding checkout. If cross-repository context is needed, query the reviewed/merged remote state rather than local machine directories. Do not use unversioned status tracking files.
