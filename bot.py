import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import wikipedia

wikipedia.set_lang('ru')

TOKEN = 'c8609dbab269881672ed0d2af7db0c1571afda27778617fb9f1572a2e2b88007f5bbbcbdcde2bc66c9e4d'


def main():
    flag = True
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, '194027853')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            text = event.obj.message['text'].lower()
            if flag:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="О чем вы хотите узнать?",
                                 random_id=random.randint(0, 2 ** 64))
                flag = False
            else:
                try:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=wikipedia.summary(text),
                                     random_id=random.randint(0, 2 ** 64))
                except:
                    print('Сформулируйте свой запрос по другому, назовите вещь о коророй хотите узнать')


if __name__ == '__main__':
    main()
