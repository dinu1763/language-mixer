import moviepy.editor as mp
import speech_recognition as sr
import googletrans
from googletrans import Translator
from gtts import gTTS
import codecs



clip = mp.VideoFileClip("videoplayback.mp4")
clip.audio.write_audiofile("theaudio.wav")


r = sr.Recognizer()


with sr.AudioFile('theaudio.wav') as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('Working on...')
        print(text)
    except:
        print('Sorry.. run again...')
		
		
		
		
with open('audio_to_text.txt', 'a') as the_file:
	the_file.write(text)
   
   
   
translator = Translator()
result = translator.translate(text, src='hi', dest='ta')


with codecs.open('converted_text.txt', 'a', encoding='utf-8') as convert_file:
	convert_file.write(result.text)
	
	
language = 'ta'

output = gTTS(text=result.text, lang=language, slow=False)

output.save("output.mp3")