from django.contrib import admin
from . import models as m


admin.site.register((m.Network, m.Subgroup, m.Delivery, m.Product, m.Purchase, m.Plural))
