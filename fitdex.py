import sys
import configparser
from time import sleep
import smtplib
import requests

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_last_bg(dex_config):
    value = 0
    payload = {'applicationId': str(dex_config['ApplicationId']) , 'accountName': str(dex_config['Username']), 'password': dex_config['Password'] }
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    sessionIdRequest = requests.post(dex_config['API_base_url'] + 'General/LoginPublisherAccountByName', json=payload, headers=headers)
    if sessionIdRequest.status_code == 200:
        sessionId = sessionIdRequest.text[1:-1]
        uri = dex_config['API_base_url'] + 'Publisher/ReadPublisherLatestGlucoseValues?sessionID=' + sessionId +'&minutes=5&maxCount=1'
        bgRequest = requests.post(uri, headers=headers)
        if bgRequest.status_code == 200:
            if len(bgRequest.json()) > 0 and 'Value' in bgRequest.json()[0]:
                result = bgRequest.json()[0]['Value']
                value = int(result)

    return value

def send_email(email_config,last_value):
    server = smtplib.SMTP(email_config['SMTP_Server'], int(email_config['SMTP_Port']))
    server.starttls()
    server.login(email_config['Email_Username'], email_config['Email_Password'])
    server.sendmail(email_config['Email_Address'], email_config['SMS_Gateway'], str(last_value))
    server.close()

def main():
    config = load_config()
    last_value = 0
    while True:
        value = get_last_bg(config['DEXCOM'])
        if value == last_value or value == 0:
            continue
        last_value = value
        send_email(config['EMAIL'], last_value)
        print('SMS sent. value: ' + str(last_value))
        sleep(int(config['DEXCOM']['Notification_Frequency_Seconds']))

if __name__ == '__main__':
    main()
