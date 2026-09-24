import json
from collections import Counter
from pathlib import Path


def summarize(path: Path) -> Counter[str]:
    items = json.loads(path.read_text())
    return Counter(item["state"] for item in items)


if __name__ == "__main__":
    counts = summarize(Path(__file__).with_name("items.json"))
    for state in ("open", "closed"):
        print(f"{state}: {counts[state]}")
