# Wildfire Simulator (FastAPI)

Simple cellular-automata wildfire simulator served as a small FastAPI web app.

## Requirements

- Python 3.10+ (tested with Python 3.12)

## Quickstart

Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the dev server:

```bash
uvicorn main:app --reload
```

Open:

- `http://127.0.0.1:8000/` (UI)

## Endpoints

- `GET /` renders a small HTML UI.
- `GET /render?density=0.60&steps=50` runs the simulation and returns a PNG.

Parameters:

- `density` (float, 0.0–1.0): initial fraction of tree cells
- `steps` (int, >= 0): number of simulation steps to run

## Project layout

- `main.py`: FastAPI app + image rendering
- `fire.py`: simulation code (`simulate_fire`)
