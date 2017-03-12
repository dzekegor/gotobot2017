# gotobot2017
Телеграм бот для весенней школы Goto, написанный на Python и PHP
## Инструкция по установке

ТРЕБОВАНИЯ: Windows 7 и новее

* Скачайте [Python v3.4](https://www.python.org/downloads/release/python-344/) (это ОЧЕНЬ ВАЖНО, Python v3.5/3.6 не будет работать)
* Скачайте и установите с [официального сайта MySQL](https://dev.mysql.com/downloads/connector/python/) mysql-connector-python-2.1.5-py3.4 для архитектуры вашего процесора (32 или 64)
* Скачайте и установите [XAMPP 5.6](https://www.apachefriends.org/ru/index.html) в папку C:\\xampp (далее - ~)
* скопируйте файл camp.sql в папку (далее - path)
* В командной строке перейдите в папку ~/mysql/bin
* наберите mysql -u root
* наберите source path/camp.sql
* В любую удобную вам папку скопируйте папку CampBot
* В папку ~/htdocs скопируйте все оставшиеся папки и файлы (папку images и файлы .htaccess, index.html, panel1.php, panel2.php, panel3.php, panel4.php, styles.css, menu.css

## Запуск
* Запустите программу XAMPP Control Panel и запустите Apache и MySQL. Поставьте Apache на порты 80, 443 и MySQL на 3306.
* Запустите в терминале все программы из папки CampBot
* Откройте в браузере localhost

### Доп. информация
Если вас не устраивает название моего бота (GotoBot с username @goto_msk_bot), вы можете в каждом файле найти токен моего бота и заменить его на свой.
