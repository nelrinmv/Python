m1 = int(input("Enter the marks of student 1:"))  
m2 = int(input("Enter the marks of student 2:"))   
m3 = int(input("Enter the marks of student 3:"))   
m4 = int(input("Enter the marks of student 4:"))   
m5 = int(input("Enter the marks of student 5:")) 

markslist = [m1,m2,m3,m4,m5]

print("\n","Complete list of marks that are scored by the students:", markslist,"\n")

highest = max(markslist)
print("Highest marks amoung the students:", highest,"\n")

lowest = min(markslist)
print("Lowest marks amoung the students:", lowest,"\n")

sortedmarks = markslist.sort()
print("Marks in sorted order:", markslist,"\n")

totalmarks = m1+m2+m3+m4+m5
print("Total marks in the class:",totalmarks,"\n")

avgmarks = totalmarks/5
print("Average Marks in the class:",avgmarks,"\n")