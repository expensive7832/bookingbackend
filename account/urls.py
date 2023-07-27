from django.urls import path
from .views import Signup, Login, updateAccount, deleteAccount 

urlpatterns = [
    path("signup/", Signup),
    path("login/", Login),
    path("update/<int:id>", updateAccount),
    path("delete/<int:id>", deleteAccount)
]