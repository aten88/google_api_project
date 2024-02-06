from apiclient import discovery
from google.oauth2.service_account import Credentials


SCOPES = [
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive',
]

CREDENTIALS_FILE = 'mythic-plexus-413322-3b94900b03a5.json'


def auth():
    # Создаём экземпляр класса Credentials.
    credentials = Credentials.from_service_account_file(
                  filename=CREDENTIALS_FILE, scopes=SCOPES
                )
    # Создаём экземпляр класса Resource.
    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service, credentials


def create_spreadsheet(service):
    spreadsheet_body = {
        'properties': {
            'title': 'Бюджет путешествий',
            'locale': 'ru_RU'
        },
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Отпуск 2077',
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 100
                }
            }
        }]
    }
    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    spreadsheet_id = response['spreadsheetId']
    print('https://docs.google.com/spreadsheets/d/' + spreadsheet_id)
    return spreadsheet_id


def set_user_permissions(spreadsheet_id, credentials):
    permissions_body = {
        'type': 'user',  # Тип учётных данных.
        'role': 'writer',  # Права доступа для учётной записи.
        'emailAddress': 'kudoman47@gmail.com'
    }  # Ваш личный гугл-аккаунт.

    # Создаётся экземпляр класса Resource для Google Drive API.
    drive_service = discovery.build('drive', 'v3', credentials=credentials)

    # Формируется и сразу выполняется запрос на выдачу прав вашему аккаунту.
    drive_service.permissions().create(
        fileId=spreadsheet_id,
        body=permissions_body,
        fields='id'
    ).execute()


service, credentials = auth()
spreadsheetId = create_spreadsheet(service)
set_user_permissions(spreadsheetId, credentials)
