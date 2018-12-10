from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os #اضاقه مكتبة نظام التشغيل
import random #اضافة مكتبة العشوائيه
from time import sleep



memory = [] #لسته فاضية لتخزين الجواب
xxx= ["red","blue","green","yellow"] #تعريف الالوان 
global clicks #تعريف المتغير على انه متغير لجميع اقسام البرنامج
global first_time #تعريف المتغير على انه متغير لجميع اقسام البرنامج
global allowed_clicks_ram #تعريف المتغير على انه متغير لجميع اقسام البرنامج
global allowed_clicks #تعريف المتغير على انه متغير لجميع اقسام البرنامج
clicks = [] #تعريف ليست لتسجيل الضغطات
first_time = True #تعريف اول تشغيل
allowed_clicks = 1 #عدد الضغطات المسموحة 
allowed_clicks_ram = 0 #عدد الضغطات اللتي تم ضغطها

def clear_screen(): #تعريف مسح شاشه
    os.system('cls')  # مسح شاشه


def add_num():# تعريف دالة اضافة لون
    memory.append(random.choice(xxx)) #اختيار لون عشوائى واضافه الى القائمه 

def print_list(): #تعريف دالة طباعة ليست الالوان
    print(" ".join(memory))#عرض لستة الالوان على هيئة نص



def GAMEOVER(): #تعريف دالة انتهاء اللعبة
    global first_time #تعريف المتغير على انه متغير لجميع اقسام البرنامج
    global allowed_clicks_ram #تعريف المتغير على انه متغير لجميع اقسام البرنامج
    global allowed_clicks #تعريف المتغير على انه متغير لجميع اقسام البرنامج
    print("Game Over") #طباعة نص نهاية اللعبة
    window.title('GAMEOVER score: '+str(allowed_clicks-1)) #تغيير عنوان البرنامج الى عدد النقاط اللتي تم الحصول عليها اثناء التشغيل
    print("restart the game to play again") #طباعة نص نهاية اللعبة
    allowed_clicks = 1 #اعادة المتغيرات الى حالتها الافتراضية
    allowed_clicks_ram = 0 #اعادة المتغيرات الى حالتها الافتراضية
    first_time = True #اعادة المتغيرات الى حالتها الافتراضية
    red1.config(state=tk.DISABLED) #تعطيل امكانية الضغط على الازرار
    blue1.config(state=tk.DISABLED) #تعطيل امكانية الضغط على الازرار
    green1.config(state=tk.DISABLED) #تعطيل امكانية الضغط على الازرار
    yellow1.config(state=tk.DISABLED) #تعطيل امكانية الضغط على الازرار

def maingame(color):#تعريف الدالة الاساس
    global first_time #تعريف المتغير على انه متغير لجميع اقسام البرنامج
    global allowed_clicks_ram #تعريف المتغير على انه متغير لجميع اقسام البرنامج
    global allowed_clicks #تعريف المتغير على انه متغير لجميع اقسام البرنامج
    if first_time == True: #اذا كان اول تشغيل
        add_num() #استدعاء دالة اضافة لون
        print_list() #استدعاء دالة طباعة ليست الالوان
        first_time = False #تعطيل خيارات اول تشغيل
    else:# اذا لم يكن اول تشغيل
        clicks.append(color) #اضافة لون في قائمة الضغطات
        if clicks[allowed_clicks_ram] != memory[allowed_clicks_ram]: #اذا لم تكن الالوان المختارة نفس الالوان المسجلة
            GAMEOVER()# استدعاء دالة انتهاء اللعبة
        allowed_clicks_ram = allowed_clicks_ram +1 #اضافة 1 على عدد الضغطات اللتي تم ضغطها
        if allowed_clicks_ram == allowed_clicks: #اذا تساوى عدد الضغطات المسموحة مع عدد الضغطات
            if clicks == memory: #اذا كانت الاوان المختارة نفس الالوان المخزنة في الذاكرة
                clear_screen() #مسح الشاشة
                print(True) #طباعة صحيح
                window.title('score: '+str(allowed_clicks)) #عرض النقاط  في شريط العنوان
                allowed_clicks = allowed_clicks + 1 #اضافة 1 على عدد الضغطات المسموح
                allowed_clicks_ram = 0 #اعادة المتغيرات الى حالتها الافتراضية
                clicks.clear() #اعادة المتغيرات الى حالتها الافتراضية
                add_num() #استدعاء دالة اضافة لون بالليست
                print_list() #استددعاء دالة عرض الالوان

        
def red(): #تعريف دالة اللون الاحمر
    maingame("red")#استدعاء دالة الاساس مع ارسال اللون الاحمر
def blue(): #تعريف دالة اللون الازرق
    maingame("blue")#استدعاء دالة الاساس مع ارسال اللون الازرق
def green(): #تعريف ددالة اللون الاخضر
    maingame("green")#استدعاء دالة الاساس مع ارسال اللون الاخضر
def yellow(): #تعريف دالة اللون الاصفر
    maingame("yellow")#استدعاء دالة الاساس مع ارسال اللون الاصفر



window=Tk() #تعريف الواجهة
window.title('simon') #اضافة عنوان
window.geometry('400x400') #تغيير الحجم

red1=Button(window,bg='red',width=28,height=12,command=red) #تعريف زر اللون الاحمر مع اضافة استدعاء لدالة اللون الاحمر
red1.grid(row=0,column=0) #تغيير مكان الزر

blue1=Button(window,bg='blue',width=28,height=12,command=blue) #تعريف زر اللون الازرق مع اضافة استدعاء لدالة اللون الازرق
blue1.grid(row=0,column=1) #تغيير مكان الزر

yellow1=Button(window,bg='yellow',width=28,height=12,command=yellow) #تعريف زر اللون الاصفر مع اضافة استدعاء لدالة اللون الاصفر
yellow1.grid(row=1,column=0) #تغيير مكان الزر

green1=Button(window,bg='green',width=28,height=12,command=green) #تعريف زر اللون الاخضر مع اضافة استدعاء لدالة اللون الاخضر
green1.grid(row=1,column=1) #تغيير مكان الزر


window.mainloop() #تشغيل تكرار الواجهة