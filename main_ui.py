# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_libraryApp(object):
    def setupUi(self, libraryApp):
        if not libraryApp.objectName():
            libraryApp.setObjectName(u"libraryApp")
        libraryApp.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(libraryApp.sizePolicy().hasHeightForWidth())
        libraryApp.setSizePolicy(sizePolicy)
        libraryApp.setMaximumSize(QSize(1280, 720))
        self.mainWidget = QWidget(libraryApp)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.libStackedWidget = QStackedWidget(self.mainWidget)
        self.libStackedWidget.setObjectName(u"libStackedWidget")
        self.libStackedWidget.setStyleSheet(u"QLabel {\n"
"	color: #1a0f0f;\n"
"}\n"
"QFrame, QWidget {\n"
"	background-color: #f2e9e8;\n"
"	color: #1a0f0f;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #864e4b;\n"
"	border: none;\n"
"	color: #f2e9e8;\n"
"	padding: 4px 4px 4px 4px;\n"
"	border-radius: 6px;\n"
"}\n"
"QListView {\n"
"	background-color: #e7d5d5;\n"
"}\n"
"QAbstractItemView {\n"
"	padding: 6px 6px 6px 6px;\n"
"}\n"
"QListView::item:selected {\n"
"	background-color: #764542;\n"
"	color: #f2e9e8;\n"
"}\n"
"QLineEdit, QPlainTextEdit {\n"
"	background-color: #f2e9e8;\n"
"	border: 2px solid #864e4b;\n"
"	padding: 4px 4px 4px 4px;\n"
"}")
        self.landingPage = QWidget()
        self.landingPage.setObjectName(u"landingPage")
        self.horizontalLayout = QHBoxLayout(self.landingPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.landingMainFrame = QFrame(self.landingPage)
        self.landingMainFrame.setObjectName(u"landingMainFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.landingMainFrame.sizePolicy().hasHeightForWidth())
        self.landingMainFrame.setSizePolicy(sizePolicy1)
        self.landingMainFrame.setFrameShape(QFrame.NoFrame)
        self.landingMainFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.landingMainFrame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.landing_HeadingLbl = QLabel(self.landingMainFrame)
        self.landing_HeadingLbl.setObjectName(u"landing_HeadingLbl")
        sizePolicy.setHeightForWidth(self.landing_HeadingLbl.sizePolicy().hasHeightForWidth())
        self.landing_HeadingLbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Montserrat Black"])
        font.setPointSize(48)
        font.setBold(True)
        self.landing_HeadingLbl.setFont(font)
        self.landing_HeadingLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.landing_HeadingLbl)

        self.landing_DescLbl = QLabel(self.landingMainFrame)
        self.landing_DescLbl.setObjectName(u"landing_DescLbl")
        sizePolicy.setHeightForWidth(self.landing_DescLbl.sizePolicy().hasHeightForWidth())
        self.landing_DescLbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(16)
        self.landing_DescLbl.setFont(font1)
        self.landing_DescLbl.setAlignment(Qt.AlignCenter)
        self.landing_DescLbl.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.landing_DescLbl)

        self.landing_Btn = QPushButton(self.landingMainFrame)
        self.landing_Btn.setObjectName(u"landing_Btn")
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.landing_Btn.setFont(font2)
        self.landing_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.landing_Btn.setFlat(False)

        self.verticalLayout_2.addWidget(self.landing_Btn)


        self.horizontalLayout.addWidget(self.landingMainFrame)

        self.libStackedWidget.addWidget(self.landingPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"QLabel {\n"
"	color: #864e4b;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.homePage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.homeHeaderFrame = QFrame(self.homePage)
        self.homeHeaderFrame.setObjectName(u"homeHeaderFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.homeHeaderFrame.sizePolicy().hasHeightForWidth())
        self.homeHeaderFrame.setSizePolicy(sizePolicy2)
        self.homeHeaderFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #864e4b;\n"
"	color: #f2e9e8;\n"
"	border-radius: 6px;\n"
"}")
        self.homeHeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.homeHeaderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.homeHeaderFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home_TotalBooksLbl = QLabel(self.homeHeaderFrame)
        self.home_TotalBooksLbl.setObjectName(u"home_TotalBooksLbl")
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(16)
        self.home_TotalBooksLbl.setFont(font3)

        self.verticalLayout_4.addWidget(self.home_TotalBooksLbl)

        self.home_StatusLbl = QLabel(self.homeHeaderFrame)
        self.home_StatusLbl.setObjectName(u"home_StatusLbl")
        self.home_StatusLbl.setFont(font3)

        self.verticalLayout_4.addWidget(self.home_StatusLbl)


        self.verticalLayout_3.addWidget(self.homeHeaderFrame)

        self.homeMainFrame = QFrame(self.homePage)
        self.homeMainFrame.setObjectName(u"homeMainFrame")
        self.homeMainFrame.setFrameShape(QFrame.StyledPanel)
        self.homeMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.homeMainFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeHeadingLbl = QLabel(self.homeMainFrame)
        self.homeHeadingLbl.setObjectName(u"homeHeadingLbl")
        sizePolicy2.setHeightForWidth(self.homeHeadingLbl.sizePolicy().hasHeightForWidth())
        self.homeHeadingLbl.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamilies([u"Montserrat Black"])
        font4.setPointSize(28)
        font4.setBold(True)
        self.homeHeadingLbl.setFont(font4)

        self.verticalLayout_5.addWidget(self.homeHeadingLbl)

        self.homeBtnsFrame = QFrame(self.homeMainFrame)
        self.homeBtnsFrame.setObjectName(u"homeBtnsFrame")
        font5 = QFont()
        font5.setFamilies([u"Montserrat Black"])
        font5.setPointSize(32)
        self.homeBtnsFrame.setFont(font5)
        self.homeBtnsFrame.setStyleSheet(u"QPushButton {\n"
"	background-color: #e7d5d5;\n"
"	color: #864e4b;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #864e4b;\n"
"	color: #f2e9e8;\n"
"}")
        self.homeBtnsFrame.setFrameShape(QFrame.NoFrame)
        self.homeBtnsFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.homeBtnsFrame)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.home_ViewBooksBtn = QPushButton(self.homeBtnsFrame)
        self.home_ViewBooksBtn.setObjectName(u"home_ViewBooksBtn")
        sizePolicy.setHeightForWidth(self.home_ViewBooksBtn.sizePolicy().hasHeightForWidth())
        self.home_ViewBooksBtn.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Montserrat SemiBold"])
        font6.setPointSize(32)
        self.home_ViewBooksBtn.setFont(font6)
        self.home_ViewBooksBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_ViewBooksBtn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.home_ViewBooksBtn, 1, 0, 1, 3)

        self.home_RemoveBooksBtn = QPushButton(self.homeBtnsFrame)
        self.home_RemoveBooksBtn.setObjectName(u"home_RemoveBooksBtn")
        sizePolicy.setHeightForWidth(self.home_RemoveBooksBtn.sizePolicy().hasHeightForWidth())
        self.home_RemoveBooksBtn.setSizePolicy(sizePolicy)
        self.home_RemoveBooksBtn.setFont(font6)
        self.home_RemoveBooksBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_RemoveBooksBtn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.home_RemoveBooksBtn, 0, 2, 1, 1)

        self.home_AddBooksBtn = QPushButton(self.homeBtnsFrame)
        self.home_AddBooksBtn.setObjectName(u"home_AddBooksBtn")
        sizePolicy.setHeightForWidth(self.home_AddBooksBtn.sizePolicy().hasHeightForWidth())
        self.home_AddBooksBtn.setSizePolicy(sizePolicy)
        self.home_AddBooksBtn.setFont(font6)
        self.home_AddBooksBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_AddBooksBtn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.home_AddBooksBtn, 0, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.homeBtnsFrame)


        self.verticalLayout_3.addWidget(self.homeMainFrame)

        self.libStackedWidget.addWidget(self.homePage)
        self.viewBooksPage = QWidget()
        self.viewBooksPage.setObjectName(u"viewBooksPage")
        self.verticalLayout_6 = QVBoxLayout(self.viewBooksPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.viewBooksHeaderFrame = QFrame(self.viewBooksPage)
        self.viewBooksHeaderFrame.setObjectName(u"viewBooksHeaderFrame")
        sizePolicy2.setHeightForWidth(self.viewBooksHeaderFrame.sizePolicy().hasHeightForWidth())
        self.viewBooksHeaderFrame.setSizePolicy(sizePolicy2)
        self.viewBooksHeaderFrame.setStyleSheet(u"QPushButton {\n"
"	background-color: #e7d5d5;\n"
"	color: #864e4b;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #864e4b;\n"
"	color: #f2e9e8;\n"
"}")
        self.viewBooksHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.viewBooksHeaderFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.viewBooksHeaderFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.viewBooks_HomeBtn = QPushButton(self.viewBooksHeaderFrame)
        self.viewBooks_HomeBtn.setObjectName(u"viewBooks_HomeBtn")
        sizePolicy1.setHeightForWidth(self.viewBooks_HomeBtn.sizePolicy().hasHeightForWidth())
        self.viewBooks_HomeBtn.setSizePolicy(sizePolicy1)
        self.viewBooks_HomeBtn.setMaximumSize(QSize(64, 64))
        self.viewBooks_HomeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewBooks_HomeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.viewBooks_HomeBtn)

        self.viewBooks_HeaderLbl = QLabel(self.viewBooksHeaderFrame)
        self.viewBooks_HeaderLbl.setObjectName(u"viewBooks_HeaderLbl")
        sizePolicy2.setHeightForWidth(self.viewBooks_HeaderLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_HeaderLbl.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"Montserrat Black"])
        font7.setPointSize(28)
        self.viewBooks_HeaderLbl.setFont(font7)
        self.viewBooks_HeaderLbl.setStyleSheet(u"QLabel {\n"
"	background-color: #864e4b;\n"
"	color: #f2e9e8;\n"
"	border-radius: 6px;\n"
"	padding: 4px 4px 4px 4px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.viewBooks_HeaderLbl)


        self.verticalLayout_6.addWidget(self.viewBooksHeaderFrame)

        self.viewBooksMainFrame = QFrame(self.viewBooksPage)
        self.viewBooksMainFrame.setObjectName(u"viewBooksMainFrame")
        self.viewBooksMainFrame.setFrameShape(QFrame.NoFrame)
        self.viewBooksMainFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.viewBooksMainFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.viewBooksListWidget = QListWidget(self.viewBooksMainFrame)
        self.viewBooksListWidget.setObjectName(u"viewBooksListWidget")
        sizePolicy.setHeightForWidth(self.viewBooksListWidget.sizePolicy().hasHeightForWidth())
        self.viewBooksListWidget.setSizePolicy(sizePolicy)
        self.viewBooksListWidget.setFrameShape(QFrame.NoFrame)
        self.viewBooksListWidget.setFrameShadow(QFrame.Plain)
        self.viewBooksListWidget.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.viewBooksListWidget)

        self.viewBooksRightFrame = QFrame(self.viewBooksMainFrame)
        self.viewBooksRightFrame.setObjectName(u"viewBooksRightFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.viewBooksRightFrame.sizePolicy().hasHeightForWidth())
        self.viewBooksRightFrame.setSizePolicy(sizePolicy3)
        self.viewBooksRightFrame.setFrameShape(QFrame.NoFrame)
        self.viewBooksRightFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.viewBooksRightFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.viewBooksDetailsFrame = QFrame(self.viewBooksRightFrame)
        self.viewBooksDetailsFrame.setObjectName(u"viewBooksDetailsFrame")
        sizePolicy.setHeightForWidth(self.viewBooksDetailsFrame.sizePolicy().hasHeightForWidth())
        self.viewBooksDetailsFrame.setSizePolicy(sizePolicy)
        self.viewBooksDetailsFrame.setFrameShape(QFrame.NoFrame)
        self.viewBooksDetailsFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.viewBooksDetailsFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.viewBooks_TitleLbl = QLabel(self.viewBooksDetailsFrame)
        self.viewBooks_TitleLbl.setObjectName(u"viewBooks_TitleLbl")
        sizePolicy2.setHeightForWidth(self.viewBooks_TitleLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_TitleLbl.setSizePolicy(sizePolicy2)
        font8 = QFont()
        font8.setFamilies([u"Montserrat Black"])
        font8.setPointSize(18)
        self.viewBooks_TitleLbl.setFont(font8)
        self.viewBooks_TitleLbl.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.viewBooks_TitleLbl)

        self.viewBooks_ISBNLbl = QLabel(self.viewBooksDetailsFrame)
        self.viewBooks_ISBNLbl.setObjectName(u"viewBooks_ISBNLbl")
        sizePolicy2.setHeightForWidth(self.viewBooks_ISBNLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_ISBNLbl.setSizePolicy(sizePolicy2)
        font9 = QFont()
        font9.setFamilies([u"Montserrat Medium"])
        font9.setPointSize(14)
        self.viewBooks_ISBNLbl.setFont(font9)
        self.viewBooks_ISBNLbl.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.viewBooks_ISBNLbl)

        self.viewBooks_AuthorLbl = QLabel(self.viewBooksDetailsFrame)
        self.viewBooks_AuthorLbl.setObjectName(u"viewBooks_AuthorLbl")
        sizePolicy2.setHeightForWidth(self.viewBooks_AuthorLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_AuthorLbl.setSizePolicy(sizePolicy2)
        font10 = QFont()
        font10.setFamilies([u"Montserrat Medium"])
        font10.setPointSize(12)
        self.viewBooks_AuthorLbl.setFont(font10)
        self.viewBooks_AuthorLbl.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.viewBooks_AuthorLbl)

        self.viewBooks_StatusLbl = QLabel(self.viewBooksDetailsFrame)
        self.viewBooks_StatusLbl.setObjectName(u"viewBooks_StatusLbl")
        sizePolicy2.setHeightForWidth(self.viewBooks_StatusLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_StatusLbl.setSizePolicy(sizePolicy2)
        self.viewBooks_StatusLbl.setFont(font10)
        self.viewBooks_StatusLbl.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.viewBooks_StatusLbl)

        self.viewBooks_GenreLbl = QLabel(self.viewBooksDetailsFrame)
        self.viewBooks_GenreLbl.setObjectName(u"viewBooks_GenreLbl")
        sizePolicy2.setHeightForWidth(self.viewBooks_GenreLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_GenreLbl.setSizePolicy(sizePolicy2)
        self.viewBooks_GenreLbl.setFont(font10)
        self.viewBooks_GenreLbl.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.viewBooks_GenreLbl)


        self.verticalLayout_8.addWidget(self.viewBooksDetailsFrame)

        self.viewBooksDescFrame = QFrame(self.viewBooksRightFrame)
        self.viewBooksDescFrame.setObjectName(u"viewBooksDescFrame")
        self.viewBooksDescFrame.setFrameShape(QFrame.StyledPanel)
        self.viewBooksDescFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.viewBooksDescFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.viewBooks_DescHeadingLbl = QLabel(self.viewBooksDescFrame)
        self.viewBooks_DescHeadingLbl.setObjectName(u"viewBooks_DescHeadingLbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.viewBooks_DescHeadingLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_DescHeadingLbl.setSizePolicy(sizePolicy4)
        font11 = QFont()
        font11.setFamilies([u"Montserrat Black"])
        font11.setPointSize(12)
        self.viewBooks_DescHeadingLbl.setFont(font11)

        self.verticalLayout_9.addWidget(self.viewBooks_DescHeadingLbl)

        self.viewBooks_DescLbl = QLabel(self.viewBooksDescFrame)
        self.viewBooks_DescLbl.setObjectName(u"viewBooks_DescLbl")
        sizePolicy.setHeightForWidth(self.viewBooks_DescLbl.sizePolicy().hasHeightForWidth())
        self.viewBooks_DescLbl.setSizePolicy(sizePolicy)
        self.viewBooks_DescLbl.setMaximumSize(QSize(350, 16777215))
        font12 = QFont()
        font12.setFamilies([u"Montserrat Medium"])
        font12.setPointSize(10)
        font12.setKerning(True)
        self.viewBooks_DescLbl.setFont(font12)
        self.viewBooks_DescLbl.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.viewBooks_DescLbl)


        self.verticalLayout_8.addWidget(self.viewBooksDescFrame)

        self.viewBooksStatusBtnsFrame = QFrame(self.viewBooksRightFrame)
        self.viewBooksStatusBtnsFrame.setObjectName(u"viewBooksStatusBtnsFrame")
        sizePolicy2.setHeightForWidth(self.viewBooksStatusBtnsFrame.sizePolicy().hasHeightForWidth())
        self.viewBooksStatusBtnsFrame.setSizePolicy(sizePolicy2)
        self.viewBooksStatusBtnsFrame.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #e7d5d5;\n"
"	color: #864e4b;\n"
"}")
        self.viewBooksStatusBtnsFrame.setFrameShape(QFrame.NoFrame)
        self.viewBooksStatusBtnsFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.viewBooksStatusBtnsFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.viewBooks_ReturnBtn = QPushButton(self.viewBooksStatusBtnsFrame)
        self.viewBooks_ReturnBtn.setObjectName(u"viewBooks_ReturnBtn")
        self.viewBooks_ReturnBtn.setFont(font10)
        self.viewBooks_ReturnBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.viewBooks_ReturnBtn)

        self.viewBooks_BorrowBtn = QPushButton(self.viewBooksStatusBtnsFrame)
        self.viewBooks_BorrowBtn.setObjectName(u"viewBooks_BorrowBtn")
        self.viewBooks_BorrowBtn.setFont(font10)
        self.viewBooks_BorrowBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.viewBooks_BorrowBtn)


        self.verticalLayout_8.addWidget(self.viewBooksStatusBtnsFrame)


        self.horizontalLayout_2.addWidget(self.viewBooksRightFrame)


        self.verticalLayout_6.addWidget(self.viewBooksMainFrame)

        self.libStackedWidget.addWidget(self.viewBooksPage)
        self.addBookPage = QWidget()
        self.addBookPage.setObjectName(u"addBookPage")
        self.addBookPage.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #e7d5d5;\n"
