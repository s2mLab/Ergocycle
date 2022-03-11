import numpy as np

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

