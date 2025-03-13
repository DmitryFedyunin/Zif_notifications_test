import requests

# Константы для OAuth 2.0 авторизации
TOKEN_URL = "https://test-1.dev-zif-0.hub.zyfra.com/auth/realms/ziiot/protocol/openid-connect/token"
CLIENT_ID = "test-client"
CLIENT_SECRET = "XzH6xQMX4Auy"
USERNAME = "test-user3"
PASSWORD = "539620lol"

def get_oauth_token(custom_token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJPQjNQc3RSYmptTEItRDlJbkRLc2pJUzk3ckNVS3pwd3l1LU5paVU0OVY0In0.eyJleHAiOjE3NDE2OTU5MzUsImlhdCI6MTc0MTY4MTUzNSwiYXV0aF90aW1lIjoxNzQxNjgxNTIxLCJqdGkiOiJkNTYxNmM0YS1jOTFiLTQwY2ItODYyNS1hOTcyZGU1NTcxYjEiLCJpc3MiOiJodHRwczovL3Rlc3QtMS5kZXYtemlmLTAuaHViLnp5ZnJhLmNvbS9hdXRoL3JlYWxtcy96aWlvdCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ZTllNmZlYS05NDAzLTRkOGQtOTQ2MS1kM2ZiZTk0OTdkZmEiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ6dWktYXBwLXNoZWxsIiwibm9uY2UiOiI4YjAxNmM0Zi0wYmI4LTQ5ZTYtODFjOS01NjU4MWNmYzA4OTkiLCJzZXNzaW9uX3N0YXRlIjoiMTYzMzc5MDMtZDgzOC00OThlLThhMGUtYTJjMjI3YmJkNTk3IiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIiwiaHR0cHM6Ly90ZXN0LTEuZGV2LXppZi0wLmh1Yi56eWZyYS5jb20iXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbInppaW90LWFkbWluIiwiZGVmYXVsdC1yb2xlcy16aWlvdCIsIm9mZmxpbmVfYWNjZXNzIiwiQWRtaW5pc3RyYXRvcnMiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiIxNjMzNzkwMy1kODM4LTQ5OGUtOGEwZS1hMmMyMjdiYmQ1OTciLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQlNC80LjRgtGA0LjQuSDQpNC10LTRjtC90LjQvSIsInByZWZlcnJlZF91c2VybmFtZSI6InRlc3QtdXNlcjMiLCJnaXZlbl9uYW1lIjoi0JTQvNC40YLRgNC40LkiLCJmYW1pbHlfbmFtZSI6ItCk0LXQtNGO0L3QuNC9IiwiZW1haWwiOiJkbWl0cml5LmZlZHl1bmluQHp5ZnJhLmNvbSJ9.kRriQ-rM5e9JWiATdaVk8tz8vKIDTwhhLrLQ4u5mQqBm4NyxxD9m7q1b31ZSruATxBtIdaS9Ku27TdNFQL7ejz4KwZ0yGpR1vHlI3ViHtSSNbRgrrr3RScKBEH6TpXvU7wiIatacHnAzj5WgveM6WOxcgJAasS8ygTnDK9EO_UXKvyVVCUtMbxuFTjlgwQVpRPY21i40vGcR_2JQSKt1YyRUfppzc3j-M5VesTQnSUYFyW4OOfkeZRUcxX9WBxB33d-RcJV_CXvmqMATdbZK669cTe4DSsHa0IR7eJjtp4MwWkR1GZ9RBBWzIiW0ZxwsAfZhh_sLB_q44mcxbZ5lMQ"):
    """
    Получение токена OAuth 2.0 или использование переданного кастомного токена.
    :param custom_token: Кастомный токен для авторизации. Если передан, то используется он.
    :return: access_token (str)
    """
    # Если передан кастомный токен, используем его
    if custom_token:
        print("Используется кастомный токен.")
        return custom_token

    # Параметры запроса для получения нового токена
    data = {
        'grant_type': 'password',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'username': USERNAME,
        'password': PASSWORD
    }

    # Отправляем POST запрос для получения токена
    response = requests.post(TOKEN_URL, data=data)
    response_data = response.json()

    # Проверка успешности получения токена
    if response.status_code == 200 and 'access_token' in response_data:
        access_token = response_data['access_token']
        print("Токен успешно получен.")
        return access_token
    else:
        raise Exception(f"Ошибка при получении токена: {response_data}")



# import requests
#
# # URL для получения токена
# TOKEN_URL = "https://test-1.dev-zif-0.hub.zyfra.com/auth/realms/ziiot/protocol/openid-connect/token"
#
# # Данные для авторизации
# USER_NAME = "test-user3"
# PASSWORD = "539620lol"
# CLIENT_ID = "test-client"  # Замените на правильный client_id
# CLIENT_SECRET = "XzH6xQMX4Auy"  # Замените на правильный client_secret
#
#
# def get_oauth_token():
#     """Функция для получения токена OAuth 2.0"""
#     payload = {
#         'grant_type': 'password',
#         'username': USER_NAME,
#         'password': PASSWORD,
#         'client_id': CLIENT_ID,
#         'client_secret': CLIENT_SECRET,
#     }
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#
#     # Отправка POST запроса на получение токена
#     response = requests.post(TOKEN_URL, data=payload, headers=headers)
#
#     # Проверка успешности запроса
#     if response.status_code != 200:
#         raise Exception(f"Ошибка получения токена: {response.text}")
#
#     # Извлечение токена из ответа
#     token = response.json().get("access_token")
#     if not token:
#         raise Exception("Токен не найден в ответе")
#
#     return token
