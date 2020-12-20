sum=range(11)
flag=0
for i in sum:
    for j in sum:
        for k in sum:
            if i>0 and j >0 and k >0 and i+j+k==10:
                flag+=1
                print("I,J,K:",i,j,k)
print(flag)