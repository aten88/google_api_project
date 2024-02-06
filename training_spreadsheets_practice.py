from datetime import datetime

from googleapiclient import discovery
from google.oauth2.service_account import Credentials

EMAIL_USER = 'ya_hungry_chef@gmail.com'
FORMAT = "%Y/%m/%d %H:%M:%S"

SCOPES = [
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive',
]

info = {
  "type": "service_account",
  "project_id": "mythic-plexus-413322",
  "private_key_id": "3b94900b03a5cebc3b982c53ab25631bbdcd8b9a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQClJSRvMoZHlZN2\ngkPxr7ZTJ3/YfvC4JUqiMgsYXCGbwxOKanzq+Ag83GN5APxolCMPjWGVaPu8daVu\nD+YLF5jFEqiRDk1aaX3Cna7VrSKV4kFATS037UeOi0fBqZhnCk7PW9vfmrqiJIFP\nAYutaj1knYp4njmGVzyrCIjEsd3eUGOWE/mz8sxLh5+zAkz/8drVlneQy4ZVLPDf\ntZFjT1PmMLgWap2wHNc9tGcDR8CUSpXap02EaclE0ju2RKtnN5rk513UNgdy3f8m\nSUw8QeS2RhtKiBPFRuT2vPg3vAYbU6D1N9+Y/z3P25N0M3CCPbrnWfmoMpOJfu0y\nod8Ev7tzAgMBAAECggEAGTDyPtgZLaA+b0xtqtdf241h7hdnBuABY354vM2I/uah\n+3JE/d65+vavYczps9YtBvlNEmqCQ/w6MPDR6Y0+64juF7pzyD/hRCejfMq9RNnP\nlExxgl96k97hIkSJj+Y9oVnkz1Yd9A/XfcLBmMFk/g0eC0ovgjOaeIiDvGVZb8ja\nvJC/aWapH7lmR5iN3zTo1C9vqgobfqrTyyFjG2cLrHTC1xgn38pwepXYqp1cClPg\nluOTj3CGQHHOIHQ32OJ1V+ZureZRLIwcH//JhyAHeMhx2Ir/F1Z2DDJQVUamlq+K\nTF3SN3EMX/+CQE81vHOF4j8d13XxMeJv75dOh72M+QKBgQDPknABbqyrLqaFmKHF\nMhuVG0lD9ncM2U9XFAhHkRRV65hDdjpQYYqONOJk0vvsWjb3SEjKpuDhSKZnZmUZ\nsIa4M3TjKyM4CQXZ1vKWSrtS1nwMr9nHDNnVAw4wBux/O+K7WaqTfuKLsSEhaTsR\nv6mkQ8536C1Ns0uIKU7cVCyWRQKBgQDLrLClbQpzM4DKl19XLmIxHHLzfqDZPJs9\nTT9FjNRn4SFfTFlnMpmNDD5SlcDQUSArV9n0TpctdaCCSLG/1JfIvk7YEZqoNikm\nty4b6l3qRtY0YDj5gzL5ZnkElYatLFz5e0iABxQsUZaQD0k88OVo7BdsychcZsqJ\nKwsZ3Q2iVwKBgQCDWvcYYPJSDd6BUpqk0NXVoQPXR2QFNIvZ3ipzJ6NH0CR2JJ44\nedGVtm/CQCX+ZwS7rfmqjLpotnHfo1O9UxGeBaoljAnojwUt2rF/XGF4xZSQ7sOR\nDFfZTeqvh+Injj0oNFEWr8grgHcnzpD75V80PViuVrY8oobc7s8h7P6eRQKBgQDA\nu2ltIQICgXoeO5+8n+fLEWC1id4rs24zVCXLariUlDVAOL9hKECleDCBdbQ/bIVE\nfp2A0d285tI8dw28uS/ohi2VyRLQmm/WcwDu6Zh1WRLZ/TPs6HoUByP9coE+3fwd\nGMxCWnB8f7g6GjzzrgFoiACisU8oIR0HL/QRRVzhgQKBgF9MRhKUJklZ/gTHtWN6\nWHbSgDR1G1pDd0dy5LiRv/OT6vMhxgyOAEtFr/Jb1Ffy0eVTe9R9UQiqUzP0Y/qK\n1qsiJP/XitLEYhmxoDuFHCfOh5JnvJNAsL9CqLW9rr96+eUHSK7EdR8cuJgB4KpB\n+z2WhKoB7tidyuPXotWFW/h7\n-----END PRIVATE KEY-----\n", # noqa
  "client_email": "aten-admin@mythic-plexus-413322.iam.gserviceaccount.com",
  "client_id": "112919711322354002703",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/aten-admin%40mythic-plexus-413322.iam.gserviceaccount.com", # noqa
  "universe_domain": "googleapis.com"
}


def auth():
    credentials = Credentials.from_service_account_info(
                  info=info, scopes=SCOPES
                )
    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service, credentials


def create_spreadsheet(service):

    formatted_datetime = datetime.now().strftime(FORMAT)

    spreadsheet_body = {
        'properties': {
            'title': 'Morelia viridis menu',
            'locale': 'ru_RU'
        },
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': formatted_datetime,
                'gridProperties': {
                    'rowCount': 20,
                    'columnCount': 11
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
