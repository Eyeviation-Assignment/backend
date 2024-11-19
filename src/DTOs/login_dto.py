from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class LoginDTO(DataClassJsonMixin):
    username: str
