import os
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from keep_alive import keep_alive
import random
import math

autorize = vk_api.VkApi(token = os.getenv('TOKEN')) 
longpoll = VkLongPoll(autorize) 
upload = VkUpload(autorize)

image1 = "gaga.jpg"
image2 = "cat.jpg"
image3 = "dog.jpg"
image4 = "goodday.jpg"
image5 = "idk.jpg"
image6 = "catdog.jpg"
list_of_users = []
list_of_cats = []
broadcast = False
smile = 51117
N = random.randint(-100, 100)
hello = [51117, 54129, 13312, 12671, 12970, 9976, 5937, ]
bye = [51161, 54130, 20086, 14751, 9199, 5956, 4582, 8350]
cats = [18945, 18946, 18948, 18959, 18950]
dogs = [2047, 2046, 2050, 3067, 3064, 4918]

keyboard = VkKeyboard(one_time=True)
keyboard.add_openlink_button('НЕ ОТКРЫВАЙ', link='https://mai.ru/')
keyboard.add_button('Инфо', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('Привет')
keyboard.add_button('Пока')
keyboard.add_line()
keyboard.add_button('Кототест', color=VkKeyboardColor.PRIMARY)

keyboard2 = VkKeyboard(one_time=True)
keyboard2.add_button('Ссылки на конференции и папки',  color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_openlink_button('Расписание', link='https://vk.cc/bWWV6R')
keyboard2.add_openlink_button('Сдача лаб', link='https://vk.cc/bWWV8W')
keyboard2.add_line()
keyboard2.add_button('Подписаться на рассылку', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Кототест', color=VkKeyboardColor.PRIMARY)

keyboard4 = VkKeyboard(one_time=True)
keyboard4.add_openlink_button('МегаСкат', link='https://vk.cc/bWWVrw')
keyboard4.add_openlink_button('Папка faq8', link='https://vk.cc/bWWVvp')
keyboard4.add_line()
keyboard4.add_openlink_button('Алгебра и Геометрия', link='https://vk.cc/bWWVP7')
keyboard4.add_openlink_button('ЛМС(зочем)', link='https://lms.mai.ru/')
keyboard4.add_line()
keyboard4.add_button('Инфо', color=VkKeyboardColor.POSITIVE)

def write_message(sender, message):
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'attachment': ','.join(attachment), 'keyboard': keyboard.get_keyboard()})

def hi_message(sender, message):
    smile = random.choice(hello)
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'attachment': ','.join(attachment), 'keyboard': keyboard.get_keyboard()})
    autorize.method('messages.send', {'user_id': sender, 'sticker_id': smile, 'random_id': get_random_id()})

def bye_message(sender, message):
    smile = random.choice(bye)
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'attachment': ','.join(attachment), 'keyboard': keyboard.get_keyboard()})
    autorize.method('messages.send', {'user_id': sender, 'sticker_id': smile, 'random_id': get_random_id()})

def info_message(sender, message):
    smile = random.choice(hello)
    autorize.method('messages.send', {'user_id': sender, 'sticker_id': smile, 'random_id': get_random_id()})
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard2.get_keyboard()})

def info2_message(sender, message):
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard4.get_keyboard()})

def cat_message(sender, message):
    smile = random.choice(cats)
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'attachment': ','.join(attachment), 'keyboard': keyboard.get_keyboard()})
    autorize.method('messages.send', {'user_id': sender, 'sticker_id': smile, 'random_id': get_random_id()})

def dog_message(sender, message):
    smile = random.choice(dogs)
    autorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'attachment': ','.join(attachment), 'keyboard': keyboard.get_keyboard()})
    autorize.method('messages.send', {'user_id': sender, 'sticker_id': smile, 'random_id': get_random_id()})

keep_alive()
for event in longpoll.listen():
    f = open("register_mail.txt", "r")
    for line in f:
        list_of_users.append(str(line))
    f.close()
    list_of_users = [str(line).rstrip() for line in list_of_users]
    list_of_users = list(filter(None, list_of_users))
    list_of_users = list(set(list_of_users)) 
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text.lower()
        sender = event.user_id
        attachment = []

        if received_message == "привет":
            upload_image = upload.photo_messages(photos = image4)[0]
            attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            hi_message(sender, "Приветик")
        
        elif received_message == "инфо" or received_message == "начать":
            info_message(sender, "806-ой ракетный взвод!&#127775;\nЗдесь ты можешь найти всю нужную (или ненужную) тебе информацию!&#9992;")
        
        elif received_message == "ссылки на конференции и папки":
            info2_message(sender, "Ссылки на различные папки с полезными материалами\n\nП.С. Вся остальная информация появится в начале второго семестра")
        
        elif received_message == "подписаться на рассылку":
            if list_of_users.count(sender) == 0:
                list_of_users.append(sender)
                with open("register_mail.txt", "w") as file:
                    print(*list_of_users, file=file, sep='\n')
                upload_image = upload.photo_messages(photos = image5)[0]
                attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                write_message(sender, "Ты подписан на уведомления")
                list_of_users = [str(line).rstrip() for line in list_of_users]
                list_of_users = list(filter(None, list_of_users))
                list_of_users = list(set(list_of_users))
            else:
                upload_image = upload.photo_messages(photos = image1)[0]
                attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                write_message(sender, "Уже есть в списке")
        
        elif received_message == "пока":
            bye_message(sender, "Тiкай з городу")
        
        elif received_message == "рассылка" and (sender == 293203613 or sender == 74991919) and broadcast == False:
            broadcast = True
            write_message(sender, "Напиши то, что нужно разослать")
        
        elif received_message == "кототест":
            list_of_cats.append(sender)
            N = random.randint(-5, 5)
            if N > 0:
                N = random.randint(1, 100)
                upload_image = upload.photo_messages(photos = image2)[0]
                attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                cat_message(sender, "Вау!\nТы на " + str(N) + "% котик&#128568;")
            elif N == 0:
                upload_image = upload.photo_messages(photos = image6)[0]
                attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                write_message(sender, "Ну ничоси\nТы - котопёс!&#128125;")
            else:
                N = random.randint(1, 100)
                upload_image = upload.photo_messages(photos = image3)[0]
                attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                dog_message(sender, "Ё моё, да ты на " + str(math.ceil(math.fabs(N))) + "% собака &#128021;")
        
        else:
            if (sender == 293203613 or sender == 74991919) and broadcast == True:
                for user in list_of_users:
                    write_message(user, received_message)
                broadcast = False
            else:
                upload_image = upload.photo_messages(photos = image1)[0]
                attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                write_message(sender, "Я тебя не понимаю, нажми на кнопку \"Инфо\"" + "  &#9992;")  
