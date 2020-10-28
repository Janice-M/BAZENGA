from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.response import Response
# from rest_framework.views import APIView
# from . serializers import MeasurementSerializer
from rest_framework import status
from measurement.measures import Distance
from .models import Measurement
import json

# Create your tests here.

client  = Client()

class ConvertMeasurementsTest(TestCase):
    ''' Test module for converting measurements '''

    def setUp(self):
        self.valid_payload = {
            'val':6,
            'unit_1':'m',
            'unit_2':"yd"
        }
        self.invalid_payload = {
            'value':6,
            'unit_1':'m',
            'unit_2':"yd"
        }

    def test_convert_valid_payloas(self):
        response = client.post(
            reverse('measurements_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_convert_invalid_payloas(self):
        response = client.post(
            reverse('measurements_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)