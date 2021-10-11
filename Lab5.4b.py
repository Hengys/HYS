#Student ID: 1201201639
#Student Name : Heng Yee Siang

def rectangle(width,length):
    area = width*length
    return area

def triangle(width,length):
    area = width*length/2
    return area

i = 0
while(i<2):
    width = float(input("Enter width   : "))
    length = float(input("Enter length  : "))

    area_rec = rectangle(width,length)
    area_tri = triangle(width,length)

    print("Rectangle area : {:.2f}".format(area_rec))
    print("Triangle area  : {:.2f}".format(area_tri))
    i += 1
