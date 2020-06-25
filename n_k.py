# Author: Peihong Man
# University of Illinois at Chicago

import numpy as np
import matplotlib.pyplot as plt
import csv
import os.path


class NandK: 
    """Calculate n and k of MCT (Hg1-xCdxTe). """
    
    def __init__(self, x, temp, lamda, material, save_to_file):
        self.x = x
        self.temp = temp
        self.lamda = lamda
        
        # Parameters for n calculation
        self.A1 = 13.173 - 9.852 * x + 2.909 * x * x + 0.0001 * (300 - temp)
        self.B1 = 0.83 - 0.246 * x - 0.0961 * x * x + 8 * 0.00001 * (300 - temp)
        self.C1 = 6.706 - 14.437 * x + 8.531 * x * x + 7 * 0.00001 * (300 - temp)
        self.D1 = 1.953 * 0.00001 - 0.00128 * x + 1.853 * 0.00001 * x * x
        
        # Parameters for p calculation
        self.T0 = 61.9  # Initial parameter is 81.9. Adjusted.
        self.W = self.T0 + temp
        self.E0 = -0.3424 + 1.838 * x + 0.148 * x * x * x * x
        self.sigma = 3.267E4 * (1 + x)
        self.alpha0 = np.exp(53.61 * x - 18.88)
        self.beta = 3.109E5 * np.sqrt((1 + x) / self.W)  # Initial parameter is 2.109E5. Adjusted.
        self.Eg = self.E0 + (6.29E-2 + 7.68E-4 * temp) * ((1 - 2.14 * x) / (1 + x))

        print("Showing result for {}, x={}, at {}K. ".format(material, x, temp))
        print("Corresponding band gap: {:.2f} meV, cutoff wavelength: {:.2f}um. ".format(self.Eg*1000, 1.24/self.Eg))
        
        # print(self.beta)
        
        if type(lamda) == 'float': 
            self.n = self.cal_n(lamda)
            self.k1, self.k2 = self.cal_k(lamda, material)
        else: 
            self.n = []
            self.k1 = []
            self.k2 = []
            for lam in lamda:
                self.n.append(self.cal_n(lam))
                k1, k2 = self.cal_k(lam, material)
                self.k1.append(k1)
                self.k2.append(k2)
        
        if save_to_file:
            self.save_to_file()
        
    def cal_n(self, lamda): 
        n = np.sqrt(self.A1 + self.B1 / (1 - (self.C1 / lamda) * (self.C1 / lamda)) + self.D1 * lamda * lamda)
        return n

    def cal_k(self, lamda, material):

        """Calculate k based on the type of material at a certain lamda."""

        k = 0
        if material == "CdTe":
            return 0
        elif material == "MCT" or material == "SL":
            E = 4.13566743 * 3 / 10 / lamda
            # print(E)
            # print(Eg)
            ab1 = self.alpha0 * np.exp(self.sigma * (E - self.E0) / self.W) # Urbach
            if E >= self.Eg:
                ab2 = self.beta * np.sqrt(E - self.Eg)  # Intrinsic
            else:
                ab2 = 0
            
            
            k1 = ab1 / 4 / np.pi * lamda / 10000 
            k2 = ab2 / 4 / np.pi * lamda / 10000
            # print(k1)
            # print(k2)

            # if ab1 < crossover_a and ab2 < crossover_a:
            #     return k1
            # else:
            #     if ab2 != 0:
            #         return k2
            #     else:
            #         return k1
            return k1, k2
    
    def save_to_file(self): 
        filename = 'result.csv'
        if os.path.exists(filename):
            n = 1
            while True: 
                if os.path.exists('result{}.csv'.format(n)):
                    n += 1
                else: 
                    filename = 'result{}.csv'.format(n)
                    break    

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["x={}".format(self.x), "temp={}".format(self.temp)])
            writer.writerow(["Wavelength(um)", "n", "k1 (Urbach Zone)", "k2 (Intrinsic Zone)"])
            writer.writerows(zip(self.lamda, self.n, self.k1, self.k2))
    
    def plot_all(self):
        plt.plot(self.lamda, self.n)
        plt.xlabel('Wavelength (um)')
        plt.ylabel("n")
        plt.show()
        plt.plot(self.lamda, self.k1, label = "k1 (Urbach Zone)")
        plt.plot(self.lamda, self.k2, label = "k2 (Intrinsic Zone)")
        plt.xlabel('Wavelength (um)')
        plt.ylabel("k")
        plt.yscale('log')
        plt.legend()
        plt.show()
        
    def printall(self):
        print("n: {}".format(self.n))
        print("k1: {}".format(self.k1))
        print("k2: {}".format(self.k2))
            

def main():
    material = "MCT"
    x = 0.3     # Hg1-xCdxTe
    temp=300    # Kelvin
    lamdas = np.arange(1, 3, 0.02)  # Start, stop and increment
    save_to_file = True     # If true, the result will be saved to the root folder as a csv file. 
    
    cal = NandK(x=x, temp=temp, lamda = lamdas, material = material, save_to_file = save_to_file)
    # cal.printall()
    cal.plot_all()

if __name__ == '__main__':
    main()

