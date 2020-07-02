import json
from dataclasses import dataclass


@dataclass(init=False)
class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
