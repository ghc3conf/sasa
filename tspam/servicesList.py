


allServices='[\
{"url": "https://ng-api.webbankir.com/user/v2/create",\
"kind": "json",\
"data": {"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone": "$phone$","email": "$email$","smsCode":""}},\
    \
{"url": "https://m.tiktok.com/node-a/send/download_link",\
"kind": "json",\
"data": {"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":"$phone$","page":{"pageName":"home","launchMode":"direct","trafficType":""}}},\
    \
{"url": "https://msk.tele2.ru/api/validation/number/",\
"kind": "json",\
"data": {"sender": "Tele2"}},\
    \
{"url": "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",\
"kind": "json",\
"data": {"phone": "$phone$", "otpId": 0}},\
    \
{"url": "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",\
"kind": "data",\
"data": {"st.r.phone": "+$phone$"}},\
    \
{"url": "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",\
"kind": "params",\
"data": {"msisdn": "$phone$"}},\
    \
{"url": "https://moneyman.ru/registration_api/actions/send-confirmation-code",\
"kind": "params",\
"data": "+$phone$"},\
    \
{"url": "https://my.modulbank.ru/api/v2/registration/nameAndPhone",\
"kind": "json",\
"data": {"FirstName": "$name$", "CellPhone": "$phone$", "Package": "optimal"}},\
    \
{"url": "https://lenta.com/api/v1/authentication/requestValidationCode",\
"kind": "json",\
"data": {"phone": "+$phone$"}},\
    \
{"url": "https://api.imgur.com/account/v1/phones/verify",\
"kind": "json",\
"data": {"phone_number": "$phone$", "region_code": "RU"}},\
    \
{"url": "https://www.icq.com/smsreg/requestPhoneValidation.php",\
"kind": "data",\
"data": {"msisdn": "$phone$","locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}},\
    \
{"url": "https://api.eldorado.ua/v1/sign/",\
"kind": "params",\
"data": {"login": "$phone$","step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"}},\
    \
{"url": "https://www.citilink.ru/registration/confirm/phone/$phone$/",\
"kind": "data",\
"data": ""},\
    \
{"url": "https://youla.ru/web-api/auth/request_code",\
"kind": "data",\
"data": {"phone": "$phone$"} },\
    \
{"url": "https://eda.yandex/api/v1/user/request_authentication_code",\
"kind": "json",\
"data": {"phone_number": "+$phone$"} }\
]'
