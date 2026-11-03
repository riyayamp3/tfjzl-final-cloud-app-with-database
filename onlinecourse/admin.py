
from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner
from .models import Enrollment, Question, Choice, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
