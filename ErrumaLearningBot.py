import telebot
from telebot import types

bot = telebot.TeleBot('6885740367:AAEbT6dXTieIxCGnPwWttMOwoVfPrjxgrDQ')

@bot.message_handler(commands=['start'])
def startBot(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)  # Задаем ширину строки клавиатуры
    item1 = types.KeyboardButton("Unity")
    item2 = types.KeyboardButton("C#")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите пункт для изучения:", reply_markup=markup)

# ! Обработчик команд для Unity
@bot.message_handler(func=lambda message: message.text == 'Unity')
def unity_topics(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton("Установка Unity")
    item2 = types.KeyboardButton("Создание первого проекта")
    item3 = types.KeyboardButton("Добавление объектов на сцену")
    item4 = types.KeyboardButton("Создание первого скрипта (передвижение)")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Вы выбрали Unity. Какую тему хотите изучить?", reply_markup=markup)

# ! Далее обработчик команд внутри темы Unity
# * Тема "Установка Unity"
@bot.message_handler(func=lambda message: message.text == 'Установка Unity')
def unity_download(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityDownload.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
                   caption="Для того чтобы скачать юнити, вам необходимо зарегистрироваться на "
                   "[официальном сайте Unity3D](https://unity.com/ru/download) и нажать на кнопку"
                   "*Загрузить версию для Windows*", parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, unity_install)
    
def unity_install(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityInstall.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
        caption="После того как вы скачали Unity, вам необходимо установить его. Выберите путь куда хотите установить его и дождитесь полной установки.",
        parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, unity_install_editor)

def unity_install_editor(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityInstallEditor.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
        caption="После установку Unity Hub вам необходимо установить версию Unity для продолжения работы. " 
        "Для этого нажмите на кнопку *Insdte Editor* и выберите рекомендовоную версию и модули которые нужны именно вам. " 
        "Также советую вам создать отдельную папку для всех версий Unity.", parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, unity_add_license)

def unity_add_license(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unitylicenses.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
        caption="Последним шагом надо добавить персональную лицензию. "
        "Для этого выберите настройки, найдитек вкладку *Licenses* и нажмите на кнопку *Add license*. "
        "Выбираете Personal и всё готово!", parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, unity_location)
    
def unity_location(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityInstalls.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
        caption="Также советую изменить пути для инсталлов. Для этого зайдите в настройки и найдите пункт *Installs*. "
        "И оба этих пути так же измените для удобных вам.", parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, unity_final)

def unity_final(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Назад")
    markup.add(item1)
    bot.send_message(message.chat.id,
        "Вот и всё. Теперь вы можете создавать абсолютно любые проекты, творить в них что угодно и становиться знаменитым разработчиком! =)", reply_markup=markup)
    bot.register_next_step_handler(message, back_to_main_menu)

def back_to_main_menu(message):
    unity_topics(message)

# * Тема "Создание первого проекта"
@bot.message_handler(func=lambda message: message.text == 'Создание первого проекта')
def new_priject(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityProjectsNew.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
                   caption="Для создания своего первого проекта необходимо нажать на кнопку *New Project* на главном экране.",
                   parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, first_project)

def first_project(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Далее")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityProjectsCreate.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
                   caption="После этого у вас повяится окно выбора предзаготовок проекта, таких как 2D или 3D проект это будет, заготовка под мобильные телефоны, VR, AR и т.д.",
                   parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, unity_selected)

def unity_selected(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Назад")
    markup.add(item1)
    bot.send_message(message.chat.id,
        "После выбора проекта необходимо дать имя проекту *(изначально это My project)*, выбрать папку проекта и нажать на кнопку *Create project*.", reply_markup=markup)
    bot.register_next_step_handler(message, back_to_main_menu)

def back_to_main_menu(message):
    unity_topics(message)

# * Тема "Добавление объектов на сцену"
@bot.message_handler(func=lambda message: message.text == "Добавление объектов на сцену")
def add_objects(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton("Назад")
    markup.add(item1)
    photo = open('D:\\Программирование\\Python\\Projects\\ErrumaLearningBot\\img\\unityObjects.png', 'rb')
    bot.send_photo(message.chat.id, photo, 
        caption="Для добавления объектов на сцену необходимо нажать правой кнопкой мыши по *окну иерархии (Hierarchy)* и выбрать какой именно объект вы хотите создать",
    parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(message, back_to_main_menu)

def back_to_main_menu(message):
    unity_topics(message)

bot.polling(none_stop=True)