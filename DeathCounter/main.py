#author: Ian Whitesel, 2022
#MIT License

from pynput import keyboard

counterFile = 'D:\DeathCounter\deaths.txt'
#load last death count
f = open(counterFile, "r")
deathText = f.readline()
deathCount = int(deathText[7:10])

print("Starting deaths: ", str(deathCount))

def on_press(key):
    global deathCount, counterFile
    #Exit key example
    #if key == keyboard.Key.esc:
        #return False  # stop listener
    try:
        k = key.char
    except:
        k = key.name
    if k in ['f1', 'f2']:
        print('Key pressed: ' + k)
        if k == 'f1':
            deathCount -= 1
        if k == 'f2':
            deathCount += 1
        strDeathCount = str(deathCount)
        if deathCount < 100:
            strDeathCount = "0" + strDeathCount
        if deathCount < 10:
            strDeathCount = "0" + strDeathCount
        f = open(counterFile, "w")
        f.write("DEATHS:" + strDeathCount)
        f.close()


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys