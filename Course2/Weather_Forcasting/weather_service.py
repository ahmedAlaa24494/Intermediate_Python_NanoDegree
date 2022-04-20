
import requests

class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = 'f1082b6828a0525b3af8974e32b27c92'

    @classmethod
    def getForecast(cls, city="new york", country="us"):
        url = f'{cls.baseUrl}/forecast'

        response = requests.get(url, params=[
            ('q', f'{city},{country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
            ])

        data = response.json()

        return data['list']

if __name__ == "__main__":
    print(WeatherService.getForecast())