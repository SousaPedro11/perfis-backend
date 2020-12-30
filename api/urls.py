from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'endereco', views.EnderecoViewSet)
router.register(r'curso', views.CursoViewSet)
router.register(r'profissional', views.ProfissionalViewSet)
router.register(r'perfil', views.PerfilViewSet)

urlpatterns = router.urls
