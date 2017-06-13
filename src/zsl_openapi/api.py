from typing import Dict

from typing import List

from werkzeug.datastructures import ImmutableDict, ImmutableList


class ApiExternalDocs:
    def __init__(self):
        self.description = None  # type: str
        self.url = None  # type: str


class ApiTag:
    def __init__(self):
        self.name = None  # type: str
        self.description = None  # type: str
        self.external_docs = ApiExternalDocs()


class ApiLicense:
    def __init__(self):
        self.name = None  # type:str
        self.url = None  # type:str


class ApiContact:
    def __init__(self):
        self.email = None  # type:str


class ApiDescriptionInfo:
    def __init__(self):
        self.description = None  # type: str
        self.version = None  # type: str
        self.title = None  # type: str
        self.terms_of_service = None  # type: str
        self.contact = ApiContact()
        self.license = ApiLicense()


class ApiModelProperty:
    def __init__(self):
        self.name = None  # type: str
        self.type = None  # type: str
        self.format = None  # type: str


class ApiModelDefinition:
    def __init__(self):
        self.name = None  # type: str
        self.type = None  # type: str
        self._properties = {}  # type: Dict[str, ApiModelProperty]

    @property
    def properties(self) -> Dict[str, ApiModelProperty]:
        return ImmutableDict(self._properties)

    def add_property(self, model_property: ApiModelProperty):
        self._properties[model_property.name] = model_property


class ApiDescription:
    def __init__(self):
        self.info = ApiDescriptionInfo()
        self.external_docs = ApiExternalDocs()
        self._tags = []  # type: List[ApiTag]
        self._definitions = {}  # type: Dict[str, ApiModelDefinition]

    @property
    def tags(self) -> List[ApiTag]:
        return ImmutableList(self._tags)

    @property
    def definitions(self) -> Dict[str, ApiModelDefinition]:
        return ImmutableDict(self._definitions)

    def add_model_definition(self, model_definition: ApiModelDefinition) -> None:
        self._definitions[model_definition.name] = model_definition

    def add_tag(self, tag):
        self._tags.append(tag)
