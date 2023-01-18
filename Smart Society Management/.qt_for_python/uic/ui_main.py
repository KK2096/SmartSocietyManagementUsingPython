# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 550)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setPixmap(QPixmap(u"../../.designer/backup/icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/1x/homeAsset 46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon4)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_bug = QFrame(self.frame_bottom_west)
        self.frame_bug.setObjectName(u"frame_bug")
        self.frame_bug.setMinimumSize(QSize(80, 55))
        self.frame_bug.setMaximumSize(QSize(160, 55))
        self.frame_bug.setFrameShape(QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_manage_society = QPushButton(self.frame_bug)
        self.bn_manage_society.setObjectName(u"bn_manage_society")
        self.bn_manage_society.setMinimumSize(QSize(80, 55))
        self.bn_manage_society.setMaximumSize(QSize(160, 55))
        self.bn_manage_society.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/1x/icons8_view_details_200px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_manage_society.setIcon(icon5)
        self.bn_manage_society.setIconSize(QSize(22, 22))
        self.bn_manage_society.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_manage_society)


        self.verticalLayout_3.addWidget(self.frame_bug)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName(u"frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_whatsapp_notice = QPushButton(self.frame_cloud)
        self.bn_whatsapp_notice.setObjectName(u"bn_whatsapp_notice")
        self.bn_whatsapp_notice.setMinimumSize(QSize(80, 55))
        self.bn_whatsapp_notice.setMaximumSize(QSize(160, 55))
        self.bn_whatsapp_notice.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/1x/icons8_whatsapp_200px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_whatsapp_notice.setIcon(icon6)
        self.bn_whatsapp_notice.setIconSize(QSize(28, 28))
        self.bn_whatsapp_notice.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_whatsapp_notice)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_android = QFrame(self.frame_bottom_west)
        self.frame_android.setObjectName(u"frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_complaint_forum = QPushButton(self.frame_android)
        self.bn_complaint_forum.setObjectName(u"bn_complaint_forum")
        self.bn_complaint_forum.setMinimumSize(QSize(80, 55))
        self.bn_complaint_forum.setMaximumSize(QSize(160, 55))
        self.bn_complaint_forum.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/1x/icons8_strike_200px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_complaint_forum.setIcon(icon7)
        self.bn_complaint_forum.setIconSize(QSize(30, 30))
        self.bn_complaint_forum.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_complaint_forum)


        self.verticalLayout_3.addWidget(self.frame_android)

        self.frame_about = QFrame(self.frame_bottom_west)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setFrameShape(QFrame.NoFrame)
        self.frame_about.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_about)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bn_about = QPushButton(self.frame_about)
        self.bn_about.setObjectName(u"bn_about")
        self.bn_about.setMinimumSize(QSize(80, 55))
        self.bn_about.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/1x/icons8_about_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_about.setIcon(icon8)
        self.bn_about.setIconSize(QSize(23, 22))

        self.verticalLayout_4.addWidget(self.bn_about)

        self.frame_6 = QFrame(self.frame_about)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_about)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_28 = QGridLayout(self.page_home)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.page_home)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 30))
        self.frame_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_android_contact = QFrame(self.frame_menu)
        self.frame_android_contact.setObjectName(u"frame_android_contact")
        self.frame_android_contact.setMinimumSize(QSize(80, 30))
        self.frame_android_contact.setMaximumSize(QSize(80, 30))
        self.frame_android_contact.setFrameShape(QFrame.NoFrame)
        self.frame_android_contact.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_android_contact)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.sub_btn_owner = QPushButton(self.frame_android_contact)
        self.sub_btn_owner.setObjectName(u"sub_btn_owner")
        self.sub_btn_owner.setMinimumSize(QSize(80, 30))
        self.sub_btn_owner.setMaximumSize(QSize(80, 30))
        self.sub_btn_owner.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/1x/icons8_landlord_180px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sub_btn_owner.setIcon(icon9)
        self.sub_btn_owner.setIconSize(QSize(22, 22))
        self.sub_btn_owner.setFlat(True)

        self.horizontalLayout_21.addWidget(self.sub_btn_owner)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_game = QFrame(self.frame_menu)
        self.frame_android_game.setObjectName(u"frame_android_game")
        self.frame_android_game.setMinimumSize(QSize(80, 30))
        self.frame_android_game.setMaximumSize(QSize(80, 30))
        self.frame_android_game.setFrameShape(QFrame.NoFrame)
        self.frame_android_game.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_game)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.sub_btn_staff = QPushButton(self.frame_android_game)
        self.sub_btn_staff.setObjectName(u"sub_btn_staff")
        self.sub_btn_staff.setMinimumSize(QSize(80, 30))
        self.sub_btn_staff.setMaximumSize(QSize(80, 30))
        self.sub_btn_staff.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/1x/icons8_janitor_200px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sub_btn_staff.setIcon(icon10)
        self.sub_btn_staff.setIconSize(QSize(22, 22))
        self.sub_btn_staff.setFlat(True)

        self.horizontalLayout_22.addWidget(self.sub_btn_staff)


        self.horizontalLayout_20.addWidget(self.frame_android_game)

        self.frame_android_clean = QFrame(self.frame_menu)
        self.frame_android_clean.setObjectName(u"frame_android_clean")
        self.frame_android_clean.setMinimumSize(QSize(80, 30))
        self.frame_android_clean.setMaximumSize(QSize(80, 30))
        self.frame_android_clean.setFrameShape(QFrame.NoFrame)
        self.frame_android_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_android_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.sub_btn_member = QPushButton(self.frame_android_clean)
        self.sub_btn_member.setObjectName(u"sub_btn_member")
        self.sub_btn_member.setMinimumSize(QSize(80, 30))
        self.sub_btn_member.setMaximumSize(QSize(80, 30))
        self.sub_btn_member.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/1x/peopleAsset 62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sub_btn_member.setIcon(icon11)
        self.sub_btn_member.setIconSize(QSize(20, 20))
        self.sub_btn_member.setFlat(True)

        self.horizontalLayout_23.addWidget(self.sub_btn_member)


        self.horizontalLayout_20.addWidget(self.frame_android_clean)

        self.frame_android_world = QFrame(self.frame_menu)
        self.frame_android_world.setObjectName(u"frame_android_world")
        self.frame_android_world.setMinimumSize(QSize(80, 30))
        self.frame_android_world.setMaximumSize(QSize(80, 30))
        self.frame_android_world.setFrameShape(QFrame.NoFrame)
        self.frame_android_world.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_android_world)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.sub_btn_vehicle = QPushButton(self.frame_android_world)
        self.sub_btn_vehicle.setObjectName(u"sub_btn_vehicle")
        self.sub_btn_vehicle.setMinimumSize(QSize(80, 30))
        self.sub_btn_vehicle.setMaximumSize(QSize(80, 30))
        self.sub_btn_vehicle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/icons8_car_200px_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sub_btn_vehicle.setIcon(icon12)
        self.sub_btn_vehicle.setIconSize(QSize(20, 20))
        self.sub_btn_vehicle.setFlat(True)

        self.horizontalLayout_24.addWidget(self.sub_btn_vehicle)


        self.horizontalLayout_20.addWidget(self.frame_android_world)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.gridLayout_28.addWidget(self.frame_menu, 0, 0, 1, 1)

        self.stackedWidget_home = QStackedWidget(self.page_home)
        self.stackedWidget_home.setObjectName(u"stackedWidget_home")
        self.stackedWidget_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_owner = QWidget()
        self.page_owner.setObjectName(u"page_owner")
        self.page_owner.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_owner)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.page_owner)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 55))
        self.label_4.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(24)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.page_owner)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.o_male_radio = QRadioButton(self.frame_13)
        self.o_male_radio.setObjectName(u"o_male_radio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.o_male_radio.sizePolicy().hasHeightForWidth())
        self.o_male_radio.setSizePolicy(sizePolicy1)
        self.o_male_radio.setMinimumSize(QSize(70, 0))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.o_male_radio.setFont(font2)
        self.o_male_radio.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.o_male_radio.setAutoExclusive(True)

        self.horizontalLayout_27.addWidget(self.o_male_radio)

        self.o_female_radio = QRadioButton(self.frame_13)
        self.o_female_radio.setObjectName(u"o_female_radio")
        sizePolicy1.setHeightForWidth(self.o_female_radio.sizePolicy().hasHeightForWidth())
        self.o_female_radio.setSizePolicy(sizePolicy1)
        self.o_female_radio.setMinimumSize(QSize(40, 0))
        self.o_female_radio.setFont(font2)
        self.o_female_radio.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.o_female_radio.setAutoExclusive(True)

        self.horizontalLayout_27.addWidget(self.o_female_radio)


        self.gridLayout_4.addWidget(self.frame_13, 4, 3, 1, 3)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.gridLayout_14 = QGridLayout(self.frame_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(6)
        self.o_save_btn = QPushButton(self.frame_14)
        self.o_save_btn.setObjectName(u"o_save_btn")
        self.o_save_btn.setEnabled(True)
        self.o_save_btn.setMinimumSize(QSize(69, 25))
        self.o_save_btn.setMaximumSize(QSize(69, 25))
        self.o_save_btn.setFont(font2)
        self.o_save_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_14.addWidget(self.o_save_btn, 0, 3, 1, 1)

        self.o_reset_btn = QPushButton(self.frame_14)
        self.o_reset_btn.setObjectName(u"o_reset_btn")
        self.o_reset_btn.setMinimumSize(QSize(69, 25))
        self.o_reset_btn.setMaximumSize(QSize(69, 25))
        self.o_reset_btn.setFont(font2)
        self.o_reset_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_14.addWidget(self.o_reset_btn, 0, 0, 1, 1)

        self.o_delete_btn = QPushButton(self.frame_14)
        self.o_delete_btn.setObjectName(u"o_delete_btn")
        self.o_delete_btn.setMinimumSize(QSize(69, 25))
        self.o_delete_btn.setMaximumSize(QSize(69, 25))
        self.o_delete_btn.setFont(font2)
        self.o_delete_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_14.addWidget(self.o_delete_btn, 0, 1, 1, 1)

        self.o_edit_btn = QPushButton(self.frame_14)
        self.o_edit_btn.setObjectName(u"o_edit_btn")
        self.o_edit_btn.setMinimumSize(QSize(69, 25))
        self.o_edit_btn.setMaximumSize(QSize(69, 25))
        self.o_edit_btn.setFont(font2)
        self.o_edit_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_14.addWidget(self.o_edit_btn, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_14, 15, 2, 1, 6)

        self.verticalSpacer_16 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_16, 1, 8, 1, 1)

        self.lab_person_icon_4 = QLabel(self.frame_12)
        self.lab_person_icon_4.setObjectName(u"lab_person_icon_4")
        self.lab_person_icon_4.setMinimumSize(QSize(200, 160))
        self.lab_person_icon_4.setMaximumSize(QSize(200, 160))
        self.lab_person_icon_4.setPixmap(QPixmap(u":/icons/icons/1x/icons8_landlord_180px.png"))

        self.gridLayout_4.addWidget(self.lab_person_icon_4, 0, 0, 6, 1)

        self.label_30 = QLabel(self.frame_12)
        self.label_30.setObjectName(u"label_30")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_30, 5, 1, 1, 2)

        self.verticalSpacer_17 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_17, 7, 0, 1, 1)

        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_31, 10, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_19, 9, 6, 1, 1)

        self.o_pwd_txt = QLineEdit(self.frame_12)
        self.o_pwd_txt.setObjectName(u"o_pwd_txt")
        self.o_pwd_txt.setEnabled(True)
        self.o_pwd_txt.setMinimumSize(QSize(160, 25))
        self.o_pwd_txt.setMaximumSize(QSize(16777215, 160))
        self.o_pwd_txt.setFont(font2)
        self.o_pwd_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.o_pwd_txt.setFrame(True)
        self.o_pwd_txt.setReadOnly(True)

        self.gridLayout_4.addWidget(self.o_pwd_txt, 13, 4, 1, 4)

        self.o_phno_txt = QLineEdit(self.frame_12)
        self.o_phno_txt.setObjectName(u"o_phno_txt")
        self.o_phno_txt.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.o_phno_txt.sizePolicy().hasHeightForWidth())
        self.o_phno_txt.setSizePolicy(sizePolicy2)
        self.o_phno_txt.setMinimumSize(QSize(180, 25))
        self.o_phno_txt.setMaximumSize(QSize(400, 25))
        self.o_phno_txt.setFont(font2)
        self.o_phno_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.o_phno_txt.setMaxLength(10)

        self.gridLayout_4.addWidget(self.o_phno_txt, 6, 3, 1, 4)

        self.o_marital_combo = QComboBox(self.frame_12)
        self.o_marital_combo.addItem("")
        self.o_marital_combo.addItem("")
        self.o_marital_combo.addItem("")
        self.o_marital_combo.setObjectName(u"o_marital_combo")
        self.o_marital_combo.setMinimumSize(QSize(180, 0))
        self.o_marital_combo.setFont(font2)
        self.o_marital_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.o_marital_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.o_marital_combo.setFrame(False)
        self.o_marital_combo.setModelColumn(0)

        self.gridLayout_4.addWidget(self.o_marital_combo, 5, 3, 1, 4)

        self.label_32 = QLabel(self.frame_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_32, 6, 1, 1, 2)

        self.verticalSpacer_20 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 12, 4, 1, 2)

        self.o_owner_id_txt = QLineEdit(self.frame_12)
        self.o_owner_id_txt.setObjectName(u"o_owner_id_txt")
        self.o_owner_id_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.o_owner_id_txt.sizePolicy().hasHeightForWidth())
        self.o_owner_id_txt.setSizePolicy(sizePolicy2)
        self.o_owner_id_txt.setMinimumSize(QSize(180, 25))
        self.o_owner_id_txt.setMaximumSize(QSize(150, 25))
        self.o_owner_id_txt.setFont(font2)
        self.o_owner_id_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.o_owner_id_txt, 2, 3, 1, 4)

        self.o_generate_btn = QPushButton(self.frame_12)
        self.o_generate_btn.setObjectName(u"o_generate_btn")
        self.o_generate_btn.setMinimumSize(QSize(69, 25))
        self.o_generate_btn.setMaximumSize(QSize(120, 25))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.o_generate_btn.setFont(font4)
        self.o_generate_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.o_generate_btn, 13, 9, 1, 1)

        self.o_curr_owners_combo = QComboBox(self.frame_12)
        self.o_curr_owners_combo.addItem("")
        self.o_curr_owners_combo.setObjectName(u"o_curr_owners_combo")
        sizePolicy2.setHeightForWidth(self.o_curr_owners_combo.sizePolicy().hasHeightForWidth())
        self.o_curr_owners_combo.setSizePolicy(sizePolicy2)
        self.o_curr_owners_combo.setFont(font2)
        self.o_curr_owners_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.o_curr_owners_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.o_curr_owners_combo.setFrame(False)
        self.o_curr_owners_combo.setModelColumn(0)

        self.gridLayout_4.addWidget(self.o_curr_owners_combo, 0, 3, 1, 2)

        self.label_33 = QLabel(self.frame_12)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_33, 0, 1, 1, 2)

        self.verticalSpacer_21 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_21, 14, 5, 1, 1)

        self.label_34 = QLabel(self.frame_12)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_34, 2, 1, 1, 2)

        self.o_status_lbl = QLabel(self.frame_12)
        self.o_status_lbl.setObjectName(u"o_status_lbl")
        self.o_status_lbl.setEnabled(True)
        self.o_status_lbl.setFont(font2)
        self.o_status_lbl.setStyleSheet(u"\n"
"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color:rgb(112,0,0);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.o_status_lbl, 8, 3, 1, 3)

        self.o_owner_name_txt = QLineEdit(self.frame_12)
        self.o_owner_name_txt.setObjectName(u"o_owner_name_txt")
        self.o_owner_name_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.o_owner_name_txt.sizePolicy().hasHeightForWidth())
        self.o_owner_name_txt.setSizePolicy(sizePolicy2)
        self.o_owner_name_txt.setMinimumSize(QSize(0, 0))
        self.o_owner_name_txt.setFont(font2)
        self.o_owner_name_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.o_owner_name_txt, 3, 3, 1, 6)

        self.label_35 = QLabel(self.frame_12)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_35, 7, 1, 1, 1)

        self.o_uname_txt = QLineEdit(self.frame_12)
        self.o_uname_txt.setObjectName(u"o_uname_txt")
        self.o_uname_txt.setEnabled(True)
        self.o_uname_txt.setMinimumSize(QSize(150, 25))
        self.o_uname_txt.setFont(font2)
        self.o_uname_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.o_uname_txt.setReadOnly(True)

        self.gridLayout_4.addWidget(self.o_uname_txt, 13, 1, 1, 3)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_10, 4, 1, 1, 1)

        self.label_36 = QLabel(self.frame_12)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_36, 11, 1, 1, 1)

        self.label_37 = QLabel(self.frame_12)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_37, 3, 1, 1, 2)

        self.o_flat_no_combo = QComboBox(self.frame_12)
        self.o_flat_no_combo.addItem("")
        self.o_flat_no_combo.addItem("")
        self.o_flat_no_combo.addItem("")
        self.o_flat_no_combo.setObjectName(u"o_flat_no_combo")
        self.o_flat_no_combo.setMaximumSize(QSize(16777215, 25))
        self.o_flat_no_combo.setFont(font2)
        self.o_flat_no_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.o_flat_no_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.o_flat_no_combo.setFrame(False)
        self.o_flat_no_combo.setModelColumn(0)

        self.gridLayout_4.addWidget(self.o_flat_no_combo, 11, 3, 1, 6)

        self.o_wing_combo = QComboBox(self.frame_12)
        self.o_wing_combo.addItem("")
        self.o_wing_combo.addItem("")
        self.o_wing_combo.addItem("")
        self.o_wing_combo.setObjectName(u"o_wing_combo")
        self.o_wing_combo.setMaximumSize(QSize(16777215, 25))
        self.o_wing_combo.setFont(font2)
        self.o_wing_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.o_wing_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.o_wing_combo.setFrame(False)
        self.o_wing_combo.setModelColumn(0)

        self.gridLayout_4.addWidget(self.o_wing_combo, 10, 3, 1, 6)

        self.o_address_txt = QPlainTextEdit(self.frame_12)
        self.o_address_txt.setObjectName(u"o_address_txt")
        sizePolicy2.setHeightForWidth(self.o_address_txt.sizePolicy().hasHeightForWidth())
        self.o_address_txt.setSizePolicy(sizePolicy2)
        self.o_address_txt.setMaximumSize(QSize(16777215, 120))
        self.o_address_txt.setStyleSheet(u"QPlainTextEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QPlainTextEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.o_address_txt, 7, 3, 1, 6)

        self.o_start_videocam_btn = QPushButton(self.frame_12)
        self.o_start_videocam_btn.setObjectName(u"o_start_videocam_btn")
        sizePolicy2.setHeightForWidth(self.o_start_videocam_btn.sizePolicy().hasHeightForWidth())
        self.o_start_videocam_btn.setSizePolicy(sizePolicy2)
        self.o_start_videocam_btn.setMinimumSize(QSize(69, 25))
        self.o_start_videocam_btn.setMaximumSize(QSize(120, 25))
        self.o_start_videocam_btn.setFont(font4)
        self.o_start_videocam_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.o_start_videocam_btn, 8, 6, 1, 3)


        self.gridLayout_5.addWidget(self.frame_12, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.vsb_about_home_2 = QScrollBar(self.page_owner)
        self.vsb_about_home_2.setObjectName(u"vsb_about_home_2")
        self.vsb_about_home_2.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_about_home_2.setOrientation(Qt.Vertical)

        self.gridLayout_5.addWidget(self.vsb_about_home_2, 1, 2, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_23, 2, 0, 1, 1)

        self.stackedWidget_home.addWidget(self.page_owner)
        self.page_staff = QWidget()
        self.page_staff.setObjectName(u"page_staff")
        self.page_staff.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_6 = QGridLayout(self.page_staff)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.page_staff)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 55))
        self.label.setMaximumSize(QSize(16777215, 55))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.page_staff)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_12, 3, 1, 1, 2)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_9, 4, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 1, 8, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 7, 0, 1, 1)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_18, 5, 1, 1, 2)

        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_21, 10, 1, 1, 1)

        self.lab_person_icon_2 = QLabel(self.frame_7)
        self.lab_person_icon_2.setObjectName(u"lab_person_icon_2")
        self.lab_person_icon_2.setMinimumSize(QSize(200, 160))
        self.lab_person_icon_2.setMaximumSize(QSize(200, 160))
        self.lab_person_icon_2.setPixmap(QPixmap(u":/icons/icons/1x/icons8_reception_165px.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon_2, 0, 0, 6, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_18, 9, 6, 1, 1)

        self.s_phno_txt = QLineEdit(self.frame_7)
        self.s_phno_txt.setObjectName(u"s_phno_txt")
        self.s_phno_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.s_phno_txt.sizePolicy().hasHeightForWidth())
        self.s_phno_txt.setSizePolicy(sizePolicy2)
        self.s_phno_txt.setMinimumSize(QSize(180, 25))
        self.s_phno_txt.setMaximumSize(QSize(400, 25))
        self.s_phno_txt.setFont(font2)
        self.s_phno_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.s_phno_txt.setMaxLength(10)

        self.gridLayout_3.addWidget(self.s_phno_txt, 6, 3, 1, 4)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_14, 11, 4, 1, 2)

        self.s_marital_combo = QComboBox(self.frame_7)
        self.s_marital_combo.addItem("")
        self.s_marital_combo.addItem("")
        self.s_marital_combo.addItem("")
        self.s_marital_combo.setObjectName(u"s_marital_combo")
        self.s_marital_combo.setMinimumSize(QSize(180, 0))
        self.s_marital_combo.setFont(font2)
        self.s_marital_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.s_marital_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.s_marital_combo.setFrame(False)
        self.s_marital_combo.setModelColumn(0)

        self.gridLayout_3.addWidget(self.s_marital_combo, 5, 3, 1, 4)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_20, 6, 1, 1, 2)

        self.s_staff_id_txt = QLineEdit(self.frame_7)
        self.s_staff_id_txt.setObjectName(u"s_staff_id_txt")
        self.s_staff_id_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.s_staff_id_txt.sizePolicy().hasHeightForWidth())
        self.s_staff_id_txt.setSizePolicy(sizePolicy2)
        self.s_staff_id_txt.setMinimumSize(QSize(180, 25))
        self.s_staff_id_txt.setMaximumSize(QSize(150, 25))
        self.s_staff_id_txt.setFont(font2)
        self.s_staff_id_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_3.addWidget(self.s_staff_id_txt, 2, 3, 1, 4)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 2)

        self.s_status_lbl = QLabel(self.frame_7)
        self.s_status_lbl.setObjectName(u"s_status_lbl")
        self.s_status_lbl.setEnabled(True)
        self.s_status_lbl.setFont(font2)
        self.s_status_lbl.setStyleSheet(u"\n"
"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color:rgb(112,0,0);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.s_status_lbl, 8, 3, 1, 3)

        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_19, 2, 1, 1, 2)

        self.s_staff_name_txt = QLineEdit(self.frame_7)
        self.s_staff_name_txt.setObjectName(u"s_staff_name_txt")
        self.s_staff_name_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.s_staff_name_txt.sizePolicy().hasHeightForWidth())
        self.s_staff_name_txt.setSizePolicy(sizePolicy2)
        self.s_staff_name_txt.setMinimumSize(QSize(0, 0))
        self.s_staff_name_txt.setFont(font2)
        self.s_staff_name_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_3.addWidget(self.s_staff_name_txt, 3, 3, 1, 6)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.label_16, 7, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.s_male_radio = QRadioButton(self.frame_8)
        self.s_male_radio.setObjectName(u"s_male_radio")
        sizePolicy1.setHeightForWidth(self.s_male_radio.sizePolicy().hasHeightForWidth())
        self.s_male_radio.setSizePolicy(sizePolicy1)
        self.s_male_radio.setMinimumSize(QSize(70, 0))
        self.s_male_radio.setFont(font2)
        self.s_male_radio.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.s_male_radio.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.s_male_radio)

        self.s_female_radio = QRadioButton(self.frame_8)
        self.s_female_radio.setObjectName(u"s_female_radio")
        sizePolicy1.setHeightForWidth(self.s_female_radio.sizePolicy().hasHeightForWidth())
        self.s_female_radio.setSizePolicy(sizePolicy1)
        self.s_female_radio.setMinimumSize(QSize(40, 0))
        self.s_female_radio.setFont(font2)
        self.s_female_radio.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.s_female_radio.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.s_female_radio)


        self.gridLayout_3.addWidget(self.frame_8, 4, 3, 1, 3)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.gridLayout_12 = QGridLayout(self.frame_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(6)
        self.s_save_btn = QPushButton(self.frame_10)
        self.s_save_btn.setObjectName(u"s_save_btn")
        self.s_save_btn.setEnabled(True)
        self.s_save_btn.setMinimumSize(QSize(69, 25))
        self.s_save_btn.setMaximumSize(QSize(69, 25))
        self.s_save_btn.setFont(font2)
        self.s_save_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_12.addWidget(self.s_save_btn, 0, 3, 1, 1)

        self.s_reset_btn = QPushButton(self.frame_10)
        self.s_reset_btn.setObjectName(u"s_reset_btn")
        self.s_reset_btn.setMinimumSize(QSize(69, 25))
        self.s_reset_btn.setMaximumSize(QSize(69, 25))
        self.s_reset_btn.setFont(font2)
        self.s_reset_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_12.addWidget(self.s_reset_btn, 0, 0, 1, 1)

        self.s_delete_btn = QPushButton(self.frame_10)
        self.s_delete_btn.setObjectName(u"s_delete_btn")
        self.s_delete_btn.setMinimumSize(QSize(69, 25))
        self.s_delete_btn.setMaximumSize(QSize(69, 25))
        self.s_delete_btn.setFont(font2)
        self.s_delete_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_12.addWidget(self.s_delete_btn, 0, 1, 1, 1)

        self.s_edit_btn = QPushButton(self.frame_10)
        self.s_edit_btn.setObjectName(u"s_edit_btn")
        self.s_edit_btn.setMinimumSize(QSize(69, 25))
        self.s_edit_btn.setMaximumSize(QSize(69, 25))
        self.s_edit_btn.setFont(font2)
        self.s_edit_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_12.addWidget(self.s_edit_btn, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_10, 12, 2, 1, 6)

        self.s_position_combo = QComboBox(self.frame_7)
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.addItem("")
        self.s_position_combo.setObjectName(u"s_position_combo")
        self.s_position_combo.setMaximumSize(QSize(16777215, 25))
        self.s_position_combo.setFont(font2)
        self.s_position_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.s_position_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.s_position_combo.setFrame(False)
        self.s_position_combo.setModelColumn(0)

        self.gridLayout_3.addWidget(self.s_position_combo, 10, 3, 1, 6)

        self.s_address_txt = QPlainTextEdit(self.frame_7)
        self.s_address_txt.setObjectName(u"s_address_txt")
        sizePolicy2.setHeightForWidth(self.s_address_txt.sizePolicy().hasHeightForWidth())
        self.s_address_txt.setSizePolicy(sizePolicy2)
        self.s_address_txt.setMaximumSize(QSize(16777215, 120))
        self.s_address_txt.setStyleSheet(u"QPlainTextEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QPlainTextEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_3.addWidget(self.s_address_txt, 7, 3, 1, 6)

        self.s_start_videocam_btn = QPushButton(self.frame_7)
        self.s_start_videocam_btn.setObjectName(u"s_start_videocam_btn")
        sizePolicy2.setHeightForWidth(self.s_start_videocam_btn.sizePolicy().hasHeightForWidth())
        self.s_start_videocam_btn.setSizePolicy(sizePolicy2)
        self.s_start_videocam_btn.setMinimumSize(QSize(69, 25))
        self.s_start_videocam_btn.setMaximumSize(QSize(120, 25))
        self.s_start_videocam_btn.setFont(font4)
        self.s_start_videocam_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_3.addWidget(self.s_start_videocam_btn, 8, 6, 1, 3)

        self.s_curr_staff_combo = QComboBox(self.frame_7)
        self.s_curr_staff_combo.addItem("")
        self.s_curr_staff_combo.setObjectName(u"s_curr_staff_combo")
        sizePolicy2.setHeightForWidth(self.s_curr_staff_combo.sizePolicy().hasHeightForWidth())
        self.s_curr_staff_combo.setSizePolicy(sizePolicy2)
        self.s_curr_staff_combo.setFont(font2)
        self.s_curr_staff_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.s_curr_staff_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.s_curr_staff_combo.setFrame(False)
        self.s_curr_staff_combo.setModelColumn(0)

        self.gridLayout_3.addWidget(self.s_curr_staff_combo, 0, 3, 1, 6)


        self.gridLayout_6.addWidget(self.frame_7, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.stackedWidget_home.addWidget(self.page_staff)
        self.page_member_registration = QWidget()
        self.page_member_registration.setObjectName(u"page_member_registration")
        self.page_member_registration.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_member_registration)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_member_registration)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font1)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_member_registration)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_13 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u":/icons/icons/1x/peopleAsset 62.png"))

        self.gridLayout_13.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_android_field)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.frame_android_field)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.m_male_radio = QRadioButton(self.frame_4)
        self.m_male_radio.setObjectName(u"m_male_radio")
        self.m_male_radio.setFont(font2)
        self.m_male_radio.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.m_male_radio.setAutoExclusive(True)

        self.horizontalLayout_25.addWidget(self.m_male_radio)

        self.m_female_radio = QRadioButton(self.frame_4)
        self.m_female_radio.setObjectName(u"m_female_radio")
        self.m_female_radio.setFont(font2)
        self.m_female_radio.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.m_female_radio.setAutoExclusive(True)

        self.horizontalLayout_25.addWidget(self.m_female_radio)


        self.gridLayout.addWidget(self.frame_4, 4, 2, 1, 1)

        self.frame_3 = QFrame(self.frame_android_field)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(6)
        self.m_reset_btn = QPushButton(self.frame_3)
        self.m_reset_btn.setObjectName(u"m_reset_btn")
        self.m_reset_btn.setMinimumSize(QSize(69, 25))
        self.m_reset_btn.setMaximumSize(QSize(69, 25))
        self.m_reset_btn.setFont(font2)
        self.m_reset_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_8.addWidget(self.m_reset_btn, 0, 0, 1, 1)

        self.m_save_btn = QPushButton(self.frame_3)
        self.m_save_btn.setObjectName(u"m_save_btn")
        self.m_save_btn.setEnabled(True)
        self.m_save_btn.setMinimumSize(QSize(69, 25))
        self.m_save_btn.setMaximumSize(QSize(69, 25))
        self.m_save_btn.setFont(font2)
        self.m_save_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_8.addWidget(self.m_save_btn, 0, 3, 1, 1)

        self.m_delete_btn = QPushButton(self.frame_3)
        self.m_delete_btn.setObjectName(u"m_delete_btn")
        self.m_delete_btn.setMinimumSize(QSize(69, 25))
        self.m_delete_btn.setMaximumSize(QSize(69, 25))
        self.m_delete_btn.setFont(font2)
        self.m_delete_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_8.addWidget(self.m_delete_btn, 0, 1, 1, 1)

        self.m_edit_btn = QPushButton(self.frame_3)
        self.m_edit_btn.setObjectName(u"m_edit_btn")
        self.m_edit_btn.setMinimumSize(QSize(69, 25))
        self.m_edit_btn.setMaximumSize(QSize(69, 25))
        self.m_edit_btn.setFont(font2)
        self.m_edit_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_8.addWidget(self.m_edit_btn, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 10, 0, 1, 4)

        self.m_email_txt = QLineEdit(self.frame_android_field)
        self.m_email_txt.setObjectName(u"m_email_txt")
        self.m_email_txt.setEnabled(True)
        self.m_email_txt.setMinimumSize(QSize(300, 25))
        self.m_email_txt.setMaximumSize(QSize(400, 25))
        self.m_email_txt.setFont(font2)
        self.m_email_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout.addWidget(self.m_email_txt, 6, 2, 1, 2)

        self.label_8 = QLabel(self.frame_android_field)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.m_start_videocam_btn = QPushButton(self.frame_android_field)
        self.m_start_videocam_btn.setObjectName(u"m_start_videocam_btn")
        self.m_start_videocam_btn.setMinimumSize(QSize(69, 25))
        self.m_start_videocam_btn.setMaximumSize(QSize(120, 25))
        self.m_start_videocam_btn.setFont(font4)
        self.m_start_videocam_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout.addWidget(self.m_start_videocam_btn, 8, 3, 1, 1)

        self.m_status_lbl = QLabel(self.frame_android_field)
        self.m_status_lbl.setObjectName(u"m_status_lbl")
        self.m_status_lbl.setEnabled(True)
        self.m_status_lbl.setFont(font2)
        self.m_status_lbl.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.m_status_lbl, 8, 2, 1, 1)

        self.m_curr_mem_combo = QComboBox(self.frame_android_field)
        self.m_curr_mem_combo.addItem("")
        self.m_curr_mem_combo.setObjectName(u"m_curr_mem_combo")
        self.m_curr_mem_combo.setMaximumSize(QSize(16777215, 25))
        self.m_curr_mem_combo.setFont(font2)
        self.m_curr_mem_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.m_curr_mem_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.m_curr_mem_combo.setFrame(False)
        self.m_curr_mem_combo.setModelColumn(0)

        self.gridLayout.addWidget(self.m_curr_mem_combo, 0, 2, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 11, 1, 1, 1)

        self.label_14 = QLabel(self.frame_android_field)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 2)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.m_ph_txt = QLineEdit(self.frame_android_field)
        self.m_ph_txt.setObjectName(u"m_ph_txt")
        self.m_ph_txt.setEnabled(True)
        self.m_ph_txt.setMinimumSize(QSize(300, 25))
        self.m_ph_txt.setMaximumSize(QSize(400, 25))
        self.m_ph_txt.setFont(font2)
        self.m_ph_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.m_ph_txt.setMaxLength(10)

        self.gridLayout.addWidget(self.m_ph_txt, 7, 2, 1, 2)

        self.m_member_name_txt = QLineEdit(self.frame_android_field)
        self.m_member_name_txt.setObjectName(u"m_member_name_txt")
        self.m_member_name_txt.setEnabled(True)
        self.m_member_name_txt.setMinimumSize(QSize(300, 25))
        self.m_member_name_txt.setMaximumSize(QSize(400, 25))
        self.m_member_name_txt.setFont(font2)
        self.m_member_name_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout.addWidget(self.m_member_name_txt, 3, 2, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.m_member_id_txt = QLineEdit(self.frame_android_field)
        self.m_member_id_txt.setObjectName(u"m_member_id_txt")
        self.m_member_id_txt.setEnabled(True)
        self.m_member_id_txt.setMinimumSize(QSize(300, 25))
        self.m_member_id_txt.setMaximumSize(QSize(400, 25))
        self.m_member_id_txt.setFont(font2)
        self.m_member_id_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout.addWidget(self.m_member_id_txt, 2, 2, 1, 2)

        self.label_11 = QLabel(self.frame_android_field)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 2)

        self.m_relation_combo = QComboBox(self.frame_android_field)
        self.m_relation_combo.addItem("")
        self.m_relation_combo.setObjectName(u"m_relation_combo")
        self.m_relation_combo.setMaximumSize(QSize(16777215, 25))
        self.m_relation_combo.setFont(font2)
        self.m_relation_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.m_relation_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.m_relation_combo.setFrame(False)
        self.m_relation_combo.setModelColumn(0)

        self.gridLayout.addWidget(self.m_relation_combo, 5, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 4, 1, 1)

        self.label_7 = QLabel(self.frame_android_field)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_13 = QLabel(self.frame_android_field)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 9, 2, 1, 1)


        self.gridLayout_13.addWidget(self.frame_android_field, 0, 1, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_home.addWidget(self.page_member_registration)
        self.page_vehicle_registration = QWidget()
        self.page_vehicle_registration.setObjectName(u"page_vehicle_registration")
        self.page_vehicle_registration.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_vehicle_registration)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_vehicle_registration)
        self.lab_gamepad.setObjectName(u"lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        self.lab_gamepad.setFont(font1)
        self.lab_gamepad.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_vehicle_registration)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.textEdit_gamepad = QTextEdit(self.frame_textbar)
        self.textEdit_gamepad.setObjectName(u"textEdit_gamepad")
        self.textEdit_gamepad.setGeometry(QRect(6, 1, 256, 192))
        self.textEdit_gamepad.setFont(font2)
        self.textEdit_gamepad.setStyleSheet(u"color:rgb(255,255,255);")
        self.textEdit_gamepad.setFrameShape(QFrame.NoFrame)
        self.textEdit_gamepad.setFrameShadow(QFrame.Plain)
        self.textEdit_gamepad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_gamepad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.vsb_gamepad = QScrollBar(self.frame_textbar)
        self.vsb_gamepad.setObjectName(u"vsb_gamepad")
        self.vsb_gamepad.setGeometry(QRect(689, 1, 20, 40))
        self.vsb_gamepad.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_gamepad.setOrientation(Qt.Vertical)
        self.vsb_gamepad.setInvertedControls(True)
        self.frame_android_bottom_3 = QFrame(self.frame_textbar)
        self.frame_android_bottom_3.setObjectName(u"frame_android_bottom_3")
        self.frame_android_bottom_3.setGeometry(QRect(0, 0, 727, 356))
        self.frame_android_bottom_3.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_15 = QGridLayout(self.frame_android_bottom_3)
        self.gridLayout_15.setSpacing(5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.lab_person_icon_3 = QLabel(self.frame_android_bottom_3)
        self.lab_person_icon_3.setObjectName(u"lab_person_icon_3")
        self.lab_person_icon_3.setMinimumSize(QSize(200, 160))
        self.lab_person_icon_3.setMaximumSize(QSize(200, 160))
        self.lab_person_icon_3.setPixmap(QPixmap(u":/icons/icons/icons8_car_180px.png"))

        self.gridLayout_15.addWidget(self.lab_person_icon_3, 0, 0, 1, 1)

        self.frame_android_field_3 = QFrame(self.frame_android_bottom_3)
        self.frame_android_field_3.setObjectName(u"frame_android_field_3")
        self.frame_android_field_3.setFrameShape(QFrame.NoFrame)
        self.frame_android_field_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_16 = QGridLayout(self.frame_android_field_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_24 = QLabel(self.frame_android_field_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_24, 0, 0, 1, 3)

        self.label_28 = QLabel(self.frame_android_field_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_28, 3, 0, 2, 3)

        self.v_fetch_using_api_btn = QPushButton(self.frame_android_field_3)
        self.v_fetch_using_api_btn.setObjectName(u"v_fetch_using_api_btn")
        self.v_fetch_using_api_btn.setMinimumSize(QSize(69, 25))
        self.v_fetch_using_api_btn.setMaximumSize(QSize(130, 25))
        self.v_fetch_using_api_btn.setFont(font2)
        self.v_fetch_using_api_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_16.addWidget(self.v_fetch_using_api_btn, 1, 3, 2, 2)

        self.v_reg_no_api_btn = QLineEdit(self.frame_android_field_3)
        self.v_reg_no_api_btn.setObjectName(u"v_reg_no_api_btn")
        self.v_reg_no_api_btn.setEnabled(True)
        self.v_reg_no_api_btn.setMinimumSize(QSize(300, 25))
        self.v_reg_no_api_btn.setMaximumSize(QSize(400, 25))
        self.v_reg_no_api_btn.setFont(font2)
        self.v_reg_no_api_btn.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_16.addWidget(self.v_reg_no_api_btn, 0, 3, 1, 2)

        self.v_curr_veh_combo = QComboBox(self.frame_android_field_3)
        self.v_curr_veh_combo.addItem("")
        self.v_curr_veh_combo.setObjectName(u"v_curr_veh_combo")
        self.v_curr_veh_combo.setMaximumSize(QSize(16777215, 25))
        self.v_curr_veh_combo.setFont(font2)
        self.v_curr_veh_combo.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.v_curr_veh_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.v_curr_veh_combo.setFrame(False)
        self.v_curr_veh_combo.setModelColumn(0)

        self.gridLayout_16.addWidget(self.v_curr_veh_combo, 4, 3, 1, 2)

        self.v_owner_name_txt = QLineEdit(self.frame_android_field_3)
        self.v_owner_name_txt.setObjectName(u"v_owner_name_txt")
        self.v_owner_name_txt.setEnabled(True)
        self.v_owner_name_txt.setMinimumSize(QSize(300, 25))
        self.v_owner_name_txt.setMaximumSize(QSize(400, 25))
        self.v_owner_name_txt.setFont(font2)
        self.v_owner_name_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_16.addWidget(self.v_owner_name_txt, 6, 3, 1, 2)

        self.label_25 = QLabel(self.frame_android_field_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_25, 6, 0, 1, 3)

        self.label_26 = QLabel(self.frame_android_field_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_26, 7, 0, 1, 1)

        self.v_model_txt = QLineEdit(self.frame_android_field_3)
        self.v_model_txt.setObjectName(u"v_model_txt")
        self.v_model_txt.setEnabled(True)
        self.v_model_txt.setMinimumSize(QSize(300, 25))
        self.v_model_txt.setMaximumSize(QSize(400, 25))
        self.v_model_txt.setFont(font2)
        self.v_model_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_16.addWidget(self.v_model_txt, 7, 3, 1, 2)

        self.label_22 = QLabel(self.frame_android_field_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_22, 9, 0, 1, 2)

        self.v_rto_name_txt = QLineEdit(self.frame_android_field_3)
        self.v_rto_name_txt.setObjectName(u"v_rto_name_txt")
        self.v_rto_name_txt.setEnabled(True)
        self.v_rto_name_txt.setMinimumSize(QSize(300, 25))
        self.v_rto_name_txt.setMaximumSize(QSize(400, 25))
        self.v_rto_name_txt.setFont(font2)
        self.v_rto_name_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_16.addWidget(self.v_rto_name_txt, 8, 3, 1, 2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_9, 8, 5, 1, 1)

        self.label_27 = QLabel(self.frame_android_field_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_27, 8, 0, 1, 2)

        self.v_reg_date_txt = QDateEdit(self.frame_android_field_3)
        self.v_reg_date_txt.setObjectName(u"v_reg_date_txt")
        self.v_reg_date_txt.setEnabled(True)
        self.v_reg_date_txt.setMinimumSize(QSize(200, 25))
        self.v_reg_date_txt.setMaximumSize(QSize(400, 25))
        self.v_reg_date_txt.setFont(font2)
        self.v_reg_date_txt.setMouseTracking(False)
        self.v_reg_date_txt.setAcceptDrops(True)
        self.v_reg_date_txt.setStyleSheet(u"QDateEdit{\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_16.addWidget(self.v_reg_date_txt, 9, 3, 1, 2)

        self.v_reg_no_txt = QLineEdit(self.frame_android_field_3)
        self.v_reg_no_txt.setObjectName(u"v_reg_no_txt")
        self.v_reg_no_txt.setEnabled(True)
        self.v_reg_no_txt.setMinimumSize(QSize(300, 25))
        self.v_reg_no_txt.setMaximumSize(QSize(400, 25))
        self.v_reg_no_txt.setFont(font2)
        self.v_reg_no_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.v_reg_no_txt.setMaxLength(10)

        self.gridLayout_16.addWidget(self.v_reg_no_txt, 10, 3, 1, 2)

        self.label_23 = QLabel(self.frame_android_field_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_16.addWidget(self.label_23, 10, 0, 1, 2)

        self.verticalSpacer_12 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_12, 11, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_10, 13, 2, 1, 1)

        self.frame_9 = QFrame(self.frame_android_field_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.gridLayout_17 = QGridLayout(self.frame_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.v_reset_btn = QPushButton(self.frame_9)
        self.v_reset_btn.setObjectName(u"v_reset_btn")
        self.v_reset_btn.setMinimumSize(QSize(69, 25))
        self.v_reset_btn.setMaximumSize(QSize(69, 25))
        self.v_reset_btn.setFont(font2)
        self.v_reset_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_17.addWidget(self.v_reset_btn, 0, 0, 1, 1)

        self.v_delete_btn = QPushButton(self.frame_9)
        self.v_delete_btn.setObjectName(u"v_delete_btn")
        self.v_delete_btn.setMinimumSize(QSize(69, 25))
        self.v_delete_btn.setMaximumSize(QSize(69, 25))
        self.v_delete_btn.setFont(font2)
        self.v_delete_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_17.addWidget(self.v_delete_btn, 0, 1, 1, 1)

        self.v_edit_btn = QPushButton(self.frame_9)
        self.v_edit_btn.setObjectName(u"v_edit_btn")
        self.v_edit_btn.setMinimumSize(QSize(69, 25))
        self.v_edit_btn.setMaximumSize(QSize(69, 25))
        self.v_edit_btn.setFont(font2)
        self.v_edit_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_17.addWidget(self.v_edit_btn, 0, 2, 1, 1)

        self.v_save_btn = QPushButton(self.frame_9)
        self.v_save_btn.setObjectName(u"v_save_btn")
        self.v_save_btn.setMinimumSize(QSize(69, 25))
        self.v_save_btn.setMaximumSize(QSize(69, 25))
        self.v_save_btn.setFont(font2)
        self.v_save_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_17.addWidget(self.v_save_btn, 0, 3, 1, 1)


        self.gridLayout_16.addWidget(self.frame_9, 12, 0, 1, 5)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_22, 5, 3, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(13, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_11, 3, 3, 1, 1)


        self.gridLayout_15.addWidget(self.frame_android_field_3, 0, 1, 2, 1)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_home.addWidget(self.page_vehicle_registration)

        self.gridLayout_28.addWidget(self.stackedWidget_home, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.stackedWidget_home.raise_()
        self.frame_menu.raise_()
        self.page_tmp = QWidget()
        self.page_tmp.setObjectName(u"page_tmp")
        self.page_tmp.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_tmp)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_tmp)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home.setFont(font1)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_tmp)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_about_home)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.vsb_about_home = QScrollBar(self.frame_about_home)
        self.vsb_about_home.setObjectName(u"vsb_about_home")
        self.vsb_about_home.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_about_home.setOrientation(Qt.Vertical)

        self.gridLayout_7.addWidget(self.vsb_about_home, 0, 3, 1, 1)

        self.label_29 = QLabel(self.frame_about_home)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setPixmap(QPixmap(u":/icons/icons/1x/icons8_company_380px.png"))

        self.gridLayout_7.addWidget(self.label_29, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_about_home)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_15)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.gridLayout_18 = QGridLayout(self.frame_16)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.w_clear_btn = QPushButton(self.frame_16)
        self.w_clear_btn.setObjectName(u"w_clear_btn")
        self.w_clear_btn.setMinimumSize(QSize(69, 25))
        self.w_clear_btn.setMaximumSize(QSize(69, 25))
        self.w_clear_btn.setFont(font2)
        self.w_clear_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_18.addWidget(self.w_clear_btn, 0, 0, 1, 1)

        self.w_add_btn = QPushButton(self.frame_16)
        self.w_add_btn.setObjectName(u"w_add_btn")
        self.w_add_btn.setEnabled(True)
        self.w_add_btn.setMinimumSize(QSize(69, 25))
        self.w_add_btn.setMaximumSize(QSize(69, 25))
        self.w_add_btn.setFont(font2)
        self.w_add_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_18.addWidget(self.w_add_btn, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.frame_16, 6, 0, 1, 2)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_19.addWidget(self.frame_17, 7, 0, 1, 2)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout_19.addWidget(self.frame_18, 0, 0, 1, 1)

        self.w_tot_flats_txt = QLineEdit(self.frame_15)
        self.w_tot_flats_txt.setObjectName(u"w_tot_flats_txt")
        self.w_tot_flats_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.w_tot_flats_txt.sizePolicy().hasHeightForWidth())
        self.w_tot_flats_txt.setSizePolicy(sizePolicy2)
        self.w_tot_flats_txt.setMinimumSize(QSize(0, 0))
        self.w_tot_flats_txt.setFont(font2)
        self.w_tot_flats_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.w_tot_flats_txt.setMaxLength(2)

        self.gridLayout_19.addWidget(self.w_tot_flats_txt, 5, 1, 1, 1)

        self.label_40 = QLabel(self.frame_15)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Segoe UI Black")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_40.setFont(font5)
        self.label_40.setLayoutDirection(Qt.LeftToRight)
        self.label_40.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_40, 2, 0, 1, 2)

        self.w_wing_name_txt = QLineEdit(self.frame_15)
        self.w_wing_name_txt.setObjectName(u"w_wing_name_txt")
        self.w_wing_name_txt.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.w_wing_name_txt.sizePolicy().hasHeightForWidth())
        self.w_wing_name_txt.setSizePolicy(sizePolicy2)
        self.w_wing_name_txt.setMinimumSize(QSize(180, 25))
        self.w_wing_name_txt.setMaximumSize(QSize(150, 25))
        self.w_wing_name_txt.setFont(font2)
        self.w_wing_name_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_19.addWidget(self.w_wing_name_txt, 4, 1, 1, 1)

        self.label_39 = QLabel(self.frame_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_19.addWidget(self.label_39, 4, 0, 1, 1)

        self.label_38 = QLabel(self.frame_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_19.addWidget(self.label_38, 5, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_19.addWidget(self.frame_19, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_15, 0, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_15, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_tmp)
        self.page_society_notice = QWidget()
        self.page_society_notice.setObjectName(u"page_society_notice")
        self.page_society_notice.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_11 = QGridLayout(self.page_society_notice)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lab_cloud_main = QLabel(self.page_society_notice)
        self.lab_cloud_main.setObjectName(u"lab_cloud_main")
        self.lab_cloud_main.setMinimumSize(QSize(0, 55))
        self.lab_cloud_main.setMaximumSize(QSize(16777215, 55))
        self.lab_cloud_main.setFont(font1)
        self.lab_cloud_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.gridLayout_11.addWidget(self.lab_cloud_main, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page_society_notice)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 235))
        self.frame_2.setFont(font2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(15)
        self.gridLayout_9.setContentsMargins(50, -1, -1, -1)
        self.wh_clear_btn = QPushButton(self.frame_5)
        self.wh_clear_btn.setObjectName(u"wh_clear_btn")
        self.wh_clear_btn.setMinimumSize(QSize(69, 25))
        self.wh_clear_btn.setMaximumSize(QSize(69, 25))
        self.wh_clear_btn.setFont(font2)
        self.wh_clear_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_9.addWidget(self.wh_clear_btn, 0, 0, 1, 1)

        self.wh_send_btn = QPushButton(self.frame_5)
        self.wh_send_btn.setObjectName(u"wh_send_btn")
        self.wh_send_btn.setEnabled(True)
        self.wh_send_btn.setMinimumSize(QSize(90, 25))
        self.wh_send_btn.setMaximumSize(QSize(80, 25))
        self.wh_send_btn.setFont(font2)
        self.wh_send_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_9.addWidget(self.wh_send_btn, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_5, 3, 3, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)

        self.wh_msg_id_txt = QLineEdit(self.frame_2)
        self.wh_msg_id_txt.setObjectName(u"wh_msg_id_txt")
        self.wh_msg_id_txt.setEnabled(False)
        self.wh_msg_id_txt.setMinimumSize(QSize(150, 25))
        self.wh_msg_id_txt.setMaximumSize(QSize(100, 25))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Light")
        font6.setPointSize(12)
        self.wh_msg_id_txt.setFont(font6)
        self.wh_msg_id_txt.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.wh_msg_id_txt, 0, 3, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.wh_msg_txt = QPlainTextEdit(self.frame_2)
        self.wh_msg_txt.setObjectName(u"wh_msg_txt")
        self.wh_msg_txt.setMinimumSize(QSize(300, 200))
        self.wh_msg_txt.setMaximumSize(QSize(300, 280))
        self.wh_msg_txt.setFont(font6)
        self.wh_msg_txt.setStyleSheet(u"QPlainTextEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QPlainTextEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.wh_msg_txt, 2, 3, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 5, 1, 1)

        self.vert_divide_2 = QFrame(self.frame_2)
        self.vert_divide_2.setObjectName(u"vert_divide_2")
        self.vert_divide_2.setMaximumSize(QSize(100, 290))
        self.vert_divide_2.setFrameShape(QFrame.VLine)
        self.vert_divide_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.vert_divide_2, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 3, 1, 1)


        self.gridLayout_11.addWidget(self.frame_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_society_notice)
        self.page_complaint_forum = QWidget()
        self.page_complaint_forum.setObjectName(u"page_complaint_forum")
        self.page_complaint_forum.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_5 = QVBoxLayout(self.page_complaint_forum)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lab_about_home_2 = QLabel(self.page_complaint_forum)
        self.lab_about_home_2.setObjectName(u"lab_about_home_2")
        self.lab_about_home_2.setMinimumSize(QSize(0, 55))
        self.lab_about_home_2.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home_2.setFont(font1)
        self.lab_about_home_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_5.addWidget(self.lab_about_home_2)

        self.frame_11 = QFrame(self.page_complaint_forum)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 110, 331, 101))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Light")
        font7.setPointSize(24)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color:rgb(255,255,255);")
        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 130, 91, 61))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/1x/icons8_wrench_180px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon13)
        self.pushButton.setIconSize(QSize(70, 70))
        self.pushButton.raise_()
        self.label_3.raise_()

        self.verticalLayout_5.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_complaint_forum)
        self.page_brochure = QWidget()
        self.page_brochure.setObjectName(u"page_brochure")
        self.page_brochure.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_brochure)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_brochure)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.gridLayout_10 = QGridLayout(self.frame_home_main)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName(u"lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 55))
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semilight")
        font8.setPointSize(24)
        self.lab_home_main_hed.setFont(font8)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.RichText)

        self.gridLayout_10.addWidget(self.lab_home_main_hed, 0, 0, 1, 1)

        self.lab_home_main_disc = QLabel(self.frame_home_main)
        self.lab_home_main_disc.setObjectName(u"lab_home_main_disc")
        self.lab_home_main_disc.setFont(font4)
        self.lab_home_main_disc.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_home_main_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lab_home_main_disc.setWordWrap(True)
        self.lab_home_main_disc.setMargin(5)

        self.gridLayout_10.addWidget(self.lab_home_main_disc, 1, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_brochure)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_brochure)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.lab_home_stat_hed = QLabel(self.frame_home_stat)
        self.lab_home_stat_hed.setObjectName(u"lab_home_stat_hed")
        self.lab_home_stat_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_stat_hed.setMaximumSize(QSize(16777215, 55))
        self.lab_home_stat_hed.setFont(font8)
        self.lab_home_stat_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_stat_hed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lab_home_stat_hed)

        self.lab_home_stat_disc = QLabel(self.frame_home_stat)
        self.lab_home_stat_disc.setObjectName(u"lab_home_stat_disc")
        self.lab_home_stat_disc.setFont(font4)
        self.lab_home_stat_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.lab_home_stat_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_brochure)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font9)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.navigation_txt = QLabel(self.frame_tab)
        self.navigation_txt.setObjectName(u"navigation_txt")
        font10 = QFont()
        font10.setFamily(u"Segoe UI Light")
        font10.setPointSize(10)
        self.navigation_txt.setFont(font10)
        self.navigation_txt.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.navigation_txt)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_home.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">User8455</span></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_manage_society.setToolTip(QCoreApplication.translate("MainWindow", u"Manage Society ", None))
