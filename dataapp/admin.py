from django.contrib import admin
from .models import PharmaSales, DrugsReview

class PharmaSalesAdmin(admin.ModelAdmin):
    list_display=['id','year','datum','m01ab','m01ae','n02ba','n02be','n05b','n05c','r03','r06']
admin.site.register(PharmaSales, PharmaSalesAdmin)

class DrugsReviewAdmin(admin.ModelAdmin):
    list_display =['id', 'year', 'date', 'drug_name', 'rating', 'review', 'useful_count']
admin.site.register(DrugsReview, DrugsReviewAdmin)