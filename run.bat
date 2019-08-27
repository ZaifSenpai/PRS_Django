@ECHO off
py manage.py shell -c "from PRS.engine import start_service;start_service();"
py manage.py runserver 192.168.2.2:8000
