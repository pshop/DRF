from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICE

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.ImageField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     lineos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICE, default='friendly')
#
#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.tittle = validated_data.get('title', instance.title)
#         instance.code = validated_data('code', instance.code)
#         instance.lineos = validated_data('lineos', instance.lineos)
#         instance.language = validated_data('language', instance.language)
#         instance.style = validated_data('style', instance.style)
#         instance.save()
#         return instance

#IS SIMILAR TO

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'