Init commit


🚨 Требования 🚨  
----------
### Установки 📎
---

```
+--------------------+
|     service        |
+====================+
| Python pip 3.5-3.6 |  ✅ $ sudo apt-get install python3-pip python3-dev
+--------------------+
| Flask and Gunicorn |  ✅ $ pip install gunicorn flask
+--------------------+
| Nginx              |  ✅ $ sudo nginx -t
+--------------------+
| Supervisor         |  ✅ $ sudo apt-get install supervisor
+--------------------|
| Tinify             |  ✅ $ pip install --upgrade tinify
+--------------------+
| PostgreSQL         |  ✅ $ sudo apt-get install postgresql postgresql-contrib, sudo -u postgres psql
+--------------------+
```  

### Установка google-chrome-stable ⚠️  
---
* **1** - wget -q -O -  https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
* **2** - sudo sh -c 'echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/_stable main" >> /etc/apt/sources.list.d/google-chrome.list'
* **3** - sudo apt-get update
* **4** - sudo apt-get install google-chrome-stable


### Проект находиться
-------
https://github.com/KorkaYess/image_optimizer

### Установка python3-pip python3-dev nginx ⚠️
```
sudo apt-get update	
sudo apt-get install python3-pip python3-dev nginx
```

### Активация виртуального окружения

```
source /home/installer/optimizer/optimizer/bin/activate	
```
### Открыть папку
```
cd optimizer	
```
### Запустить flask файл 
```
nano ~/optimizer/app.py	
```
### Открыть доступ к 5000 порту
```
sudo ufw allow 5000	
```
### Запустить flask приложение
```
python3 app.py
```
### Создание файла WSGI

nano ~/optimizer/wsgi.py

### Тестирование Gunicorn
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
### Перейти на адрес
```
http://server_domain_or_IP:5000
```
### Выключить виртуальное окружение 
```
deactivate
```
### Создать системный файл модуля

sudo nano /etc/systemd/system/image_optimizer.service

```
[Unit]
Description=Gunicorn instance to serve image_optimizer
After=network.target

[Service]
User=installer
Group=www-data
WorkingDirectory=/home/installer/optimizer
Environment=""PATH=/home/installer/optimizer/optimizer/bin""
ExecStart=/home/installer/optimizer/optimizer/bin/gunicorn --workers 3 --bind u$

[Install]
WantedBy=multi-user.target
```
### Запуск gunicorn
```
sudo systemctl start image_optimizer.service	
sudo systemctl enable image_optimizer
```
### Проверяем статус подключения gunicorn, должен быть active
```
sudo systemctl status image_optimizer	
```
### Настройка запросов Nginx к прокси и создание файла
```
sudo nano /etc/nginx/sites-available/image_optimizer
```
```
server {
    listen 80;
    server_name 2.59.41.44;
    
    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000;
    }
}
```

### Чтобы включить только что созданную конфигурацию блока сервера Nginx,
### Свяжите файл с sites-enabled каталогом	
```
sudo ln -s /etc/nginx/sites-available/image_optimizer /etc/nginx/sites-enabled
```
### Запуск Nginx
```
sudo nginx -t	
sudo systemctl restart nginx
```
### Проверяем статус подключения nginx, должен быть active
```
sudo systemctl status nginx
```
### Удалить доступ к 5000 порту
```
sudo ufw delete allow 5000	
sudo ufw allow 'Nginx Full'	
```
Теперь вы должны иметь возможность перейти на доменное
имя или IP-адрес вашего сервера в веб-браузере:
	
http://server_domain_or_IP


### Установка supervisor
```
sudo apt-get install supervisor
```
### Создать файл конфигурации gunicorn.conf в /optimizer/
```
sudo nano /home/installer/optimizer/gunicorn.conf
```
В файле прописать следующие данные
```
import multiprocessing

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '/home/installer/optimizer/logs/gunicorn_access.log'
errorlog = '/home/installer/optimizer/logs/gunicorn_error.log'
capture_output = True
```

### Создать файл конфигурации gunicorn.conf в /etc/ : 
```
sudo nano /etc/supervisor/conf.d/gunicorn.conf
```
В файле прописать следующие данные
```
[program:gunicorn]
directory=/home/installer/optimizer/
command=/home/installer/optimizer/optimizer/bin/gunicorn -c gunicorn.conf wsgi:app
autostart=true
autorestart=true
stderr_logfile=/home/installer/optimizer/logs/supervisor.err.log
stdout_logfile=/home/installer/optimizer/logs/supervisor.out.log
```
### Запуск supervisor
```
sudo supervisorctl start gunicorn
```
### Проверяем статус подключения supervisor, должен быть active
```
sudo supervisorctl status
```
### Очистить supervisor, в случае ошибок подключения
```
sudo apt purge supervisor
```
