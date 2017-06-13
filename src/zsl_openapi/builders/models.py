from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import *  # NOQA

from zsl_openapi.api import ApiDescription  # NOQA
from zsl_openapi.builders import ApiDescriptionBuilder


class ApiDescriptionSqlAlchemyModelDefinitionsBuilder(ApiDescriptionBuilder):
    def __init__(self, package):
        self._models = []

    def build(self, api_description):
        # type: (ApiDescription)->None
        pass
