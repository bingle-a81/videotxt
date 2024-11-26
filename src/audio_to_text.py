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
    a=re.split('}],', result, maxsplit=0, flags=0)[-1]
    with open(output_txt_file, "w") as text_file:
        text_file.write(a)

