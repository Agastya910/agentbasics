import json
from datetime import datetime

from config import CAL_FILE, FMT


def load():
    with open(CAL_FILE) as f:
        return json.load(f)


def save(events):
    with open(CAL_FILE, "w") as f:
        json.dump(events, f, indent=2)


def list_events(date):
    return sorted((e for e in load() if e["start"].startswith(date)), key=lambda e: e["start"])


def find_free_slots(date):
    day_start = datetime.strptime(f"{date}T09:00", FMT)
    day_end = datetime.strptime(f"{date}T18:00", FMT)
    busy = sorted((datetime.strptime(e["start"], FMT), datetime.strptime(e["end"], FMT)) for e in list_events(date))
    free, cur = [], day_start
    for s, e in busy:
        if s > cur:
            free.append((cur, min(s, day_end)))
        cur = max(cur, e)
    if cur < day_end:
        free.append((cur, day_end))
    return [f"{a:%H:%M}-{b:%H:%M}" for a, b in free]


def add_event(title, start, end):
    events = load()
    new = {"id": max((e["id"] for e in events), default=0) + 1, "title": title, "start": start, "end": end}
    save(events + [new])
    return new


def move_event(id, start, end):
    events = load()
    for e in events:
        if e["id"] == int(id):
            e["start"], e["end"] = start, end
            save(events)
            return e
    return {"error": f"no event with id {id}"}


def delete_event(id):
    events = load()
    kept = [e for e in events if e["id"] != int(id)]
    save(kept)
    return {"deleted": len(events) - len(kept)}