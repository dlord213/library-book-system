from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from main_ui import Ui_libraryApp
import json
import sys

dataPath = './datas/books.json'

class mainApp(QMainWindow, Ui_libraryApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initUI()

    def initUI(self):
        self.libStackedWidget.setCurrentIndex(0)
        self.viewBooksRightFrame.hide()
        self.removeBookRightFrame.hide()

        with open(dataPath, 'r') as file:
            data = json.load(file)
            self.home_TotalBooksLbl.setText(
                f"Total number of books - {len(data)}")
            if len(data) > 0:
                self.home_StatusLbl.setText("Library is online!")
            else:
                self.home_StatusLbl.setText("Library is offline")

        self.initIcons()
        self.initBtnsFunctions()

        self.initBookList()

    def initIcons(self):
        # HOME PAGE
        self.home_ViewBooksBtn.setIcon(QPixmap("./icons/book-solid.svg"))
        self.home_AddBooksBtn.setIcon(QPixmap("./icons/plus-solid.svg"))
        self.home_RemoveBooksBtn.setIcon(QPixmap("./icons/minus-solid.svg"))

        # VIEW BOOKS PAGE
        self.viewBooks_HomeBtn.setIcon(QPixmap("./icons/arrow-left-solid.svg"))

        # ADD BOOKS PAGE
        self.addBook_HomeBtn.setIcon(QPixmap("./icons/arrow-left-solid.svg"))

        # REMOVE BOOKS PAGE
        self.removeBook_HomeBtn.setIcon(
            QPixmap("./icons/arrow-left-solid.svg"))

    def initBtnsFunctions(self):
        self.landing_Btn.clicked.connect(
            lambda: self.libStackedWidget.setCurrentIndex(1))

        # HOME PAGE
        with open(dataPath, 'r') as file:
            data = json.load(file)
            self.home_TotalBooksLbl.setText(
                f"Total number of books - {len(data)}")
            if len(data) > 0:
                self.home_ViewBooksBtn.clicked.connect(
                    lambda: self.libStackedWidget.setCurrentIndex(2))
            else:
                messageBox = QMessageBox(self)
                messageBox.setWindowTitle("Library is offline!")
                messageBox.setText(
                    "You can't browse the book list, library is offline.")
                messageBox.exec()

        self.home_RemoveBooksBtn.clicked.connect(
            lambda: self.libStackedWidget.setCurrentIndex(4))
        self.home_AddBooksBtn.clicked.connect(
            lambda: self.libStackedWidget.setCurrentIndex(3))

        # VIEW BOOKS PAGE
        self.viewBooks_BorrowBtn.clicked.connect(
            lambda: self.borrowBook()
        )
        self.viewBooks_ReturnBtn.clicked.connect(
            lambda: self.returnBook()
        )
        self.viewBooks_HomeBtn.clicked.connect(
            lambda: self.libStackedWidget.setCurrentIndex(1)
        )

        # ADD BOOKS PAGE
        self.addBook_HomeBtn.clicked.connect(
            lambda: self.libStackedWidget.setCurrentIndex(1)
        )
        self.addBook_SubmitBtn.clicked.connect(
            lambda: self.addBook()
        )

        # REMOVE BOOKS PAGE
        self.removeBook_HomeBtn.clicked.connect(
            lambda: self.libStackedWidget.setCurrentIndex(1)
        )
        self.removeBook_RemoveBtn.clicked.connect(
            lambda: self.removeBook()
        )

    def initBookList(self):
        viewBookListWidget = self.viewBooksListWidget
        removeBookListWidget = self.removeBookListWidget

        with open(dataPath, 'r') as file:
            data = json.load(file)

            tempList = []
            for book in data:
                for elem, val in book.items():
                    if elem == 'title':
                        tempList.append(val)

            viewBookListWidget.addItems(tempList)
            removeBookListWidget.addItems(tempList)

            for row in range(0, len(tempList)):
                viewBookListWidget.item(row).setFont(
                    QFont("Montserrat Medium", 12))
                removeBookListWidget.item(row).setFont(
                    QFont("Montserrat Medium", 12))

            viewBookListWidget.itemClicked.connect(lambda: self.getBookInfo(1))
            removeBookListWidget.itemClicked.connect(
                lambda: self.getBookInfo(2))

    def getBookInfo(self, widget_type: int):
        # VIEW BOOK WIDGET -> 1
        # REMOVE BOOK WIDGET -> 2

        viewBookListWidget = self.viewBooksListWidget
        removeBookListWidget = self.removeBookListWidget

        with open(dataPath, 'r') as file:
            data = json.load(file)
            if widget_type == 1:
                bookIndex = data[viewBookListWidget.currentRow()]
                
                for elem, val in bookIndex.items():
                    if elem == 'author':
                        self.viewBooks_AuthorLbl.setText(str(val))
                    elif elem == 'title':
                        self.viewBooks_TitleLbl.setText(str(val))
                    elif elem == 'isbn':
                        self.viewBooks_ISBNLbl.setText(str(val))
                    elif elem == 'status':
                        if val == 0:
                            self.viewBooks_BorrowBtn.setVisible(True)
                            self.viewBooks_ReturnBtn.setVisible(False)
                            self.viewBooks_StatusLbl.setText(
                                "Available for borrow")
                        else:
                            self.viewBooks_BorrowBtn.setVisible(False)
                            self.viewBooks_ReturnBtn.setVisible(True)
                            self.viewBooks_StatusLbl.setText(
                                "Unavailable for borrow")
                    elif elem == 'genre':
                        self.viewBooks_GenreLbl.setText(str(val))
                    elif elem == 'desc':
                        self.viewBooks_DescLbl.setText(val)
                self.viewBooksRightFrame.setVisible(True)
            else:
                bookIndex = data[removeBookListWidget.currentRow()]

                for elem, val in bookIndex.items():
                    if elem == 'author':
                        self.removeBook_AuthorLbl.setText(str(val))
                    elif elem == 'title':
                        self.removeBook_TitleLbl.setText(str(val))
                    elif elem == 'isbn':
                        self.removeBook_ISBNLbl.setText(str(val))
                    elif elem == 'genre':
                        self.removeBook_GenreLbl.setText(str(val))
                self.removeBookRightFrame.setVisible(True)

    def borrowBook(self):
        listWidget = self.viewBooksListWidget
        temp = []

        with open(dataPath, 'r') as file:
            temp = json.load(file)

            temp[listWidget.currentRow()]['status'] = 1

        with open(dataPath, 'w') as file:
            json.dump(temp, file, indent=4, separators=(',', ': ')
                      )

        self.getBookInfo(1)

    def returnBook(self):
        listWidget = self.viewBooksListWidget
        temp = []

        with open(dataPath, 'r') as file:
            temp = json.load(file)

            temp[listWidget.currentRow()]['status'] = 0

        with open(dataPath, 'w') as file:
            json.dump(temp, file, indent=4, separators=(',', ': ')
                      )

        self.getBookInfo(1)

    def addBook(self):
        messageBox = QMessageBox(self)
        if self.addBook_AuthorLineEdit.text() == '':
            messageBox.setWindowTitle("Author is empty!")
            messageBox.setText("Please enter the author's name.")
            messageBox.exec()
        else:
            author = self.addBook_AuthorLineEdit.text()

        if self.addBook_TitleLineEdit.text() == '':
            messageBox.setWindowTitle("Title is empty!")
            messageBox.setText("Please enter the title of the book.")
            messageBox.exec()
        else:
            title = self.addBook_TitleLineEdit.text()

        if self.addBook_ISBNThreeLineEdit.text() == '':
            if self.addBook_ISBNTenLineEdit.text() == '':
                messageBox.setWindowTitle("The ten line digit ISBN is empty!")
                messageBox.setText("Please enter the ten digit ISBN.")
                messageBox.exec()
            else:
                messageBox.setWindowTitle("ISBN is empty")
                messageBox.setText("Please enter the ISBN.")
                messageBox.exec()
        else:
            isbn = f"{self.addBook_ISBNThreeLineEdit.text()}-{self.addBook_ISBNTenLineEdit.text()}"

        if self.addBook_GenreLineEdit.text() == '':
            messageBox.setWindowTitle("Genre is empty!")
            messageBox.setText("Please enter the genre of the book.")
            messageBox.exec()
        else:
            genre = self.addBook_GenreLineEdit.text()

        if self.addBook_DescTextEdit.toPlainText() == '':
            messageBox.setWindowTitle("Description is empty!")
            messageBox.setText(
                "Please enter the description/synopsis of the book.")
            messageBox.exec()
        else:
            desc = self.addBook_DescTextEdit.toPlainText()

        temp = []
        with open(dataPath, 'r') as file:
            temp = json.load(file)

            temp.append(
                {
                    "author": author,
                    "title": title,
                    "isbn": isbn,
                    "status": 0,
                    "genre": genre,
                    "desc": desc
                }
            )

        with open(dataPath, 'w') as file:
            json.dump(temp, file, indent=4, separators=(',', ': ')
                      )

        self.libStackedWidget.setCurrentIndex(1)
        self.viewBooksListWidget.clear()
        self.removeBookListWidget.clear()
        self.initBookList()

    def removeBook(self):
        listWidget = self.removeBookListWidget
        temp = []

        with open(dataPath, 'r') as file:
            temp = json.load(file)

            temp.pop(listWidget.currentRow())
            listWidget.takeItem(listWidget.currentRow())

            self.viewBooksListWidget.takeItem(listWidget.currentRow())

        with open(dataPath, 'w') as file:
            json.dump(temp, file, indent=4, separators=(',', ': ')
                      )
        
        self.getBookInfo(2)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainApp()
    win.show()

    app.exec()
