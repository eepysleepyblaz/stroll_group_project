from django.contrib import admin
from stroll.models import Walk, User, Question, WalkComment, QuestionComment


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'date_of_birth',
                    'description',
                    'password',
                    'is_moderator',
                    'total_likes',
                    'total_views',
                    'email_address',
                    'picture',)

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
admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(WalkComment)
admin.site.register(QuestionComment)