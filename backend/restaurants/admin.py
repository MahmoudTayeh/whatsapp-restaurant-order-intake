from django.contrib import admin
from .models import Restaurant, RestaurantChannel, MenuCategory, MenuItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")

@admin.register(RestaurantChannel)
class RestaurantChannelAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "inbound_identifier", "is_active")

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "name", "order")
    inlines = [MenuItemInline]
