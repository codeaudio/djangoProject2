from django.shortcuts import render
from djangoProject2.icecream.models import icecream_db
from djangoProject2.anfisa.models import friends_db
from djangoProject2.anfisa.services import Service

ABOUT = 'Анфиса обращается к сервису wttr.in для получения погоды.' + \
        ' Достает город по имени друга из базы и отпраялет запрос для получения погоды в этом городе.'


class Homepage:
    async def index(self):
        icecreams = ''
        friends = ''
        city_weather = ''
        friend_output = ''
        conclusion = ''
        maps = ''

        for friend in friends_db:
            friends += (f'<div class="friend"><input type="radio" name="friend"'
                        f' required value="{friend}">{friend}</div>')

        for i in range(len(icecream_db)):
            ice_form = (f'<input type="radio" name="icecream" required'
                        f' value="{icecream_db[i]["name"]}">{icecream_db[i]["name"]}')

            ice_link = f'<a href="icecream/{i}/">Узнать состав</a>'
            icecreams += f'<div class="cream">{ice_form} | {ice_link}</div>'

        if self.method == 'POST':
            selected_friend = self.POST['friend']
            selected_icecream = self.POST['icecream']
            city = friends_db[selected_friend]
            weather = await Service.what_weather(city)
            parsed_temperature = await Service.what_temperature(weather)
            maps_of_friend = await Service.city_map(city)
            conclusion = f'<h3>{await Service.what_conclusion(parsed_temperature)}</h3></div>'
            friend_output = f'<br><div class="weather">{selected_friend}, тебе прислали {selected_icecream}!'
            city_weather = f'<p>В городе {city} погода: {weather}</p>'
            maps = f'<h3>Город друга<h3><br><img src="{maps_of_friend}"title="удерживайте правую кнопку мыши для увеличения масштаба">'

        context = {
            'icecreams': icecreams,
            'friends': friends,
            'friend_output': friend_output,
            'city_weather': city_weather,
            'conclusion': conclusion,
            'about': ABOUT,
            'maps': maps,
        }

        return render(self, 'homepage/index.html', context)
