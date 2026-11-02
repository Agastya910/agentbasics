from tools.calendar_tools import list_events, find_free_slots, add_event, move_event, delete_event

TOOLS = {f.__name__: f for f in [list_events, find_free_slots, add_event, move_event, delete_event]}


def schema(fn, desc, **params):
    return {"type": "function", "function": {
        "name": fn.__name__, "description": desc,
        "parameters": {"type": "object",
                       "properties": {k: {"type": t, "description": d} for k, (t, d) in params.items()},
                       "required": list(params)}}}


DATE = ("string", "YYYY-MM-DD")
TIME = "YYYY-MM-DDTHH:MM"

SCHEMAS = [
    schema(list_events, "List all events on a date.", date=DATE),
    schema(find_free_slots, "Free time between 09:00 and 18:00 on a date.", date=DATE),
    schema(add_event, "Create an event.", title=("string", "event title"), start=("string", TIME), end=("string", TIME)),
    schema(move_event, "Reschedule an event.", id=("integer", "event id"), start=("string", TIME), end=("string", TIME)),
    schema(delete_event, "Delete an event.", id=("integer", "event id")),
]