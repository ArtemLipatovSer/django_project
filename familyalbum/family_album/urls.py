from django.urls import path
from .views import home, FolderCreateView, FolderDetailView, PhotoUploadView, PhotoAlbumView, FolderRenameView, FolderDeleteView, PhotoDeleteView, page_not_found_view
from django.conf.urls import handler404

urlpatterns = [
    path('', home, name='home'),
    path('my_album/',PhotoAlbumView.as_view(), name='home_user'),
    path('folder/create/', FolderCreateView.as_view(), name='folder_create'),
    path('folder/<int:folder_id>/', FolderDetailView.as_view(), name='folder_detail'),
    path('upload/<int:folder_id>/', PhotoUploadView.as_view(), name='photo_upload_in_folder'),
    path('folder/rename/<int:pk>/', FolderRenameView.as_view(), name='folder_rename'),
    path('folder/delete/<int:pk>/', FolderDeleteView.as_view(), name='folder_delete'),
    path('delete/photo/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
]

handler404 = page_not_found_view
