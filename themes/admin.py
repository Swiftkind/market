from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ( 
    UserDownloadLog, Theme, Review, Thumbnail, Screenshot, Browser, Category, Topic, Label, License, Subscriber)


class UserDownloadLogAdmin(admin.ModelAdmin):
    """user download log admin
    """
    model = UserDownloadLog

    list_display = (
        'user',
        'theme',
        'download_times',
        'date_created',
        'date_modified',
    )


class ThemeAdmin(admin.ModelAdmin):
    """themes admin
    """
    model = Theme

    list_display = (
        'name',
        'description',
        'rating',
        'price',
        'discount',
        'version',
    )


class ReviewAdmin(admin.ModelAdmin):
    """review admin
    """
    model = Review

    list_display = (
        'user',
        'rating',
        'comment',
        'date_created',
        'date_modified',
    )


class ThumbnailAdmin(admin.ModelAdmin):
    """thumbnail admin
    """
    model = Thumbnail

    list_display = (
        'theme',
        'thumbnail',
        'date_created',
        'date_modified',
    )


class ScreenshotAdmin(admin.ModelAdmin):
    """screenshot admin
    """
    model = Screenshot

    list_display = (
        'theme',
        'image',
        'date_created',
        'date_modified',
    )


class BrowserAdmin(admin.ModelAdmin):
    """browsers admin
    """
    model = Browser

    list_display = (
        'browser',
        'date_created',
        'date_modified',
    )


class CategoryAdmin(admin.ModelAdmin):
    """category admin
    """
    model = Category

    list_display = (
        'category',
        'date_created',
        'date_modified',
    )

class TopicAdmin(admin.ModelAdmin):
    """topic admin
    """
    model = Topic

    list_display = (
        'topic',
        'date_created',
        'date_modified',
    )


class LabelAdmin(admin.ModelAdmin):
    """label admin
    """
    model = Label

    list_display = (
        'label',
        'date_created',
        'date_modified',
    )


class LicenseAdmin(admin.ModelAdmin):
    """license admin
    """
    model = License

    list_display = (
        'license',
        'date_created',
        'date_modified',
    )


class SubscriberAdmin(admin.ModelAdmin):
    """subscribers admin
    """

    model = Subscriber

    list_display = (
        'user',
        'date_created',
        'date_modified',
    )


admin.site.register(UserDownloadLog, UserDownloadLogAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(Browser, BrowserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
