import pandas as pd
from win10toast import ToastNotifier
import time
import requests
import smtplib
import datetime

def send_text(to, message, name, subject):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = f"sender_id=FSTSMS&message={message}&language=english&route=p&numbers={to}"

    headers = {
        "authorization": "api_key",
        "content-type": "application/x-www-form-urlencoded",
        "cache-control": "no-cache",
    }

    response_obj = requests.request("POST", url, data=payload, headers=headers)

    print(response_obj.text)
    print("SMS text sent to " + str(to) + " with subject :" + str(subject) + " and message :" + str(message))

    toast.show_toast("SMS text sent!" , f"{name} was sent a message", threaded = True, icon_path = None, duration = 6)

    while toast.notification_active():
        time.sleep(0.1)

if __name__ == "__main__":

    dataframe = pd.read_excel("excelsheet.xlsx") # read excel sheet containing contacts info
    today = datetime.datetime.now().strftime("%d-%m") # today's date DD-MM
    year_now = datetime.datetime.now().strftime("%Y") # current year YY

    writeInd = []

    for i, item in dataframe.iterrows():
        message = "Happy Birthday! I hope you have a great day." + str(item["name"])

        birthday = item["birthday"].strftime("%d-%m")

        if today == birthday and year_now not in str(item["year"]):
            send_text(item["contact"], message, item["name"], "Happy Birthday")

            writeInd.append(i)

    for i in writeInd:
        yr = dataframe.loc[i, "year"]
        dataframe.loc[i, "year"] = str(yr) + "," + str(year_now)

    dataframe.to_excel("excelsheet.xlsx", index = False)