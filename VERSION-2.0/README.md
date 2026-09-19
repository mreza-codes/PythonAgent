## Python Agent – Version 2.0 Changes

Version 2.0 introduces two major improvements over Version 1.0:

### 1. Agentic RAG System
- The agent now uses an Agentic RAG loop instead of a simple retrieval system.
- Supports multi-step reasoning, tool usage, and structured actions.
- More stable decision-making and better handling of complex queries.

### 2. Persistent Memory System
- Added a lightweight memory module that stores user interactions.
- Memory files are created automatically at runtime (not included in the repository).
- Allows the agent to maintain context across sessions.

### Notes
- The database from Version 1.0 is unchanged and not included in this version.
- Only core source files were updated; no changes were made to the UI or database structure.
