import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
D = b**2 - 4*a*c




if D < 0:

    print ("Дискриминант = 0")

    print ("Корней нет")

elif D == 0:     #Если D = 0, то корень 1

    x = (-b + D** .5) / (2*a)


    print (int(x))

else:    #Если D > 0, то 2 корня

    x1 =  (-b + D** .5) / (2*a)

    x2 =  (-b - D** .5) / (2*a)



    print (int(x1))

    print (int(x2))