from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.ToDoList)
class CustomToDoListAdmin(admin.ModelAdmin):

    """ Custom ToDoList Admin """

    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "host",
                    "toDo",
                )
            },
        ),
    )

    list_display = (
        "host",        
        "toDo",
    )

    list_filter = (
        "host__school",
        "host__gender",
        "host__grade",
    )

    search_fields = (
        "school",
    )