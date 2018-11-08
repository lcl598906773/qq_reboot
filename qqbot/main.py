# -*- coding: utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot, juheapi


@qqbotslot

def onQQMessage(bot, contact, member, content):
    nick = bot.conf.nick
    qq = bot.conf.qq
    str = '@' + nick
    num = getattr(member, 'uin', None)
    if num is None:
        if bot.isMe(contact, member):
            pass
        else:
            daan = juheapi.main(content)
            bot.SendTo(contact, daan)
    else:
        if str in content:
            if bot.isMe(contact, member):
                pass
            else:
                daan = juheapi.main(content)
                bot.SendTo(contact, daan)
if __name__ == '__main__':
    RunBot()