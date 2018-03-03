from typing import List, Callable
from typing import Optional


class OpenAPIMetadata:

    def __init__(self):
        self.tags = []  # type: List[str]
        self.operation_id = None  # type: Optional[str]
        self.summary = None  # type: Optional[str]


class OpenAPI:

    @staticmethod
    def tags(tags: List[str]) -> Callable[[type], type]:
        def wrapper(cls: type) -> type:
            meta = get_metadata(cls)
            meta.tags = tags
            return cls

        return wrapper

    @staticmethod
    def operation_id(operation_id: str) -> Callable[[type], type]:
        def wrapper(cls: type) -> type:
            meta = get_metadata(cls)
            meta.operation_id = operation_id
            return cls

        return wrapper

    @staticmethod
    def summary(summary: str) -> Callable[[type], type]:
        def wrapper(cls: type) -> type:
            meta = get_metadata(cls)
            meta.summary = summary
            return cls

        return wrapper


def get_metadata(cls: type) -> OpenAPIMetadata:
    if not hasattr(cls, '__open_api__'):
        cls.__open_api__ = OpenAPIMetadata()
    return cls.__open_api__
