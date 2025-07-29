from django.urls import path, include
from website.views import *

urlpatterns = [
    path("", index, name="index"),
    path("send", send_request, name="send")

]