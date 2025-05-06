import json

def save_authors_json(authors, path):
    data = [{'name': a.full_name, 'resident': a.is_resident} for a in authors]
    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_authors_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return [Author(a['name'], a['resident']) for a in data]
