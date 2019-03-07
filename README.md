## ESP8266 обновление времени с NTP сервера

[![micropython](https://user-images.githubusercontent.com/13176091/53680744-4dfcc080-3ce8-11e9-94e1-c7985181d6a5.png)](https://micropython.org/)

Часы в esp8266 очень не точные, за 1 час погрешность может составлять до **+/- 10с**. 

Код который используется в стандартной библиотеке [ntptime.py](https://github.com/micropython/micropython/blob/master/ports/esp8266/modules/ntptime.py) при *отсутствии соединения с интернетом или превышения времени ожидания ответа*, **завершается ошибкой**. 

В данную библиотеку добавлен обработчик ошибок. При отсутствии соединения или превышения времени ожидания код не завешается ошибкой, а localtime микроконтроллера остается без изменний.

Библиотека используется так же как и стандартная [ntptime.py](https://github.com/micropython/micropython/blob/master/ports/esp8266/modules/ntptime.py)

***Пример использования:***
```python
from time import localtime
import ntp
print(localtime())
ntp.settime()
print(localtime()) 
```
