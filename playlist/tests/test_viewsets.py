from rest_framework.test import APITestCase
from rest_framework import status
from playlist.models import Video, Categoria


class VideoTests(APITestCase):
    def setUp(self) -> None:
        super()
        self.url = '/videos/'
        self.categoria = Categoria.objects.create(
            titulo='Categoria 1',
            cor='blue'
        )

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
            "categoria_id": self.categoria.id
        }
        response = self.__send_post(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(Video.objects.get().titulo, data['titulo'])
        self.assertEqual(Video.objects.get().descricao, data['descricao'])
        self.assertEqual(Video.objects.get().url, data['url'])
        self.assertEqual(self.categoria.id, data['categoria_id'])

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
        """
        Test if blank fields return a error message, with code == 'blank'.
        """
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

    def test_should_list_all_videos(self):
        """
        Tests if the route GET /videos/ if working
        """
        Video.objects.create(titulo="teste", descricao="teste", url="https://test.com")
        Video.objects.create(titulo="teste 2", descricao="teste 2", url="https://teste.com", categoria=self.categoria)
        response = self.client.get(self.url)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for video in response_data:
            self.assertIn('id', video)
            self.assertIn('titulo', video)
            self.assertIn('descricao', video)
            self.assertIn('categoria', video)
            self.assertIsNotNone(video['titulo'])
            self.assertIsNotNone(video['descricao'])
            self.assertIsNotNone(video['url'])
        self.assertIsNone(response_data[0]['categoria'])
        self.assertIsNotNone(response_data[1]['categoria'])


class CategoriasViewsetTest(APITestCase):
    def setUp(self) -> None:
        super()

    def __send_post(self, data):
        return self.client.post('/categorias/', data)

    def test_should_create_categoria_if_request_is_valid(self):
        """
        Tests if a valid POST request to the /categoria/ endpoint creates a 'categoria'
        """
        data = {
            "titulo": "Backend",
            "cor": "teal"
        }
        response = self.__send_post(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(Categoria.objects.last().titulo, data['titulo'])
        self.assertEqual(Categoria.objects.last().cor, data['cor'])

    def test_should_list_videos_of_categoria(self):
        """
        Test if is possible to list the videos by a category.
        """
        categoria = Categoria.objects.create(
            titulo='test_hi',
            cor='black'
        )
        Video.objects.create(
            titulo='test_video',
            descricao='lorem ipsum hello world.!',
            url='http://localhost.com',
            categoria=categoria
        )
        response = self.client.get(f'/categorias/{categoria.id}/videos')
        videos = response.data
        self.assertEqual(len(videos), 1)
        self.assertEqual(type(videos[0]['titulo']), str)
        self.assertEqual(type(videos[0]['id']), int)
        print(videos[0][categoria])
        self.assertEqual(type(videos[0]['descricao']), str)
        self.assertEqual(type(videos[0]['url']), str)

    def test_should_list_categories(self):
        Categoria.objects.create(
            titulo="Categoria 1",
            cor="#CCCCDD"
        )

        response = self.client.get('/categorias/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(type(response.data[0]['titulo']), str)
        self.assertEqual(type(response.data[0]['id']), int)
        self.assertEqual(type(response.data[0]['cor']), str)
