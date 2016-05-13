import os
while True:
    try:
        sngName=str(input('Song Name: '))
        for i in os.listdir(os.getcwd()):
            if (sngName.lower() in i.lower()) == True:
                f = i
        break
    except(NameError,TypeError,SyntaxError):
        print 'invalid'

page=open(f,'r+')
lines=page.readlines()
#first we find and get the scale factor for each number
if len(lines[3])<20:
    mant=float(lines[3][3:6])
    power=float(lines[3][8:10])
    scale=mant*10**power
    start=5
else:
    scale=1
    start = 3
print(scale)#scale is good
print(lines[start])
#then we make a list for the points
points=[]
for i in range(start,len(lines)-1):
    tempLst=[]
    for j in range(3):
        ten=j*10
        tPt=scale*float(lines[i][ten+4:ten+10])
        sign=lines[i][ten+3]
        if sign=='-':
            tPt=(-1*tPt)
        tempLst.append(tPt)
    points.append(tempLst)
#here marks the end of the points list
    
#now we need to connect the dots into triangles
stMat=[]
for i in range(len(points)):
    uTrip=[]
    lTrip=[]
    if i > 7874:
        if points[i]==points[i%63]:
            continue
        else:
            if ((i%63)==0):
                lTrip.append(points[i])
                lTrip.append(points[i%63])
                lTrip.append(points[(i+1)])
            elif ((i%63)==62):
                uTrip.append(points[i])
                uTrip.append(points[i%63])
                uTrip.append(points[(i%63)-1])
            else:
                uTrip.append(points[i])
                uTrip.append(points[i%63])
                uTrip.append(points[(i%63)-1])
                lTrip.append(points[i])
                lTrip.append(points[i%63])
                lTrip.append(points[(i+1)])
    else:
        if points[i]==points[i+63]:
            continue
        else:
            if ((i%63)==0):
                lTrip.append(points[i])
                lTrip.append(points[i+63])
                lTrip.append(points[i+1])
            elif ((i%63)==62):
                uTrip.append(points[i])
                uTrip.append(points[i+63])
                uTrip.append(points[i+62])
            else:
                uTrip.append(points[i])
                uTrip.append(points[i+63])
                uTrip.append(points[i+62])
                lTrip.append(points[i])
                lTrip.append(points[i+63])
                lTrip.append(points[i+1])
    if uTrip!=[]:
        stMat.append(uTrip)
    if lTrip!=[]:
        stMat.append(lTrip)
     
print(stMat[0][0])
print(stMat[len(stMat)-1])
print(len(points))
print(points[len(points)-1])
page.close()

with open(f+'.stl','w+') as file:
    file.write('\nsolid Default')
    for i in range(len(stMat)):
        file.write('\n  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00 \n    outer loop \n')
        for j in range(len(stMat[i])):
            file.write('      vertex '+str(stMat[i][j][0])+' '+str(stMat[i][j][1])+' '+str(stMat[i][j][2]))
            file.write('\n')
        file.write('    endloop\n  endfacet')
    file.write('\nendsolid Default')
    
