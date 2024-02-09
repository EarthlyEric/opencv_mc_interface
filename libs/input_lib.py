import pydirectinput as input
# Key STATUS

def hand1_pos_solver(finger_angle):
    f1 = finger_angle[0]   
    f2 = finger_angle[1]   
    f3 = finger_angle[2]   
    f4 = finger_angle[3]   
    f5 = finger_angle[4]

    if f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
        input.keyDown("a")
        print("a")
    elif f1<50 and f2<50 and f3>=50 and f4<50 and f5<50:
        input.keyDown("s")
        print("s")
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
        input.keyDown("w")
        print("w")
    elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        input.keyDown("d")
        print("d")
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        input.mouseDown(button="left") 
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        input.keyUp("w")
        input.keyUp("a")
        input.keyUp("s")
        input.keyUp("d")
        print("CLEAR")
        

            
    

    
