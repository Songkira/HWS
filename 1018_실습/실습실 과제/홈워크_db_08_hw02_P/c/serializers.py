# 홈워크_db_08_hw02_P-c.py
# serializers.py

class MusicSerializer(serializers.ModelSerializer):
    __(c)__ = serializers.IntegerField(
        __(a)__='__(b)__',
        read_only=True,
    )

    class Meta:
        model = Music
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', '__(c)__',)

(a) => source
(b) => comment_set.count
(c) => comment_count