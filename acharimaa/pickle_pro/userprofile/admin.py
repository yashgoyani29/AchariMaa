from django.contrib import admin
from .models import *

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'payment_method', 'total', 'order_status', 'created_at')
    list_editable = ('order_status',)  # 👈 Make 'order_status' editable from list view
    search_fields = ('full_name', 'email', 'phone')  # 👈 Search by name, email, phone
    list_filter = ('order_status', 'payment_method', 'created_at')  # 👈 Filter by status, payment method, date
    ordering = ('-created_at',)  # 👈 Latest orders first

admin.site.register(Checkout, CheckoutAdmin)

# other model registrations
admin.site.register(CustomUser)
admin.site.register(MangoProduct)
admin.site.register(LemonProduct)
admin.site.register(MixedProduct)
admin.site.register(PanjabiProduct)
admin.site.register(KerdaProduct)
admin.site.register(CarrotProduct)
admin.site.register(ContactUs)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CarouselImage)
admin.site.register(CheckoutProduct)
