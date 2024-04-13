from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn", "price", )


    def validate(self, data):
        title = data.get("title", None)
        author = data.get("author", None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Название книги должно иметь буквы"
                }
            )

        if title == author:
            raise ValidationError(
                {
                    "status": False,
                    'message': "Название и автор не должно быть одинаковым"
                }
            )
        return data

