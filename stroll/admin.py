from django.contrib import admin
from stroll.models import Walk, UserProfile, Question, WalkComment, QuestionComment


class WalkAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'title',
                    'area',
                    'description',
                    'date_published',
                    'likes',
                    'views',
                    'difficulty',
                    'length',
                    'thumbnail',
                    'tags',
                    'gallery_image_1',
                    'gallery_image_2',
                    'gallery_image_3',
                    'gallery_image_4',
                    'map_coordinates',)
    def delete_queryset(self, request, queryset):
        for x in queryset:
            x.delete()

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'date_published',
                    'title',
                    'text',)
    
class UserProfileAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for x in queryset:
            x.delete()


admin.site.register(Walk, WalkAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(WalkComment)
admin.site.register(QuestionComment)