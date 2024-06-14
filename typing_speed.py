import time

def typing_speed(start,end,t,txt):
    if (txt==t):
        totaltime=end-start
        words=txt.split()
        no=len(words)
        speed =no/(totaltime/60)
        print("You are perfect!!!")
        return speed
    
    else:
        print("Your entered Text is not same as given!!!\nTRY AGAIN!!!\n")
        tryagain()
    
def tryagain():
    print("Welcome to the Typing Speed Test!\n\nType the following text as fast as you can:")
    txt ="Hello Friends, my name is sanket bhuite."
    print(txt)

    input("\nPress Enter when you're ready to start typing...")
    start= time.time()
    t= input("Start typing:\n ")
    end= time.time()

    speed=typing_speed(start, end, t,txt)
    print("And Your typing speed is",int(speed)," words per minute.")
 
tryagain()
