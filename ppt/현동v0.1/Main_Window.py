import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import kiwoomMain
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_main_class = uic.loadUiType("Main_Window.ui")[0]
form_Last_Day_class=uic.loadUiType("Last_Day_Window.ui")[0]
form_Today_Traiding_class=uic.loadUiType("Today_Training.ui")[0]
Increase_Volume_class=uic.loadUiType("Increase_Volume.ui")[0]




#----------------------메인 윈도우 UI <START>----------------------  
class Main_WindowClass(QMainWindow, form_main_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
    def Last_Day_Button_In_Main(self):
        self.hide()
        self.w=Last_Day_Class()
        self.w.exec()
        self.show()
        
    
    def Today_Traiding_Button_In_Main(self):
        self.hide()
        self.w=Today_Traiding_Class()
        self.w.exec()
        self.show()
        
    def Increase_Volume_Button_In_Main(self):
        self.hide()
        self.w=Today_Increase_Volume_Class()
        self.w.exec()
        self.show()
        
#----------------------메인 윈도우 UI <END>----------------------     


#----------------------전일거래량 상위 UI <START>----------------------  
class Last_Day_Class(QDialog,QWidget,form_Last_Day_class):
    def __init__(self):
        super(Last_Day_Class,self).__init__()
        self.initUi()
        self.show()
        
    def initUi(self):
        self.setupUi(self)
        
    def Back_To_Main_Button_In_Last_Day_Class(self):
        self.hide()
#----------------------전일거래량 상위 UI <END>----------------------  


#----------------------당일거래량 상위 UI <START>----------------------  
class Today_Traiding_Class(QDialog,QWidget,form_Today_Traiding_class):
    def __init__(self):
        super(Today_Traiding_Class,self).__init__()
        self.initUi()
        self.setupUi(self)
        
    def initUi(self):
        self.setupUi(self)    
        
    def Back_To_Main_Button_In_Today_Traiding_Class(self):
        self.hide()
#----------------------당일거래량 상위 UI <END>----------------------  


#----------------------거래량 급증 UI <START>----------------------  
class Today_Increase_Volume_Class(QDialog,QWidget,Increase_Volume_class):
    def __init__(self):
        super(Today_Increase_Volume_Class,self).__init__()
        self.initUi()
        self.setupUi(self)
        
    def initUi(self):
        self.setupUi(self)
    
    def Back_To_Main_Window_Button_In_Today_Increase_Volume(self):
        self.hide()
#----------------------거래량 급증 UI <END>----------------------  
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    api_con = kiwoomMain.kiwoonMain()
    state = api_con.Login()
    print(api_con.getLoginInfo())
    
    print(state)
    if state:
        #WindowClass의 인스턴스 생성
        myWindow = Main_WindowClass() 

        #프로그램 화면을 보여주는 코드
        myWindow.show()

        #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
        app.exec_()
    else:
        print("로그인 실패")