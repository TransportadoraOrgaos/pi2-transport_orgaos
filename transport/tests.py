from django.test import TestCase
from transportadora_orgaos.settings import INSTALLED_APPS


# TESTE PARA NAO QUEBRAR A BUILD
class SettingsTest(TestCase):    
    def test_transport_is_configured(self):
        assert 'transport' in INSTALLED_APPS
