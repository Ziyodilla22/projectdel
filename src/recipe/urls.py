from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('blog/', blog, name="blog"),
    path('elements/', element, name="elements"),
    path('recipe/<int:pk>/', recipe, name="recipe_one"),
    path('recipe_ctg/<slug>/', rec_ctg, name="receipe_ctg"),
    path('recipe_ctg/', rec_ctg, name="receipe_ctg_search"),
]