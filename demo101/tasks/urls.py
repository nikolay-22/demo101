from django.urls import path
from demo101.tasks.views import index, index_old, index_db_no_template

urlpatterns = (
    path("", index),
    path("old/", index_old),
    path("not/", index_db_no_template),
)
