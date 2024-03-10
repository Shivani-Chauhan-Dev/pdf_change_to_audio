import PyPDF2
import pyttsx3


path = open("C:/Users/91801/Desktop/file.pdf.pdf","rb")

reader = PyPDF2.PdfReader(path) 


from_page = reader.pages[6]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()