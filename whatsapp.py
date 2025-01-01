import pywhatkit as kit
import pandas as pd
import time

file_path = "phone.xlsx"
data = pd.read_excel(file_path)

for index, row in data.iterrows():
    phone_number = str(row['Phone'])
    if not phone_number.startswith("+91"):
        phone_number = "+91" + phone_number

    message = row['Message']

   
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min


    hour = 9
    minute = 30 + index 

    
    if minute >= 60:
        minute -= 60
        hour += 1

    print(f"Message will be sent at: {hour}:{minute}")

    try:
       
        kit.sendwhatmsg(phone_number, message, hour, minute, 18)
        print(f"Message successfully scheduled for {phone_number} at {hour}:{minute}")

        time.sleep(15)  
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
