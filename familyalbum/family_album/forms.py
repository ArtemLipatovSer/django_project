from django import forms
from .models import Folder, Photo

class FolderForm(forms.ModelForm):
    name = forms.CharField(label='Название')
    class Meta:
        model = Folder
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Название альбома'
            }),
}
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'folder']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Photo Title'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded'
            }),
            'folder': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded'
            }),
    }