
Датчик надо настроить на mqtt. 
Для этого в Вебке датчика указать IP-параметры и 
IP mqtt брокера, имя юзера, пароль

На IP надо чтобы крутился сервис mosquitto 

c таким конфигом

```
bind_address 0.0.0.0
allow_anonymous false
password_file /etc/mosquitto/passwd

```

Файл passwd делается так

```
mosquitto_passwd -c /etc/mosquitto/passwd user
chown mosquitto /etc/mosquitto/passwd

```