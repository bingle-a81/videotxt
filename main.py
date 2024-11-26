import os
import src
import re

import logging.config
logging.config.fileConfig(".\\.ini\\log.ini",disable_existing_loggers=False)

def path_folder(path_file:str):
    ls=path_file.split('\\')[:-1]
    a='\\'.join(ls)
    if not os.path.exists(a):
        os.makedirs(a)


if __name__ == '__main__':
    a=".\\.tmp\\video\\"
    model_path = '.\\.tmp\\vosk-model-ru-0.42'
    # model_path='.\\.tmp\\vosk-model-en-us-0.42-gigaspeech'
    logger = logging.getLogger(__name__)
    logger.debug('start')
    for x in src.path_folder.file_search(a):
        audio_file_name=x.replace('video','audio').replace('mp4','wav')
        path_folder(audio_file_name)
        txt_file_name=x.replace('video','text').replace('.mp4','')
        path_folder(txt_file_name)
        src.mp4_to_wav.extract_audio_from_video_with_pydub(x,audio_file_name)
        src.audio_to_text.transcribe_audio(audio_file_name,txt_file_name,model_path)
        logger.debug(x)

    logger.debug('end')


