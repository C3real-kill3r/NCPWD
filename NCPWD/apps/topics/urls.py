from .views import TopicViewSet
from rest_framework import routers


app_name = "topics"

router = routers.SimpleRouter()

router.register(r"topics", TopicViewSet)

urlpatterns = router.urls

