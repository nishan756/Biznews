from django.contrib import admin

from .models import NewsCategory, News, NewsImage


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):

    list_display = ["title"]

    search_fields = ['title']



class NewsImageInline(admin.TabularInline):

    model = NewsImage

    extra = 2

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ["author","title", "category" ,"created_at", "updated_at"]

    list_filter = ["category", "author", "created_at", "updated_at"]

    search_fields = ["title"]

    actions = ["mark_selected_news_as_inactive", "mark_selected_news_as_active"]

    inlines = [NewsImageInline]

    @admin.action(description = "Mark selected news as inactive")
    def mark_selected_news_as_inactive(self, request, queryset):

        count = queryset.update(is_active = False)

        return self.message_user(request, f"Successfully marked {count} news(s) as inactive")

    @admin.action(description = "Mark selected news as inactive")
    def mark_selected_news_as_active(self, request, queryset):
    
        count = queryset.update(is_active = True)
    
        return self.message_user(request, f"Successfully marked {count} news(s) as active")