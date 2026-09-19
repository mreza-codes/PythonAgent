## Python Agent – Version 2.0 Update Notes

This release introduces a cleaner, more stable, and more modular structure for the Python Agent project.  
Version 2.0 focuses on improving the core logic, simplifying the architecture, and removing unnecessary components while keeping the original database untouched.

### Key Changes Compared to Version 1.0

### 1. Refactored Core Files
- Updated and cleaned the main agent logic.
- Improved structure and readability across `main.py`, `agent.py`, `rag.py`, and `tools.py`.
- Removed unused or experimental code paths.

### 2. Simplified RAG & Memory System
- Memory files are no longer included in the repository.
- The agent now automatically creates fresh memory files on first run.
- Reduced risk of corrupted or outdated memory affecting new versions.

### 3. Database Handling
- The main ChromaDB database is **not included** in this version.
- Version 2.0 relies on the existing database from Version 1.0.
- No changes were made to the database schema or stored data.

### 4. Cleaner Project Structure
- Removed temporary folders (`dist/`, `build/`, `__pycache__/`).
- Removed PyInstaller artifacts and spec files.
- Version 2.0 contains only essential source code and assets.

### 5. UI Stability Improvements
- The PyQt6 interface remains the same but is now better integrated with the updated agent logic.
- No UI design changes, only internal stability improvements.

### Notes
- This version is intended primarily for personal use and development.
- Users who need the full database should refer to Version 1.0.
- The agent will generate new memory files automatically during runtime.
