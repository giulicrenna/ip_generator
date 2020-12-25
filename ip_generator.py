import random


file = open(r'C:\Users\giuli\Desktop\ip_list.txt', 'w')

for i in range (0,244):
    rand1 = random.randint(0,254)
    rand2 = random.randint(0,254)
    rand3 = random.randint(0,254)
    rand4 = random.randint(0,254)
    file.write("{}.{}.{}.{}\n".format(rand1,rand2,rand3,rand4) )