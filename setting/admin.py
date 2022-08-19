from django.contrib import admin
from .models import Location, Division, District, Thana, PostOffice, PostCode

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('division', 'district', 'thana', 'post_office', 'post_code')
    #new need to create Media class(first step for dependent dropdown at admin)
    # second step is the views where need to apply restapi
    class Media:
        js = ("admindropd/newajax.js",)


admin.site.register(Division)
admin.site.register(District)
admin.site.register(Thana)
admin.site.register(PostOffice)
admin.site.register(PostCode)