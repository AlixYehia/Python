
continue_check=0
while continue_check ==0:
  print("please enter the default matrix then the matrix you want to convert to: z, y, h, t: ")
  default_matrix=input("from matrix: ")
  convert_to_matrix=input("to matrix: ")
  x1=float(input("enter 1st paramter "))
  x2=float(input("enter 2nd paramter "))
  x3=float(input("enter 3rd paramter "))
  x4=float(input("enter 4th paramter "))
  delta_matrix=(x1*x4)-(x3*x2)
  if default_matrix =='z':
    z1=x1
    z2=x2
    z3=x3
    z4=x4
  elif default_matrix =='y':

    z1=(x4/delta_matrix)
    z2=(-x2/delta_matrix)
    z3=(-x3/delta_matrix)
    z4=(x1/delta_matrix)
  elif default_matrix =='h':

    z1=(delta_matrix/x4)
    z2=(x2/x4)
    z3=(-x3/x4)
    z4=(1/x4)
  elif default_matrix =='t':

    z1=(x1/x3)
    z2=(delta_matrix/x3)
    z3=(1/x3)
    z4=(x4/x3)
  else:
    print("pelase enter a vaild default matrix")

  delta_z=((z1*z4)-(z2*z3))
  if convert_to_matrix =='z':
    z1=z1
    z2=z2
    z3=z3
    z4=z4
    print("z11=", z1)
    print("z12=", z2)
    print("z21=", z3)
    print("z22=", z4)
  elif convert_to_matrix =='y':
    y1=(z4/delta_z)
    y2=(-z2/delta_z)
    y3=(-z3/delta_z)
    y4=(z1/delta_z)
    print("y11=", y1)
    print("y12=", y2)
    print("y21=", y3)
    print("y22=", y4)
  elif convert_to_matrix =='h':
    h1=(delta_z/z4)
    h2=(z2/z4)
    h3=(-z3/z4)
    h4=(1/z4)
    print("h11=", h1)
    print("h12=", h2)
    print("h21=", h3)
    print("h22=", h4)
  elif convert_to_matrix =='t':
    t1=(z1/z3)
    t2=(delta_z/z3)
    t3=(1/z3)
    t4=(z4/z3)
    print("t11=", t1)
    print("t12=", t2)
    print("t21=", t3)
    print("t22=", t4)
  else:
    print("please enter a valid operation to convert to")
  continue_check=float(input("if you want to continue enter 0: "))
print ("done")