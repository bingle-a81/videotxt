from vosk import Model, KaldiRecognizer
import wave
import re


def transcribe_audio(input_audio_filepath,output_txt_file,model_path):    
    # Укажите путь к вашей модели    
    model = Model(model_path)
    # Откройте аудиофайл с помощью wave
    wf = wave.open(input_audio_filepath, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)  # Чтобы получать слова вместо простых результатов
    # Чтение данных и распознавание
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print("Процесс распознавания...")  # Логирование процесса

    # Получение итогового результата
    result = rec.FinalResult()
    slpit_file(output_txt_file, result)

def slpit_file(output_txt_file, result):
    a=re.split('}],', result, maxsplit=0, flags=0)[-1]
    pat=re.finditer(r'\b\w+?\b',a)
    st=''
    q=1
    for i in pat:
        if len(st)<3950:
            st=st+' '+i[0]
        else:
            with open(output_txt_file+'('+str(q)+').txt','w') as f:
                f.write(st)            
            q+=1
            st=i[0]
    else:
        if len(st)!=0:
            with open(output_txt_file+str(q)+'.txt','w') as f:
                f.write(st)
