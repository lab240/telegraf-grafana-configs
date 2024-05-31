# Привет !

## Что это

Это набор конфигов и файлов для опроса устройств Exagate, ELEMY по SNMP через telegraf и дашборды для отображения в Grafana.

Elemy:
- Elemy ATS1204\ATS1205\ATS1206
- Elemy PDU-1502
- Elemy CCU-1001\CCU-1002

Exagate:

- Exagate PWG-9332-307-91-SIPH
- Exagate SYSG-7001

По аналогии можно подключить, опрашивать и отображать другие устройства.

>В конфигах telegraf участвует конфиг-процессор на starlark (один для всех датчиков), который выкидывает нулевые значения и генерирует метрики. 

:::tip
NapiLinux (http://napilinux.ru) поддерживает telegraf и garafana из коробки с управлением через Веб-интерфейс
:::

## На что обратить внимание

1. MIB-файлы могут тащить зависимости, смотреть внутрь на параметр IMPORT. Те от которых зависят текущие MIB-ы положены в папочку snmp/common
2. В конфиге telegraf: имя устройства получается из опроса SNMP и нужно проверить чтобы оно было такое же в описании опроса таблицы.
3. Во всех конфигах telegraf над изменить IP и порты на ваши.

## Помощь в составлении конфигов \ даш бордов

Мы можем сделать конфиги и дашборды под ваши устройства через простоколы SNMP, MODBUS RTU\TCP, MQTT. 

Напишите dmn@nnz.ru в Телеграм @dmn240


## Видео

https://youtu.be/2gW4XfBO398?si=e6LAAGi06oH1PseR

## Ссылки

- Телеграмканал NapiLinux \ NapiWorld: @napiworld
- Сайт NapiLinux: http://napilinux.ru
- Сайт NapiWorld: http://napiworld.ru
- Сайт Elemy: http://elemy.ru
- Сайт Exagate: http://exagate.ru


## Иллюстрации

1

![img](img/SYSG-7001.jpg)

2
![img](img/SIPH1.jpg)
3
![img](img/OUTLETS_XX.jpg)
4
![](img/1204.jpg)
