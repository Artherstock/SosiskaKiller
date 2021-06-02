# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

# настройки
# opts = {
#     "alias": ('кеша', 'кеш', 'инокентий', 'иннокентий', 'кишун', 'киш',
#               'кишаня', 'кяш', 'кяша', 'кэш', 'кэша'),
#     "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
#     "cmds": {
#         "ctime": ('текущее время', 'сейчас времени', 'который час'),
#         "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
#         "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты')
#     }
pts = {"Привет":["Привет!", "Приветульки"],
       "Как дела?":["Нормально", "Отлично", "Плохо"],
       "Почему?":["Сам не знаю", "Просто настроения нету"],
       "Кто твои родители?": ["По сути у меня нету родителей, но у меня есть создатели, Артур и Степа!"],
       "Что ты умеешь?": ["Я пока что мало что знаю и умею, но если ты меня будешь обучать я стану умнее"]}

while True:
    new_question = input('Введи новый вопрос >>')
    new_answer = input('Введи ответ на вопрос >>')

    for i in list(pts):
        if new_question in i:
            print('Такой вопрос есть, введи другой')

        elif new_question not in i:
            pts.update({new_question : new_answer})

    print(pts)




def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)
        speak_engine.say(voice)
        speak_engine.runAndWait()
        speak_engine.stop()

        # if voice.startswith(opts["alias"]):
        #     # обращаются к Кеше
        #     cmd = voice
        #
        #     for x in opts['alias']:
        #         cmd = cmd.replace(x, "").strip()
        #
        #     for x in opts['tbr']:
        #         cmd = cmd.replace(x, "").strip()
        #
        #     # распознаем и выполняем команду
        #     cmd = recognize_cmd(cmd)
        #     execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
        speak_engine.say('Голос не распознан')
        speak_engine.runAndWait()
        speak_engine.stop()
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


# def recognize_cmd(cmd):
#     RC = {'cmd': '', 'percent': 0}
#     for c, v in opts['cmds'].items():
#
#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > RC['percent']:
#                 RC['cmd'] = c
#                 RC['percent'] = vrt
#
#     return RC


# def execute_cmd(cmd):
#     if cmd == 'ctime':
#         # сказать текущее время
#         now = datetime.datetime.now()
#         speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
#
#     elif cmd == 'radio':
#         # воспроизвести радио
#         os.system("D:\\Jarvis\\res\\radio_record.m3u")
#
#     elif cmd == 'stupid1':
#         # рассказать анекдот
#         speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
#
#     else:
#         print('Команда не распознана, повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

# with m as source:
#     r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
# voices = speak_engine.getProperty('voices')
# speak_engine.setProperty('voice', voices[4].id)


speak("Добрый день, повелитель")
speak("Кеша слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop