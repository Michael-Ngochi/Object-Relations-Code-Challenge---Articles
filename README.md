# Articles Database Project

This is a terminal-based Python project for managing a publication system with Authors, Magazines, and Articles using SQLAlchemy ORM and SQLite. Users can perform CRUD operations directly through the terminal.

## Features

- Add and view authors, magazines, and articles
- Search by ID, name, title, and category
- Relationship management (e.g., articles linked to authors and magazines)

## Technologies

- Python 3.11+
- SQLite (via SQLAlchemy ORM)
- Pytest (for automated testing)
- CLI interface via main.py

## Project Structure

```
Object-Relations-Code-Challenge---Articles/
├── lib/
│   ├── db/              # Database engine, session, seed
│   └── models/          # ORM models for Author, Magazine, Article
├── scripts/             # CLI setup and seed scripts
├── tests/               # Pytest test cases
├── main.py              # Terminal interface for CRUD
├── README.md            # This file
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd Object-Relations-Code-Challenge---Articles
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Initialize the database

```bash
python scripts/setup_db.py
python scripts/seed_data.py
```

### 4. Run the CLI

```bash
python main.py
```

## Running Tests

```bash
pytest tests/
```

## Example Usage

MAIN MENU
1. Create Author
2. Create Magazine
3. Create Article
4. View Authors
5. View Magazines
6. View Articles
0. Exit

## Author Deliverables

- Save to DB
- Find by ID or name
- Name validation
- View articles written

## Magazine Deliverables

- Save to DB
- Find by ID, name, or category
- Name/category validation
- View articles published

## Article Deliverables

- Save to DB
- Find by ID, title, author, or magazine
- Title validation
- Access linked author and magazine


## Author

Developed by Michael Ngochi