from django.urls import path
from .views import *

urlpatterns = [
    path('addprod/',ProductView,name='add'),
    path('allprod/',allProdsDisplay,name='display'),
    path('update/<int:i>',updateProduct, name='updt'),
    path('delete/<int:oid>', deleteProduct, name='del'),

]
