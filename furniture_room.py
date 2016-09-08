class furniture_room():
    """This class isn't finished, but the end goal is to haveit generate a 1000px by 1000px "room" and some furniture to go inside. That way, there can be a room for each person."""

    def __init__(self, background_color, win):
        room-background = visual.Rect(win,lineColor=background_color,fillColor=[100,100,255],size=[100,100],
            pos=[0,0],units="pix", fillColorSpace="rgb255",lineColorSpace="rgb255")
        room-background.draw()
        return
