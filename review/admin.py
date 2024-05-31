from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pizza', 'user', 'rating', 'created_on')
    list_filter = ('pizza', 'rating', 'created_on')
    search_fields = ('user__username', 'pizza__title', 'comment')


admin.site.register(Review, ReviewAdmin)
