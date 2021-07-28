from django.test import testcases
from playlist.models import Categoria, Video
from django.db.utils import IntegrityError


class CategoriaModelTestCase(testcases.TestCase):
    def setUp(self) -> None:
        self.titulo = "Hello World!"
        self.cor = 'teal'

    def test_should_save_categoria_if_no_info_is_null(self):
        Categoria.objects.create(titulo=self.titulo, cor=self.cor)
        self.assertEqual(Categoria.objects.count(), 1)
        self.assertEqual(Categoria.objects.last().titulo, self.titulo)
        self.assertEqual(Categoria.objects.last().cor, self.cor)

    def test_should_failed_to_save_categoria_if_some_info_is_null(self):
        with self.assertRaises(IntegrityError):
            Categoria.objects.create(titulo=self.titulo, cor=None)
            with self.assertRaises(IntegrityError):
                Categoria.objects.create(titulo=None, cor=self.cor)


class VideoModelTest(testcases.TestCase):
    def setUp(self) -> None:
        self.categoria = Categoria.objects.create(titulo='Backend', cor='purple')

    def test_should_create_video_in_a_category(self):
        video = Video.objects.create(
            titulo='Thread no Discord, adeus Slack para comunidades',
            descricao='Agora o Discord tem a'
                      'funcionlildade de Threads (conversas) e de'
                      'fato não temos nenhum motivo para usar o Slack para comunidades de'
                      'programação ou comunidades de opensources!',
            url='https://www.youtube.com/watch?v=58pdYkEyrqE',
            categoria=self.categoria
        )
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(video.categoria.id, self.categoria.id)
