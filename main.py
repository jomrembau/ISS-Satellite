import requests
from datetime import datetime
import smtplib

MY_LAT = 51.435150
MY_LONG = 6.762690
email = "enter_email_here"
password = "enter_your_app_password_here"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
if (
    (time_now.hour >= sunset or time_now.hour < sunrise)
    and (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5)
    and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)
    ):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email, password=password)
        message = ("Subject: Look Up!!\n\n"
                   "ISS Satellite Overhead!")
        connection.sendmail(from_addr=email,
                            to_addrs="recipient_address",
                            msg=message)

        connection.quit()




