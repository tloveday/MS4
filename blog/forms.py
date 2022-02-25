from django import forms
from .widgets import CustomClearableFileInput
from .models import Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        # Get friendly names
        super().__init__(*args, **kwargs)
        topic = Topic.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in topics]

        # Use friendly names
        self.fields['topic'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-3 mt-2'
