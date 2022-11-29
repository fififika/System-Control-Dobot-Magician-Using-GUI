import threading
import DobotDllType as dType
import kivy
import math
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.screen import Screen
from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.lang import Builder
Window.size = (850, 580)
KV = '''
MDFloatLayout:
    MDSwitch:
        pos_hint: {'center_x': .92, 'center_y': .15}
        on_active: app.kompresor(self, self.active)
        size_hint: 0.05, 0.1
'''
# _koordinatan niali dan entry nilai
nilai_x = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,408))
nilai_y = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,358))
nilai_z = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,308))
nilai_r = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,258))
nilai_j1 = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,179))
nilai_j2 = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,129))
nilai_j3 = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,79))
nilai_j4 = TextInput(text='', size_hint=(0.08, 0.05),pos=(205,29))
label_1 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-90),font_size=13, color='black')
label_2 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-110),font_size=13, color='black')
label_3 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-130),font_size=13, color='black')
label_4 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-150),font_size=13, color='black')
label_5 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-170),font_size=13, color='black')
label_6 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-190),font_size=13, color='black')
label_7 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-210),font_size=13, color='black')
label_8 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-230),font_size=13, color='black')
label_9 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-250),font_size=13, color='black')
label_10 = Label(text="0, 0, 0, 0 ; 0",pos =(80,-270),font_size=13, color='black')
label_11 = Label(text='1. ', pos=(-15,-90),font_size=13, color='black')
label_12 = Label(text='2. ', pos=(-15,-110),font_size=13, color='black')
label_13 = Label(text='3. ', pos=(-15,-130),font_size=13, color='black')
label_14 = Label(text='4. ', pos=(-15,-150),font_size=13, color='black')
label_15 = Label(text='5. ', pos=(-15,-170),font_size=13, color='black')
label_16 = Label(text='6. ', pos=(-15,-190),font_size=13, color='black')
label_17 = Label(text='7. ', pos=(-15,-210),font_size=13, color='black')
label_18 = Label(text='8. ', pos=(-15,-230),font_size=13, color='black')
label_19 = Label(text='9. ', pos=(-15,-250),font_size=13, color='black')
label_20 = Label(text='10. ', pos=(-15,-270),font_size=13, color='black')
label26 = Label(text='Antrean', pos=(0,-70),font_size=14,color='black',halign="left")
x_koordinat = 0
y_koordinat = 0
z_koordinat = 0
r_koordinat = 0
for_rec_X=0
for_rec_Y=0
for_rec_Z=0
for_rec_R=0
L1 = 138
L2 = 135
L3 = 147
L4 = 61
J1kin = 0
J2kin = 0
J3kin = 0
J4kin = 0
J1_akhir = 0
J2_akhir = 0
J3_akhir = 0
J4_akhir = 0
J4 =0
i = 0
for_rec_kompresor = 0
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
#Load Dll and get the CDLL object
api = dType.load()
#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])
if (state == dType.DobotConnect.DobotConnect_NoError):
    dType.SetHOMECmd(api, temp = 0, isQueued = 1) # kalibrasi
    dType.SetPTPCmdEx(api, 4, 35,  0, 0, 0) # move on joint
    class MainApp(MDApp):
        global J1_akhir
        global J2_akhir
        global J3_akhir
        global x_koordinat
        global y_koordinat
        global z_koordinat
        global for_rec_X
        global for_rec_Y
        global for_rec_Z
        global for_rec_R
        global L1
        global L2
        global L3
        global L4
        def build(self):
            screen = Screen()
            image1 = Image(source ='unp.png', pos_hint = {'center_x': 0.85, 'center_y': 0.62})
            label1 = Label(text="       IMPLEMENTASI GRAPHICAL USER INTERFACE (GUI)\nUNTUK SISTEM KONTROL ROBOT LENGAN MENGGUNAKAN\n                      BAHASA PEMROGRAMAN PYTHON", 
                        pos_hint = {'center_x': 0.5, 'center_y': 0.93}, color='black', font_size=16) 
            label2 = Label(text="Koordinat", 
                        pos_hint = {'center_x': 0.095, 'center_y': 0.8}, color='black', font_size=16)
            label3 = Label(text="Angular  ", 
                        pos_hint = {'center_x': 0.075, 'center_y': 0.4}, color='black', font_size=16)
            label22 = Label(text="Nama : Rafika Silfia", 
                        pos_hint = {'center_x': 0.85, 'center_y': 0.45},font_size=14, color='black')
            label23 = Label(text="NIM  : 18130070", 
                        pos_hint = {'center_x': 0.85, 'center_y': 0.40},font_size=14, color='black')
            label24 = Label(text="Dosen Pembimbing : Risfendra, Ph.D", 
                        pos_hint = {'center_x': 0.85, 'center_y': 0.35},font_size=14, color='black')
            label25 = Label(text="Suction Cup",
                        pos_hint = {'center_x': 0.8, 'center_y': 0.15},font_size=14, color='black' )
            label27 = Label(text="(mm)",
                        pos_hint = {'center_x': 0.28, 'center_y': 0.8},font_size=14, color='black' )
            label28 = Label(text="(°)",
                        pos_hint = {'center_x': 0.28, 'center_y': 0.4},font_size=14, color='black' )
            #button koordinat
            button1 = MDRectangleFlatButton(text =' X+ ', pos = (10, 405), on_press = self.xplus)
            button2 = MDRectangleFlatButton(text =' X- ', pos = (102, 405), on_press = self.xmin)
            button3 = MDRectangleFlatButton(text =' Y+ ', pos = (10, 355), on_press = self.yplus)
            button4 = MDRectangleFlatButton(text =' Y- ', pos = (102, 355), on_press = self.ymin)
            button5 = MDRectangleFlatButton(text =' Z+ ', pos = (10, 305), on_press = self.zplus)
            button6 = MDRectangleFlatButton(text =' Z- ', pos = (102, 305), on_press = self.zmin)
            button7 = MDRectangleFlatButton(text =' R+ ', pos = (10, 255), on_press = self.rplus)
            button8 = MDRectangleFlatButton(text =' R- ', pos = (102, 255), on_press = self.rmin)
            #button joint
            button9 = MDRectangleFlatButton(text =' J1+ ', pos = (10, 175), on_press = self.j1plus)
            button10 = MDRectangleFlatButton(text =' J1- ', pos = (102,175), on_press = self.j1min)
            button11 = MDRectangleFlatButton(text =' J2+ ', pos = (10, 125), on_press = self.j2plus)
            button12 = MDRectangleFlatButton(text =' J2- ', pos = (102, 125), on_press = self.j2min)
            button13 = MDRectangleFlatButton(text =' J3+ ', pos = (10, 75), on_press = self.j3plus)
            button14 = MDRectangleFlatButton(text =' J3- ', pos = (102, 75), on_press = self.j3min)
            button15 = MDRectangleFlatButton(text =' J4+ ', pos = (10, 25), on_press = self.j4plus)
            button16 = MDRectangleFlatButton(text =' J4- ', pos = (102, 25), on_press = self.j4min)
            button17 = MDRectangleFlatButton(text ='RESET', pos = (625, 120), on_press = self.reset)
            button24 = MDRectangleFlatButton(text='KALIBRASI',pos=(725, 120), on_press = self.kalibrasi)
            button18 = MDRectangleFlatButton(text='S\n\nE\n\nN\n\nD', pos=(285,257), size_hint=(0.01, 0.315), on_press = self.entry_inverse)
            button19 = MDRectangleFlatButton(text='S\n\nE\n\nN\n\nD', pos=(285,28), size_hint=(0.01, 0.315), on_press = self.entry_forward)
            button20 = MDRectangleFlatButton(text='REFRESH', pos=(390, 398), size_hint=(0.15, 0.07), on_press = self.refresh)
            button21 = MDRectangleFlatButton(text='RECORD', pos=(390, 348), size_hint=(0.15, 0.07), on_press = self.record)
            button22 = MDRectangleFlatButton(text='CLEAR', pos=(390, 298), size_hint=(0.15, 0.07), on_press = self.clear_record)
            button23 = MDRectangleFlatButton(text='PLAYBACK', pos=(390, 248), size_hint=(0.15, 0.07), on_press = self.playback)
            sc = Builder.load_string(KV)
            screen.add_widget(sc)
            screen.add_widget(image1)
            screen.add_widget(label1)
            screen.add_widget(label2)
            screen.add_widget(label3)
            screen.add_widget(label22)
            screen.add_widget(label23)
            screen.add_widget(label24)
            screen.add_widget(label25)
            screen.add_widget(label26)
            screen.add_widget(label27)
            screen.add_widget(label28)
            screen.add_widget(label_1)
            screen.add_widget(label_2)
            screen.add_widget(label_3)
            screen.add_widget(label_4)
            screen.add_widget(label_5)
            screen.add_widget(label_6)
            screen.add_widget(label_7)
            screen.add_widget(label_8)
            screen.add_widget(label_9)
            screen.add_widget(label_10)
            screen.add_widget(label_11)
            screen.add_widget(label_12)
            screen.add_widget(label_13)
            screen.add_widget(label_14)
            screen.add_widget(label_15)
            screen.add_widget(label_16)
            screen.add_widget(label_17)
            screen.add_widget(label_18)
            screen.add_widget(label_19)
            screen.add_widget(label_20)
            screen.add_widget(button1)
            screen.add_widget(button2)
            screen.add_widget(button3)
            screen.add_widget(button4)
            screen.add_widget(button5)
            screen.add_widget(button6)
            screen.add_widget(button7)
            screen.add_widget(button8)
            screen.add_widget(button9)
            screen.add_widget(button10)
            screen.add_widget(button11)
            screen.add_widget(button12)
            screen.add_widget(button13)
            screen.add_widget(button14)
            screen.add_widget(button15)
            screen.add_widget(button16)
            screen.add_widget(button17)
            screen.add_widget(button18)
            screen.add_widget(button19)
            screen.add_widget(button20)
            screen.add_widget(button21)
            screen.add_widget(button22)
            screen.add_widget(button23)
            screen.add_widget(button24)
            screen.add_widget(nilai_x)
            screen.add_widget(nilai_y)
            screen.add_widget(nilai_z)
            screen.add_widget(nilai_r)
            screen.add_widget(nilai_j1)
            screen.add_widget(nilai_j2)
            screen.add_widget(nilai_j3)
            screen.add_widget(nilai_j4)
            return screen

        def kalibrasi(self,obj):
            print('----------------------KALIBRASI------------------------')
            dType.SetHOMECmd(api, temp = 0, isQueued = 1)
            global J1
            global J2
            global J3
            global J4
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            dType.SetPTPCmdEx(api, 4, 35,  0, 0, 0) # move on joint
            J1 = dType.GetPoseEx(api, 5) # Get data joint from dobot
            J1 = J1 - 35
            J2 = dType.GetPoseEx(api, 6)
            J3 = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1)    # konversi radians ke degree
            J2kon = math.radians(J2)
            J3kon = math.radians(J3)
            J1_akhir = J1kon
            J2_akhir = J2kon
            J3_akhir = J3kon
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_aksen = (z1 - z2)
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1, ndigits=2)))
            nilai_j2.text = str(float(round(J2, ndigits=2)))
            nilai_j3.text = str(float(round(J3, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def refresh(self, obj):
            print('----------------------REFRESH------------------------')
            global J1
            global J2
            global J3
            global J4
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J1 = dType.GetPoseEx(api, 5) # Get data joint from dobot
            J1 = J1 - 35
            J2 = dType.GetPoseEx(api, 6)
            J3 = dType.GetPoseEx(api, 7)
            J4 = dType.GetPoseEx(api, 8)
            J1kon = math.radians(J1)    # konversi radians ke degree
            J2kon = math.radians(J2)
            J3kon = math.radians(J3)
            J1_akhir = J1kon
            J2_akhir = J2kon
            J3_akhir = J3kon
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1, ndigits=2)))
            nilai_j2.text = str(float(round(J2, ndigits=2)))
            nilai_j3.text = str(float(round(J3, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def reset(self, obj):
            print('----------------------RESET------------------------')
            global J1
            global J2
            global J3
            global J4
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global J4kin
            dType.SetPTPCmdEx(api, 4, 35,  0, 0, 0) # move on joint
            J1 = dType.GetPoseEx(api, 5) # Get data joint from dobot
            J1 = J1 - 35
            J2 = dType.GetPoseEx(api, 6)
            J3 = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1)    # konversi radians ke degree
            J2kon = math.radians(J2)
            J3kon = math.radians(J3)
            J1_akhir = J1kon
            J2_akhir = J2kon
            J3_akhir = J3kon
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            J4kin = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1, ndigits=2)))
            nilai_j2.text = str(float(round(J2, ndigits=2)))
            nilai_j3.text = str(float(round(J3, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def xplus(self, obj):
            print('----------------------X PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal-L4
            z_aksen = z_koordinat-L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            x_koordinat = x_koordinat + 5   # BESAR PERPINDAHAN---------------------------------------------
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir+J3b_akhir)   # J3
            J1 = J1_akhir - J1_awal     # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal     
            J3 = J3_akhir - J3_awal
            dType.SetPTPCmdEx(api,6,J1,J2,J3,0) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def xmin(self, obj):
            print('----------------------X MIN------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            x_koordinat = x_koordinat - 5      # BESAR PERPINDAHAN---------------------------------------------
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir+J3b_akhir)   # J3
            J1 = J1_akhir - J1_awal     # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal
            J3 = J3_akhir - J3_awal
            dType.SetPTPCmdEx(api,6,J1,J2,J3,0) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def yplus(self, obj):
            print('----------------------Y PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            y_koordinat = y_koordinat + 5      # BESAR PERPINDAHAN---------------------------------------------
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir+J3b_akhir)   # J3
            J1 = J1_akhir - J1_awal     # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal
            J3 = J3_akhir - J3_awal
            dType.SetPTPCmdEx(api,6,J1,J2,J3,0) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def ymin(self, obj):
            print('----------------------Y MIN------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            y_koordinat = y_koordinat - 5      # BESAR PERPINDAHAN---------------------------------------------
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir+J3b_akhir)   # J3
            J1 = J1_akhir - J1_awal # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal
            J3 = J3_akhir - J3_awal
            dType.SetPTPCmdEx(api,6,J1,J2,J3,0) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def zplus(self, obj):
            print('----------------------Z PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            z_koordinat = z_koordinat + 5   # BESAR PERPINDAHAN---------------------------------------------
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir+J3b_akhir)   # J3
            J1 = J1_akhir - J1_awal     # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal
            J3 = J3_akhir - J3_awal
            dType.SetPTPCmdEx(api,6,J1,J2,J3,0) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def zmin(self, obj):
            print('----------------------Z MIN------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            z_koordinat = z_koordinat - 5   # BESAR PERPINDAHAN---------------------------------------------
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat - L1
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir+J3b_akhir)   # J3
            J1 = J1_akhir - J1_awal     # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal
            J3 = J3_akhir - J3_awal
            dType.SetPTPCmdEx(api,6,J1,J2,J3,0) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4, ndigits=2)))

        def rplus(self, obj):
            print('----------------------R PLUS------------------------')
            global J4kin
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J4 = 0
            J4 += 1     # NILAI YANG DIJALANKAN
            J4kin += 1
            dType.SetPTPCmdEx(api,6,0,0,0,J4) # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_r.text = str(float(round(J4kin, ndigits=2)))
            nilai_j4.text = str(float(round(J4kin, ndigits=2)))

        def rmin(self, obj):
            print('----------------------R MIN------------------------')
            global J4kin
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J4 = 0
            J4 -= 1     # NILAI YANG DIJALANKAN
            J4kin -= 1
            dType.SetPTPCmdEx(api,6,0,0,0,J4) #-----------------------instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_r.text = str(float(round(J4kin, ndigits=2)))
            nilai_j4.text = str(float(round(J4kin, ndigits=2)))

        def j1plus(self, obj):
            print('----------------------J1 PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J1 = 0
            J1 += 1     # NILAI YANG DIJALANKAN
            dType.SetPTPCmdEx(api,6,J1,0,0,0) # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1_akhir)  # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))

        def j1min(self, obj):
            print('----------------------J1 MIN------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J1 = 0
            J1 -= 1     # NILAI YANG DIJALANKAN
            dType.SetPTPCmdEx(api,6,J1,0,0,0) # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1_akhir)  # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))

        def j2plus(self, obj):
            print('----------------------J2 PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J2 = 0
            J2 += 2     # NILAI YANG DIJALANKAN
            dType.SetPTPCmdEx(api,6,0,J2,0,0)       # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7) 
            J1kon = math.radians(J1_akhir)      # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))

        def j2min(self, obj):
            print('----------------------J2 MIN------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J2 = 0
            J2 -= 2     # NILAI YANG DIJALANKAN
            dType.SetPTPCmdEx(api,6,0,J2,0,0)       # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1_akhir)      # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))

        def j3plus(self, obj):
            print('----------------------J3 PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J3 = 0
            J3 += 2     # NILAI YANG DIJALANKAN
            dType.SetPTPCmdEx(api,6,0,0,J3,0)       # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7) 
            J1kon = math.radians(J1_akhir)      # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))

        def j3min(self, obj):
            print('----------------------J3 PLUS------------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J3 = 0
            J3 -= 2     # NILAI YANG DIJALANKAN
            dType.SetPTPCmdEx(api,6,0,0,J3,0)       # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1_akhir)      # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            
        def j4plus(self, obj):
            global J4kin
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J4 = 0
            J4 += 1     # NILAI YANG DI JALANKAN
            dType.SetPTPCmdEx(api,6,0,0,0,J4)   # instruksi run dobot
            J4kin += 1
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_r.text = str(float(round(J4kin, ndigits=2)))
            nilai_j4.text = str(float(round(J4kin, ndigits=2)))

        def j4min(self, obj):
            global J4kin
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            J4 = 0
            J4 -= 1 # NILAI YANG DI JALANKAN
            dType.SetPTPCmdEx(api,6,0,0,0,J4)   # instruksi run dobot
            J4kin -= 1
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_r.text = str(float(round(J4kin, ndigits=2)))
            nilai_j4.text = str(float(round(J4kin, ndigits=2)))

        def entry_inverse(self, obj):
            print('----------------------ENTRY INVERSE------------------------')
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global r_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global L1
            global L2
            global L3
            global L4
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global J4kin
            J1_awal = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat -L1
            hipotenus_awal = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_awal = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_awal = math.degrees(math.acos(((L2**2)+(hipotenus_awal**2)-(L3**2)) / (2*L2*hipotenus_awal)))
            J2_awal = 90 -(J2a_awal + J2b_awal) # J2    
            J3a_awal = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_awal**2)) / (2*L2*L3)))
            J3b_awal = 180-(90+J2_awal)
            J3_awal = 180-(J3a_awal+J3b_awal)   # J3
            print('-----------------GET ENTRY VALUE--------------------')
            x_koordinat = float(nilai_x.text) 
            y_koordinat = float(nilai_y.text)
            z_koordinat = float(nilai_z.text)
            r_koordinat_entry = float(nilai_r.text)
            J1_akhir = math.degrees(math.atan(y_koordinat/x_koordinat))  # J1
            x_diagonal = ((x_koordinat**2)+(y_koordinat**2))**(1/2)
            x_aksen = x_diagonal - L4
            z_aksen = z_koordinat - L1
            hipotenus_akhir = ((x_aksen**2)+(z_aksen**2))**(1/2)
            J2a_akhir = math.degrees(math.atan(z_aksen/x_aksen))
            J2b_akhir = math.degrees(math.acos(((L2**2)+(hipotenus_akhir**2)-(L3**2)) / (2*L2*hipotenus_akhir)))
            J2_akhir = 90 -(J2a_akhir + J2b_akhir) # J2    
            J3a_akhir = math.degrees(math.acos(((L2**2)+(L3**2)-(hipotenus_akhir**2)) / (2*L2*L3)))
            J3b_akhir = 180-(90+J2_akhir)
            J3_akhir = 180-(J3a_akhir + J3b_akhir)   # J3
            J1 = (J1_akhir - J1_awal)       # NILAI YANG AKAN DI JALANKAN
            J2 = J2_akhir - J2_awal
            J3 = J3_akhir - J3_awal
            J4 = r_koordinat_entry - J4kin
            J4kin = r_koordinat_entry
            dType.SetPTPCmdEx(api,6,J1,J2,J3,J4)     # instruksi run dobot
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(r_koordinat_entry, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(r_koordinat_entry, ndigits=2)))

        def entry_forward(self,obj):
            print('----------------------ENTRY FORWARD----------------------')
            global J1_akhir
            global J2_akhir
            global J3_akhir
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global r_koordinat
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global J4kin
            J1_entry = float(nilai_j1.text)     # GET ENTRY VALUE  
            J2_entry = float(nilai_j2.text)
            J3_entry = float(nilai_j3.text)
            J4_entry = float(nilai_j4.text)
            print('-run-')
            J1 = J1_entry - J1_akhir        # NILAI YANG AKAN DI JALANKAN
            J2 = J2_entry - J2_akhir
            J3 = J3_entry - J3_akhir
            J4 = J4_entry - J4kin
            J4kin = J4_entry
            dType.SetPTPCmdEx(api,6,J1,J2,J3,J4)      # instruksi run dobot
            J1_akhir = dType.GetPoseEx(api, 5)
            J1_akhir = J1_akhir - 35
            J2_akhir = dType.GetPoseEx(api, 6)
            J3_akhir = dType.GetPoseEx(api, 7)
            J1kon = math.radians(J1_akhir)      # konversi radians ke degree
            J2kon = math.radians(J2_akhir)
            J3kon = math.radians(J3_akhir)
            x1 = math.sin(J2kon)*L2
            x2 = math.cos(J3kon)*L3
            x_aksen = (x1 + x2) 
            x_diagonal = x_aksen + L4  
            y_koordinat = math.sin(J1kon)*x_diagonal
            x_koordinat = math.cos(J1kon)*x_diagonal
            z1 = math.cos(J2kon)*L2
            z2 = math.sin(J3kon)*L3
            z_koordinat = L1 + (z1 - z2)
            for_rec_X = dType.GetPoseEx(api, 5)
            for_rec_Y = dType.GetPoseEx(api, 6)
            for_rec_Z = dType.GetPoseEx(api, 7)
            for_rec_R = dType.GetPoseEx(api, 8)
            nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
            nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
            nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
            nilai_r.text = str(float(round(J4_entry, ndigits=2)))
            nilai_j1.text = str(float(round(J1_akhir, ndigits=2)))
            nilai_j2.text = str(float(round(J2_akhir, ndigits=2)))
            nilai_j3.text = str(float(round(J3_akhir, ndigits=2)))
            nilai_j4.text = str(float(round(J4_entry, ndigits=2)))

        def record(self,obj):
            global i
            global x_koordinat
            global y_koordinat
            global z_koordinat
            global r_koordinat
            global J1_record_1
            global J2_record_1
            global J3_record_1
            global J4_record_1
            global J1_record_2
            global J2_record_2
            global J3_record_2
            global J4_record_2
            global J1_record_3
            global J2_record_3
            global J3_record_3
            global J4_record_3
            global J1_record_4
            global J2_record_4
            global J3_record_4
            global J4_record_4
            global J1_record_5
            global J2_record_5
            global J3_record_5
            global J4_record_5
            global J1_record_6
            global J2_record_6
            global J3_record_6
            global J4_record_6
            global J1_record_7
            global J2_record_7
            global J3_record_7
            global J4_record_7
            global J1_record_8
            global J2_record_8
            global J3_record_8
            global J4_record_8
            global J1_record_9
            global J2_record_9
            global J3_record_9
            global J4_record_9
            global J1_record_10
            global J2_record_10
            global J3_record_10
            global J4_record_10
            global J1_rec_show_1
            global J2_rec_show_1
            global J3_rec_show_1
            global J4_rec_show_1
            global J1_rec_show_2
            global J2_rec_show_2
            global J3_rec_show_2
            global J4_rec_show_2
            global J1_rec_show_3
            global J2_rec_show_3
            global J3_rec_show_3
            global J4_rec_show_3
            global J1_rec_show_4
            global J2_rec_show_4
            global J3_rec_show_4
            global J4_rec_show_4
            global J1_rec_show_5
            global J2_rec_show_5
            global J3_rec_show_5
            global J4_rec_show_5
            global J1_rec_show_6
            global J2_rec_show_6
            global J3_rec_show_6
            global J4_rec_show_6
            global J1_rec_show_7
            global J2_rec_show_7
            global J3_rec_show_7
            global J4_rec_show_7
            global J1_rec_show_8
            global J2_rec_show_8
            global J3_rec_show_8
            global J4_rec_show_8
            global J1_rec_show_9
            global J2_rec_show_9
            global J3_rec_show_9
            global J4_rec_show_9
            global J1_rec_show_10
            global J2_rec_show_10
            global J3_rec_show_10
            global J4_rec_show_10
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global for_rec_R
            global for_rec_kompresor
            global rec_kompresor_1
            global rec_kompresor_2
            global rec_kompresor_3
            global rec_kompresor_4
            global rec_kompresor_5
            global rec_kompresor_6
            global rec_kompresor_7
            global rec_kompresor_8
            global rec_kompresor_9
            global rec_kompresor_10
            global kompresor_show_1
            global kompresor_show_2
            global kompresor_show_3
            global kompresor_show_4
            global kompresor_show_5
            global kompresor_show_6
            global kompresor_show_7
            global kompresor_show_8
            global kompresor_show_9
            global kompresor_show_10
            global J4kin
            print('--------rec--------')
            i += 1
            print('i=', i)
            if i == 1:
                print('--------rec_1--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_1 = for_rec_X
                J2_record_1 = for_rec_Y
                J3_record_1 = for_rec_Z
                J4_record_1 = for_rec_R
                rec_kompresor_1 = for_rec_kompresor
                J1_rec_show_1 = x_koordinat
                J2_rec_show_1 = y_koordinat
                J3_rec_show_1 = z_koordinat
                J4_rec_show_1 = J4kin
                kompresor_show_1 = for_rec_kompresor
                label_1.text = str(round(J1_rec_show_1,ndigits=2)) + str(', ') + str(round(J2_rec_show_1,ndigits=2)) + str(', ') + str(round(J3_rec_show_1,ndigits=2)) + str(', ') + str(round(J4_rec_show_1,ndigits=2)) + str(" ; ") + str(rec_kompresor_1)
            if i == 2:
                print('--------rec_2--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_2 = for_rec_X
                J2_record_2 = for_rec_Y
                J3_record_2 = for_rec_Z
                J4_record_2 = for_rec_R
                rec_kompresor_2 = for_rec_kompresor
                J1_rec_show_2 = x_koordinat
                J2_rec_show_2 = y_koordinat
                J3_rec_show_2 = z_koordinat
                J4_rec_show_2 = J4kin
                kompresor_show_2 = for_rec_kompresor 
                label_2.text = str(round(J1_rec_show_2,ndigits=2)) + str(', ') + str(round(J2_rec_show_2,ndigits=2)) + str(', ') + str(round(J3_rec_show_2,ndigits=2)) + str(', ') + str(round(J4_rec_show_2,ndigits=2)) + str(" ; ") + str(rec_kompresor_2) 
            if i == 3:
                print('--------rec_3--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_3 = for_rec_X
                J2_record_3 = for_rec_Y
                J3_record_3 = for_rec_Z
                J4_record_3 = for_rec_R
                rec_kompresor_3 = for_rec_kompresor
                J1_rec_show_3 = x_koordinat
                J2_rec_show_3 = y_koordinat
                J3_rec_show_3 = z_koordinat
                J4_rec_show_3 = J4kin
                kompresor_show_3 = for_rec_kompresor 
                label_3.text = str(round(J1_rec_show_3,ndigits=2)) + str(', ') + str(round(J2_rec_show_3,ndigits=2)) + str(', ') + str(round(J3_rec_show_3,ndigits=2)) + str(', ') + str(round(J4_rec_show_3,ndigits=2)) + str(" ; ") + str(rec_kompresor_3) 
            if i == 4:
                print('--------rec_4--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_4 = for_rec_X
                J2_record_4 = for_rec_Y
                J3_record_4 = for_rec_Z
                J4_record_4 = for_rec_R
                rec_kompresor_4 = for_rec_kompresor
                J1_rec_show_4 = x_koordinat
                J2_rec_show_4 = y_koordinat
                J3_rec_show_4 = z_koordinat
                J4_rec_show_4 = J4kin
                kompresor_show_4 = for_rec_kompresor 
                label_4.text = str(round(J1_rec_show_4,ndigits=2)) + str(', ') + str(round(J2_rec_show_4,ndigits=2)) + str(', ') + str(round(J3_rec_show_4,ndigits=2)) + str(', ') + str(round(J4_rec_show_4,ndigits=2)) + str(" ; ") + str(rec_kompresor_4) 
            if i == 5:
                print('--------rec_5--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_5 = for_rec_X
                J2_record_5 = for_rec_Y
                J3_record_5 = for_rec_Z
                J4_record_5 = for_rec_R
                rec_kompresor_5 = for_rec_kompresor
                J1_rec_show_5 = x_koordinat
                J2_rec_show_5 = y_koordinat
                J3_rec_show_5 = z_koordinat
                J4_rec_show_5 = J4kin
                kompresor_show_5 = for_rec_kompresor 
                label_5.text = str(round(J1_rec_show_5,ndigits=2)) + str(', ') + str(round(J2_rec_show_5,ndigits=2)) + str(', ') + str(round(J3_rec_show_5,ndigits=2)) + str(', ') + str(round(J4_rec_show_5,ndigits=2)) + str(" ; ") + str(rec_kompresor_5) 
            if i == 6:
                print('--------rec_6--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_6 = for_rec_X
                J2_record_6 = for_rec_Y
                J3_record_6 = for_rec_Z
                J4_record_6 = for_rec_R
                rec_kompresor_6 = for_rec_kompresor
                J1_rec_show_6 = x_koordinat
                J2_rec_show_6 = y_koordinat
                J3_rec_show_6 = z_koordinat
                J4_rec_show_6 = J4kin
                kompresor_show_6 = for_rec_kompresor 
                label_6.text = str(round(J1_rec_show_6,ndigits=2)) + str(', ') + str(round(J2_rec_show_6,ndigits=2)) + str(', ') + str(round(J3_rec_show_6,ndigits=2)) + str(', ') + str(round(J4_rec_show_6,ndigits=2)) + str(" ; ") + str(rec_kompresor_6) 
            if i == 7:
                print('--------rec_7--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_7 = for_rec_X
                J2_record_7 = for_rec_Y
                J3_record_7 = for_rec_Z
                J4_record_7 = for_rec_R
                rec_kompresor_7 = for_rec_kompresor
                J1_rec_show_7 = x_koordinat
                J2_rec_show_7 = y_koordinat
                J3_rec_show_7 = z_koordinat
                J4_rec_show_7 = J4kin
                kompresor_show_7 = for_rec_kompresor 
                label_7.text = str(round(J1_rec_show_7,ndigits=2)) + str(', ') + str(round(J2_rec_show_7,ndigits=2)) + str(', ') + str(round(J3_rec_show_7,ndigits=2)) + str(', ') + str(round(J4_rec_show_7,ndigits=2)) + str(" ; ") + str(rec_kompresor_7) 
            if i == 8:
                print('--------rec_8--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_8 = for_rec_X
                J2_record_8 = for_rec_Y
                J3_record_8 = for_rec_Z
                J4_record_8 = for_rec_R
                rec_kompresor_8 = for_rec_kompresor
                J1_rec_show_8 = x_koordinat
                J2_rec_show_8 = y_koordinat
                J3_rec_show_8 = z_koordinat
                J4_rec_show_8 = J4kin
                kompresor_show_8 = for_rec_kompresor 
                label_8.text = str(round(J1_rec_show_8,ndigits=2)) + str(', ') + str(round(J2_rec_show_8,ndigits=2)) + str(', ') + str(round(J3_rec_show_8,ndigits=2)) + str(', ') + str(round(J4_rec_show_8,ndigits=2)) + str(" ; ") + str(rec_kompresor_8) 
            if i == 9:
                print('--------rec_9--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_9 = for_rec_X
                J2_record_9 = for_rec_Y
                J3_record_9 = for_rec_Z
                J4_record_9 = for_rec_R
                rec_kompresor_9 = for_rec_kompresor
                J1_rec_show_9 = x_koordinat
                J2_rec_show_9 = y_koordinat
                J3_rec_show_9 = z_koordinat
                J4_rec_show_9 = J4kin
                kompresor_show_9 = for_rec_kompresor 
                label_9.text = str(round(J1_rec_show_9,ndigits=2)) + str(', ') + str(round(J2_rec_show_9,ndigits=2)) + str(', ') +str(round(J3_rec_show_9,ndigits=2)) + str(', ') + str(round(J4_rec_show_9,ndigits=2)) + str(" ; ") + str(rec_kompresor_9) 
            if i == 10:
                print('--------rec_10--------')
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_10 = for_rec_X
                J2_record_10 = for_rec_Y
                J3_record_10 = for_rec_Z
                J4_record_10 = for_rec_R
                rec_kompresor_10 = for_rec_kompresor
                J1_rec_show_10 = x_koordinat
                J2_rec_show_10 = y_koordinat
                J3_rec_show_10 = z_koordinat
                J4_rec_show_10 = J4kin
                kompresor_show_10 = for_rec_kompresor 
                label_10.text = str(round(J1_rec_show_10,ndigits=2)) + str(', ') + str(round(J2_rec_show_10,ndigits=2)) + str(', ') + str(round(J3_rec_show_10,ndigits=2)) + str(', ') + str(round(J4_rec_show_10,ndigits=2)) + str(" ; ") + str(rec_kompresor_10) 
            if i > 10:
                i = 10

        def clear_record(self,obj):
            global i
            global J1_record_1
            global J2_record_1
            global J3_record_1
            global J4_record_1
            global J1_record_2
            global J2_record_2
            global J3_record_2
            global J4_record_2
            global J1_record_3
            global J2_record_3
            global J3_record_3
            global J4_record_3
            global J1_record_4
            global J2_record_4
            global J3_record_4
            global J4_record_4
            global J1_record_5
            global J2_record_5
            global J3_record_5
            global J4_record_5
            global J1_record_6
            global J2_record_6
            global J3_record_6
            global J4_record_6
            global J1_record_7
            global J2_record_7
            global J3_record_7
            global J4_record_7
            global J1_record_8
            global J2_record_8
            global J3_record_8
            global J4_record_8
            global J1_record_9
            global J2_record_9
            global J3_record_9
            global J4_record_9
            global J1_record_10
            global J2_record_10
            global J3_record_10
            global J4_record_10
            global J1_rec_show_1
            global J2_rec_show_1
            global J3_rec_show_1
            global J4_rec_show_1
            global J1_rec_show_2
            global J2_rec_show_2
            global J3_rec_show_2
            global J4_rec_show_2
            global J1_rec_show_3
            global J2_rec_show_3
            global J3_rec_show_3
            global J4_rec_show_3
            global J1_rec_show_4
            global J2_rec_show_4
            global J3_rec_show_4
            global J4_rec_show_4
            global J1_rec_show_5
            global J2_rec_show_5
            global J3_rec_show_5
            global J4_rec_show_5
            global J1_rec_show_6
            global J2_rec_show_6
            global J3_rec_show_6
            global J4_rec_show_6
            global J1_rec_show_7
            global J2_rec_show_7
            global J3_rec_show_7
            global J4_rec_show_7
            global J1_rec_show_8
            global J2_rec_show_8
            global J3_rec_show_8
            global J4_rec_show_8
            global J1_rec_show_9
            global J2_rec_show_9
            global J3_rec_show_9
            global J4_rec_show_9
            global J1_rec_show_10
            global J2_rec_show_10
            global J3_rec_show_10
            global J4_rec_show_10
            global for_rec_X
            global for_rec_Y
            global for_rec_Z
            global rec_kompresor_1
            global rec_kompresor_2
            global rec_kompresor_3
            global rec_kompresor_4
            global rec_kompresor_5
            global rec_kompresor_6
            global rec_kompresor_7
            global rec_kompresor_8
            global rec_kompresor_9
            global rec_kompresor_10
            global kompresor_show_1
            global kompresor_show_2
            global kompresor_show_3
            global kompresor_show_4
            global kompresor_show_5
            global kompresor_show_6
            global kompresor_show_7
            global kompresor_show_8
            global kompresor_show_9
            global kompresor_show_10
            i -= 1
            print('i= ',i)
            if i == 0:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_1 = 0
                J2_record_1 = 0
                J3_record_1 = 0 
                J4_record_1 = 0
                rec_kompresor_1 = 0
                J1_rec_show_1 = 0
                J2_rec_show_1 = 0
                J3_rec_show_1 = 0 
                J4_rec_show_1 = 0
                kompresor_show_1 = 0
                label_1.text = str(round(J1_rec_show_1,ndigits=2)) + str(', ') + str(round(J2_rec_show_1,ndigits=2)) + str(', ') + str(round(J3_rec_show_1,ndigits=2)) + str(", ") + str(round(J4_rec_show_1,ndigits=2)) + str(" ; ") + str(rec_kompresor_1)
            if i == 1:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_2 = 0
                J2_record_2 = 0
                J3_record_2 = 0 
                J4_record_2 = 0
                rec_kompresor_2 = 0
                J1_rec_show_2 = 0
                J2_rec_show_2 = 0
                J3_rec_show_2 = 0 
                J4_rec_show_2 = 0
                kompresor_show_2 = 0
                label_2.text = str(round(J1_rec_show_2,ndigits=2)) + str(', ') + str(round(J2_rec_show_2,ndigits=2)) + str(', ') + str(round(J3_rec_show_2,ndigits=2)) + str(", ") + str(round(J4_rec_show_2,ndigits=2)) + str(" ; ") + str(rec_kompresor_2) 
            if i == 2:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_3 = 0
                J2_record_3 = 0
                J3_record_3 = 0 
                J4_record_3 = 0
                rec_kompresor_3 = 0
                J1_rec_show_3 = 0
                J2_rec_show_3 = 0
                J3_rec_show_3 = 0 
                J4_rec_show_3 = 0
                kompresor_show_3 = 0
                label_3.text = str(round(J1_rec_show_3,ndigits=2)) + str(', ') + str(round(J2_rec_show_3,ndigits=2)) + str(', ') + str(round(J3_rec_show_3,ndigits=2)) + str(", ") + str(round(J4_rec_show_3,ndigits=2)) + str(" ; ") + str(rec_kompresor_3)
            if i == 3:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_4 = 0
                J2_record_4 = 0
                J3_record_4 = 0 
                J3_record_4 = 0
                J4_record_4 = 0
                rec_kompresor_4 = 0
                J1_rec_show_4 = 0
                J2_rec_show_4 = 0
                J3_rec_show_4 = 0 
                J4_rec_show_4 = 0
                kompresor_show_4 = 0
                label_4.text = str(round(J1_rec_show_4,ndigits=2)) + str(', ') + str(round(J2_rec_show_4,ndigits=2)) + str(', ') + str(round(J3_rec_show_4,ndigits=2)) + str(", ") + str(round(J4_rec_show_4,ndigits=2)) + str(" ; ") + str(rec_kompresor_4) 
            if i == 4:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_5 = 0
                J2_record_5 = 0
                J3_record_5 = 0 
                J4_record_5 = 0
                rec_kompresor_5 = 0
                J1_rec_show_5 = 0
                J2_rec_show_5 = 0
                J3_rec_show_5 = 0 
                J4_rec_show_5 = 0
                kompresor_show_5 = 0
                label_5.text = str(round(J1_rec_show_5,ndigits=2)) + str(', ') + str(round(J2_rec_show_5,ndigits=2)) + str(', ') + str(round(J3_rec_show_5,ndigits=2)) + str(", ") + str(round(J4_rec_show_5,ndigits=2)) + str(" ; ") + str(rec_kompresor_5)
            if i == 5:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_6 = 0
                J2_record_6 = 0
                J3_record_6 = 0 
                J4_record_6 = 0
                rec_kompresor_6 = 0
                J1_rec_show_6 = 0
                J2_rec_show_6 = 0
                J3_rec_show_6 = 0 
                J4_rec_show_6 = 0
                kompresor_show_6 = 0
                label_6.text = str(round(J1_rec_show_6,ndigits=2)) + str(', ') + str(round(J2_rec_show_6,ndigits=2)) + str(', ') + str(round(J3_rec_show_6,ndigits=2)) + str(", ") + str(round(J4_rec_show_6,ndigits=2)) + str(" ; ") + str(rec_kompresor_6)
            if i == 6:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_7 = 0
                J2_record_7 = 0
                J3_record_7 = 0 
                J4_record_7 = 0
                rec_kompresor_7 = 0
                J1_rec_show_7 = 0
                J2_rec_show_7 = 0
                J3_rec_show_7 = 0 
                J4_rec_show_7 = 0
                kompresor_show_7 = 0
                label_7.text = str(round(J1_rec_show_7,ndigits=2)) + str(', ') + str(round(J2_rec_show_7,ndigits=2)) + str(', ') + str(round(J3_rec_show_7,ndigits=2)) + str(", ") + str(round(J4_rec_show_7,ndigits=2)) + str(" ; ") + str(rec_kompresor_7)
            if i == 7:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_8 = 0
                J2_record_8 = 0
                J3_record_8 = 0 
                J4_record_8 = 0
                rec_kompresor_8 = 0
                J1_rec_show_8 = 0
                J2_rec_show_8 = 0
                J3_rec_show_8 = 0 
                J4_rec_show_8 = 0
                kompresor_show_8 = 0
                label_8.text = str(round(J1_rec_show_8,ndigits=2)) + str(', ') + str(round(J2_rec_show_8,ndigits=2)) + str(", ") + str(round(J4_rec_show_8,ndigits=2)) + str(', ') + str(round(J3_rec_show_8,ndigits=2)) + str(" ; ") + str(rec_kompresor_8)
            if i == 8:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_9 = 0
                J2_record_9 = 0
                J3_record_9 = 0 
                J4_record_9 = 0
                rec_kompresor_9 = 0
                J1_rec_show_9 = 0
                J2_rec_show_9 = 0
                J3_rec_show_9 = 0 
                J4_rec_show_9 = 0
                kompresor_show_9 = 0
                label_9.text = str(round(J1_rec_show_9,ndigits=2)) + str(', ') + str(round(J2_rec_show_9,ndigits=2)) + str(', ') + str(round(J3_rec_show_9,ndigits=2)) + str(", ") + str(round(J4_rec_show_9,ndigits=2)) + str(" ; ") + str(rec_kompresor_9)
            if i == 9:
                # buatkan variabel baru untuk menyimpan data point (koordinat) untuk masing-masing joint
                J1_record_10 = 0
                J2_record_10 = 0
                J3_record_10 = 0 
                J4_record_10 = 0
                rec_kompresor_10 = 0
                J1_rec_show_10 = 0
                J2_rec_show_10 = 0
                J3_rec_show_10 = 0 
                J3_record_10 = 0
                kompresor_show_10 = 0
                label_10.text = str(round(J1_rec_show_10,ndigits=2)) + str(', ') + str(round(J2_rec_show_10,ndigits=2)) + str(", ") + str(round(J4_rec_show_10,ndigits=2)) + str(', ') + str(round(J3_rec_show_10,ndigits=2)) + str(" ; ") + str(rec_kompresor_10)
            if i < 0:
                i = 0

        def playback(self,obj):
            global J1_record_1
            global J2_record_1
            global J3_record_1
            global J4_record_1
            global J1_record_2
            global J2_record_2
            global J3_record_2
            global J4_record_2
            global J1_record_3
            global J2_record_3
            global J3_record_3
            global J4_record_3
            global J1_record_4
            global J2_record_4
            global J3_record_4
            global J4_record_4
            global J1_record_5
            global J2_record_5
            global J3_record_5
            global J4_record_5
            global J1_record_6
            global J2_record_6
            global J3_record_6
            global J4_record_6
            global J1_record_7
            global J2_record_7
            global J3_record_7
            global J4_record_7
            global J1_record_8
            global J2_record_8
            global J3_record_8
            global J4_record_8
            global J1_record_9
            global J2_record_9
            global J3_record_9
            global J4_record_9
            global J1_record_10
            global J2_record_10
            global J3_record_10
            global J4_record_10
            # record 1 
            dType.SetPTPCmdEx(api,5,J1_record_1,J2_record_1,J3_record_1,J4_record_1)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_1, 1)
            dType.dSleep(500) # 1 detik 
            dType.SetPTPCmdEx(api,5,J1_record_2,J2_record_2,J3_record_2,J4_record_2)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_2, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_3,J2_record_3,J3_record_3,J4_record_3)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_3, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_4,J2_record_4,J3_record_4,J4_record_4)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_4, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_5,J2_record_5,J3_record_5,J4_record_5)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_5, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_6,J2_record_6,J3_record_6,J4_record_6)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_6, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_7,J2_record_7,J3_record_7,J4_record_7)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_7, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_8,J2_record_8,J3_record_8,J4_record_8)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_8, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_9,J2_record_9,J3_record_9,J4_record_9)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_9, 1)
            dType.dSleep(500)
            dType.SetPTPCmdEx(api,5,J1_record_10,J2_record_10,J3_record_10,J4_record_10)
            dType.SetEndEffectorSuctionCupEx(api, rec_kompresor_10, 1)
            dType.dSleep(500)
            
        def kompresor(self, instance, value):
            global for_rec_kompresor
            global for_rec_kompresor
            if value is True:
                print("Switch On")
                dType.SetEndEffectorSuctionCupEx(api, 1, 1)
                for_rec_kompresor = 1
            else:
                print("Switch Off")
                dType.SetEndEffectorSuctionCupEx(api, 0, 1)
                for_rec_kompresor = 0

        J1 = dType.GetPoseEx(api, 5)    # Get data joint from dobot
        J1 = J1 - 35
        J2 = dType.GetPoseEx(api, 6)
        J3 = dType.GetPoseEx(api, 7)
        J1kon = math.radians(J1)    # konversi radians ke degree
        J2kon = math.radians(J2)
        J3kon = math.radians(J3)
        x1 = math.sin(J2kon)*L2
        x2 = math.cos(J3kon)*L3
        x_aksen = (x1 + x2) 
        x_diagonal = x_aksen + L4  
        y_koordinat = math.sin(J1kon)*x_diagonal
        x_koordinat = math.cos(J1kon)*x_diagonal
        z1 = math.cos(J2kon)*L2
        z2 = math.sin(J3kon)*L3
        z_aksen = (z1 - z2)
        z_koordinat = L1 + (z1 - z2)
        for_rec_X = dType.GetPoseEx(api, 5)
        for_rec_Y = dType.GetPoseEx(api, 6)
        for_rec_Z = dType.GetPoseEx(api, 7)
        nilai_x.text = str(float(round(x_koordinat, ndigits=2)))
        nilai_y.text = str(float(round(y_koordinat, ndigits=2)))
        nilai_z.text = str(float(round(z_koordinat, ndigits=2)))
        nilai_r.text = str(float(round(J4, ndigits=2)))
        nilai_j1.text = str(float(round(J1, ndigits=2)))
        nilai_j2.text = str(float(round(J2, ndigits=2)))
        nilai_j3.text = str(float(round(J3, ndigits=2)))
        nilai_j4.text = str(float(round(J4, ndigits=2)))

    MainApp().run()