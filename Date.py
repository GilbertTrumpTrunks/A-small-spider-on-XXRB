temp=0
with open ('Date.txt','w') as d:
    for i in range(1,13):
        if(i==2):
            temp=28
        elif(i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12):
            temp=31
        else :
            temp=30
        for j in range(1,temp+1):
            if (i<10 and j>=10):
                d.write('0'+str(i)+str(j)+'\n')
            elif (j<10 and i>=10):
                d.write(str(i)+'0'+str(j)+'\n')
            elif (j<10 and i<10):
                d.write('0'+str(i)+'0'+str(j)+'\n')
            else:
                d.write(str(i)+str(j)+'\n')
