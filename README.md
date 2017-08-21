## FitDex - Display BG readings from Dexcom CGM on a FitBit device

A purpose of this tool is to display the newest Dexcom CGM blood glucose readings on a FitBit device. It's an ad-hoc solution developed to allow a user to be aware of its blood glucose values while the phone is away, but in Dexcom transmitter Bluetooth radius e.g. gym, CrossFit, marathon race etc.

![FitDex Screen](https://s27.postimg.org/qwnnqe4wz/EE6_C4090-7456-4_C81-9_B10-2_C8_F319_D013_F.jpg)

FitDex utilizes _text-message-over-email_ services and a Dexcom API. The tool will make a request to the Dexcom API to get the latest glucose value on every N seconds and then send a value as an SMS via _text-message-over-email_ service which will be displayed on a FitBit device.

It is tested only on Fitbit Charge 2, but it should work on any Fitbit device which supports text notifications (Fitbit Blaze, Fitbit Alta, Fitbit Alta HR, Fitbit Charge 2, Fitbit Flex 2, Fitbit Surge) [[src]](https://help.fitbit.com/articles/en_US/Help_article/1979).

### Configure

In order to be able to run this tool one has to:
1. Have a Dexcom account
2. Have an Email account
3. Have a cell phone number from one the listed carriers [[src]](https://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/)

To configure the tool, edit the config.ini file. Replace the username and password values in the _DEXCOM_ section, your email details in the _EMAIL_ section and substitute your 10-digit cell number for _number_ for one of the carriers below (P.S. tested only with T-Mobile and Verizon gateways):

- AT&T: number@txt.att.net
- T-Mobile: number@tmomail.net)
- Verizon: number@vtext.com (text-only)
- Sprint: number@messaging.sprintpcs.com or number@pm.sprint.com
- Virgin Mobile: number@vmobl.com
- Tracfone: number@mmst5.tracfone.com
- Metro PCS: number@mymetropcs.com
- Boost Mobile: number@myboostmobile.com
- Cricket: number@mms.cricketwireless.net
- Ptel: number@ptel.com
- Republic Wireless: number@text.republicwireless.com
- Google Fi (Project Fi): number@msg.fi.google.com
- Suncom: number@tms.suncom.com
- Ting: number@message.ting.com
- U.S. Cellular: number@email.uscc.net
- Consumer Cellular: number@cingularme.com
- C-Spire: number@cspire1.com
- Page Plus: number@vtext.com


```markdown
[DEXCOM] 
API_base_url = https://share1.dexcom.com/ShareWebServices/Services/
Username = **YOUR_DEXCOM_ACCOUNT_USERNAME**
Password = **YOUR_DEXCOM_ACCOUNT_PASSWORD**
ApplicationId = 13A907FB-AC7E-4F90-B4EC-2F2B8BE1C607
Notification_Frequency_Seconds = 300

[EMAIL]
SMS_Gateway = **YOUR_CELL_NUMBER**@**CHOSEN_EMAIL_GATEWAY** ; example: 5555555555@vtext.com
Email_Address = **YOUR_EMAIL** ; example: user@gmail.com
Email_Username = **YOUR_EMAIL_ACCOUNT_USERNAME**  ; example: user
Email_Password = **YOUR_EMAIL_ACCOUNT_PASSWORD**  ; example: password12345
SMTP_Server = **YOUR_SMTP_SERVER_ADDRESS**  ; example: 587
SMTP_Port = **YOUR_SMTP_SERVER_PORT**  ; example: smtp.gmail.com
```

### Run

Open CMD, navigate to the directory where you extracted the FitDex and type:

`py FitDex.py`


### Donate

Donations are welcome if you find this tool useful! Please use the wallet address below to donate:
```bitcoin
BTC: 1JfszdofhyQkry6h7JSfbge3J12dUnJ8kP
