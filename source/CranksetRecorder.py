from Crankset import Crankset
import numpy as np
import csv
import time


class CSV(Crankset):
    def __init__(self):
        super().__init__()

    def writef(self, t, x):
        timestr = self.now.strftime("%m_%d_%Y, %H;%M;%S")
        file = open(timestr + " force.csv", "a")  # Open the csv file

        # time = str(t)
        value = np.append(t, x)

        # create the csv writter
        writer = csv.writer(file)

        # write a row to the csv file
        writer.writerow(map(lambda y: [y], value))

    # file.write(time+ "\t" + value)
        # file.write("\n")

        # Close the csv file
        file.close()

    def readAngle(self, Ts):
        # Ts is the sampling time
        nmbOfVal = 0

        while True:
            valuef = self.readcard()
            valueangle= self.readangle()
            nmbOfVal = nmbOfVal+1

            # Find the Force/Torque data Left
            forceL = self.multGU(self.gL, valuef[0:6])
            forceR = self.multGU(self.gR, valuef[6:12])
            vectforce = np.append(forceL, forceR,valueangle)
            self.writef(nmbOfVal*Ts, vectforce)
            # print("valeurk",vectforce[0],nmbOfVal)

            # To stop the while
            if nmbOfVal == int(250):
                print("You stop the acquisition")
                break

            time.sleep(Ts)

