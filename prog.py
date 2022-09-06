#
class mur:
    def init (self, vcc, gnd, out):
        self.out=[]
        self.vcc=2
        self.gnd=6

class hum(mur):
    def init (self, vcc, gnd, out, val):
        self.val=val
        self.out.append(val)
        
def get_val(self):
    return self.val
