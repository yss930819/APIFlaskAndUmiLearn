from dataclasses import field

from marshmallow.validate import Length
from marshmallow_dataclass import dataclass


@dataclass
class UserRequest:
    name: str = field(
        default="Name",
        metadata={
            "title": "用户名",
            "description": "创建用户时使用",
            "required": True,
            "validate": Length(min=1, max=10),
        }
    )


