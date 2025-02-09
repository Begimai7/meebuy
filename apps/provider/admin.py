from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Provider, Tag, Condition, Delivery, ProvideImg, ProvideFiles, TypePay


class ProvideImgInline(admin.TabularInline):
    model = ProvideImg
    extra = 1
    fields = ['image']


class ProvideFilesInline(admin.TabularInline):
    model = ProvideFiles
    extra = 1
    fields = ['image']


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'address', 'is_active', 'is_modered')
    list_filter = ('is_active', 'is_modered', 'type')
    search_fields = ('title', 'description', 'mini_descr', 'post_index', 'address')
    inlines = [ProvideImgInline, ProvideFilesInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
        if db_field.name == "conditions":
            kwargs["queryset"] = Condition.objects.all()
        if db_field.name == "deliveries":
            kwargs["queryset"] = Delivery.objects.all()
        if db_field.name == "type_pay":
            kwargs["queryset"] = TypePay.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_category')
    search_fields = ('title',)

    def parent_category(self, obj):
        return obj.category.title if obj.category else '---'

    parent_category.short_description = 'Parent Category'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(TypePay)
class TypePayAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# Register your models here
admin.site.register(Provider, ProviderAdmin)
admin.site.register(ProvideImg)  # Optional: If you want to manage images separately as well
admin.site.register(ProvideFiles)  # Optional: If you want to manage files separately as well
