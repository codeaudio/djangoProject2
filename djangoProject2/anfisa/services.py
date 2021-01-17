import requests


class Service:
    async def what_weather(self):
        url = f'http://wttr.in/{self}'
        weather_parameters = {
            'format': 2,
            'M': ''
        }
        try:
            response = requests.get(url, params=weather_parameters)
        except requests.ConnectionError:
            return '<сетевая ошибка>'
        if response.status_code == 200:
            return response.text.strip()
        else:
            return '<ошибка на сервере погоды. попробуйте позже>'

    async def city_map(self):
        API_KEY = 'YcO-vY3ZVJ08dHVvUKkjnXtzdpmlaWos_NQcpDx1doE'
        url = f'https://image.maps.ls.hereapi.com/mia/1.6/mapview?ci={self}&apiKey={API_KEY}&w=1280&h=720&u=4m&z=11.5'
        try:
            response = requests.get(url)
        except requests.ConnectionError:
            return '<сетевая ошибка>'
        if response.status_code == 200:
            f = open('static/maps.jpg', 'wb')
            f.write(response.content)
            return "/static/maps.jpg"
        else:
            return '<ошибка на сервере карт. попробуйте позже>'

    async def what_temperature(weather):
        if (weather == '<сетевая ошибка>' or
                weather == '<ошибка на сервере погоды. попробуйте позже>'):
            return weather
        temperature = weather.split()[1]
        parsed_temperature = ''
        for char in temperature:
            if char == '-':
                parsed_temperature += char
            try:
                char = int(char)
                parsed_temperature += str(char)
            except ValueError:
                continue
        return int(parsed_temperature)

    async def what_conclusion(self):
        try:
            temperature = str(self)
            if int(temperature) < 18:
                return 'холодно'
            elif 18 <= int(temperature) <= 27:
                return 'в самый раз!'
            if int(temperature) > 27:
                return 'Жарко, как в Африке, нужны две порции!'
        except ValueError:
            return f'Не могу узнать погоду'
