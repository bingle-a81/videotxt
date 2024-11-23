
import src

import logging.config
logging.config.fileConfig(".\\.ini\\log.ini",disable_existing_loggers=False)






if __name__ == '__main__':
    a="c:\\Users\\breat\\OneDrive\\Рабочий стол\\48\\NX CAM NEW\\"
    logger = logging.getLogger(__name__)
    logger.debug('start')
    for x in src.path_folder.file_search(a):
        print(x.split('\\')[-1])



    # for i in logging.root.manager.loggerDict:
    #     print(i)

