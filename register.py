#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5 import QtCore, QtGui, QtWidgets ,QtSql
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#from Ui_Main import Ui_MainWindow  #由.UI檔案生成.py檔案後，匯入建立的GUI類
from register_window import Ui_MainWindow as register_ui
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import os
import cv2 




class Register_Window(QtWidgets.QMainWindow):  
 
    def __init__(self): 
        super(Register_Window, self).__init__()
        self.ui = register_ui()
        self.ui.setupUi(self)
        self.setWindowTitle('Register_Window')
        # 將點選事件與槽函式進行連線
        self.ui.pushButton.clicked.connect(self.get_started)
        self.ui.pushButton_run.clicked.connect(self.run)
    def run(self):
        print('hello')
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('DB.sqlite') 

        self.db.open() 
        self.query = QSqlQuery()
        user_input_1 = self.ui.input_query_1.text()
        #user_input_2 = self.ui.input_query_2.text()
        #print(type(user_input))
        self.query.exec("{}".format(user_input_1))
        print('hello',self.query.next())

    def get_started(self):
        user_name = self.ui.lineEdit.text()
        e_mail = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()
        phone_number = self.ui.lineEdit_4.text()
        
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('DB.sqlite') 

        self.db.open() 
        print(self.db.open() )
        self.query = QSqlQuery()
        self.query.exec("Create Table User_info (User_name varchar(20) NOT NULL,Password varchar(20) NOT NULL, Email varchar(30) , Phone_number varchar(20) , Name varchar(30) , School_id varchar(30) , Department varchar(30) , Post_office varchar(30) )")
        self.query.exec("Create Table Salary (Name varchar(20) , January varchar(20) ,February varchar(20) , March varchar(20) , April varchar(20) , May varchar(20) , June varchar(20) , July varchar(20) , August varchar(20) , September varchar(20) , Octobor varchar(20) , November varchar(20) , December varchar(20))")
        
        
        print(self.query.next())
        self.query.exec("Select User_name From User_info Where User_name = '{}'".format(user_name) )
        print(self.query.next())
        if not self.query.next():
            self.query.exec("Insert Into User_info (User_name,Password,Email,Phone_number)""VALUES('{}','{}','{}','{}')".format(user_name,password,e_mail,phone_number) )
            print(self.query.next())
            self.query.exec("Insert Into Salary (Name,January,February,March,April,May,June,July,August,September,Octobor,November,December) VALUES('{}','0','0','0','0','0','0','0','0','0','0','0','0')".format(user_name ))
            QMessageBox.about(self,'提醒','註冊成功！')

            self.close()

        else :
            QMessageBox.about(self,'提醒','使用者名稱已存在，請從新輸入。')
        
        
        
        
        #result = self.query.exec_("SELECT * FROM record")
        self.db.close()
        QSqlDatabase.removeDatabase("QSQLITE")
        #query = QtSql.QSqlQuery() 
        
        #query = QSqlQuery("SELECT * FROM record ")
        #print(result)
         




