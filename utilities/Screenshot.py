


from selenium import webdriver
from docx import Document
import docx
from docx.shared import Inches

ss_fileName = []
class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "C:\\Users\\BLACKPEARL COMPUTERS\\PycharmProjects\\pythonProject\\PythonSelFramework\\tests\\screenshot\\"
        ss_fileName.append(directory+path)

        self.driver.get_screenshot_as_file(directory+path)


    def writeDoc(self,name):

        mydoc = docx.Document()

        for img in ss_fileName:
            print(img)
            mydoc.add_heading(name,0)
            mydoc.add_picture(img, width=Inches(7))
        mydoc.save("C:\\Users\\BLACKPEARL COMPUTERS\\PycharmProjects\\pythonProject\\PythonSelFramework\\tests\\screenshot\\"+name+".docx")
