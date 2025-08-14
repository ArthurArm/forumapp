from django.urls import path, include

from posts import views
from posts.views import IndexView, Dashboard, AddPostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dash'),
    path('add', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('approve/', views.approve_post, name='approve-post'),
        path('edit/', views.EditPost.as_view(), name='edit-post'),
        path('details/', views.PostDetails.as_view(), name='detail-post'),
        path('delete/', views.DeletePost.as_view(), name='delete-post'),
    ])),
    path('redirect/', views.MyRedirectView.as_view()),
]
