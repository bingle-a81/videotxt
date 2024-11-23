#telebot

import logging
import smtplib
import telebot
import logging.config

class Telegram_bot_handler(logging.Handler):
    def __init__(self, token: str, chat_id: str):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        bot = telebot.TeleBot(self.token)
        try:
            bot.send_message(self.chat_id, message)
        except:
            pass


class My_email_handler(logging.Handler):
    def __init__(self, server:str, port: int, email: str, passwd: str):
        super().__init__()
        self.server = server
        self.port = port
        self.email = email
        self.passwd = passwd

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        charset = f"Content-Type: text/plain; charset=utf-8"
        mime = "MIME-Version: 1.0"
        body = "\r\n".join(
            (
                f"From: {self.email}",
                f"To: {self.email}",
                f"Subject: File log debug.log ",
                mime,
                charset,
                "",
                message,
            )
        )
        # формируем тело письма
        try:
            # подключаемся к почтовому сервису
            smtp = smtplib.SMTP(self.server, self.port)
            smtp.starttls()
            smtp.ehlo()
            # логинимся на почтовом сервере
            smtp.login(self.email, self.passwd)
            # пробуем послать письмо
            smtp.sendmail(self.email, self.email, body.encode("utf-8"))
        except smtplib.SMTPException as err:
            print("Что - то пошло не так...")
            raise err
        finally:
            smtp.quit()

