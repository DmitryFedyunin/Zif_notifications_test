import pprint
from datetime import datetime
import pytest
import requests
import json
import uuid
import time
from auth import get_oauth_token  # Импортируем функцию для получения токена


class TestEventTypeCreation:
    """Класс для тестирования создания и обработки типов событий и рассылок"""

    # @pytest.fixture(scope="class")
    # def oauth_token(self):
    #     """Фикстура для получения токена OAuth 2.0"""
    #     return get_oauth_token()

    @pytest.fixture(scope="class")
    def oauth_token(self):
        """
        Фикстура для получения токена OAuth 2.0.
        Если требуется использовать кастомный токен, передай его сюда.
        """
        # Задай кастомный токен здесь, если нужно
        custom_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJPQjNQc3RSYmptTEItRDlJbkRLc2pJUzk3ckNVS3pwd3l1LU5paVU0OVY0In0.eyJleHAiOjE3NDE2OTU5MzUsImlhdCI6MTc0MTY4MTUzNSwiYXV0aF90aW1lIjoxNzQxNjgxNTIxLCJqdGkiOiJkNTYxNmM0YS1jOTFiLTQwY2ItODYyNS1hOTcyZGU1NTcxYjEiLCJpc3MiOiJodHRwczovL3Rlc3QtMS5kZXYtemlmLTAuaHViLnp5ZnJhLmNvbS9hdXRoL3JlYWxtcy96aWlvdCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ZTllNmZlYS05NDAzLTRkOGQtOTQ2MS1kM2ZiZTk0OTdkZmEiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ6dWktYXBwLXNoZWxsIiwibm9uY2UiOiI4YjAxNmM0Zi0wYmI4LTQ5ZTYtODFjOS01NjU4MWNmYzA4OTkiLCJzZXNzaW9uX3N0YXRlIjoiMTYzMzc5MDMtZDgzOC00OThlLThhMGUtYTJjMjI3YmJkNTk3IiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIiwiaHR0cHM6Ly90ZXN0LTEuZGV2LXppZi0wLmh1Yi56eWZyYS5jb20iXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbInppaW90LWFkbWluIiwiZGVmYXVsdC1yb2xlcy16aWlvdCIsIm9mZmxpbmVfYWNjZXNzIiwiQWRtaW5pc3RyYXRvcnMiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiIxNjMzNzkwMy1kODM4LTQ5OGUtOGEwZS1hMmMyMjdiYmQ1OTciLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQlNC80LjRgtGA0LjQuSDQpNC10LTRjtC90LjQvSIsInByZWZlcnJlZF91c2VybmFtZSI6InRlc3QtdXNlcjMiLCJnaXZlbl9uYW1lIjoi0JTQvNC40YLRgNC40LkiLCJmYW1pbHlfbmFtZSI6ItCk0LXQtNGO0L3QuNC9IiwiZW1haWwiOiJkbWl0cml5LmZlZHl1bmluQHp5ZnJhLmNvbSJ9.kRriQ-rM5e9JWiATdaVk8tz8vKIDTwhhLrLQ4u5mQqBm4NyxxD9m7q1b31ZSruATxBtIdaS9Ku27TdNFQL7ejz4KwZ0yGpR1vHlI3ViHtSSNbRgrrr3RScKBEH6TpXvU7wiIatacHnAzj5WgveM6WOxcgJAasS8ygTnDK9EO_UXKvyVVCUtMbxuFTjlgwQVpRPY21i40vGcR_2JQSKt1YyRUfppzc3j-M5VesTQnSUYFyW4OOfkeZRUcxX9WBxB33d-RcJV_CXvmqMATdbZK669cTe4DSsHa0IR7eJjtp4MwWkR1GZ9RBBWzIiW0ZxwsAfZhh_sLB_q44mcxbZ5lMQ"  # Или None, если нужен новый токен
        return get_oauth_token(custom_token=custom_token)

    @pytest.fixture
    def date1_from(self):
        """Фикстура для получения текущей даты в нужном формате"""
        return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')

    @pytest.fixture(scope="class")
    def template_id(self, oauth_token):
        """Метод для создания шаблона рассылки и получения его ID"""
        template_id = str(uuid.uuid4())
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/templates/{template_id}"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "id": template_id,
            "code": "Code_notification",
            "name": "Test_notifications1",
            "subject": "Zagolovog",
            "content": "<p>{{event.acknowledged}}</p>"
        }

        # Вывод заголовков и тела запроса
        print("\n=== Заголовки ===")
        pprint.pprint(headers)
        print("\n=== Тело запроса ===")
        pprint.pprint(payload)

        token = get_oauth_token()
        print(f"OAuth Token: {token} (Length: {len(token)})")
        response = requests.put(url, headers=headers, json=payload)

        print("\n=== Статус-код ответа ===")
        print(response.status_code)
        print("\n=== Тело ответа ===")
        print(response.text)

        assert response.status_code == 204, f"Expected status code 204, got {response.status_code}. Response: {response.text}"
        print(f"\n=== Создан шаблон рассылки ===\nTemplate ID: {template_id}")
        return template_id

    @pytest.fixture(scope="class")
    def group_id(self):
        """Фикстура для генерации уникального GUID для группы рассылки"""
        return str(uuid.uuid4())

    def test_create_delivery_group(self, oauth_token, template_id, group_id):
        """Метод для создания группы рассылки методом PUT"""
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/deliverygroups/{group_id}"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "id": group_id,
            # "code": "DeliveryGroup_notification_test",
            "name": "DeliveryGroup_notification_test",
            "description": "{{eventType.description}}",
            "notificationTemplateId": template_id,
            "groupSend": False,
            "enabled": True
        }

        response = requests.put(url, headers=headers, data=json.dumps(payload))

        # Проверка успешного выполнения запроса
        assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"
        print("Создана группа рассылки", group_id)

    def test_add_contact_to_delivery_group(self, oauth_token, group_id):
        """Метод для добавления пользователя в группу рассылки методом POST"""
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/deliverygroups/{group_id}/contacts"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        payload = [
            "951f9506-ed6f-456f-be10-8466f3503240"
        ]

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Проверка успешного выполнения запроса
        assert response.status_code == 201, f"Expected status code 200, got {response.status_code}"
        print("Пользователь добавлен в группу рассылки: 951f9506-ed6f-456f-be10-8466f3503240")

    def test_create_notification_condition(self, oauth_token, group_id):
        """Метод для создания условия уведомлений методом PUT"""
        conditional_id = str(uuid.uuid4())
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/notificationconditions/{conditional_id}"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "id": conditional_id,
            "eventTypeName": "Проверка уведомления",
            "onCreate": True,
            "onUpdate": False,
            "onDelete": False,
            "eventTypeId": "6039b3a1-3861-49b9-b7a4-a34f444f19fb",
            "deliveryGroupId": group_id
        }

        response = requests.put(url, headers=headers, data=json.dumps(payload))

        # Проверка успешного выполнения запроса
        assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"
        print("Условие события добавлено", conditional_id)

    @pytest.mark.parametrize("i", range(2))  # Параметризация для 5 повторений
    def test_create_event(self, oauth_token, i):
        """Метод для создания события на уведомление методом POST"""
        event_id = str(uuid.uuid4())  # Генерация уникального event_id
        date_from = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')  # Получение текущей даты в формате ISO 8601
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-events/events"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "id": event_id,
            "eventTypeId": "6039b3a1-3861-49b9-b7a4-a34f444f19fb",
            "from": date_from,
            "name": f"Проверка уведомления {i}",  # Добавление индекса для уникальности
            "description": "АЛАРМ"
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Проверка успешного выполнения запроса
        assert response.status_code == 201, f"Expected status code 200, got {response.status_code}"
        print("Событие с уведомление создано:", event_id, "Дата", date_from)
        return date_from

    def test_get_notifications(self, oauth_token, date1_from):
        """Метод для получения уведомлений методом GET"""
        #time.sleep(4)  # Пауза перед запросом

        # Формируем URL с параметром date1_from
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/notifications?userId=9e9e6fea-9403-4d8d-9461-d3fbe9497dfa&from={date1_from}&ispaged=false"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        # Проверка успешного выполнения запроса
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        response_data = response.json()

        # Проверка и вывод содержимого блока "content"
        print("\n=== Notification Content ===")
        content_block = response_data.get("content", [])

        if content_block:
            print(json.dumps(content_block, indent=4, ensure_ascii=False))
        else:
            print("Блок 'content' пуст или отсутствует")
        print("=============================")

    def test_send_notification_low(self, oauth_token):
        """Метод для отправки уведомлений с разными приоритетами"""
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/sendingsources/internal/sending"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        priorities = ["Low", "1", 1]

        for priority in priorities:
            payload = {
                "recipients": ["9e9e6fea-9403-4d8d-9461-d3fbe9497dfa"],
                "subject": "Low",
                "content": "Low",
                "notificationPriority": priority
            }

            response = requests.post(url, headers=headers, json=payload)

            # Проверка успешного выполнения запроса
            assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"

            print(f"\n=== Notification Sent with Priority: {priority} ===")

    def test_send_notification_medium(self, oauth_token):
        """Метод для отправки уведомлений с разными приоритетами"""
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/sendingsources/internal/sending"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        priorities = ["Medium", "2", 2]

        for priority in priorities:
            payload = {
                "recipients": ["9e9e6fea-9403-4d8d-9461-d3fbe9497dfa"],
                "subject": "Medium",
                "content": "Medium",
                "notificationPriority": priority
            }

            response = requests.post(url, headers=headers, json=payload)

            # Проверка успешного выполнения запроса
            assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"

            print(f"\n=== Notification Sent with Priority: {priority} ===")

    def test_send_notification_high(self, oauth_token):
        """Метод для отправки уведомлений с разными приоритетами"""
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/sendingsources/internal/sending"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        priorities = ["High", "3", 3]

        for priority in priorities:
            payload = {
                "recipients": ["9e9e6fea-9403-4d8d-9461-d3fbe9497dfa"],
                "subject": "High",
                "content": "High",
                "notificationPriority": priority
            }

            response = requests.post(url, headers=headers, json=payload)

            # Проверка успешного выполнения запроса
            assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"

            print(f"\n=== Notification Sent with Priority: {priority} ===")

    def test_send_notification_critical(self, oauth_token):
        """Метод для отправки уведомлений с разными приоритетами"""
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/sendingsources/internal/sending"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        priorities = ["Critical", "4", 4]

        for priority in priorities:
            payload = {
                "recipients": ["9e9e6fea-9403-4d8d-9461-d3fbe9497dfa"],
                "subject": "Critical",
                "content": "Critical",
                "notificationPriority": priority
            }

            response = requests.post(url, headers=headers, json=payload)

            # Проверка успешного выполнения запроса
            assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"

            print(f"\n=== Notification Sent with Priority: {priority} ===")

    def test_send_notification_no_priority(self, oauth_token):
        """Метод для отправки уведомлений с разными приоритетами"""
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/sendingsources/internal/sending"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }
        payload = {
                "recipients": ["9e9e6fea-9403-4d8d-9461-d3fbe9497dfa"],
                "subject": "Title",
                "content": "Text"
            }

        response = requests.post(url, headers=headers, json=payload)

        # Проверка успешного выполнения запроса
        assert response.status_code == 204, f"Expected status code 200, got {response.status_code}"

        print(f"\n=== Notification Sent with Priority: Без приоритета ===")

    @pytest.fixture
    def log_id_clean(self, oauth_token):
        """Получение идентификатора журнала уведомлений"""
        url = "https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/api/v2/sendingsources/internal/sending"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "recipients": ["9e9e6fea-9403-4d8d-9461-d3fbe9497dfa"],
            "subject": "Low",
            "content": "Low"
        }

        response = requests.post(url, headers=headers, json=payload)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        # Извлечение идентификатора из тела ответа
        log_id_clean = response.json()
        if isinstance(log_id_clean, str):
            log_id_clean = log_id_clean.strip('"')

        print(f"\n=== Полученный идентификатор:  ===",log_id_clean)

        return log_id_clean


    def test_delete_delivery_group(self, oauth_token, group_id):
        time.sleep(3)
        """Метод для удаления группы рассылки методом DELETE"""
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/deliverygroups/{group_id}"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        response = requests.delete(url, headers=headers)

        # Проверка успешного выполнения запроса
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        print("Группа рассылки удалена:",group_id)

    def test_delete_template(self, oauth_token, template_id):
        """Метод для удаления шаблона рассылки методом DELETE"""
        url = f"https://test-1.dev-zif-0.hub.zyfra.com/zif-notifications/templates/{template_id}"
        headers = {
            "Authorization": f"Bearer {oauth_token}",
            "Content-Type": "application/json"
        }

        response = requests.delete(url, headers=headers)

        # Проверка успешного выполнения запроса
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        print("Шаблон рассылки удален:", template_id)
