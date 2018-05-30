
from django.urls import path
import blog.views as bv
app_name = 'blog'
urlpatterns = [
    path('', bv.index),
    path('<int:article_id>/', bv.article_page,name='article_page'),
    path('edit/<int:article_id>/', bv.edit_page,name='edit_page'),
    path('edit/action', bv.edit_action,name='edit_action'),
]
