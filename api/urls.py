


from django.urls import path

from .views import PostViewSet



# restframework

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'',PostViewSet)
urlpatterns  = router.urls