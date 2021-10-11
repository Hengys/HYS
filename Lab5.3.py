#Student ID: 1201201639
#Student Name : Heng Yee Siang

def cm_to_meter(centimeter):
      meter=centimeter/100
      return meter

def get_cm():
  cm = float(input("Please enter a value for centimeter :"))
  m = cm_to_meter(cm)
  print(" {:.2f} cm is {:.2f} meter".format(cm,m))

def meter_to_cm(meter):
      centimeter=meter*100
      return centimeter

def get_m():
  m = float(input("Please enter a value for meter :"))
  cm = meter_to_cm(m)
  print(" {:.2f} m is {:.2f} centimeter".format(m,cm))

print("======================================")
print("                MENU")
print("======================================")

choice = int(input("Enter your choice : "))

if (choice==1):
      get_cm()

elif (choice==2):
      get_m()

else:
      print("Invalid choice")
