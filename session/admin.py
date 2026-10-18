from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ["username" , "email" , "user_type"]

    list_filter = ["user_type",]

    actions = ["mark_selected_user_as_author", "mark_selected_user_as_advertiser"]

    @admin.action(description = "Mark selected users as author")
    def mark_selected_user_as_author(self, request, queryset):

        count = queryset.update(user_type = CustomUser.UserTypeChoices.AUTHOR)

        return self.message_user(request, f"Successfully marked {count} selected user(s) as author")

    @admin.action(description = "Mark selected users as advertiser")
    def mark_selected_user_as_advertiser(self, request, queryset):
    
        count = queryset.update(user_type = CustomUser.UserTypeChoices.ADVERTISER)
    
        return self.message_user(request, f"Successfully marked {count} selected user(s) as advertiser")