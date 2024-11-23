import logging.config
import os

def file_search(path):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            if adress_file_in_check.endswith(".mp4"):
                yield adress_file_in_check  # возвращаем адрес файла




if __name__ == '__main__':
    logging.config.fileConfig(".\\.ini\\log.ini",disable_existing_loggers=False)
    for x in file_search("c:\\Users\\breat\\OneDrive\\Рабочий стол\\48\\NX CAM NEW\\"):
        print(x.split('\\')[-1])