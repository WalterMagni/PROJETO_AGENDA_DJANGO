from django.contrib import admin
from contact import models

@admin.register(models.Contact)
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = 'id',  'first_name', 'last_name', 'phone', 'show'
  ordering = 'id',
  #list_filter = 'created_date',
  search_fields = 'id', 'first_name', 'last_name',
  list_per_page = 30
  list_max_show_all= 200
  list_editable =  'show', #'first_name', 'last_name',
  list_display_links = 'id',

@admin.register(models.Category)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display = 'name', 
  ordering = 'id',
