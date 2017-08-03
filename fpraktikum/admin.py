# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import FpRegistration, FpUserRegistrant, FpUserPartner, FpWaitlist, FpInstitute


class FpInstituteAdmin(admin.ModelAdmin):

    list_display = ['name', 'places', 'graduation', 'get_registration', 'semester_half']

    def get_registration(self, obj):
        return obj.registration.semester

admin.site.register(FpInstitute, FpInstituteAdmin)


class FpInstituteInline(admin.TabularInline):
    model = FpInstitute


class FpUserPartnerAdmin(admin.ModelAdmin):

    list_display = [f.name for f in FpUserPartner._meta.get_fields()]

admin.site.register(FpUserPartner, FpUserPartnerAdmin)


class FpRegistrationAdmin(admin.ModelAdmin):

    list_display = ['semester', 'start_date', 'end_date']
    inlines = [
        FpInstituteInline,
    ]

admin.site.register(FpRegistration, FpRegistrationAdmin)


class FpUserRegistrantAdmin(admin.ModelAdmin):

    list_display = [f.name for f in FpUserRegistrant._meta.get_fields()]

admin.site.register(FpUserRegistrant, FpUserRegistrantAdmin)


class FpWaitlistAdmin(admin.ModelAdmin):

    list_display = [f.name for f in FpWaitlist._meta.get_fields()]

admin.site.register(FpWaitlist, FpWaitlistAdmin)
