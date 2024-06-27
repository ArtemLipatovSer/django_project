from django.shortcuts import render, redirect, get_object_or_404
from .models import Folder, Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import FolderForm, PhotoForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

class PhotoAlbumView(LoginRequiredMixin, View):
    def get(self, request):
        root_folders = Folder.objects.filter(user=request.user)
        photo = Photo.objects.filter(user=request.user, folder__isnull=True).first()
        return render(request, 'family_album/home_user.html', {'folders': root_folders, 'photo': photo})
    
class FolderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = FolderForm()
        return render(request, 'family_album/folder_form.html', {'form': form})
    
    def post(self, request):
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect ('folder_detail', folder_id = folder.id)
        return render(request, 'family_album/folder_form.html', {'form': form})
    
class FolderDetailView(LoginRequiredMixin, View):
    def get(self, request, folder_id):
        folder = get_object_or_404(Folder, id=folder_id, user=request.user)
        photos = folder.photos.all()
        return render(request, 'family_album/folder_detail.html', {'folder': folder, 'photos': photos})
    
class PhotoUploadView(LoginRequiredMixin, View):
    def get(self, request, folder_id=None):
        form = PhotoForm()
        return render(request, 'family_album/photo_upload.html', {'form': form, 'folder_id': folder_id})

    def post(self, request, folder_id=None):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            if folder_id:
                photo.folder = get_object_or_404(Folder, id=folder_id, user=request.user)
            photo.save()
            return redirect('folder_detail', folder_id=folder_id) if folder_id else redirect('photo_album')
        return render(request, 'family_album/photo_upload.html', {'form': form})
    
class FolderRenameView(LoginRequiredMixin, View):
    def get(self, request, pk):
        folder = get_object_or_404(Folder, id=pk, user=request.user)
        form = FolderForm(instance=folder)
        return render(request, 'family_album/folder_form.html', {'form': form, 'edit_mode': True})

    def post(self, request, pk):
        folder = get_object_or_404(Folder, id=pk, user=request.user)
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('folder_detail', folder_id=folder.id)
        return render(request, 'family_album/folder_form.html', {'form': form, 'edit_mode': True})
    
class FolderDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        folder = get_object_or_404(Folder, id=pk, user=request.user)
        folder.delete()
        return redirect('home_user')
    
class PhotoDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        photo = get_object_or_404(Photo, id=pk, user=request.user)
        folder_id = photo.folder.id if photo.folder else None
        photo.delete()
        return redirect('folder_detail', folder_id=folder_id) if folder_id else redirect('photo_album')