"	color: #864e4b;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.addBookPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.addBookHeaderFrame = QFrame(self.addBookPage)
        self.addBookHeaderFrame.setObjectName(u"addBookHeaderFrame")
        sizePolicy2.setHeightForWidth(self.addBookHeaderFrame.sizePolicy().hasHeightForWidth())
        self.addBookHeaderFrame.setSizePolicy(sizePolicy2)
        self.addBookHeaderFrame.setStyleSheet(u"QPushButton {\n"
"	background-color: #e7d5d5;\n"
"	color: #864e4b;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #864e4b;\n"
"	color: #f2e9e8;\n"
"}")
        self.addBookHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.addBookHeaderFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.addBookHeaderFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addBook_HomeBtn = QPushButton(self.addBookHeaderFrame)
        self.addBook_HomeBtn.setObjectName(u"addBook_HomeBtn")
        sizePolicy1.setHeightForWidth(self.addBook_HomeBtn.sizePolicy().hasHeightForWidth())
        self.addBook_HomeBtn.setSizePolicy(sizePolicy1)
        self.addBook_HomeBtn.setMaximumSize(QSize(64, 64))
        self.addBook_HomeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addBook_HomeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.addBook_HomeBtn)

        self.addBook_HeaderLbl = QLabel(self.addBookHeaderFrame)
        self.addBook_HeaderLbl.setObjectName(u"addBook_HeaderLbl")
        sizePolicy2.setHeightForWidth(self.addBook_HeaderLbl.sizePolicy().hasHeightForWidth())
        self.addBook_HeaderLbl.setSizePolicy(sizePolicy2)
        self.addBook_HeaderLbl.setFont(font7)
        self.addBook_HeaderLbl.setStyleSheet(u"QLabel {\n"
"	background-color: #864e4b;\n"
"	color: #f2e9e8;\n"
"	border-radius: 6px;\n"
"	padding: 4px 4px 4px 4px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.addBook_HeaderLbl)


        self.verticalLayout_10.addWidget(self.addBookHeaderFrame)

        self.addBookMainFrame = QFrame(self.addBookPage)
        self.addBookMainFrame.setObjectName(u"addBookMainFrame")
        self.addBookMainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #e7d5d5;\n"
"}")
        self.addBookMainFrame.setFrameShape(QFrame.NoFrame)
        self.addBookMainFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.addBookMainFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.addBookTitleFrame = QFrame(self.addBookMainFrame)
        self.addBookTitleFrame.setObjectName(u"addBookTitleFrame")
        sizePolicy2.setHeightForWidth(self.addBookTitleFrame.sizePolicy().hasHeightForWidth())
        self.addBookTitleFrame.setSizePolicy(sizePolicy2)
        self.addBookTitleFrame.setFrameShape(QFrame.NoFrame)
        self.addBookTitleFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.addBookTitleFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addBook_TitleLbl = QLabel(self.addBookTitleFrame)
        self.addBook_TitleLbl.setObjectName(u"addBook_TitleLbl")
        font13 = QFont()
        font13.setFamilies([u"Montserrat Black"])
        font13.setPointSize(16)
        self.addBook_TitleLbl.setFont(font13)

        self.horizontalLayout_7.addWidget(self.addBook_TitleLbl)

        self.addBook_TitleLineEdit = QLineEdit(self.addBookTitleFrame)
        self.addBook_TitleLineEdit.setObjectName(u"addBook_TitleLineEdit")
        self.addBook_TitleLineEdit.setFont(font3)

        self.horizontalLayout_7.addWidget(self.addBook_TitleLineEdit)


        self.verticalLayout_11.addWidget(self.addBookTitleFrame)

        self.addBookAuthorFrame = QFrame(self.addBookMainFrame)
        self.addBookAuthorFrame.setObjectName(u"addBookAuthorFrame")
        sizePolicy2.setHeightForWidth(self.addBookAuthorFrame.sizePolicy().hasHeightForWidth())
        self.addBookAuthorFrame.setSizePolicy(sizePolicy2)
        self.addBookAuthorFrame.setFrameShape(QFrame.NoFrame)
        self.addBookAuthorFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.addBookAuthorFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addBook_AuthorLbl = QLabel(self.addBookAuthorFrame)
        self.addBook_AuthorLbl.setObjectName(u"addBook_AuthorLbl")
        self.addBook_AuthorLbl.setFont(font13)

        self.horizontalLayout_6.addWidget(self.addBook_AuthorLbl)

        self.addBook_AuthorLineEdit = QLineEdit(self.addBookAuthorFrame)
        self.addBook_AuthorLineEdit.setObjectName(u"addBook_AuthorLineEdit")
        self.addBook_AuthorLineEdit.setFont(font3)

        self.horizontalLayout_6.addWidget(self.addBook_AuthorLineEdit)


        self.verticalLayout_11.addWidget(self.addBookAuthorFrame)

        self.addBookISBNFrame = QFrame(self.addBookMainFrame)
        self.addBookISBNFrame.setObjectName(u"addBookISBNFrame")
        sizePolicy2.setHeightForWidth(self.addBookISBNFrame.sizePolicy().hasHeightForWidth())
        self.addBookISBNFrame.setSizePolicy(sizePolicy2)
        self.addBookISBNFrame.setFrameShape(QFrame.NoFrame)
        self.addBookISBNFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.addBookISBNFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.addBook_ISBNLbl = QLabel(self.addBookISBNFrame)
        self.addBook_ISBNLbl.setObjectName(u"addBook_ISBNLbl")
        self.addBook_ISBNLbl.setFont(font13)

        self.horizontalLayout_8.addWidget(self.addBook_ISBNLbl)

        self.addBook_ISBNThreeLineEdit = QLineEdit(self.addBookISBNFrame)
        self.addBook_ISBNThreeLineEdit.setObjectName(u"addBook_ISBNThreeLineEdit")
        self.addBook_ISBNThreeLineEdit.setMaximumSize(QSize(60, 16777215))
        self.addBook_ISBNThreeLineEdit.setFont(font3)
        self.addBook_ISBNThreeLineEdit.setMaxLength(3)
        self.addBook_ISBNThreeLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.addBook_ISBNThreeLineEdit)

        self.addBook_ISBNSeparator = QLabel(self.addBookISBNFrame)
        self.addBook_ISBNSeparator.setObjectName(u"addBook_ISBNSeparator")
        font14 = QFont()
        font14.setFamilies([u"Montserrat Black"])
        font14.setPointSize(24)
        self.addBook_ISBNSeparator.setFont(font14)

        self.horizontalLayout_8.addWidget(self.addBook_ISBNSeparator)

        self.addBook_ISBNTenLineEdit = QLineEdit(self.addBookISBNFrame)
        self.addBook_ISBNTenLineEdit.setObjectName(u"addBook_ISBNTenLineEdit")
        self.addBook_ISBNTenLineEdit.setFont(font3)
        self.addBook_ISBNTenLineEdit.setMaxLength(10)
        self.addBook_ISBNTenLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.addBook_ISBNTenLineEdit)


        self.verticalLayout_11.addWidget(self.addBookISBNFrame)

        self.addBookGenreFrame = QFrame(self.addBookMainFrame)
        self.addBookGenreFrame.setObjectName(u"addBookGenreFrame")
        sizePolicy2.setHeightForWidth(self.addBookGenreFrame.sizePolicy().hasHeightForWidth())
        self.addBookGenreFrame.setSizePolicy(sizePolicy2)
        self.addBookGenreFrame.setFrameShape(QFrame.NoFrame)
        self.addBookGenreFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.addBookGenreFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.addBook_GenreLbl = QLabel(self.addBookGenreFrame)
        self.addBook_GenreLbl.setObjectName(u"addBook_GenreLbl")
        self.addBook_GenreLbl.setFont(font13)

        self.horizontalLayout_9.addWidget(self.addBook_GenreLbl)

        self.addBook_GenreLineEdit = QLineEdit(self.addBookGenreFrame)
        self.addBook_GenreLineEdit.setObjectName(u"addBook_GenreLineEdit")
        self.addBook_GenreLineEdit.setFont(font3)

        self.horizontalLayout_9.addWidget(self.addBook_GenreLineEdit)


        self.verticalLayout_11.addWidget(self.addBookGenreFrame)

        self.addBookDescFrame = QFrame(self.addBookMainFrame)
        self.addBookDescFrame.setObjectName(u"addBookDescFrame")
        self.addBookDescFrame.setFrameShape(QFrame.NoFrame)
        self.addBookDescFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.addBookDescFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.addBook_DescLbl = QLabel(self.addBookDescFrame)
        self.addBook_DescLbl.setObjectName(u"addBook_DescLbl")
        sizePolicy2.setHeightForWidth(self.addBook_DescLbl.sizePolicy().hasHeightForWidth())
        self.addBook_DescLbl.setSizePolicy(sizePolicy2)
        self.addBook_DescLbl.setFont(font13)

        self.verticalLayout_12.addWidget(self.addBook_DescLbl)

        self.addBook_DescTextEdit = QPlainTextEdit(self.addBookDescFrame)
        self.addBook_DescTextEdit.setObjectName(u"addBook_DescTextEdit")
        self.addBook_DescTextEdit.setFont(font3)
        self.addBook_DescTextEdit.setStyleSheet(u"background-color: #f2e9e8;\n"
"	color: #1a0f0f;")
        self.addBook_DescTextEdit.setFrameShape(QFrame.NoFrame)
        self.addBook_DescTextEdit.setFrameShadow(QFrame.Plain)

        self.verticalLayout_12.addWidget(self.addBook_DescTextEdit)


        self.verticalLayout_11.addWidget(self.addBookDescFrame)


        self.verticalLayout_10.addWidget(self.addBookMainFrame)

        self.addBook_SubmitBtn = QPushButton(self.addBookPage)
        self.addBook_SubmitBtn.setObjectName(u"addBook_SubmitBtn")
        self.addBook_SubmitBtn.setFont(font13)
        self.addBook_SubmitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.addBook_SubmitBtn)

        self.libStackedWidget.addWidget(self.addBookPage)

        self.verticalLayout.addWidget(self.libStackedWidget)

        libraryApp.setCentralWidget(self.mainWidget)

        self.retranslateUi(libraryApp)

        self.libStackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(libraryApp)
    # setupUi

    def retranslateUi(self, libraryApp):
        libraryApp.setWindowTitle(QCoreApplication.translate("libraryApp", u"MIRI'S LIBRARY", None))
        self.landing_HeadingLbl.setText(QCoreApplication.translate("libraryApp", u"MIRI'S LIBRARY", None))
        self.landing_DescLbl.setText(QCoreApplication.translate("libraryApp", u"A simple library system that's used to add/remove books and track the status of the book.", None))
        self.landing_Btn.setText(QCoreApplication.translate("libraryApp", u"Start", None))
        self.home_TotalBooksLbl.setText(QCoreApplication.translate("libraryApp", u"Total number of books -", None))
        self.home_StatusLbl.setText(QCoreApplication.translate("libraryApp", u"Library Status -", None))
        self.homeHeadingLbl.setText(QCoreApplication.translate("libraryApp", u"Home", None))
        self.home_ViewBooksBtn.setText(QCoreApplication.translate("libraryApp", u" View Books", None))
        self.home_RemoveBooksBtn.setText(QCoreApplication.translate("libraryApp", u" Remove Books", None))
        self.home_AddBooksBtn.setText(QCoreApplication.translate("libraryApp", u" Add Books", None))
        self.viewBooks_HomeBtn.setText("")
        self.viewBooks_HeaderLbl.setText(QCoreApplication.translate("libraryApp", u"Book List", None))
        self.viewBooks_TitleLbl.setText(QCoreApplication.translate("libraryApp", u"TITLE", None))
        self.viewBooks_ISBNLbl.setText(QCoreApplication.translate("libraryApp", u"ISBN", None))
        self.viewBooks_AuthorLbl.setText(QCoreApplication.translate("libraryApp", u"AUTHOR", None))
        self.viewBooks_StatusLbl.setText(QCoreApplication.translate("libraryApp", u"STATUS", None))
        self.viewBooks_GenreLbl.setText(QCoreApplication.translate("libraryApp", u"GENRE", None))
        self.viewBooks_DescHeadingLbl.setText(QCoreApplication.translate("libraryApp", u"Description", None))
        self.viewBooks_DescLbl.setText(QCoreApplication.translate("libraryApp", u"SHORT DESC", None))
        self.viewBooks_ReturnBtn.setText(QCoreApplication.translate("libraryApp", u"RETURN", None))
        self.viewBooks_BorrowBtn.setText(QCoreApplication.translate("libraryApp", u"BORROW", None))
        self.addBook_HomeBtn.setText("")
        self.addBook_HeaderLbl.setText(QCoreApplication.translate("libraryApp", u"Add Book", None))
        self.addBook_TitleLbl.setText(QCoreApplication.translate("libraryApp", u"Title", None))
        self.addBook_AuthorLbl.setText(QCoreApplication.translate("libraryApp", u"Author", None))
        self.addBook_ISBNLbl.setText(QCoreApplication.translate("libraryApp", u"ISBN", None))
        self.addBook_ISBNSeparator.setText(QCoreApplication.translate("libraryApp", u"-", None))
        self.addBook_GenreLbl.setText(QCoreApplication.translate("libraryApp", u"Genre", None))
        self.addBook_DescLbl.setText(QCoreApplication.translate("libraryApp", u"Description", None))
        self.addBook_SubmitBtn.setText(QCoreApplication.translate("libraryApp", u"Submit", None))
    # retranslateUi

