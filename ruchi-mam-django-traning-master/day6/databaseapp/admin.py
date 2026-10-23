from django.contrib import admin
from databaseapp.models import client, customer, order  

# Register your models here.
admin.site.register(client)
admin.site.register(customer)
admin.site.register(order)

