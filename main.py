import vk_api
import json
import random
from vk_api.longpoll import VkEventType, VkLongPoll


token = "8ddfa3de9ea35a1c3fa6e928054da310661a3c4f8063e3fdadb2aef09a54ab6ac59682e5d07f150ea7252"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "2" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but("Понедельник", "positive"), get_but("Вторник", "positive")],
        [get_but("Среда", "positive"), get_but("Четверг", "positive")],
        [get_but("Пятница", "positive")]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': random.randint(0, 100000),
                                        'keyboard': keyboard})


def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text.lower()
                name = vk_session.method("users.get", {"user_ids": event.user_id})
                name0 = name[0]["first_name"]
                name1 = name[0]["last_name"]
                if request == 'начать':
                    sender(event.user_id, "Привет, этот бот создан для твоего расписания, " + name0 + " " + name1 + "!")
                if request == 'понедельник':
                    sender(event.user_id, "Привет, Твоё расписание на ПОНЕДЕЛЬНИК\n1)ОИБ\n2)Алгоритмизация\n3)ТСИ\n"
                                          "4)Схемотехника")
                if request == 'вторник':
                    sender(event.user_id, "Привет, Твоё расписание на ВТОРНИК\n1)Схемотехника\n2)Схемотехника\n3)ОИБ\n"
                                          "4)Английский.яз")
                if request == 'среда':
                    sender(event.user_id, "Привет, Твоё расписание на СРЕДА\n1)Физ-ра\n2)История\n3)Логика\n"
                                          "4)Алгоритмизация")
                if request == 'четверг':
                    sender(event.user_id, "Привет, Твоё расписание на ЧЕТВЕРГ\n1)ОИБ\n2)Английский язык")
                if request == 'пятница':
                    sender(event.user_id, "Привет, Твоё расписание на ПЯТНИЦА\n1)1.Математика/2.История\n2)Математика\n"
                                          "3)ТСИ\n4)1.Алгоритмизация/2.ТСИ")
main()