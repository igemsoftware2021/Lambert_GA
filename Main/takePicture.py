from time import sleep 
from picamera import PiCamera


if __name__ == "__main__":
    #namefile
    fileName= print(input("Save Image As: "))
    #instantiate
    c = PiCamera () 
    #camera settins
    c.ISO = 800
    c.exposure = 'night'
    c.ss = 10000
    #start Picture
    c.start_preview()
    sleep(10)
    c.capture(f{f'{fileName}.png'})

    