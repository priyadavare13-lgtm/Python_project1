students={"Aman":[85,90,78],"Riya":[92,88,95],"Zoya":[70,65,80]}
while True:
  print("""1.Student
  2.View all
  3.Show topper
  4.Exit""")
  choice=input("enter the choice: ")
  if choice=="1":
    name=input("Name: ")
    if name in students:
      print("Student already exists.")
    else:
      marks=[]
      for i in range(3):
        mark=int(input("Enter marks:"))
        while mark<0 or mark>100:
          print("Invalid mark,try again")
          mark=int(input("Enter marks:"))
        marks.append(mark)
      students[name]=marks
      avg=sum(marks)/3
      if avg>=85:
        grade="A"
      elif avg>=70:
        grade="C"
      else:
        grade="F"
      print(name,round(avg,2),grade)
  elif choice=="2":
    for name in students:
      avg=sum(students[name])/3
      if avg>=85:
        grade="A"
      elif avg>=70:
        grade="C"
      else:
        grade="F"
      print(name,round(avg,2),grade)
  elif choice=="3":
   best=0
   topper=" "
   for name in students:
    avg=sum(students[name])/3
    if avg>best:
     best=avg
     topper=name
   print("Topper:",topper)
  elif choice=="4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice")