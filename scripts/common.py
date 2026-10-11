from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'


def load_data(name):
    with (DATA / name).open(encoding='utf-8') as file:
        return yaml.safe_load(file)


def visible_items(filename, key):
    return [entry for entry in load_data(filename)[key] if entry.get('visible', False)]
