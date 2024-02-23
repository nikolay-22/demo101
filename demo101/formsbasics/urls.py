from django.urls import path

from demo101.formsbasics.views import index_forms, index_mforms, update_employee

urlpatterns = (
    path("", index_forms, name="index_forms"),
    path("mf/", index_mforms, name="index_mforms"),
    path("mf/<int:pk>/", update_employee, name="update_employee"),
)
