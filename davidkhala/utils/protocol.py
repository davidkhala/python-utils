from typing import Protocol


class ID(Protocol):
    id: str


class SupportsClose(Protocol):
    def close(self) -> None: ...
