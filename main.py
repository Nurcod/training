from pygame import *
mw = display.set_mode((700,500))
display.set_caption('Negrd')
back = (255,255,255)
picture = image.load('gorn.png')
p = transform.scale(picture,(700,500))
mw.fill(back)
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    mw.blit(p,(0,0))

    display.update()



