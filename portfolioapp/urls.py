from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projeler/', views.projeler, name='projeler'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('hakkimda/', views.hakkimda, name='hakkimda'),
    path('blog/', views.blog, name='blog'),
    path('profile/', views.profile, name='profile'),
    # İngilizce Sayfalar
    path('indexEng/', views.indexEng, name='indexEng'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    # CV indirme
    path('download-cv/', views.download_cv, name='download_cv'),
    # Blog gönderi paylaşma
    path('share-blog-post/', views.share_blog_post, name='share_blog_post'),
    path('edit-blog-post/<int:blog_post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete-blog-post/<int:blog_post_id>/', views.delete_blog_post, name='delete_blog_post'),
    path('add-comment/<int:blog_post_id>/', views.add_comment, name='add_comment'),
    path('404/', views.custom_404, name='custom_404'),
]


