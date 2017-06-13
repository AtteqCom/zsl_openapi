from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import *  # NOQA
from inspect import isclass

from sqlalchemy.orm.attributes import InstrumentedAttribute
from zsl.db.model.sql_alchemy import DeclarativeBase
from zsl.utils.string_helper import camelcase_to_underscore

from zsl_openapi.api import ApiDescription  # NOQA
from zsl_openapi.api import ApiModelDefinition  # NOQA
from zsl_openapi.api import ApiModelProperty  # NOQA
from zsl_openapi.builders import ApiDescriptionBuilder


class ApiDescriptionSqlAlchemyModelDefinitionsBuilder(ApiDescriptionBuilder):
    def __init__(self, package):
        self._models = []
        self._append_models(package)

    def _append_models(self, package):
        for model in package.__dict__.values():
            if not isclass(model):
                continue

            if not issubclass(model, DeclarativeBase):
                continue

            if model == DeclarativeBase:
                continue

            self._models.append(model)

    def build(self, api_description):
        # type: (ApiDescription)->None
        for model in self._models:
            model_definition = self._generate_openapi_from_model(model)
            api_description.add_model_definition(model_definition)

    def _generate_openapi_from_model(self, model):
        # type: (DeclarativeBase)->ApiModelDefinition
        model_definition = ApiModelDefinition()
        model_definition.name = model.__name__
        model_definition.type = "object"

        for column_name in model.__dict__:
            column = getattr(model, column_name)
            if not isinstance(column, InstrumentedAttribute):
                continue

            property_definition = ApiModelProperty()
            property_definition.name = column_name
            property_definition.type = camelcase_to_underscore(type(column.type).__name__)
            model_definition.add_property(property_definition)

        return model_definition
