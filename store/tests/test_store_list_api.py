from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from store.views import storeList, StoreList
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView

class ApiUrlsTests(SimpleTestCase):

  def test_get_store_list_is_resolved(self):
    url = reverse('store-create')
    self.assertEquals(resolve(url).func, StoreList)