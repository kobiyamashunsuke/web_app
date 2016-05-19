from django.contrib import admin
from cms.models import Book, Impression

# admin.site.register(Book)
# admin.site.register(Impression)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'func_name', 'program_name', 'tag','author','Github',)  # 一覧に出したい項目
    list_display_links = ('id', 'func_name',)  # 修正リンクでクリックできる項目
admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
admin.site.register(Impression, ImpressionAdmin)


