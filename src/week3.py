class fuzzy():
    Xmin=2100
    Xmax=3500
    YMin=100
    YMax=250
    Zmin=1000
    Zmax=5000
    permNaik=0
    permTurun=0
    PsdSedikit=0
    PsdBanyak=0
    X=0
    Y=0
    alpha=[0]*4
    Z=[0]*4
    
    def init(self, permintaan, persediaan):
        self.X=permintaan
        self.Y=persediaan
        self.fPermTurun()
        self.fPermNaik()
        self.fPsdSedikit()
        self.fPsdBanyak()
        self.rule()
        
    def fPermTurun(self):
        if self.X < self.Xmin:
            self.permTurun=1
        elif self.X >= self.Xmin and self.X <= self.Xmax:
            self.permTurun=(self.Xmax - self.X)/(self.Xmax - self.Xmin)
        else:
            self.permTurun = 0
            
    def fPermNaik(self):
        if self.X < self.Xmin:
            self.permNaik = 0
        elif self.X >= self.Xmin and self.X <= self.Xmax:
            self.permNaik = (self.X - self.Xmin)/(self.Xmax - self.Xmin)
        else:
            self.permNaik = 1
          
            
    def fPsdSedikit(self):
        if self.Y < self.YMin:
            self.PsdSedikit = 1
        elif self.Y >= self.YMin and self.Y <= self.YMax:
            self.PsdSedikit = (self.YMax - self.Y)/(self.YMax - self.YMin)
        else:
            self.PsdSedikit = 0
    
    def fPsdBanyak(self):
        if self.Y < self.YMin:
            self.PsdBanyak = 0
        elif self.Y >= self.YMin and self.Y <= self.YMax:
            self.PsdBanyak = (self.Y - self.YMin)/(self.YMax - self.YMin)
        else:
            self.PsdBanyak = 1
            
    def rule(self):
        #rule1 : jika perm turun dan psd banyak maka produksi berkurang
        self.alpha[0] = min(self.permTurun, self.PsdBanyak)
        self.Z[0] = self.Zmax - self.alpha[0]*(self.Zmax - self.Zmin)
        
        #rule2 : jika perm turun dan persediaan sedikit maka produksi berkurang
        self.alpha[1] = min(self.permTurun, self.PsdSedikit)
        self.Z[1] = self.Zmax - self.alpha[1]*(self.Zmax - self.Zmin)
        
        #rule3 : jika perm naik dan persediaan banyak maka produksi naik
        self.alpha[2] = min(self.permNaik, self.PsdBanyak)
        self.Z[2] = self.alpha[2]*(self.Zmax - self.Zmin) + self.Zmin
        
        #rule4 : jika perm naik dan persediaan turun maka produksi naik
        self.alpha[3] = min(self.permNaik, self.PsdSedikit)
        self.Z[3] = self.alpha[3]*(self.Zmax - self.Zmin) + self.Zmin
        
    def defuzifikasi(self):
        output = (self.alpha[0] * self.Z[0]) + (self.alpha[1]*self.Z[1]) + (self.alpha[2]*self.Z[2]) + (self.alpha[3]*self.Z[3])
        output1 = self.alpha[0] + self.alpha[1] + self.alpha[2] + self.alpha[3]
        return output/output1
    

#main program
fz = fuzzy(3200,140)
print("permintaan turun = ", fz.permTurun)
print("Permintaan naik = ", fz.permNaik)
print("Permintaan sedikit = ", fz.PsdSedikit)
print("Permintaan banyak = ", fz.PsdBanyak)
print("nilai seluruh prediket = ", fz.alpha)
print("nilai seluruh z = ", fz.Z)
print("Produksi adalah ", fz.defuzifikasi())
                