# 🥒 Belly BDD Example

A simple BDD example using Python and Behave.

## Setup Instructions

1. Clone this repository or download the folder:
   ```bash
   git clone https://github.com/Pruebas-de-Software/Behave-hello-world.git
   cd belly-bdd
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   .\venv\Scripts\activate         # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the tests

Just run:

```bash
behave
```

You should see output indicating which scenarios passed or failed.

## Project Structure

```
belly-bdd/
├── belly.py
├── requirements.txt
├── features/
│   ├── belly.feature
│   └── steps/
│       └── belly_steps.py
└── README.md
```

Happy testing! 💚
