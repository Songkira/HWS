# 홈워크_db_08_hw02_P-a-2.py
# serializers.py

class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = __(d)__


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = __(e)__

(d) => ('id', 'title')
(e) => ('id', 'title', 'content', 'created_at', 'updated_at')