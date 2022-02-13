from rest_framework import serializers
from .models import Store, Author

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','book_title','author','year_of_pub','description']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"