from django.shortcuts import render
from .models import icecream_db
from djangoProject2.homepage.views import ABOUT


class Icecreampage:
    async def icecream_detail(self, pk):
        name = icecream_db[pk]['name']
        description = icecream_db[pk]['description']
        context = {
            'name': name,
            'description': description,
            'about': ABOUT,
        }
        return render(self, 'icecream/icecream-detail.html', context)
