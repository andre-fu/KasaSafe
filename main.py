from drowsy_driver import drowsiness_detector
from routing import routing
from send_texts import send_texts 
from threading import Thread
import os

if __name__ == '__main__':
    stat1 = False
    stat2 = False
    stat3 = False

    #user_num = input('What is your phone number?')
    #emerg_num = input("What is your emergency's contact number?")
    user_num = '+14168583844'
    emerg_num = '+14168583844'
    def status_1():
        stat1 = True

        #routing
        route = routing()
        places = route.possible_places()
        choice = route.chooser()
        start = route.loc
        end = choice
        instructions = route.routes(start, end)

    def status_2():
        stat2 = True
    
        #routing
        route = routing()
        places = route.possible_places()
        choice = route.chooser()
        start = route.loc
        end = choice
        instructions = route.routes(start, end)

        text = send_texts(user_num, emerg_num)
        text.send_text()
        print('------------------------------------------------------------SENT TEXT------------------------------------------------------------------')
    

    drowsy = drowsiness_detector()
    def start(drowsy):
        drowsy.vs_loop()

    vs = Thread(target = start, args = (drowsy, ))
    vs.start()
    print('Thread started with Status: ', drowsy.STATUS)

    while True:
        if (drowsy.STATUS == True) and (drowsy.STATUS_yawn == True):
            t = Thread(target = status_2)
            t.daemon = True
            t.start()
            break
        if (drowsy.STATUS == True ) and (drowsy.STATUS_yawn == False):
            t = Thread(target= status_2)
            t.daemon = True
            t.start()
            print('---------------STAT 1 ACTIVATED #1 ---------------')
            break
        if (drowsy.STATUS == False) and (drowsy.STATUS_yawn == True):
            t = Thread(target= status_1)
            t.daemon = True
            t.start()
            print('---------------STAT 1 ACTIVATED #2 ---------------')
            break



        

