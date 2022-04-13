import numpy as np
import datetime
import csv
import time


#file_object = open("test2", "w+")
#matrice = np.array([[10, 20, 30], [40, 50, 60]])
#for row in matrice:
  #for element in row:
    #valeur=str(element)

    #file_object.write(" Amplitude (mA): "+ valeur)

#file_object.close

#file_object1 = open("RegisterFile_Test", "w+")
#matrix = np.array([[" ","electrode 1", "electrode 2","electrode 3","electrode 4","electrode 5","electrode 6","electrode 7","electrode 8"],["Amplitude (mA)", self.start_parameters[1,:]],["Frequency (Hz)", self.start_parameters[2,:]], ["Impulsion length (ms)", self.start_paramters[3,:]]])
#file_object.write(str(datetime.now()))
#file_object.write(matrix)
#file_object1.close

with open('enregistrement_stimulations.csv', 'w',newline='') as f:
    fieldnames = ['Date and time', 'Electrode', 'Amplitude(mA)','Frequence(Hz)', 'Durée dimpulsion', 'muscle']
    thewriter = csv.DictWriter(f,fieldnames)
    thewriter.writeheader()
    now = datetime.datetime.now()
    date_time = now.strftime("%m-%d-%Y,%H:%M:%S")

    for col in matrix():
        thewriter.writerow({'Date and time' : date_time, 'Electrode': str(col), 'Amplitude(mA)': str(2) ,'Frequence(Hz)': str(10), 'Durée dimpulsion': str(20), 'muscle': str(4) })

now = datetime.datetime.now()
date_time = now.strftime("%m-%d-%Y_%H:%M:%S")
#file = open("C:\Users\frede\Desktop\test_nouveau.csv", mode ='w')#, newline="")
#file = open('test.csv', )
#writer = csv.writer(file)
#writer.writerow(["Muscle","Amplitude","Fréquence","Durée d'impulsion"])
#writer.writerow(["Temps d'entraînement"])
#def write_in_csv_file(matrix):
        #writer = csv.writer(file)
        #writer.writerow("Muscle","Amplitude","Fréquence","Durée d'impulsion")
        #writer.writerow("Temps d'entraînement")
        #for col in matrix:
            #writer.writerow(matrix[:,1],matrix[:,2],matrix[:,3],matrix[:,4])
            
        #file.close

#designed_matrix = [[1,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0],[3,0,0,0,0,0,0,0],[4,0,0,0,0,0,0,0]]
#write_in_csv_file(designed_matrix)

