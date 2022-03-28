# users/serializers.py
from allauth.account.adapter import get_adapter

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser



class UserSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    pv = serializers.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', "name", "address", "pv", 'last_login', 'date_joined', 'is_staff')

    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name'),
            'address': self.validated_data.get('address'),
            'pv': self.validated_data.get('pv'),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.name = self.cleaned_data.get('name')
        user.address = self.cleaned_data.get('address')
        user.pv = self.cleaned_data.get('pv')
        user.save()
        adapter.save_user(request, user, self)
        return user