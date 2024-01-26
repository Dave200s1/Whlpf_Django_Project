from  django.test import TestCase

from django.utils import timezone

from MovieUpdateView import MovieUpdateViewClass

class MovieUpdateViewTest(TestCase):
    
    @classmethod
    def test_update_form_date_field_label(self):
        pass
    
    def test_update_form_date_too_far_in_future(self):
        pass
    
    def test_update_form_date_today(self):
        pass
    
    def test_update_form_date_in_past(self):
        pass