from django.urls import path
from .views import PostlistView, PostDetailView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, Followers, AddLike, UserSearch

urlpatterns = [
    path('', PostlistView.as_view(), name='post-list'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/search/<int:pk>/', UserSearch.as_view(), name='profile-search'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('profile/<int:pk>/follow/', Followers.as_view(), name='profile-follow'),
]