#endif // QT_CONFIG(tooltip)
        self.bn_manage_society.setText("")
#if QT_CONFIG(tooltip)
        self.bn_whatsapp_notice.setToolTip(QCoreApplication.translate("MainWindow", u"Notice", None))
#endif // QT_CONFIG(tooltip)
        self.bn_whatsapp_notice.setText("")
#if QT_CONFIG(tooltip)
        self.bn_complaint_forum.setToolTip(QCoreApplication.translate("MainWindow", u"Complaint", None))
#endif // QT_CONFIG(tooltip)
        self.bn_complaint_forum.setText("")
#if QT_CONFIG(tooltip)
        self.bn_about.setToolTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(tooltip)
        self.bn_about.setText("")
#if QT_CONFIG(tooltip)
        self.sub_btn_owner.setToolTip(QCoreApplication.translate("MainWindow", u"Owner", None))
#endif // QT_CONFIG(tooltip)
        self.sub_btn_owner.setText("")
#if QT_CONFIG(tooltip)
        self.sub_btn_staff.setToolTip(QCoreApplication.translate("MainWindow", u"Staff", None))
#endif // QT_CONFIG(tooltip)
        self.sub_btn_staff.setText("")
#if QT_CONFIG(tooltip)
        self.sub_btn_member.setToolTip(QCoreApplication.translate("MainWindow", u"Add Member", None))
