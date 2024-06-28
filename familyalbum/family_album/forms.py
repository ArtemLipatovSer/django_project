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
        fields = ['title', 'image']
        labels = {
            'title': 'Название',
            'image': 'Фотография',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'photo-input',
                'placeholder': 'Название фотографии'
            }),
            'image': forms.FileInput(),
    }