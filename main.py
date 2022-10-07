# Write your code below this line 👇
#program greeting
print("Hello!  You have discovered a new, rare plant.  Let's give it a name.")

genus = input("Write the name of your favorite plant: ")
species = input("Write the name of a place you found the rare specimen: ")
import random
g_ending = ['um', 'is', 'irs']
s_ending = ['or', 'a', 'us']

print("The name of your newly discovered species is")
print(str.title(genus) + random.choice(g_ending) + " " + species + random.choice(s_ending))