#endif // QT_CONFIG(tooltip)
        self.sub_btn_member.setText("")
#if QT_CONFIG(tooltip)
        self.sub_btn_vehicle.setToolTip(QCoreApplication.translate("MainWindow", u"Add Vehicle", None))
#endif // QT_CONFIG(tooltip)
        self.sub_btn_vehicle.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Owner Registration", None))
        self.o_male_radio.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.o_female_radio.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.o_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.o_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.o_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.o_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.lab_person_icon_4.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Marital Status:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Wing:", None))
        self.o_pwd_txt.setText("")
        self.o_pwd_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.o_phno_txt.setText("")
        self.o_phno_txt.setPlaceholderText("")
        self.o_marital_combo.setItemText(0, "")
        self.o_marital_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Married", None))
        self.o_marital_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Unmarried", None))

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Whatsapp No:", None))
        self.o_owner_id_txt.setText("")
        self.o_owner_id_txt.setPlaceholderText("")
        self.o_generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.o_curr_owners_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Current Owners: ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Owner ID: ", None))
        self.o_status_lbl.setText(QCoreApplication.translate("MainWindow", u"Status: Not Registered", None))
        self.o_owner_name_txt.setText("")
        self.o_owner_name_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Middle Last", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.o_uname_txt.setText("")
        self.o_uname_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gender: ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Flat No:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Member Name: ", None))
        self.o_flat_no_combo.setItemText(0, "")
        self.o_flat_no_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Married", None))
        self.o_flat_no_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Unmarried", None))

        self.o_wing_combo.setItemText(0, "")
        self.o_wing_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Married", None))
        self.o_wing_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Unmarried", None))

        self.o_start_videocam_btn.setText(QCoreApplication.translate("MainWindow", u"Start VideoCam", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Manage Staff ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Staff Name: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gender: ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Marital Status:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.lab_person_icon_2.setText("")
        self.s_phno_txt.setText("")
        self.s_phno_txt.setPlaceholderText("")
        self.s_marital_combo.setItemText(0, "")
        self.s_marital_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Married", None))
        self.s_marital_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Unmarried", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Whatsapp No:", None))
        self.s_staff_id_txt.setText("")
        self.s_staff_id_txt.setPlaceholderText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Current Staff: ", None))
        self.s_status_lbl.setText(QCoreApplication.translate("MainWindow", u"Status: Not Registered", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Staff ID: ", None))
        self.s_staff_name_txt.setText("")
        self.s_staff_name_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Middle Last", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.s_male_radio.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.s_female_radio.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.s_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.s_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.s_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.s_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.s_position_combo.setItemText(0, "")
        self.s_position_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"VIP", None))
        self.s_position_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Manager", None))
        self.s_position_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Security Guard", None))
        self.s_position_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Laundry", None))
        self.s_position_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"Electrician", None))
        self.s_position_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"Plumber", None))
        self.s_position_combo.setItemText(7, QCoreApplication.translate("MainWindow", u"Maintainence ", None))
        self.s_position_combo.setItemText(8, QCoreApplication.translate("MainWindow", u"Janitor", None))

        self.s_start_videocam_btn.setText(QCoreApplication.translate("MainWindow", u"Start VideoCam", None))
        self.s_curr_staff_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"Members Registration", None))
        self.lab_person_icon.setText("")
        self.m_male_radio.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.m_female_radio.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.m_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.m_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.m_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.m_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.m_email_txt.setText("")
        self.m_email_txt.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ph:", None))
        self.m_start_videocam_btn.setText(QCoreApplication.translate("MainWindow", u"Start VideoCam", None))
        self.m_status_lbl.setText(QCoreApplication.translate("MainWindow", u"Status: Not Registered", None))
        self.m_curr_mem_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Current Members: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gender: ", None))
        self.m_member_name_txt.setText("")
        self.m_member_name_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Middle Last", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Relation:", None))
        self.m_member_id_txt.setText("")
        self.m_member_id_txt.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Member Name: ", None))
        self.m_relation_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Member ID: ", None))
        self.lab_gamepad.setText(QCoreApplication.translate("MainWindow", u"Vehicle Registration", None))
        self.lab_person_icon_3.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Reg. No: ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Current Vehicles:", None))
        self.v_fetch_using_api_btn.setText(QCoreApplication.translate("MainWindow", u"Fetch Using API", None))
        self.v_reg_no_api_btn.setText("")
        self.v_reg_no_api_btn.setPlaceholderText("")
        self.v_curr_veh_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.v_owner_name_txt.setText("")
        self.v_owner_name_txt.setPlaceholderText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Owner Name:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.v_model_txt.setText("")
        self.v_model_txt.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Reg. Date:", None))
        self.v_rto_name_txt.setText("")
        self.v_rto_name_txt.setPlaceholderText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RTO Name:", None))
        self.v_reg_date_txt.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Reg. No:", None))
        self.v_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.v_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.v_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.v_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"Manage Society Wings", None))
        self.label_29.setText("")
        self.w_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.w_add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.w_tot_flats_txt.setText("")
        self.w_tot_flats_txt.setPlaceholderText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"ADD NEW WING:", None))
        self.w_wing_name_txt.setText("")
        self.w_wing_name_txt.setPlaceholderText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Wing Name: ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Total Flats:", None))
        self.lab_cloud_main.setText(QCoreApplication.translate("MainWindow", u"Society Notice", None))
        self.wh_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.wh_send_btn.setText(QCoreApplication.translate("MainWindow", u"Brodcast", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Message ID :", None))
        self.lab_about_home_2.setText(QCoreApplication.translate("MainWindow", u"Society Complaint Forum", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Under Maintainence", None))
        self.pushButton.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Society Brochure</span></p></body></html>", None))
        self.lab_home_main_disc.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Name:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Age:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /"
                        "></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Adress:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Managememt :Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum i"
                        "ure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</span></p></body></html>", None))
        self.lab_home_stat_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Stat </span></p></body></html>", None))
        self.lab_home_stat_disc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Weather: Rainy<br/>Skys: Cloudy<br/>Wind: blowing Fast<br/>Temperature: 32 Degree Celcious</span></p></body></html>", None))
        self.navigation_txt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

