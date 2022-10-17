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
from manager_page_window import Ui_MainWindow as manager_page_ui
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel

class Manager_Page_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Manager_Page_Window , self).__init__()
        self.ui = manager_page_ui()
        self.ui.setupUi(self)
        self.setWindowTitle("Manager_Page_Window")
        self.button_db_dict = { "pushButton_morning_1" : "Morning_1" , "pushButton_afternoon_1" : "Afternoon_1" , "pushButton_morning_2" : "Morning_2" , "pushButton_afternoon_2" : "Afternoon_2" , "pushButton_morning_3" : "Morning_3" , "pushButton_afternoon_3" : "Afternoon_3" , "pushButton_morning_4" : "Morning_4" , "pushButton_afternoon_4" : "Afternoon_4" , "pushButton_morning_5" : "Morning_5" , "pushButton_afternoon_5" : "Afternoon_5" }
        self.month_dict = { "1" : "January" , "2" : "February" , "3" : "March" , "4" : "April" , "5" : "May" , "6" : "June" , "7": "July", "8" : "August" , "9" : "September" , "10" : "Octobor" , "11" : "November" , "12" : "December" } 
        self.ui.pushButton_run.clicked.connect(self.run)
        self.ui.pushButton_salary_run.clicked.connect(self.salary_run)
        self.ui.pushButton_save.clicked.connect(self.save)
        self.ui.pushButton_morning_1.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_morning_1 ) )
        self.ui.pushButton_afternoon_1.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_afternoon_1 ) )
        self.ui.pushButton_morning_2.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_morning_2 ) )
        self.ui.pushButton_afternoon_2.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_afternoon_2) )
        self.ui.pushButton_morning_3.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_morning_3 ) )
        self.ui.pushButton_afternoon_3.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_afternoon_3 ) )
        self.ui.pushButton_morning_4.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_morning_4 ) )
        self.ui.pushButton_afternoon_4.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_afternoon_4 ) )
        self.ui.pushButton_morning_5.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_morning_5 ) )
        self.ui.pushButton_afternoon_5.clicked.connect( lambda:self.schedule_by_manager( self.ui.pushButton_afternoon_5 ) )
        for i in range(12):
            self.ui.comboBox.insertItem(i , self.month_dict[str(i+1)])
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_index_change)
    def save(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.db_info.transaction()
        cur_row = self.ui.tableView.currentIndex().row()
        cur_col = self.ui.tableView.currentIndex().column()
        #print(self.model.index(cur_row,cur_col).data())
        self.model.setData(self.model.index(cur_row,cur_col),self.model.index(cur_row,cur_col).data())
        if self.model.submitAll():
            self.db_info.commit()
            #print('111')
    def salary_run(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        user_input = self.ui.textEdit_salary_query.toPlainText()
        self.query.exec("{}".format(user_input))
        print(self.query.next())
        self.model.select() 
    def run(self):
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite') 
        self.db_info.open() 
        self.query = QSqlQuery()
        user_input = self.ui.textEdit_query.toPlainText()
        self.query.exec("{}".format(user_input))
        print(self.query.next())
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
    def set_message(self):
        
        self.db_info = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db_info.setDatabaseName('DB.sqlite')             
        self.db_info.open() 
        self.query = QSqlQuery()
        self.query.exec("Create Table Schedule (Month varchar(20) , Morning_1 varchar(20) ,Afternoon_1 varchar(20) , Morning_2 varchar(20) , Afternoon_2 varchar(20) , Morning_3 varchar(20) , Afternoon_3 varchar(20) , Morning_4 varchar(20) , Afternoon_4 varchar(20) , Morning_5 varchar(20) , Afternoon_5 varchar(20) )")
        self.query.exec("Select * From Schedule")
        if not self.query.next():
            for i in range(12):
                self.query.exec("Insert Into Schedule (Month , Morning_1,Afternoon_1,Morning_2,Afternoon_2,Morning_3,Afternoon_3,Morning_4,Afternoon_4,Morning_5,Afternoon_5)""VALUES('{}','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody','Nobody')".format(self.month_dict[str(i+1)]) )
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
        
        
        
       
        self.model = QSqlTableModel()
        self.model.setTable("Salary")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit) 
        self.model.select() 
        self.ui.tableView.setModel(self.model)
    def schedule_by_manager(self,button):
        self.query = QSqlQuery()
        text, okPressed = QInputDialog.getText(self, "Input Name of Class","Name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            button.setText(text)
            self.query.exec("Update Schedule Set '{}' = '{}' Where Month = '{}' ".format(self.button_db_dict[button.objectName()],text,self.ui.comboBox.currentText() ) )
            #print(self.query.next())
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
            
        
        
        
        

