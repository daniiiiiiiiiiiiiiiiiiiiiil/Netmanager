# Network Diagnostic Utility

Инструмент для настройки сетевых интерфейсов, управления маршрутизацией и анализа трафика.

## Основные возможности
* Просмотр активных сетевых адаптеров.
* Изменение IP-адреса, маски и шлюза через.
* Диагностика соединений.
* Анализ трафика в реальном времени.

## Требования к системе
* **ОС:** Windows 10/11.
* **Python:** 3.10 или выше.
* **Драйвер:** Npcap. 
    * *При установке Npcap выберите опцию "Install Npcap in WinPcap API-compatible Mode".*

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/daniiiiiiiiiiiiiiiiiiiiiil/Netmanager/
   cd netmanager
   
2. **Настройте окружение:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   install django psutil scapy
   
3. **Инициализируйте базу данных**
   ```bash
   python manage.py migrate
4. **Запуск: Откройте терминал от имени Администратора и выполните**
   ```bash
   python manage.py runserver

**Откройте в браузере: http://127.0.0.1:8000/**
