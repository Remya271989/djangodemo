from django.contrib import admin
from cart.models import Cart,Payment,order_details

admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(order_details)


