import numpy as np
class City:
    def __init_-(self,dx,dy):
        self.dx=dx
        self.dy=dy
        self.City=np.ndarray(shape=(dx,dy),dtype=int)
        self.City.fill(0)

    def valueofq(self,q):
        self.q=q

    def valueofn(self,n):
        self.n=n
