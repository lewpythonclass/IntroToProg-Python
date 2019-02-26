#Assignment07 Python Pickling
#Laura Wick
#02/25/2019

#Create a simple example of how you would use Python Pickling

#import the pickle libraries
import pickle

#creat a list
players = ["Popeye","Olive","Sweet Pea","Bluto"]
print("\nThe players are:  ")
print(players)

#open file to pickle to
filename = open("PickledPlayers.dat","wb")

#pickle takes object and filename
pickle.dump(players, filename)

#close the file
filename.close()

#retrieve it, using new object instances
f2 = open("PickledPlayers.dat","rb")
players2 = pickle.load(f2)
print("\nUn-packed previously pickled players:  ")
print(players2)
