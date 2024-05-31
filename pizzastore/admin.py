from django.contrib import admin
from .models import Pizza
from review.models import Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stocks', 'stocks_available', 'modified_on', 'created_on')
    list_filter = ('category', 'stocks_available', 'created_on')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ReviewInline]


admin.site.register(Pizza, PizzaAdmin)
