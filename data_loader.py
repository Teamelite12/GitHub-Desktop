# BUGGY VERSION
# Inefficient + poor error handling + dead code

import json

def load_json(path):
    f = open(path)
    data = f.read()
    f.close()
    return json.loads(data)

def load_lines(path):
    with open(path) as f:
        return [l.strip() for l in f.readlines() if l.strip() != ""]
    return []  # unreachable