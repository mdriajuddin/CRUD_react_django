



from rest_framework import serializers
from demo.models import Post
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Post


