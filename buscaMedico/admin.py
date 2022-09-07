from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', ('role', ), 'image', 'birthday', 'specialties', 'address')
    exclude = ('favorites', 'creates_at', 'update_at', )
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birthday',)
    list_display_links = ('user', 'role',)
    list_filter = ('user__is_active', 'role')
    empty_value_display = 'Vazio'
    readonly_fields = ('user',)
    search_fields = ('user__username', )



# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)

