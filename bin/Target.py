
class Target:
    lightblue = (255, 221, 0)
    Xmax = 0
    Ymax = 0
    Xmin = 1000
    Ymin = 1000
    Xmid = 0
    Ymid = 0

    def __init__(self,array):
        for corner in array:                                # for loop that iterates through each corner array in the given array
            if(self.Xmax<corner[0][0]):                     # series of if statements that get the minimum and maximum x and y values of the corners
                self.Xmax = corner[0][0]
            if(self.Xmin>corner[0][0]):
                self.Xmin = corner[0][0]
            if(self.Ymax<corner[0][1]):
                self.Ymax = corner[0][1]
            if(self.Ymin>corner[0][1]):
                self.Ymin = corner[0][1]
        self.Xmid = int((self.Xmax+self.Xmin)/2)
        self.Ymid = int((self.Ymax+self.Ymin)/2)

    def getCenter(self):                                    # getter method for the center x and y values
        return(self.Xmid,self.Ymid)

    def getWidth(self):                                     # getter method for the width of the target
        return(self.Xmax-self.Xmin)

    def getHeight(self):                                    # getter method for the height of the target
        return(self.Ymax-self.Ymin)
