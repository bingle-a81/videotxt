import os
import src

import logging.config
logging.config.fileConfig(".\\.ini\\log.ini",disable_existing_loggers=False)

def path_folder(path_file:str):
    ls=path_file.split('\\')[:-1]
    a='\\'.join(ls)
    if not os.path.exists(a):
        os.makedirs(a)


if __name__ == '__main__':
    a=".\\.tmp\\video\\"
    logger = logging.getLogger(__name__)
    logger.debug('start')
    for x in src.path_folder.file_search(a):
        # print(x)
        # x1=x.replace('video','audio')
        # print(x1)
        # a1=x.split('\\')[-1].split('.')[-2]
        audio_file_name=x.replace('video','audio').replace('mp4','wav')
        path_folder(audio_file_name)
        txt_file_name=x.replace('video','text').replace('mp4','txt')
        path_folder(txt_file_name)
        # audio_file_name=os.path.join(".\\.tmp\\audio\\",x.split('\\')[-2], a1+'.wav')
        # print(audio_file_name)
        # src.mp4_to_wav.extract_audio_from_video_with_pydub(x,audio_file_name)
        # text=src.audio_to_text.transcribe_audio(audio_file_name)
        # with open(txt_file_name,'w') as f:
        #     f.write(text)
        logger.debug(x)

    logger.debug('end')






    # for i in logging.root.manager.loggerDict:
    #     print(i)

