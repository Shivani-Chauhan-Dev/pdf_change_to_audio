import PyPDF2
import pyttsx3

Path = input("please enter the pdf path: ")
Page_no =int(input("please enter the page number: "))
file = open(Path,"rb")

reader = PyPDF2.PdfReader(file) 


from_page = reader.pages[Page_no]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()