from django . urls import path
from . import views
urlpatterns=[
    path('K/',views.create,name="create"),
    path('',views.read,name="read"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('a',views.two),

 ]