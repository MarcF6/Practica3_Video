# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import os
import moviepy.editor as mp
import subprocess

class Video:

    def __init__(self,archivo_input,archivo_output):
        self.archivo_input= archivo_input
        self.archivo_output= archivo_output



# Press the green button in the gutter to run the script.


if __name__ == '__main__':





    prueba = int(input("Introduce un numero de la opción que quieres ejecutar:\n"
                       "1-Obtener nuevo archivo con subtitulos y audio diferente\n"
                       "2 Saber el broadcasting que puede ser\n"
                       "3-Introducir codecs audio y video y saber el broadcasting que puede ser\n"))

    if (prueba != 3):
        archivo_input = input("Introduce el directorio del video \n")
        archivo_output = input("Introduce el directorio de donde quieres guardar el video y su nombre\n")
        video = Video(archivo_input, archivo_output)


    if(prueba==1):
        #archivo_input = input("Introduce el directorio del vídeo")
        #output=input("Introduce el directorio del resultado final + su nombre")
        directorio = input('Introduce SOLO el directorio donde quieras que se guarden los archivos')
        subtitulos = input('Introduce el directorio del archivo de los subtitulos')

        os.system("ffmpeg -i "+video.archivo_input+" -vn -acodec mp3 "+directorio+"/audio.mp3") #Extrae el audio
        os.system("ffmpeg -i "+video.archivo_input+" -c copy -an "+directorio+"/no_audio.mp4") #Quita el sonido
        os.system("ffmpeg -i "+directorio+"/audio.mp3 -ac 1 "+directorio+"/monoaudio.mp3")  #Passa el audio a mono
        os.system("ffmpeg -i "+directorio+"/monoaudio.mp3 -b:v 50K "+directorio+"/lowbit_audio.mp3") #Reduce el bitrate del audio
        os.system("ffmpeg -i "+directorio+"/no_audio.mp4 -i "+directorio+"/lowbit_audio.mp3  -vf subtitles="+subtitulos+" "+video.archivo_output+"")
        #Finalmente, introduce el nuevo audio dentro del video

    if(prueba==2):

        #archivo_input = input("Introduce el directorio del vídeo")
        codec_audio = subprocess.check_output('ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 '+video.archivo_input,shell=True)

        codec_video=subprocess.check_output('ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 '+video.archivo_input,shell=True)

        codec_video=str(codec_video[:len(codec_video)-1])
        codec_audio=str(codec_audio[:len(codec_audio)-1])
        print(codec_video)
        print(codec_audio)

        print("Como se puede ver, no consigo guardar unicamente el nombre del codec en la variable, en caso que se hiciera correctamente, unicamente")
        print("se tendria que usar los if's del siguiente ejercicio y se printaria por pantalla los broadcasters que pueden ser")


    if(prueba==3):

        #En este ejercicio le pedimos a el usuario que introduzca un codec de audio y uno de video y se mostrara por pantalla
        #las opciones de broadcasting que puede haber dependiendo del codec introducido.
        video_codec = input("Introduce el codec de video")
        audio_codec = input("Introduce el codec de audio")
        exito=0
        if video_codec in ["mpeg2","h.264"]:
            if audio_codec in ["acc","ac-3","mp3"]:
                print("el broadcasting puede ser DVB")
                exito=1
            if audio_codec in ["acc"]:
                print("el broadcasting puede ser ISDB")
                exito=1

            if audio_codec in ["ac-3"]:
                print("el broadcasting puede ser ATSC")
                exito = 1
        if video_codec in ["aus","aust","mpeg2","h.264"]:
            if audio_codec in ["dra","aac","ac-3","mp2","mp3"]:
                print("el broadcasting puede ser DTMB")
                exito = 1

        if exito==0:
            print("Error")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
