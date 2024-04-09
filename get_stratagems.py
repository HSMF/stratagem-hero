import sys
from bs4 import BeautifulSoup
import json
import os

with open(sys.argv[1] or "a.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

def map_dir(dir):
    if dir == "Arrow 4 U":
        return "up"
    if dir == "Arrow 1 D":
        return "down"
    if dir == "Arrow 2 L":
        return "left"
    if dir == "Arrow 3 R":
        return "right"

    raise ValueError("invalid dir: " + dir)

all = []

for row in soup.find_all("tr"):
    children = row.find_all("td")
    if len(children) == 0:
        continue
    name = children[1].text.strip()
    icon_loc = children[0].find("img")
    icon = None
    alt = None
    if icon_loc is not None:
        icon = icon_loc.get("data-src")
        alt = icon_loc.get("alt").replace("icon", "")
    if icon is None or alt is None:
        continue
    path = f"src/assets/stratagems/{alt.replace(' ', '-')}.png"
    os.system(f"curl --silent -o '{path}' '{icon}'")
    all.append({
        "name": name,
        "path": path,
        "alt": alt,
        "code": [
            map_dir(x.get("alt")) for x in
            children[2].find_all("img")
        ]
    })

with open("stratagems.json", "w") as f:
    json.dump(all, f)
