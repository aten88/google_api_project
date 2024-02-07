from google.oauth2.service_account import Credentials
from googleapiclient import discovery

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

SPREADSHEET_ID = '1ROfBpouFFpzILWXekFo9M8emMnCfP8OJ8-g-cO-Ireg'

EMAIL_USER = 'ya_hungry_chef@gmail.com'

info = {
  "type": "service_account",
  "project_id": "chef-project",
  "private_key_id": "ae966c09408cd809ff4ce5b90159ca9a81b4dfd3",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCj71Jq/QP7toLH\nAknNQZOclheRw4jMIkc1RoJX5Z5WMl7RFUsf8dXNGV0xR+3uLmhvrJ6EZCs3l0x/\nDk4B1VDLTrZUOemEwKYQPh8wvPlKjh6hMMrYnI5Pclg4TRaiT8AWwTYyv0HGAWa5\nk3VXA6E6YJVu654P5mG5B5+MNVQIwUrt0Md8awyP0Luqr9DrQWO92OhTO2x21W/B\nFZTDRmOknruU44R7TDyg2ZorxQk6pbHYnWitXWY5Ay2JJem1mQSR6Qt1oJQWr6LE\nkKr3M1cJxHJpz8E2Wlk43Ih5g2WuWKaBdGd6NTlHjcF23CS1EQOf8LLzdEZ8T7is\n3wgA4mgnAgMBAAECgf8BYy/PYqol9zrOybYrho05RgvtBTqjKlHFTFN4wE4WwgEL\nbqK0IoKCDzTlYIvNouw/Wwv8aDH1cSe0lj+9buYVfRUN9sTYhXONBPmT8AWBcV0m\nVW4MvJvNEFVZefg3EiBjZj852WSKcyNAxClkvc3KMLG9vpYX4bCctZ55ZqTPbiU8\ncrkuGyKZCMl71VC6ERcK4PMgPVghN9N21i0znUL+QY7uS8W6eY6UvELadejICAIb\nTO7zV92/t8O5VOCFWM/B8F2OU8tqejbNEeI2FmvEYfpidi7CvmG97C0GfjupUcuu\nVudNHGhgQ55fbLUM1qrMIyditEzE6dgyUNVdGTECgYEAzoV8XWzOjjklzB/Sro60\nQT6+xi9MwhuAZlqe7j2TL80+KjdrWeRaZ2QUU0Sxk3fHXCtC890zP6bBHNMhwT5d\ndDD2f3KA2lGY8d+kHqqrMBexGkx/02TtlPtzHn67U2dOcz+PVOYNsPpPlI+a9BzA\niBjmQhgF1/8hpsSaulCL4RcCgYEAyzXjDCPGA8x9d0GSaggFPPjzq3AF4SyVVlM+\nogDe7BBae0dMdnm8bC3rnuCR9rYyRWF9HBHxB/57jb5asA4Al7mBjJ2T2BsbBiXW\nudnHS84xc5qWv9og2aNLvubQ7FSFbkWgAfTndiU+zfXVR0QjHLHVH2JYhVBIBOkF\nrqSye3ECgYAD6r44G2czhVv1KilZzDUZA7KkmaMQD2t5BYD8LcjL4E2siU6M7urU\nCS7lgWkIzf3G/r8PVwOw0l3ZSRvbyW4GVSNnuWk+Osv20nIPbtc+W0StpgPKo6Bp\n8fb1/htZcp0nTG5QguiBkc3OmIas2JrCOg6r9D6wIROnURVKMVrl0wKBgQC6q97N\naRNeq/vZkF/ajVGaiCr3IqoUBquMqF3R3jDp87/anU2NTBkd2zUmNq9/TjFx8LNI\nFOcw68I+HE4cilBbEGsEbEDC9Wtmw120Tm04ospkou62gL9KjipnzIrBfocwHD93\nbK0vp9lAxAJPPDVxB596/BHLLUtrT1AL9XmL0QKBgFe0XXZoyoeyhIS4ZAWpw30P\nDifqdn3j/rRTW7U5Wxl832vBlmOS7/EKbyc/JoypdpLXK9VMDvO1hMz2b/zMC2A3\nRIRIENZX91hkocQ1fujezBYIyLITxFqDFVsca3tUWca6USGv8+4fA7F6/UnDtDF5\n1WswjrILyaQuv1ZA6G1v\n-----END PRIVATE KEY-----\n", # noqa
  "client_email": "test@chef-project.iam.gserviceaccount.com",
  "client_id": "101814793754218499111",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test%40chef-project.iam.gserviceaccount.com" # noqa
}


def auth():
    credentials = Credentials.from_service_account_info(
        info=info, scopes=SCOPES
    )
    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service, credentials


def update_ranges_values(service, SPREADSHEET_ID):
    mon_menu = ['Понедельник', ['Салат из свеклы', '100г'], ['Борщ', '250г'], ['Плов', '150г']] # noqa
    mon_range = 'Лист1!B1:C4'

    wed_menu = ['Среда', ['Оливье', '100г'], ['Куриная лапша', '250г'], ['Спагетти', '150г']] # noqa
    wed_range = 'Лист1!E1:F4'

    fri_menu = ['Пятница', ['Витаминный', '100г'], ['Харчо', '250г'], ['Тушёный картофель', '150г']] # noqa
    fri_range = 'Лист1!H1:I4'
    body = {
        'valueInputOption': 'RAW',
        'data': [
            {
                'range': mon_range,
                'majorDimension': 'ROWS',
                'values': mon_menu
            },
            {
                'range': wed_range,
                'majorDimension': 'ROWS',
                'values': wed_menu
            },
            {
                'range': fri_range,
                'majorDimension': 'ROWS',
                'values': fri_menu
            },
        ]
    }
    request = service.spreadsheets().values().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, body=body
    )
    return request.execute()
