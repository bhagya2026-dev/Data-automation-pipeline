## Project Structure

```
data-automation-demo/
│
├── .github/
│   └── workflows/
│       └── data-pipeline.yml
│
├── data/
│   ├── raw/
│   │   └── customers.csv
│   └── processed/
│
├── prepare_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.x
- Git
- pip

---

## Clone the Repository

```bash
git clone <repository-url>
```

## Create a Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Data Pipeline

```bash
python prepare_data.py
```

