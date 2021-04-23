import vk_api, json
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
#from si

vk_session = vk_api.VkApi(token="ac4a1efc08aba9faa25bb28e290debf62e3d5c2932430a57020cb07fa37698472f69a06b33bad06bad251")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

upload = VkUpload(vk_session)
def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }

k = {
    "one_time": False,
    "buttons": [
        [get_but('Расписание пар', 'secondary'), get_but('Расписание звонков', 'secondary'), get_but('стикер', 'negative')],
    ]
}

k = json.dumps(k, ensure_ascii=False).encode('utf-8')
k = str(k.decode('utf-8'))

k1 = {
    "one_time": False,
    "buttons": [
        [get_but('первый курс', 'secondary'), get_but('второй курс', 'secondary')],
        [get_but('третий курс', 'secondary'), get_but('четвёртый курс', 'secondary'), get_but('Назад', 'negative')]
    ]
}

k1 = json.dumps(k1, ensure_ascii=False).encode('utf-8')
k1 = str(k1.decode('utf-8'))

k2 = {
    "one_time": False,
    "buttons": [
        [get_but('ИБС-125', 'secondary'), get_but('Курсы', 'negative')]
    ]
}

k2 = json.dumps(k2, ensure_ascii=False).encode('utf-8')
k2 = str(k2.decode('utf-8'))

k3 = {
    "one_time": False,
    "buttons": [
        [get_but('понедельник', 'secondary')],
        [get_but('вторник', 'secondary'), get_but('среда', 'secondary')],
        [get_but('четверг', 'secondary'), get_but('пятница', 'secondary'), get_but('группы', 'negative')]
    ]
}

k3 = json.dumps(k3, ensure_ascii=False).encode('utf-8')
k3 = str(k3.decode('utf-8'))

def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k})

def sender2(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k1})

def sender3(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k2})

def sender4(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k3})


def main():
    for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.to_me:
                   name = vk_session.method("users.get", {"user_ids": event.user_id})
                   name0 = name[0]["first_name"]
                   name1 = name[0]["last_name"]
                   request = event.text.lower()
                   if request == "расписание пар":
                     sender2(event.user_id, "\nВыбери курс ")
                   if request == "начать":
                     sender(event.user_id, "\nКаничива,я твой босс ," + name1 +" "+ name0 )
                   if request == "назад":
                     sender(event.user_id, "\nТы вернулся назад!")
                   if request == "первый курс":
                     sender3(event.user_id, "\nВыбери свою группу!")
                   if request == "курсы":
                     sender2(event.user_id, "\nКурсы!")
                   if request == "группы":
                     sender3(event.user_id, "\nГруппы!")
                   if request == "ибс-125":
                     sender4(event.user_id, "\nВыбери день!")
                   if request == "понедельник":
                     sender4(event.user_id, "Каничива🔥🔥🔥🔥🔥.""Твоё расписание  \n 1)ОИБ\n2)Алгоритмизация\n3)ТСИ\n4)Электротехника")
                   if request == "вторник":
                     sender4(event.user_id, "Каничива🔥🔥🔥🔥.""Твоё расписание \n1)Электротехника\n2)Электротехника\n 3)ОИБ\n4)Англ")
                   if request == "среда":
                     sender4(event.user_id, "Каничива🔥🔥🔥.""Твоё расписание \n 1)Физра\n2)История\n3)Логика\n4)Алгоритмизация")
                   if request == "четверг":
                     sender4(event.user_id, "Каничива🔥🔥.""Твоё расписание \n 1)ОИБ\n2)Англ")
                   if request == "пятница":
                     sender4(event.user_id, "Каничива🔥.""Твоё расписание \n 1)Мат\n2)Мат\n 3)ТСИ\n 4)Алгоритмизация")
                   if request == "привет":
                     sender(event.user_id, "С возвращением семпай  ," + name1 +" "+ name0 )
                   print("Дорогой/ая " + name1 +" "+ name0 + " написал/а сообщение: " + request)

main()
