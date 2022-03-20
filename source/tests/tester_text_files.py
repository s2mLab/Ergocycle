import numpy as np
import datetime
#def create_file(file_name, param_matrix):
    #f = open(file_name, "w+")
    #for row in range(param_matrix):
        #f.write("amplitude: ", param_matrix[row][0])
    #f.write("")
#matrice_inventee = [[100, 50, 20], [101, 51, 21]]
#nouveau_patient = create_file()

#fichier = create_file(test_user1, C:\Users\frede\Desktop\enregistrements

file_object = open("test2", "w+")
matrice = np.array([[10, 20, 30], [40, 50, 60]])
for row in matrice:
  for element in row:
    valeur=str(element)
    #if element
    file_object.write(" Amplitude (mA): "+ valeur)

file_object.close
#for i in range(10):
    # file_object.write("This is line %d\r\n" % (i+1))

#amplitude : self.start_parameters[1,:]
#frequency : self.start_parameters[2,:]
#length impulsion: self.start_parameters[3,:]

file_object1 = open("InstructionWindow")
matrix = np.array([[" ","electrode 1", "electrode 2","electrode 3","electrode 4","electrode 5","electrode 6","electrode 7","electrode 8"],["Amplitude (mA)", self.start_parameters[1,:]],["Frequency (Hz)", self.start_parameters[2,:]], ["Impulsion length (ms)", self.start_paramters[3,:]]])
file_object.write(str(datetime.now()))
file_object.write(matrix)
