from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ["name" , "email" , "contact_for" , "subject" , "read_status" , "created_at"]

    list_filter = ["contact_for" , "read_status" ,]

    list_per_page = 100

    actions = ["mark_selected_message_as_read" , "mark_selected_message_as_unread"]

    @admin.action(description = "Mark selected messages as read")
    def mark_selected_message_as_read(self, request, queryset):

        count = queryset.update(read_status = True)

        return self.message_user(request, f"Successfully marked {count} message(s) as read")

    @admin.action(description = "Mark selected messages as unread")
    def mark_selected_message_as_unread(self, request, queryset):
    
        count = queryset.update(read_status = False)
    
        return self.message_user(request, f"Successfully marked {count} message(s) as unread")