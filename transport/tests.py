from django.test import TestCase

# Create your tests here.
class SettingsTest(TestCase):    
    def test_camara_is_configured(self):
        assert 'camara' in INSTALLED_APPS
