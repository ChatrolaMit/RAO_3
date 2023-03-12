file = open('input.txt','r')
t = int(file.readline())

def secToTime(sec):
    rem = sec%3600 
    hour = sec//3600 
    sec = rem
    rem = sec%60 
    minn = sec//60 
    sec = rem 
    # print(hour,minn,sec)
    if len(str(sec))!=2 :
        sec = '0'+str(sec)
    if len(str(minn))!=2 :
        minn = '0'+str(minn)
    if len(str(hour))<2 :
        hour = '0'+str(hour)
    ff = f"{hour}:{minn}:{sec}"
    return ff
def timebound(t1,t2):
    t1 = t1.split(':')
    t2 = t2.split(':')
    
    ans1 = int(t1[0])*60*60+ int(t1[1])*60 + int(t1[2])
    ans2 = int(t2[0])*60*60+ int(t2[1])*60 + int(t2[2])
    return ans2-ans1
    

def calculate(mon):
    clockIn = mon[0][0]
    breakStart = mon[1][0]
    breaStop = mon[2][0]
    
    if (len(mon))==4 :
        clockOut = mon[3][0]
        t1 = timebound(clockIn,breakStart)
        t2 = timebound(breaStop,clockOut)
        return t1+t2 
    else:
        t1 = timebound(clockIn,breakStart)
        t2 = timebound(breaStop,'19:30:00')
        return min(t1+t2 , 21600)
        

dirr = dict()
emp = set()
for xx in range(t):
    inx = list(file.readline().split())
    print(xx+1,inx[0])
    if inx[0] not in dirr:
    #     emp.add(inx[0])
    #     dirr[inx[0]]=dict()
        emp.add(inx[0])
        # dirr[inx[0]]=[[inx[1],inx[2],inx[3]]]
        dirr[inx[0]]=dict()
        dirr[inx[0]][inx[1]]=[[inx[2],inx[3]]]
    else:
        emp.add(inx[0])
        # dirr[inx[0]].append([inx[1],inx[2],inx[3]])
        if(inx[1] not in dirr[inx[0]] ):
            dirr[inx[0]][inx[1]]=[[inx[2],inx[3]]]
        else:
            dirr[inx[0]][inx[1]].append([inx[2],inx[3]])        
        
# print(dirr)
ans = dict()
for em in emp :
    month = dict()
    for i in dirr[em]:
        mon = i.split('-')[1]
        if mon not in month:
            month[mon]=calculate(dirr[em][i])
        else:
            month[mon]+=calculate(dirr[em][i])
    ans[em]=month

mon = ['01','02','03','04','05','06','07','08','09','10','11','12']
# for i in range(len(ans)):
#     print(ans[i])
print(ans)

for i in mon:
    summ = 0
    maxx = 0
    minn = 10000000000
    flag=0
    for em in emp:
        if i in ans[em]:
            flag=1
            maxx = max(maxx , ans[em][i])
            summ= summ + int(ans[em][i])
            minn = min(minn  , ans[em][i])
    if flag==1:
        with open('output.txt','a') as f :
            print(maxx,minn,summ//len(emp))
            f.write(f"Case #{i}: {secToTime(maxx)} {secToTime(minn)} {secToTime(summ//len(emp))}\n")
    
        
        
    
    # print(summ//3 , secToTime(int(summ)//3))
# print(ans['Emp_1'])
    
    
        
        
    
    
        
    
    
    
    
    # print(emp)
    # print(inx[0] , dirr)
    # if(str(inx[0])in dirr.keys()):
    #     if(dirr[inx[0]][inx[1]] not in dirr[inx[0]] ):
    #         dirr[inx[0]][inx[1]]=[[inx[2],inx[3]]]
    #     else:
    #         dirr[inx[0]][inx[1]].append([inx[2],inx[3]])
    
    # else:
    #     emp.append(inx[0])
    #     dirr[inx[0]]=dict()
    #     if(dirr[inx[0]][inx[1]] not in dirr[inx[0]] ):
    #         dirr[inx[0]][inx[1]]=[[inx[2],inx[3]]]
    #     else:
    #         dirr[inx[0]][inx[1]].append([inx[2],inx[3]])
    