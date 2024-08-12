from dataclasses import field

from apiflask import APIBlueprint
from marshmallow.validate import Length
from marshmallow_dataclass import dataclass

from watchlist.extensions import ResponseHandler

hello_bp = APIBlueprint("hello", __name__)


@dataclass
class HelloRequest:
    name: str = field(
        default="Name",
        metadata={
            "title": "名称",
            "description": "返回消息显示的信息",
            "required": True,
            "validate": Length(min=1, max=10),
        }
    )


@hello_bp.get("/")
@hello_bp.get("/<name>")
def get_hello_world(name: str = "World"):
    return ResponseHandler.ok_response({"message": f"Hello, {name}!"})


@hello_bp.post("/")
@hello_bp.input(HelloRequest.Schema)
def post_hello_world(json_data: HelloRequest):
    return ResponseHandler.ok_response({"message": f"Hello, {json_data.name}!"})
