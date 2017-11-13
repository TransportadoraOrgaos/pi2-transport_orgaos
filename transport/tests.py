from django.test import TestCase
from transportadora_orgaos.settings import INSTALLED_APPS

# Create your tests here.

class SettingsTest(TestCase):    
    def test_camara_is_configured(self):
        assert 'camara' in INSTALLED_APPS