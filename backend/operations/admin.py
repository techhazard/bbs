from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from operations.models import BBSUser, Product, Purchase
from operations.actions import export_as_csv_action



class BBSUserAdmin(UserAdmin):


    list_diplay = ("show_uuid", "created", "updated")
    list_filter = ("created", "updated")

    def show_uuid(self, obj):
        return str(obj.uuid)[:8]


class CommonAdmin(admin.ModelAdmin):
    list_diplay = ("show_uuid", "created", "updated")
    list_filter = ("created", "updated")
    actions = [export_as_csv_action("CSV Export")]


    def show_uuid(self, obj):
        return str(obj.uuid)[:8]



class ProductAdmin(CommonAdmin):
    pass

admin.site.register(BBSUser, CommonAdmin)
admin.site.register(Product, CommonAdmin)

admin.site.register(Purchase, CommonAdmin)
