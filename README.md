# rucaptcha_api library
Это новая легкая библиотека для простого взаимодействия с сервесом решения капчи RuCaptcha. <br>
Сразу код:
``` python
from rucaptcha import RuCaptchaConnection 

connection = RuCaptchaConnection(token='')          
captcha_file = open('./captcha.png', 'rb')
captcha = connection.send(captcha_file)
decision = captcha.wait_decision()

print(f"Successfully decided: {decision}")
```
И все, мы получили решение! Но это еще не все возможности этой библиотеки, подробнее читайте ниже.

## Список функций:

| Класс | Функция | Описание | Вывод |
|-------|---------|----------|-------|
| RuCaptchaConnection      | send(file)        | Отправка изображения на решение. Файл должен быть типа <_io.BufferedReader>.      | rucaptcha.RuCaptcha      |
| RuCaptchaConnection      | get_balance()        | Получить баланс с точностью до 2-х знаков после запятой.      | float     |
| RuCaptcha      | captcha_ready()        | Создать запрос, готов ли ответ на капчу.      | bool     |
| RuCaptcha      | get_decision()        | Получить решение на капчу. Если она еще не готова, будет выброшена ошибка "CAPCHA_NOT_READY".       | str     |
| RuCaptcha      | wait_decision()        | Ждать решения капчи. Если после первого запроса она не будет готова, библиотека отправит повторный запрос через 2 секунды. Если ответа не будет в течении минуты, выбросит ошибку "Timeout waiting decision".       | str     |

## Возможные исключения:

+ Ошибки сервиса RuCaptcha при отправке капчи: [документация](https://rucaptcha.com/api-rucaptcha#in_errors)
+ Ошибки сервиса RuCaptcha при получении капчи: [документация](https://rucaptcha.com/api-rucaptcha#res_errors)
+ Ошибки библиотеки:
  + [HTTP CODE] Could not connect to RuCatcha server! - сервер вернул код отличный от 200 OK
  + Timeout waiting decision - превышен лимит ожидания решения капчи
  
## Примеры работы с библиотекой:

### Отправка и ожидание решения капчи
``` python
from rucaptcha import RuCaptchaConnection 

connection = RuCaptchaConnection(token='')          
captcha_file = open('./captcha.png', 'rb')
captcha = connection.send(captcha_file)
decision = captcha.wait_decision()

print(f"Successfully decided: {decision}")
```

### Отправка и альетрнативное ожидание решения капчи
``` python
from rucaptcha import RuCaptchaConnection 
import time

connection = RuCaptchaConnection(token='')          
captcha_file = open('./captcha.png', 'rb')
captcha = connection.send(captcha_file)
while True:
  if(captcha.captcha_ready):
    decision = captcha.get_decision()
    break
  time.sleep(5)

print(f"Successfully decided: {decision}")
```
### Получение баланса на сервисе 
``` python
from rucaptcha import RuCaptchaConnection 

connection = RuCaptchaConnection(token='')  
balance = connection.get_balance()
print(f"Your balance: {balance} RUB")
```

* * *

**© Copyright 2020 BHS Studio**
