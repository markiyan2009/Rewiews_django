from django.urls import path
from reviews import views
urlpatterns = [
    path("",views.get_reviews,name = "index")
]