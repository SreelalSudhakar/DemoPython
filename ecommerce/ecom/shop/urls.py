from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('',views.ProdCat,name="ProdCat"),
    path('<slug:c_slug>/',views.ProdCat,name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name="ProdCatDetail"),
]