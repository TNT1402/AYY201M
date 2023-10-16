import requests
from bs4 import BeautifulSoup
import pyodbc

# Hàm lấy dữ liệu thời tiết và nhiệt độ
def get_weather_temperature(city):
    url = f"https://www.weather.com/en-IN/weather/today/l/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        weather_data = soup.find("div", class_="CurrentConditions--primary--3x9Km")
        temperature = weather_data.find("span", class_="CurrentConditions--tempValue--3KcTQ").text
        return temperature
    else:
        return None

# Kết nối đến cơ sở dữ liệu SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=<MSI>;DATABASE=<ABCCompanny>;UID=<thiendz123>;PWD=<thiendz1231>')
# Thay thế <server_name>, <database_name>, <username>, và <password> bằng thông tin cụ thể của bạn

# Lấy dữ liệu thời tiết và nhiệt độ và lưu vào cơ sở dữ liệu
cities = ["city1", "city2", "city3"]  # Thay thế bằng danh sách các thành phố bạn quan tâm
for city in cities:
    temperature = get_weather_temperature(city)
    if temperature is not None:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Weather (City, Temperature) VALUES (?, ?)", city, temperature)
        conn.commit()

# Đóng kết nối
conn.close()
