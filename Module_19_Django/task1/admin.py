from django.contrib import admin
from .models import Buyer,Game,News

# Register your models here.

admin.site.register(News)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','cost','size') #Поля для отображения
    search_fields = ('title',) # Поля для поиска
    list_filter = ('size','cost') # Поля фильтрации
    list_per_page = 20 # Кол-во обьектов на странице

    fieldsets = (
        (None, {
            'fields': ('title','cost','size') # Базовая секция
        }),
        ('Доп инф',{
            'classes': ('collapse',), # cкрыть секцию по умолчанию
            'fields' :('age_limited',)
        }),
    )

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name','balance','age') #Поля для отображения
    search_fields = ('name',) # Поля для поиска
    list_filter = ('balance','age') # Поля фильтрации
    list_per_page = 30 # Кол-во обьектов на странице
    readonly_fields =('balance',) # Поля только для чтения



