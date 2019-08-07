from enum import Enum
from enum import unique
from typing import Any
from typing import Dict
from typing import Optional

from config import DB

_Q = Dict[str, Any]
_Doc = Optional[Dict[str, Any]]


@unique
class CollectionName(Enum):
    ACTIVITIES = "activities"
    REMOTE = "remote"


def find_one_activity(q: _Q) -> _Doc:
    return DB[CollectionName.ACTIVITIES.value].find_one(q)


def update_one_activity(q: _Q, update: _Q) -> None:
    DB[CollectionName.ACTIVITIES.value].update_one(q, update)


def update_many_activities(q: _Q, update: _Q) -> None:
    DB[CollectionName.ACTIVITIES.value].update_many(q, update)


def update_one_remote(filter_: _Q, update: _Q, upsert: bool = False) -> None:
    DB[CollectionName.REMOTE.value].update_one(filter_, update, upsert)
