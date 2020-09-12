from django.contrib import admin
from .models import Candidate, Cand_details ,Job,Company

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Cand_details)
admin.site.register(Company)
admin.site.register(Job)

