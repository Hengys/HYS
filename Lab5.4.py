#Student ID: 1201201639
#Student Name : Heng Yee Siang

length=float(input("Enter Length :"))
width=float(input("Enter Width :"))

def rectangle(width,length):
    area = width*length
    return area

def triangle(width,length):
    area = width*length/2
    return area

area_rec = rectangle(width,length)
area_tri = triangle(width,length)

print("Rectangle area : {:.2f}".format(area_rec))
print("Triangle area  : {:.2f}".format(area_tri))