import os
from io import StringIO
from unittest.case import TestCase

import jinja2
import yaml
from jinja2.utils import select_autoescape

from zsl_openapi.api import ApiDescription, ApiDescriptionInfo, ApiLicense, ApiContact, ApiModelDefinition, \
    ApiModelProperty, ApiTag, ApiExternalDocs
from zsl_openapi.generator import ApiGenerator


class GeneratorTestCase(TestCase):
    def render_template(self, name, context=None):
        if context is None:
            context = {}
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            autoescape=select_autoescape(['yml'])
        )
        template = env.get_template(name, context)
        return template.render(context)

    def test_template(self):
        g = ApiGenerator()
        d = self.given_api_description
        out = StringIO()
        g.generate(d, out)
        self.thenYAMLShouldBeEqual("simple_api_spec.yml", out.getvalue(), "Result of the simple generator should be "
                                                                          "correct.")

    @property
    def given_api_description(self):
        d = ApiDescription()
        d.info = ApiDescriptionInfo()
        d.info.title = 'Title'
        d.info.terms_of_service = 'Terms of Service'
        d.info.contact = ApiContact()
        d.info.contact.email = 'Email'
        d.info.version = '0.0.0'
        d.info.description = 'Description'
        d.info.license = ApiLicense()
        d.info.license.name = 'Name'
        d.info.license.url = 'Url'

        model_definition = ApiModelDefinition()
        model_definition.name = 'Model'
        model_definition.type = 'object'
        model_property = ApiModelProperty()
        model_property.name = 'Name'
        model_property.type = 'Type'
        model_property.format = 'Format'
        model_definition.add_property(model_property)
        d.add_model_definition(model_definition)

        ext_docs = ApiExternalDocs()
        ext_docs.url = "Url"
        ext_docs.description = "Description"

        tag = ApiTag()
        tag.external_docs = ext_docs
        tag.name = "TagName"
        tag.description = "TagDescription"
        d.add_tag(tag)

        d.external_docs = ext_docs
        return d

    def thenYAMLShouldBeEqual(self, template, result, message, template_context=None):
        expected_result = self.render_template(template, template_context)
        yaml_expected = yaml.load(expected_result)
        yaml_computed = yaml.load(result)
        self.assertEquals(yaml_expected, yaml_computed, message)
