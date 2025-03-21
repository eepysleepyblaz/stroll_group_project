from django.contrib import admin
from stroll.models import Walk, UserProfile, Question, WalkComment, QuestionComment


class WalkAdmin(admin.ModelAdmin):
    list_display = ('user',
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

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'date_published',
                    'title',
                    'text',)
    



admin.site.register(Walk, WalkAdmin)
admin.site.register(UserProfile)
admin.site.register(Question, QuestionAdmin)
admin.site.register(WalkComment)
admin.site.register(QuestionComment)