#!/usr/bin
import time
print("OK! I am going to work.")
a = input("Ədədləri daxil edin: ")
a=a.split()
s=0
try:
    for i in a:
       s+=int(i)
    print(s)
except:
    print("Təəsüf ki, yalnış verilənlər veriniz. Bir daha diqqətli olun. İndi isə kampüterinizi 5 saniyə içində məhv edəcəm")
    for i in range(1,6):
        print(i)
        time.sleep(1)
    print("BOOM!!!"*3000)
    time.sleep(3)
    print('''   o          o                      o     o         
   |          |                      |     |         
 o-O o-o o-o -o- o-o o-o o  o o-o  o-O     O-o  o  o 
|  | |-'  \   |  |   | | |  | |-' |  |     |  | |  | 
 o-o o-o o-o  o  o   o-o o--O o-o  o-o     o-o  o--O 
                            |                      | 
                         o--o                   o--o ''')
    print('''               __    __                               ___      ___ 
   _______  __/ /_  / /_  ____ _____  ____ ____  ____/ (_)____/ (_)
  / ___/ / / / __ \/ __ \/ __ `/ __ \/ __ `/ _ \/ __  / / ___/ / / 
 (__  ) /_/ / /_/ / / / / /_/ / / / / /_/ /  __/ /_/ / / /  / / /  
/____/\__,_/_.___/_/ /_/\__,_/_/ /_/\__, /\___/\__,_/_/_/  /_/_/   
                                      /_/                          ''')
    print("Github: https://github.com/subhanqedirli \nMail: subhanqedirli@protonmail.com")
    
    
