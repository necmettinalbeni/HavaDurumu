import requests

api_key = "a2a9a62427c22c7a0593be311c436d51"

city = input("Hava durumu için şehir adı girin: ")

base_url = "http://api.openweathermap.org/data/2.5/weather"
complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

response = requests.get(complete_url)

print("Status Code:", response.status_code)

print("Content-Type:", response.headers['content-type'])

print("Encoding:", response.encoding)

print("Response Text:", response.text)

print("JSON Response:", response.json())
