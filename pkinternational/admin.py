from django.contrib import admin
from .models import Car, CarImage, CarColor, CarModel, FrequentQuestion, FrequesntAnswers


class CarImageInlineModels(admin.TabularInline):
    model = CarImage


class CarColorInlineModel(admin.TabularInline):
    model = CarColor


class CarInlineModel(admin.ModelAdmin):
    inlines = [CarImageInlineModels, CarColorInlineModel]


class AnsweredInline(admin.TabularInline):
    model = FrequesntAnswers


class AnsweredInlineModel(admin.ModelAdmin):
    inlines = [AnsweredInline]


admin.site.register(Car, CarInlineModel)
admin.site.register(CarModel)
admin.site.register(FrequentQuestion, AnsweredInlineModel)
