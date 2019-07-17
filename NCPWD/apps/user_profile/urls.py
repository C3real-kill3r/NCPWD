from django.urls import path
from .views import ProfileViewSet, DisabilityViewSet
from rest_framework import routers


router = routers.SimpleRouter()

app_name = "user_profile"

router.register(r"profiles", ProfileViewSet)
router.register(r"disability", DisabilityViewSet)

urlpatterns = router.urls
# import pdb; pdb.set_trace()
