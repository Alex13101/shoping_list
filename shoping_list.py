# Это мой список покупок
import telebot
from telebot import types
from time import sleep


from utils_for_shoping_list import is_user



bot = telebot.TeleBot('_____________________________')  # Создаем экземпляр бота

shopList = []




@bot.message_handler(commands=['start']) # функция обробатывающая команду /start
def handle_text(message):
    bot.send_message(message.chat.id, 'Введите пароль! ')
    bot.register_next_step_handler(message, password_chek)


def password_chek(message):
    user = is_user(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("Удалить_из_списка,_купленное")
    item3 = types.KeyboardButton("Показать_весь_список")
    markup.add(item2)
    markup.add(item3)
    if user is not None:
        bot.send_message(message.chat.id, f'Привет {user} Что делаем? ', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, " Попробуйте еще раз: /start")


@bot.message_handler(content_types=["text"])
def redirection(message):
    if message.text == "Удалить_из_списка,_купленное": # функция удаления из списка
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Удалить_из_списка,_купленное")
        item3 = types.KeyboardButton("Показать_весь_список")
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Кукую позицию удалить? ', reply_markup=markup)
        bot.register_next_step_handler(message, delete_pos_shoplist)

    elif message.text == "Показать_весь_список": # функция печати списка
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Удалить_из_списка,_купленное")
        item3 = types.KeyboardButton("Показать_весь_список")
        markup.add(item2)
        markup.add(item3)
        with open('shop_list.txt', 'r', encoding='utf8') as f:
            shopList = [line for line in f]  # запись кода в список
            print(shopList)
        for x in range(0, len(shopList)):
            bot.send_message(message.chat.id, f" {x+1}. {shopList[x]} ")

    else:
        product = message.text
        with open('shop_list.txt', 'a', encoding='utf8') as f:
            f.writelines(f'{product}\n')

        bot.send_message(message.chat.id, 'Внесено в список!')


def adding_shoplist(message):  # функция добавления в список
    product = message.text
    print(shopList)    #''' В данном примере Эта функция не используется''' Реализовано в теле функции перенаправления
    with open('shop_list.txt', 'a', encoding='utf8') as f:
        f.writelines(f'{product}\n')

    bot.send_message(message.chat.id, 'Готово')
    #bot.send_message(message.chat.id, 'Что дальше делаем?')

def delete_pos_shoplist(message):
    try:
        pos = int(message.text)
        pos = pos-1
        with open('shop_list.txt', 'r', encoding='utf8') as f: # открытие файла для чтения списка
            shopList = [line for line in f]  #  перебор по линиям из файла и чтение списка
            print(shopList)
            del shopList[pos]  # Удаление выбраной позиции
        with open('shop_list.txt', 'w', encoding='utf8') as f: # Открытие файла для записи
            for line in shopList:
                f.write(line) # Запись списка в файл после удаления
        bot.send_message(message.chat.id, 'Удалено')


    except:  # Проверка на ошибку по целому числу int
        bot.send_message(message.chat.id, " Либо не число, либо такой позиции не существует. Выбирай что делать! ")


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as E:
        print(E)
        sleep(15) 



# print('Покупки: ', end='')
# for item in shopList:
#     print(item, end='')
#
# adding = int(input("\nХотите добавить\удалить покупку? Добавить - 1, Удалить - 2:"))
# while adding == 1:  # Начинаем цикл
#     shopList.append(input("Введите что нужно купить:"))
#     adding = int(input("Хотите продолжить? Удалить- 2, Добавить-1:"))
# else:
#     print()
#
# # while adding==2:
#
#
# print(' Теперь мой список покупок таков:', shopList)
#
# print('Также нужно купить риса.')
# shopList.append("рис")
# print(' Отсортирую-ка я свой список')
# shopList.sort()
# print('Отсортированный список покупок выглядит так:', shopList)
# print(' Я должен сделать ', len(shopList), 'покупки.')
# print('Первое, что мне нужно купить, это ', shopList[0])
# for i in range(len(shopList)):
#     olditem = int(input("Позиция которую купил я :"))
#     print(' Я купил', shopList[olditem])
#     del shopList[olditem]
#     print(' Теперь мой список покупок:', shopList)
