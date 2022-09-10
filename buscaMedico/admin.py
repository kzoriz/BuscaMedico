from django.contrib import admin
from .models import *
from datetime import datetime


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profissao', 'birth',)
    #fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'address')
    exclude = ('favorites', 'creates_at', 'update_at',)
    date_hierarchy = 'created_at'

    list_display_links = ('user', 'profissao',)
    list_filter = ('user__is_active', 'role')
    empty_value_display = 'Vazio'
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    fieldsets = (
        ('Usuario', {
            'fields': ('user', 'birthday', 'image')
        }
        ),
        ('Função', {
            'fields': ('role',)
        }
        ),
        ('Extra', {
            'fields': ('specialties', 'address')
        }
         ),
    )

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")

    def profissao(self, obj):
        if obj.role:
            if obj.role == 1:
                return "Admin"
            elif obj.role == 2:
                return "Médico"
            else:
                return "Paciente"

admin.site.register(Profile, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    fields = ('neighborhood', 'name', 'latitude', 'longititude', 'status')
    readonly_fields = ('neighborhood',)
    exclude = ('favorites', 'creates_at', 'update_at',)
    list_display_links = ('name', 'neighborhood')
    date_hierarchy = 'created_at'
    list_display = ('name', 'neighborhood', 'status')
    empty_value_display = 'Vazio'
    search_fields = ('user__username',)

# Register your models here.


admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address, AddressAdmin)

admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
