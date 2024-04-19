# Учебный проект по интеграции сервисов Google API
## Данный проект дает представление о том:
  - как настраивать и применять сервисы Google Cloud Platform.
  - как использовать Python для управления сервисами Google Sheets API и Google Drive API.
  - как написать приложение для контроля бюджета с формированием отчёта в гугл-таблицах.
#### Стек проекта: Python3.9, Google API, Requests 2.31.0
## Как запустить проект:
  - клонировать репозиторий:
    ```
    git clone git@github.com:aten88/google_api_project.git
    ```
  - установить виртуальное окружение:
    ```
    python -m venv venv
    ```
  - активировать виртуальное окружение:
    ```
    source/venv/Scripts/activate
    ```
  - установить зависимости:
    ```
    pip install -r requirements.txt
    ```
  - Заполнить файл .env и разместить его в корне проекта:
    ```
      EMAIL= адрес эл. почты связанного с сервисным аккаунтом Google 
      TYPE=service_account
      PROJECT_ID=mythic-plexus-413322
      PRIVATE_KEY_ID= Указать id приватного ключа
      PRIVATE_KEY= Указать зашифрованный приватный ключ
      CLIENT_EMAIL= Указать адрес e-mail от сервисного аккаунта
      CLIENT_ID= Указать id пользователя сервисного аккаунта
      AUTH_URI=https://accounts.google.com/o/oauth2/auth
      TOKEN_URI=https://oauth2.googleapis.com/token
      AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
      CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/aten-admin%40mythic-plexus-413322.iam.gserviceaccount.com
      UNIVERSE_DOMAIN=googleapis.com
    ```
  - Запустить исполняемый файл:
    ```
    training_spreadsheets.py
    ```

### Автор: Алексей Тен.
