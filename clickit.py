import cv2
from matplotlib import pyplot as plt
class clickIt():
    def __init__(self):
        self.fname = r"C:\Users\trevo\OneDrive\Desktop\test.jpg"
        self.img = cv2.imread(self.fname)
        self.point = ()
    def __onclick__(self,click):
        self.point = (click.xdata,click.ydata)
        return self.point
    def getCoord(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.imshow(self.img)
        cid = fig.canvas.mpl_connect('button_press_event', self.__onclick__)
        plt.show()
        return self.point

