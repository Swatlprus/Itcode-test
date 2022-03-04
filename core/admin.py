from django.contrib import admin
import core.models

admin.site.register(core.models.Company)
admin.site.register(core.models.Founder)
admin.site.register(core.models.DateFound)
admin.site.register(core.models.Staff)


# Register your models here.
