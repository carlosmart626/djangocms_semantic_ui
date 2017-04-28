# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_semantic_ui.models import Segment


class SegmentTestCase(TestCase):

    def setUp(self):
        pass

    def test_models(self):
        segment = Segment.objects.create(
            label='Test',
            color='green',
            inverted_color=False,
            type_segment='raised'
        )
        self.assertEqual("green", str(segment))
        self.assertEqual("Test green <raised>", segment.get_short_description())
        self.assertEqual("green raised", segment.get_classes())
