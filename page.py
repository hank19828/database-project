#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5 import QtCore, QtGui, QtWidgets ,QtSql
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
#from Ui_Main import Ui_MainWindow  #由.UI檔案生成.py檔案後，匯入建立的GUI類
from page_window import Ui_MainWindow as page_ui
from PyQt5.QtSql import QSqlDatabase,QSqlQuery




class Page_Window(QtWidgets.QMainWindow):  
 
    def __init__(self): 
        super(Page_Window, self).__init__()
        self.ui = page_ui()
        self.ui.setupUi(self)
        self.setWindowTitle('Page_Window')
        self.user_name = None
        self.password = None
        self.button_db_dict = { "pushButton_morning_1" : "Morning_1" , "pushButton_afternoon_1" : "Afternoon_1" , "pushButton_morning_2" : "Morning_2" , "pushButton_afternoon_2" : "Afternoon_2" , "pushButton_morning_3" : "Morning_3" , "pushButton_afternoon_3" : "Afternoon_3" , "pushButton_morning_4" : "Morning_4" , "pushButton_afternoon_4" : "Afternoon_4" , "pushButton_morning_5" : "Morning_5" , "pushButton_afternoon_5" : "Afternoon_5" }
        self.month_dict = { "1" : "January" , "2" : "February" , "3" : "March" , "4" : "April" , "5" : "May" , "6" : "June" , "7": "July", "8" : "August" , "9" : "September" , "10" : "Octobor" , "11" : "November" , "12" : "December" } 
        self.ui.pushButton_update.clicked.connect( self.save_edit )
        self.ui.pushButton_run.clicked.connect( self.run )
        self.ui.pushButton_run2.clicked.connect( self.run2 )
        self.ui.pushButton_inquire_1.clicked.connect( self.run3 )
        self.ui.pushButton_salary_button.clicked.connect(self.salary_inquire)
        self.ui.pushButton_morning_1.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_morning_1 ) )
        self.ui.pushButton_afternoon_1.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_afternoon_1 ) )
        self.ui.pushButton_morning_2.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_morning_2 ) )
        self.ui.pushButton_afternoon_2.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_afternoon_2) )
        self.ui.pushButton_morning_3.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_morning_3 ) )
        self.ui.pushButton_afternoon_3.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_afternoon_3 ) )
        self.ui.pushButton_morning_4.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_morning_4 ) )
        self.ui.pushButton_afternoon_4.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_afternoon_4 ) )
        self.ui.pushButton_morning_5.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_morning_5 ) )
        self.ui.pushButton_afternoon_5.clicked.connect( lambda:self.schedule_button( self.ui.pushButton_afternoon_5 ) )
        for i in range(12):
            self.ui.comboBox.insertItem(i , self.month_dict[str(i+1)])
            self.ui.comboBox_2.insertItem(i , self.month_dict[str(i+1)])
        self.ui.comboBox_2.insertItem(12,'January_Salary>30000_Count')
        self.ui.comboBox_2.insertItem(13,'January_Avg_Salary')
        self.ui.comboBox_2.insertItem(14,'January_Max_Salary')
        self.ui.comboBox_2.insertItem(15,'January_Min_Salary')
        self.ui.comboBox_2.insertItem(16,'January_Sum_Salary')
        self.ui.comboBox_2.insertItem(17,'January_40000_User')
        self.ui.comboBox_2.insertItem(18,'phone_of_40000_User')
        self.ui.comboBox_2.insertItem(19,'phone_of_NOT_40000_User')
        self.ui.comboBox_2.insertItem(20,'post_office_if_Somebody_50000_User')
        self.ui.comboBox_2.insertItem(21,'post_office_if_not_Somebody_50000_User')
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_index_change)
        
    def salary_inquire(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        if self.ui.comboBox_2.currentText()=='January':
            self.query.exec("Select January From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='February':
            self.query.exec("Select February From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='March':
            self.query.exec("Select March From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='April':
            self.query.exec("Select April From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='May':
            self.query.exec("Select May From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='June':
            self.query.exec("Select June From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='July':
            self.query.exec("Select July From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='August':
            self.query.exec("Select August From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='September':
            self.query.exec("Select September From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='October':
            self.query.exec("Select October From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='November':
            self.query.exec("Select November From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='December':
            self.query.exec("Select December From Salary Where Name='{}'".format(self.user_name))
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(self.query.value(0) )
        elif self.ui.comboBox_2.currentText()=='January_Salary>30000_Count':
            self.query.exec("Select COUNT(Name) From Salary Where January>'30000'")
            print(self.query.next())
            self.ui.textBrowser_salary_button.setText(str(self.query.value(0)) )  
        elif self.ui.comboBox_2.currentText()=='January_Avg_Salary':
            self.query.exec("Select AVG(January) From Salary")
            print(self.query.next())
            self.ui.textBrowser_salary_button.setText(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='January_Max_Salary':
            self.query.exec("Select Max(January) From Salary")
            print(self.query.next())
            self.ui.textBrowser_salary_button.setText(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='January_Min_Salary':
            self.query.exec("Select Min(January) From Salary")
            print(self.query.next())
            self.ui.textBrowser_salary_button.setText(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='January_Sum_Salary':
            self.query.exec("Select Sum(January) From Salary")
            print(self.query.next())
            self.ui.textBrowser_salary_button.setText(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='January_40000_User':
            self.query.exec("Select Name,Max(January) From Salary Group By Name HAVING Max(January)>'40000'")
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='phone_of_40000_User':
            self.query.exec("Select Phone_number From User_info Where User_name IN (Select Name From Salary Where January>'40000')")
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(str(self.query.value(0)) )
        elif self.ui.comboBox_2.currentText()=='phone_of_NOT_40000_User':
            self.query.exec("Select Phone_number From User_info Where User_name NOT IN (Select Name From Salary Where January>'40000')")
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='post_office_if_Somebody_50000_User':
            self.query.exec("Select Post_office From User_info Where EXISTS (Select * From Salary Where January>'50000')")
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(str(self.query.value(0)) ) 
        elif self.ui.comboBox_2.currentText()=='post_office_if_not_Somebody_50000_User':
            self.query.exec("Select Post_office From User_info Where NOT EXISTS (Select * From Salary Where January>'50000')")
            self.ui.textBrowser_salary_button.clear()
            while self.query.next():
                self.ui.textBrowser_salary_button.append(str(self.query.value(0)) ) 
        
            
        #self.query.exec("Select {} From Salary Where Name='{}'".format(self.ui.comboBox_2.currentText(),self.user_name))
        #print(self.query.next())
        #print('salary',self.query.value(0))
        #self.ui.textBrowser_salary_button.setText(self.query.value(0) )        
    
    def run(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        user_input = self.ui.textEdit_query.toPlainText()
        self.query.exec("{}".format(user_input))
        #print(user_input)
        self.query.exec("Select School_id , Department , Post_office , Phone_number , Name From User_info Where User_name = '{}' ".format( self.user_name ) )
        print(self.query.next())
        #print(self.query.value(0))
        self.ui.lineEdit_school_id.setText( self.query.value(0) )
        self.ui.lineEdit_department.setText( self.query.value(1) )
        self.ui.lineEdit_post_office.setText( self.query.value(2) )
        self.ui.lineEdit_phone.setText( self.query.value(3) )
        self.ui.lineEdit_name.setText( self.query.value(4) )
    def run2(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        user_input = self.ui.textEdit_query2.toPlainText()
        self.query.exec("{}".format(user_input))
        self.query.exec("Select Morning_1,Afternoon_1,Morning_2,Afternoon_2,Morning_3,Afternoon_3,Morning_4,Afternoon_4,Morning_5,Afternoon_5 From Schedule Where Month = '{}' ".format(self.ui.comboBox.currentText() ) )
        print(self.query.next())
        
        #print(self.ui.pushButton_morning_1.objectName())
        self.ui.pushButton_morning_1.setText(self.query.value(0))
        self.ui.pushButton_afternoon_1.setText(self.query.value(1))
        self.ui.pushButton_morning_2.setText(self.query.value(2))
        self.ui.pushButton_afternoon_2.setText(self.query.value(3))
        self.ui.pushButton_morning_3.setText(self.query.value(4))
        self.ui.pushButton_afternoon_3.setText(self.query.value(5))
        self.ui.pushButton_morning_4.setText(self.query.value(6))
        self.ui.pushButton_afternoon_4.setText(self.query.value(7))
        self.ui.pushButton_morning_5.setText(self.query.value(8))
        self.ui.pushButton_afternoon_5.setText(self.query.value(9))
    def run3(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        user_input = self.ui.textEdit_query_3.toPlainText()
        self.query.exec("{}".format(user_input))
        #print(self.query.next())
        #while self.query.next():
        #    print(self.query.value(0))
        self.ui.textBrowser_result.clear()
        while self.query.next():
            self.ui.textBrowser_result.append(str(self.query.value(0)))
    def get_message(self, user_name, password):
        print(user_name, password)
        self.user_name = user_name
        self.password = password
        self.ui.lineEdit_name.setText( user_name )
    def set_message(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        #get user_information
        self.query.exec("Select School_id , Department , Post_office , Phone_number , Name From User_info Where User_name = '{}' ".format( self.user_name ) )
        print(self.query.next())
        self.ui.lineEdit_school_id.setText( self.query.value(0) )
        self.ui.lineEdit_department.setText( self.query.value(1) )
        self.ui.lineEdit_post_office.setText( self.query.value(2) )
        self.ui.lineEdit_phone.setText( self.query.value(3) )
        self.ui.lineEdit_name.setText( self.query.value(4) )
        #create schedule table
        self.query.exec("Create Table Schedule (Month varchar(20) , Morning_1 varchar(20) ,Afternoon_1 varchar(20) , Morning_2 varchar(20) , Afternoon_2 varchar(20) , Morning_3 varchar(20) , Afternoon_3 varchar(20) , Morning_4 varchar(20) , Afternoon_4 varchar(20) , Morning_5 varchar(20) , Afternoon_5 varchar(20) )")
        #get shedule information
        #print(self.query.next())
        #self.query.exec("Insert Into Schedule (Morning_1) ")
        self.query.exec("Select * From Schedule")
        if not self.query.next():
            
            for i in range(12):
                self.query.exec("Insert Into Schedule (Month , Morning_1,Afternoon_1,Morning_2,Afternoon_2,Morning_3,Afternoon_3,Morning_4,Afternoon_4,Morning_5,Afternoon_5)""VALUES('{}','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody')".format(self.month_dict[str(i+1)]) )
        self.query.exec("Select Morning_1,Afternoon_1,Morning_2,Afternoon_2,Morning_3,Afternoon_3,Morning_4,Afternoon_4,Morning_5,Afternoon_5 From Schedule Where Month = '{}' ".format(self.ui.comboBox.currentText() ) )
        print(self.query.next())
        
        #print(self.ui.pushButton_morning_1.objectName())
        self.ui.pushButton_morning_1.setText(self.query.value(0))
        self.ui.pushButton_afternoon_1.setText(self.query.value(1))
        self.ui.pushButton_morning_2.setText(self.query.value(2))
        self.ui.pushButton_afternoon_2.setText(self.query.value(3))
        self.ui.pushButton_morning_3.setText(self.query.value(4))
        self.ui.pushButton_afternoon_3.setText(self.query.value(5))
        self.ui.pushButton_morning_4.setText(self.query.value(6))
        self.ui.pushButton_afternoon_4.setText(self.query.value(7))
        self.ui.pushButton_morning_5.setText(self.query.value(8))
        self.ui.pushButton_afternoon_5.setText(self.query.value(9))
        
        
        
        
    def save_edit(self):
        self.school_id = self.ui.lineEdit_school_id.text()
        self.name = self.ui.lineEdit_name.text()
        self.department = self.ui.lineEdit_department.text()
        self.phone = self.ui.lineEdit_phone.text()
        self.post_office = self.ui.lineEdit_post_office.text()
        self.query.exec("Update User_info Set School_id='{}',Department='{}',Post_office='{}',Phone_number='{}',Name='{}' Where User_name = '{}' ".format(self.school_id,self.department,self.post_office,self.phone,self.name,self.user_name ) )
        QMessageBox.about(self,'提醒','儲存成功！')
    def schedule_button(self,button):
        msgBox = QMessageBox()
        msgBox.setText("Do you want this class?")
        msgBox.setStandardButtons(QMessageBox.Yes)
        msgBox.addButton(QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        ret = msgBox.exec()
        print(self.button_db_dict[button.objectName()])
        
        if ret == QMessageBox.Yes and button.text() == 'Nobody' :
                button.setText(self.user_name)
                self.query.exec("Update Schedule Set '{}' = '{}' Where Month = '{}' ".format(self.button_db_dict[button.objectName()],self.user_name,self.ui.comboBox.currentText() ) )
                print(self.query.next())
        elif ret == QMessageBox.Yes and button.text() != self.user_name :
                QMessageBox.about(self,'警告','此班已經有人！請選擇其他時段 ')
    def comboBox_index_change(self):
        self.query = QSqlQuery()
        self.query.exec("Select Morning_1,Afternoon_1,Morning_2,Afternoon_2,Morning_3,Afternoon_3,Morning_4,Afternoon_4,Morning_5,Afternoon_5 From Schedule Where Month = '{}' ".format(self.ui.comboBox.currentText() ) )
        print(self.query.next())
        self.ui.pushButton_morning_1.setText(self.query.value(0))
        self.ui.pushButton_afternoon_1.setText(self.query.value(1))
        self.ui.pushButton_morning_2.setText(self.query.value(2))
        self.ui.pushButton_afternoon_2.setText(self.query.value(3))
        self.ui.pushButton_morning_3.setText(self.query.value(4))
        self.ui.pushButton_afternoon_3.setText(self.query.value(5))
        self.ui.pushButton_morning_4.setText(self.query.value(6))
        self.ui.pushButton_afternoon_4.setText(self.query.value(7))
        self.ui.pushButton_morning_5.setText(self.query.value(8))
        self.ui.pushButton_afternoon_5.setText(self.query.value(9))
        
                    
            
        
    
        
        
        

    
        
        
        
        
        
        
         


 


