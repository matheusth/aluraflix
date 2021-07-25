from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from playlist.models import Video


class VideoTests(APITestCase):
    def setUp(self) -> None:
        super()
        self.url = '/videos/'

    def __send_post(self, data):
        return self.client.post(self.url, data)

    def test_should_create_video_if_request_is_valid(self):
        """
        Tests if with a valid request is possible to create a video.
        """
        data = {
            "titulo": "Teste 1",
            "descricao": "Lorem ipsum dolor sit ammet.",
            "url": "http://localhost",
        }
        response = self.__send_post(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(Video.objects.get().titulo, data['titulo'])
        self.assertEqual(Video.objects.get().descricao, data['descricao'])
        self.assertEqual(Video.objects.get().url, data['url'])

    def test_should_return_bad_request_if_url_is_invalid(self):
        """
        Test if with a invalid url the API will return a bad request
        """
        invalid_data = {
            "titulo": "Teste 1",
            "descricao": "Lorem ipsum dolor sit ammet.",
            "url": "teste",
        }
        response = self.__send_post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_return_bad_request_if_any_field_is_blank(self):
        blank_data = {
            "titulo": "",
            "descricao": "",
            "url": "",
        }

        response = self.__send_post(blank_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['titulo'][0].code, 'blank')
        self.assertEqual(response.data['descricao'][0].code, 'blank')
        self.assertEqual(response.data['url'][0].code, 'blank')
