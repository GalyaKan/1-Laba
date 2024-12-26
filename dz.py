import requests
import math
from PIL import Image
from io import BytesIO
import random

# 1. Покажите карту Москвы с метками стадионов
stadiums_location = {
    "Лужники": "37.554191,55.715551",
    "Спартак": "37.440262,55.818015",
    "Динамо": "37.559809,55.791540"
}

MAP_API_URL = "https://static-maps.yandex.ru/1.x/"

params = {
    "l": "map",
    "z": 12,
    "size": "600,450",
    "pt": "~".join([f"{coords},pm2rdm" for coords in stadiums_location.values()])
}

response = requests.get(MAP_API_URL, params=params)
image = Image.open(BytesIO(response.content))
image.show()


# 2. Длина пути и отметка в средней точке
path = [
    (37.620070, 55.753630),
    (37.654930, 55.751762),
    (37.661743, 55.763351),
    (37.635784, 55.770639)
]

# Расчет расстояния между точками

def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_latitude = math.radians((a_lat + b_lat) / 2.0)
    lat_lon_factor = math.cos(radians_latitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    return math.sqrt(dx * dx + dy * dy)

# Длина пути
path_length = sum(
    lonlat_distance(path[i], path[i + 1]) for i in range(len(path) - 1)
)

# Средняя точка пути
mid_point = path[len(path) // 2]

params = {
    "l": "map",
    "z": 14,
    "size": "600,450",
    "pt": f"{mid_point[0]},{mid_point[1]},pm2gnl~" + "~".join([f"{lon},{lat},pm2rdl" for lon, lat in path])
}

response = requests.get(MAP_API_URL, params=params)
image = Image.open(BytesIO(response.content))
image.show()


# 3. Спутниковый снимок по координатам
latitude, longitude = 55.753630, 37.620070  # Пример координат
params = {
    "l": "sat",
    "z": 15,
    "size": "600,450",
    "ll": f"{longitude},{latitude}"
}
response = requests.get(MAP_API_URL, params=params)
image = Image.open(BytesIO(response.content))
image.save("satellite.png")



# 4. Определение южного города
cities = input("Введите города через запятую: ").split(",")
city_coordinates = {}
GEOCODER_API_URL = "https://geocode-maps.yandex.ru/1.x/"

for city in cities:
    api_key = "e4f95893-ecf0-417b-9d7a-35bf2b84641e"  # Вставьте сюда ваш ключ
    for city in cities:
        url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json"
        response = requests.get(url).json()

        if 'response' not in response:
            print(f"Ошибка: Не удалось получить данные для {city}.")
            print(response)  # Покажет, что вернул API
            continue

        if not response['response']['GeoObjectCollection']['featureMember']:
            print(f"Город '{city}' не найден.")
            continue

        pos = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        print(f"{city}: {pos}")
    params = {
        "geocode": city,
        "format": "json"
    }
    response = requests.get(GEOCODER_API_URL, params=params).json()
    pos = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    lon, lat = map(float, pos.split())
    city_coordinates[city] = lat

southernmost_city = min(city_coordinates, key=city_coordinates.get)
print(f"Самый южный город: {southernmost_city}")


# 5. Ближайшая аптека к адресу
address = input("Введите адрес: ")
params = {
    "geocode": address,
    "format": "json"
}
response = requests.get(GEOCODER_API_URL, params=params).json()
pos = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
longitude, latitude = pos.split()

params = {
    "text": "аптека",
    "ll": f"{longitude},{latitude}",
    "spn": "0.005,0.005",
    "rspn": 1,
    "type": "biz",
    "format": "json"
}

SEARCH_API_URL = "https://search-maps.yandex.ru/v1/"
response = requests.get(SEARCH_API_URL, params=params).json()
nearest_pharmacy = response['features'][0]['properties']['CompanyMetaData']['name']
print(f"Ближайшая аптека: {nearest_pharmacy}")


# 6. Угадай город
cities = ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург", "Новосибирск"]
random.shuffle(cities)

for city in cities:
    params = {
        "geocode": city,
        "format": "json"
    }
    response = requests.get(GEOCODER_API_URL, params=params).json()
    pos = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    longitude, latitude = pos.split()
    z = random.randint(13, 15)
    l = random.choice(["map", "sat"])

    params = {
        "l": l,
        "z": z,
        "size": "600,450",
        "ll": f"{longitude},{latitude}"
    }
    response = requests.get(MAP_API_URL, params=params)
    image = Image.open(BytesIO(response.content))
    image.show()


# 7. Определение района по адресу
address = input("Введите адрес: ")
params = {
    "geocode": address,
    "format": "json",
    "kind": "district"
}
response = requests.get(GEOCODER_API_URL, params=params).json()
district = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
print(f"Район: {district}")
