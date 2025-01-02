import pywhatkit as kit
import pandas as pd
import time

file = "phone.xlsx"
data = pd.read_excel(file)

for index, row in data.iterrows():
    phone = str(row['Phone'])
    if not phone.startswith("+91"):
        phone = "+91" + phone

    message = row['Message']

   
    curtime = time.localtime()
    curhour = curtime.tm_hour
    curminute = curtime.tm_min


    hour = 9
    minute = 30 + index 

    
    if minute >= 60:
        minute -= 60
        hour += 1

    print(f"Message timing: {hour}:{minute}")

    try:
       
        kit.sendwhatmsg(phone, message, hour, minute, 18)
        print(f"message sented successfully  {phone_number} at {hour}:{minute}")

        time.sleep(15)  
    except Exception as e:
        print(f"failed this number {phone}: {e}")
