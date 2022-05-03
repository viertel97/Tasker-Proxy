import os

import todoist
from loguru import logger

TODOIST_API = todoist.TodoistAPI(os.environ["TODOIST_TOKEN"])
TODOIST_API.sync()

logger.add(
    os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/logs/" + os.path.basename(__file__) + ".log"),
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    backtrace=True,
    diagnose=True,
)


def get_list(list_name):
    return [item.data for item in TODOIST_API.state[list_name]]


def add_reading_other_task(name, finished):
    TODOIST_API.sync()
    if finished:
        content = "Reading-Habit-Tracker pflegen mit: {other} + in Zotero & Obsidian einpflegen".format(other=name)
    else:
        content = "Reading-Habit-Tracker pflegen mit: {other}".format(other=name)
    item = TODOIST_API.items.add(
        content,
        project_id="2244725398",
        due={"string": "Tomorrow"},
    )
    TODOIST_API.commit()