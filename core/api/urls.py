from django.urls import path, include
from home.views import ListUser, index, person, PeopleViewSet, RegisterApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', PeopleViewSet, basename='person')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('person/', person),
    path('persons/', ListUser.as_view()),
    path('register/', RegisterApi.as_view()),
]
