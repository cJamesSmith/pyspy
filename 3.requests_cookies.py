import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Cookie': '_octo=GH1.1.917573930.1614239617; tz=Asia/Shanghai; _device_id=3cbfd6adbe11196ae8e9d32811a7d09b; has_recent_activity=1; user_session=9Dbdph7jvZ5YBUSlD9yREGwZJMDO-HMklowFowm_KLbAcJCM; __Host-user_session_same_site=9Dbdph7jvZ5YBUSlD9yREGwZJMDO-HMklowFowm_KLbAcJCM; tz=Asia/Shanghai; logged_in=yes; dotcom_user=cJamesSmith; _gh_sess=gFhrAmKxSKmw/Pcn8Hq0mrlaUvYSasAu2WpGDNjEOcU76MUQvMm9ACLY0AvDanO0rR2rAoA2e18t/Y5/H3uZZg/hOh29bnszVrKbxHW2J9JlW9//2fMXSWKrKcyKyz1OzJwdRhsZH84ZaUD+JUtXzbxVPuLfeylaiRP/j8TUFQKCmoRdzmuOnb2pm5IEdX4oMkYFj9NXvmRPk1qSIGC1L8u8HwOZ1Ozpo44ua6cHNZXiHY2eZviFU1V+0yaXbXeyEfsagLgmHOuYklpHOqOYRgK5VfolMxBYgMQY2hNReGEs93SAtpugfSjkwOfHZcTK7PZ2cVcAcB457vLZ2Ar3T7PpF5MYPy2O+3QvTYlPP1qenggJg7PChkcEWSSVHbwqMZimVZ8TeXRreTojpUQmalX45yazcur/DgBrvVJ/Hy6WeRMSfU3gDr8Wdadnpz0Z1qe+ObR/3+oQCaud7ke1lL/nwt2Z+BF13R1WRmgzossPHuRSRwkY3ltKuP06w+xE6t5sQ6IrFASxt1ePBlQ5g3H+cuEMRTVIOW4dBWH5UMpgT1ibpRMi5lcgJjrA6VIkNEs02YTJ9FIJX96vjJcHj3M1yLVb3zpsbY/ZQlmm4SvwXb3den1JMOi2K2tSqzqfkaxQcim6N42/rDM2dNP0PkZS/EOMfDsCkxic4cOyt46XsLXL4mOkks/6/qUJ8U5Uzti8pXiedy0bY9gayHmeZFS6wtKGo+3ndk0iNXKPjgziiWN4xel2ZQ==--3qem8Akg3It1dXW+--uktcyOordv9854eguN9r1A=='
}

url = 'https://github.com/cJamesSmith'

response = requests.get(url, headers=headers)
with open('github.html', 'wb') as f:
    f.write(response.content)