import json
from typing import List
from dataclasses import dataclass


@dataclass(init=False)
class BaseModel:
    """Abstract class for feature class. Useful for pretty print and automatically set attribute"""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return json.dumps(vars(self), indent=4)



@dataclass(init=False)
class BaseListModel:
    has_more: bool
    data: List[any]

    """Abstract class for feature class. Useful for pretty print and automatically set attribute"""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return json.dumps({
            "has_more": self.has_more,
            "data": [
                vars(d) for d in self.data
            ]
        }, indent=4)
