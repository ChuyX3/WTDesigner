import re, sys, math
from complex import complex

class airfoil(object):

    def __init__(self):
        self.alpha = []
        self.cl = []
        self.cd = []
        self.shape = []
        self.ribs_ang = []
        self.ribs_len = []
        self.ribs_pos = []

    def clear_data(self):
        self.alpha = []
        self.cl = []
        self.cd = []

    def load_aerodynamic_data(self, filename):
        self.clear_data()
        file = open(filename, "r")
        for line in file.readlines():
            words = line.split()
            self.alpha.append(float(words[0]))
            self.cl.append(float(words[1]))
            self.cd.append(float(words[2]))        
        file.close()

    def load_geometry_data(self, filename):
        self.ribs_ang = []
        self.ribs_len = []
        self.ribs_pos = []
        file = open(filename, "r")
        for line in file.readlines():
            words = line.split()
            self.ribs_pos.append(float(words[0])) 
            self.ribs_len.append(float(words[1])) 
            self.ribs_ang.append(float(words[2]))     
        file.close()

    def load_shape_data(self, filename):
        self.shape = []
        file = open(filename, "r")
        for line in file.readlines():
            words = line.split()
            self.shape.append(complex(float(words[0]), float(words[1])))     
        file.close()

    def write_aerodynamic_data(self, filename):
        file = open(filename, 'a')
        text = ''
        i = 0
        for val in self.alpha:
            text += str(val) + ','
            if i == 20:
                text += '\n'
                i = 0
            i += 1
        file.write('alpha_data = List[\n' + text + '\n];')

        text = ''
        i = 0
        for val in self.cl:
            text += str(val) + ','
            if i == 20:
                text += '\n'
                i = 0
            i += 1
        file.write('cl_data = List[\n' + text + '\n];')

        text = ''
        i = 0
        for val in self.cd:
            text += str(val) + ','
            if i == 20:
                text += '\n'
                i = 0
            i += 1
        file.write('cd_data = List[\n' + text + '\n];')

        file.close()
    
    def write_geometry_data(self, path, transform = complex()):
        i = 0
        while i < len(self.ribs_pos):
            file = open(path + "airfoil_scale_" + str(int(self.ribs_len[i] * 1000)) + '.txt', "w")
            file.write('Polyline=true	\n')
            for val in self.shape:
                temp = complex()
                temp.real = val.real - transform.real
                temp.imag = val.imag - transform.imag
                temp.mod = temp.mod * self.ribs_len[i]
                temp.arg = temp.arg - math.pi / 2.0 + math.radians(self.ribs_ang[i])
                file.write('{0:d}'.format(int(self.ribs_pos[i] * -1000.0)) + '\t' + '{0:.2f}'.format(temp.real * 1000.0) + '\t' + '{0:.2f}\n'.format(temp.imag * 1000.0))
            file.close()
            i +=1

    def show(self):
        print(self.alpha)
        print(self.cl)
        print(self.cd)