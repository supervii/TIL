from django.contrib import admin
from .models import Article # 명시적 상대경로 표현
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    list_display_links =('content',)
    list_editable = ('title',)
    # 기본값 = 100 
    list_per_page = 3  

admin.site.register(Article, ArticleAdmin)
