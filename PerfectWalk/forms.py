from typing import Type, Tuple

from django.forms import ModelForm
from .models import User
from .models import Pet
from .models import Post


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = (
            'pet_name',
            'pet_age',
            'pet_type',
            'user',
        )


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = (
            'park_name',
            'park_location',
            'park_review',
            'park_thumbs',
            'date_visited',
            'user',
            'pet',
        )

