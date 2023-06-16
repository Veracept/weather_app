from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
place = input("Введите ваш город: ")
country = input("Введите код вашей страны: ")
country_and_place = place + ", " + country

owm = OWM('0b65431fa007d361c1b04cfdf7eed5ae')  # Ваш ключ с сайта open weather map
mgr = owm.weather_manager()  #
observation = mgr.weather_at_place(country_and_place)


w = observation.weather

status = w.detailed_status
w.wind()
humidity = w.humidity
temp = w.temperature('celsius')['temp']


def weather():
    print("В городе " + str(place) + " сейчас " + str(status) +
          "\nТемпература " + str(
        round(temp)) + " градусов по цельсию" +
          "\nВлажность составляет " + str(humidity) + "%" +
          "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")


weather()