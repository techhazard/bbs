from django.contrib import admin

# Register your models here.
from operations.models import BBSUser, Product, Purchase, Product_Purchase



class CommonAdmin(admin.ModelAdmin):
    list_diplay = ("show_uuid", "created", "updated")
    list_filter = ("created", "updated")

    def show_uuid(self, obj):
        return str(obj.uuid)[:8]


class BBSUserAdmin(CommonAdmin):
    pass


class ProductAdmin(CommonAdmin):
    pass

class PurchaseAdmin(CommonAdmin):
    pass

class Product_PurchaseAdmin(CommonAdmin):
    pass

admin.site.register(BBSUser, CommonAdmin)
admin.site.register(Product, CommonAdmin)

admin.site.register(Purchase, CommonAdmin)
admin.site.register(Product_Purchase, CommonAdmin)
