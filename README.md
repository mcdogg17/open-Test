<h3 align="center">Flask Toxic Test</h3>

  <p align="center">
    Веб-сервис определения токсичности теста
    <br>
  </p>

### О сервисе
Сервис представляет собой flask-приложение. Суть сервиса заключена в определении токсичности текста.

### Стек
При написании сервиса я использовал фреймворк flask. Также была использована готовая модель анализа текста (https://huggingface.co/blanchefort/rubert-base-cased-sentiment)
* Python
* Flask
* Docker


## Установка

Проект завернут в контейнер и оркестрируется через Docker.
* Склонируйте репозиторий
* Выполните следующие команды:
```docker build -t [NAME] .```, 
```docker run -p [PORT_service:PORT_docker] [NAME] ```

Приложение будет доступно на host: 127.0.0.1 and port: 80
