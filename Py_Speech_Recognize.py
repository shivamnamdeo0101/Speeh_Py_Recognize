import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
 	print("Speak : ")
 	audio=r.listen(source)
 	try:
 		output= r.recognize_google(audio)
 		print("You Said :{}".format(output))
 	except:
 		print("Cant Recognize")
