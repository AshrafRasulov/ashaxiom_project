Этот файл нужно создать в корневой папке проекта (`ashaxiom_project/`). Он содержит **строгие правила**, по которым нужно добавлять новые книги.

```markdown
# AshAxiom Developer Guide 📘

To maintain the intelligence and stability of the library, all contributors must follow these strict rules when adding new mathematical modules.

### 1. Directory Structure
New books must be placed in: 
`ashaxiom/lib/{Section}/hmBooks/{AuthorName}/`

- **Section**: Broad category (e.g., `hMath`, `Physics`, `Finance`).
- **Author**: Use the author's last name (e.g., `Newton`, `Euler`).
- **Book**: Filename should be `hmBookXX.py` or similar.

*Always include an empty `__init__.py` in every new directory.*

### 2. Mandatory Class Metadata
Every book class must define its identity so the AI Brain can report sources correctly:
```python
class MyNewBook:
    __title__ = "Calculus Volume 10"
    __author__ = "Author Name"

# AshAxiom Developer Guide 📘

This document defines the strict rules for expanding the AshAxiom knowledge base.

## 1. Directory Hierarchy
New knowledge must follow the path:
`ashaxiom/lib/{Section}/hmBooks/{Author}/{Book}.py`

- **Section**: Domain (e.g., `hMath`, `Physics`, `Economics`).
- **Author**: Last name of the author folder.
- **Book**: Python file containing the class.

*Every folder MUST contain an empty `__init__.py` file.*

## 2. Book Class Requirements
Every class within a book file must provide identity metadata for the AI Brain:

```python
class hmBookName:
    __title__ = "Full Title of the Book/Module"
    __author__ = "Original Author Name"

    def __init__(self):
        self.value = None # Storage for results    