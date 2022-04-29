from  django.urls import path
from authapp.views import login, RegisterView, logout, profile

app_name = "authapp"
urlpatterns = [
  path("login/", login, name="login"),
  path("register/", RegisterView.as_view(), name="register"),
  path("logout/", logout, name="logout"),
  path("profile/", profile, name="profile"),

  path("verify/<str:email>/<str:activate_key>/", RegisterView.verify, name="verify")
]
