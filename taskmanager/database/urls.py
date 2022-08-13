
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('<int:year>/<str:month>/', views.home, name='home'),
     path('add_contact',views.add_contact,name='add-contact'),
     path("list_contact", views.list_contact, name="list-contact"),
     path('show_contact/<contact_id>', views.show_contact, name='show-contact'),
     path('update_contact/<contact_id>', views.update_contact, name='update-contact'),
     path('delete_contact/<contact_id>', views.delete_contact, name='delete-contact'),
]