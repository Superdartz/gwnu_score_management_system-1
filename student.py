class Student:

    def __init__(self, data):
        items = data.split(',')

        self._sid = items[0]
        self._sname = items[1]
        self._skor = float(items[2])
        self._seng = float(items[3])
        self._smat = float(items[4])
        self._stotal = float(self._seng + self._skor + self._smat)
        self._savg = float(self._stotal/3)

    @property
    def sid(self):
        return self._sid

    @property
    def sname(self):
        return self._sname

    @property
    def skor(self):
        return self._skor
    
    @property
    def seng(self):
        return self._seng
    
    @property
    def smat(self):
        return self._smat

    @property
    def stotal(self):
        return self._stotal

    @property
    def savg(self):
        return self._savg
