from Crankset import Crankset
import numpy as np
import csv
import time


class CSV(Crankset):
    def __init__(self):
        super().__init__()  # TODO: Complete the parameter needed

    def write_force(self, t, x):
        time_str = self.now.strftime("%m_%d_%Y, %H;%M;%S")
        file = open(time_str + " force.csv", "a")  # Open the csv file

        # time = str(t)
        value = np.append(t, x)

        # create the csv writer
        writer = csv.writer(file)

        # write a row to the csv file
        writer.writerow(map(lambda y: [y], value))

        # file.write(time+ "\t" + value)
        # file.write("\n")

        # Close the csv file
        file.close()

    def read_angle_ts(self, ts):
        # ts is the sampling time
        nmb_o_f_val = 0

        while True:
            force_value = self.read_card()
            angle_value = self.read_angle()
            nmb_o_f_val = nmb_o_f_val + 1

            # Find the Force/Torque data Left
            force_left = self.multiple_gu(self.gL, force_value[0:6])
            force_right = self.multiple_gu(self.gR, force_value[6:12])
            force_vector = np.append(force_left, force_right, angle_value)
            self.write_force(nmb_o_f_val * ts, force_vector)

            # To stop the while
            if nmb_o_f_val == int(250):
                print("You stop the acquisition")
                break

            time.sleep(ts)
