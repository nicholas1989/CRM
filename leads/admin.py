from django.contrib import admin
from .models import User, Lead, Agent, UserProfile, Category, FollowUp

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(FollowUp)



    