import json
from pathlib import Path

DATA_FILES = Path(__file__).parent.parent / 'data' / 'data.json'

DATA_FILES.parent.mkdir(parents=True, exist_ok=True)

# Para manejar mi database con .json
def load_users():
    if DATA_FILES.exists():
        with open(DATA_FILES, 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(DATA_FILES, 'w') as file:
        json.dump(users, file, indent=4)

if not DATA_FILES.exists():
    save_users({})
    print(f"\n{DATA_FILES} was created!\n")
else:
    print(f"\n{DATA_FILES} was updated!\n")
   