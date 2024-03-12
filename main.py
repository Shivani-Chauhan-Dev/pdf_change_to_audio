import PyPDF2
import pyttsx3

user = input("please enter the pdf path: ")
path = open(user,"rb")

reader = PyPDF2.PdfReader(path) 


from_page = reader.pages[1]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()