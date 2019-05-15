# ToDo application
import sys, datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit

from design import Ui_MainWindow

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.record_num = 1

        self.openAction.triggered.connect(self.open_file)
        self.saveAction.triggered.connect(self.save_file)
        self.newAction.triggered.connect(self.new_file)


    def new_file(self):
        self.record_num = 1
        self.textEdit.clear()
        self.dateLine.clear()
        self.timeLine.clear()
        
    def open_file(self):
        key = "0"
        check_loc = "0"
        separ = "-" * 30
        directory = QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        
        with open(directory, "r", encoding = "utf-8") as file:
            for string in (line.rstrip() for line in file.readlines()):
                if string.startswith("Запись:") and key == "0":
                    key = "1"
                    self.textEdit.append(string)
                elif string.startswith("Мысль дня:") and key == "1":
                    key = "0"
                elif key == "1":
                    self.textEdit.append(string)
                elif string.startswith("Дата записи:"):
                    self.dateLine.clear()
                    self.dateLine.setText(string.split(": ")[1])
                elif string.startswith("Время записи:"):
                    self.timeLine.clear()
                    self.timeLine.setText(string.split(": ")[1])
                elif string.startswith("Местоположение:"):
                    self.locationText.clear()
                    self.locationText.append(string)
                    check_loc = "1"
                elif string.startswith("Планетарное расположение:"):
                    self.locationText.append(string)
                    check_loc = "0"
                elif check_loc == "1":
                    self.locationText.append(string)
                
                                          
    def save_file(self):
        directory = QFileDialog.getSaveFileName(self, "Выберите папку",".txt", "Текстовые файлы(*.txt);; Все(*.*)")[0]

        with open(directory, "a", encoding = "utf-8") as file:
            file.write("")

        with open(directory, "r", encoding = "utf-8") as new_file:
            for string in (line.rstrip() for line in new_file.readlines()):
                if string.startswith("Запись:"):
                    get_number = int(string.split(": ")[1])
                    self.record_num = get_number + 1
        
        record = "Запись: " + str(self.record_num)
        date = datetime.date.today()
        time = datetime.datetime.now()
        imper_date = "Дата записи:  9.00" + str(date.month) + "." + str(date)[1:4] + ".M3"
        planet_time = "Время записи:  " + str(time)[11:19]
        location = "Местоположение: Млечный путь, рукав Ориона, звездная система типа G2V, планета земного класса \nПланетарное наименование: Земля"
        planet_location = "Планетарное расположение: Евразийский материк, Республика Беларусь"
        slogan = "Мысль дня: Знание сила - скрой его"
        holy_words = "Император защищает"
        
        string = self.textEdit.toPlainText()
        
        with open(directory, "a", encoding = "utf-8") as file:
            file.write(imper_date + "\n")
            file.write(planet_time + "\n")
            file.write(location + "\n")
            file.write(planet_location + "\n\n")
            file.write(record + "\n")
            file.write("-" * 30 + "\n")
            file.write(string + "\n")
            file.write("-" * 30 + "\n" + slogan + "\n\n")
            file.write(holy_words + "\n\n\n")
            
            

def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        main, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )
    sys.__excepthook__(type, value, tback)

sys.excepthook = my_excepthook

def main():
    app = QApplication(sys.argv)
    main = Main_window()
    main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
