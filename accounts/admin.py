from django.contrib import admin

from .models import User,Profile
from posts.models import Scrap
from django.contrib.auth.admin import UserAdmin  as BaseUserAdmin
# Register your models here.

class ScrapInline(admin.StackedInline):
    model = Scrap
    extra = 5
    min_num = 0
    verbose_name = '즐겨찾기'


# class DiseaseInline(admin.StackedInline):
#     model = disease
#     extra = 5
#     min_num = 0
#     max_num = 5
#     verbose_name = '보유 질병'
#     verbose_name_plural = '보유 질병을 입력하세요'

# class MedicineInline(admin.StackedInline):
#     model = medicine
#     extra = 10
#     min_num = 0
#     max_num = 10
#     verbose_name = '복용중인 약'
#     verbose_name_plural = '복용중인 약을 입력해주세요'

# class AllergyInline(admin.StackedInline):
#     model = allergy
#     extra = 5
#     min_num = 0
#     max_num = 10
#     verbose_name = '보유 알러지'
#     verbose_name_plural = '보유한 알러지를 입력하세요'
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username','phone','email','pregnancy')
    inlines = (ScrapInline,)
    
# Register your models here.

admin.site.register(Profile)