from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import *  # NOQA
from unittest.case import TestCase


class ModelBuilderTestCase(TestCase):
    def testBuild(self):
        self.givenBuilderWithModels()
        self.whenGeneratingApiDescription()
        self.thenApiDescriptionShouldBeCorrect()

    def givenBuilderWithModels(self):
        pass

    def thenApiDescriptionShouldBeCorrect(self):
        pass

    def whenGeneratingApiDescription(self):
        pass
