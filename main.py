import PyPDF2
import pyttsx3

User = input("please enter the pdf path: ")
Page_no =int(input("please enter the page number: "))
path = open(User,"rb")

reader = PyPDF2.PdfReader(path) 


from_page = reader.pages[Page_no]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()