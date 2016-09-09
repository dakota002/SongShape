import os
from math import pi, ceil

while True:
    try:
        sngName=str(input('Song Name: '))
        for i in os.listdir(os.getcwd()):
            if (sngName.lower() in i.lower()) == True:
                f = i
        break
    except(NameError,TypeError,SyntaxError):
        print 'invalid'

#Get resolution of the shape
stepRes = float(sys.argv[1])

#Number of steps in the phi rotation
#Comes from rounded up value of pi/(stepRes)
phiSteps = ceil(pi/stepRes)
theSteps = ceil(2*pi/stepRes)


page=open(f,'r+')
lines=page.readlines()
#first we find and get the scale factor for each number
#Formatting changes depending on start line. So we have different conditions
#for starting on 3 or 5
if len(lines[3])<20:
    mant=float(lines[3][3:6])
    power=float(lines[3][8:10])
    scale=mant*10**power
    start=5
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

else:
    scale=1
    start = 3
    points=[]
    #then we make list for points
    for i in range(start,len(lines)-1):
        L4=range(1,5)
        L4.reverse()
        curLine=lines[i]
        for j in L4:
            curLine=curLine.replace(j*' ',',')
        commas=[]
        for j in range(len(curLine)):
            if curLine[j]==',':
                commas.append(j)
        tPt1=curLine[commas[0]+1:commas[1]]
        tPt2=curLine[commas[1]+1:commas[2]]
        tPt3=curLine[commas[2]+1:len(curLine)-1]
        points.append([tPt1,tPt2,tPt3])


#now we need to connect the dots into triangles
#the final "column" of points is found by the following:
# (StepsInThetaRotation * StepsInPhiRotation) - (StepsInPhiRotation + 1)
#This is where the 7874 previously came from
fCol = (theSteps * phiSteps) - (phiSteps + 1)

stMat=[]
for i in range(len(points)):
    uTrip=[]
    lTrip=[]
    if i > fCol:
        if points[i]==points[i%phiSteps]:
            continue
        else:
            if ((i%phiSteps)==0):
                lTrip.append(points[i])
                lTrip.append(points[i%phiSteps])
                lTrip.append(points[(i+1)])
            elif ((i%phiSteps)==(phiSteps-1)):
                uTrip.append(points[i])
                uTrip.append(points[i%phiSteps])
                uTrip.append(points[(i%phiSteps)-1])
            else:
                uTrip.append(points[i])
                uTrip.append(points[i%phiSteps])
                uTrip.append(points[(i%phiSteps)-1])
                lTrip.append(points[i])
                lTrip.append(points[i%phiSteps])
                lTrip.append(points[(i+1)])
    else:
        if points[i]==points[i+phiSteps]:
            continue
        else:
            if ((i%phiSteps)==0):
                lTrip.append(points[i])
                lTrip.append(points[i+phiSteps])
                lTrip.append(points[i+1])
            elif ((i%phiSteps)==(phiSteps-1)):
                uTrip.append(points[i])
                uTrip.append(points[i+phiSteps])
                uTrip.append(points[i+(phiSteps-1)])
            else:
                uTrip.append(points[i])
                uTrip.append(points[i+phiSteps])
                uTrip.append(points[i+(phiSteps-1)])
                lTrip.append(points[i])
                lTrip.append(points[i+phiSteps])
                lTrip.append(points[i+1])
    if uTrip!=[]:
        stMat.append(uTrip)
    if lTrip!=[]:
        stMat.append(lTrip)


page.close()

#Writes the stl file from the stMat, however, leaves an open hole in the top
with open(f+'.stl','w+') as file:
    file.write('\nsolid Default')
    for i in range(len(stMat)):
        file.write('\n  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00 \n    outer loop \n')
        for j in range(len(stMat[i])):
            file.write('      vertex '+str(stMat[i][j][0])+' '+str(stMat[i][j][1])+' '+str(stMat[i][j][2]))
            file.write('\n')
        file.write('    endloop\n  endfacet')
    for i in range(theSteps):
        file.write('\n  facet normal 0.000000e+00 0.000000e+00 -1.000000e+00 \n    outer loop \n')
        file.write('      vertex '+str(points[0][0])+' '+str(points[0][1])+' '+str(points[0][2])+'\n')
        file.write('      vertex '+str(points[i*phiSteps+1][0])+' '+str(points[i*phiSteps+1][1])+' '+str(points[i*phiSteps+1][2])+'\n')
        file.write('      vertex '+str(points[(i+1)*phiSteps+1][0])+' '+str(points[(i+1)*phiSteps+1][1])+' '+str(points[(i+1)*phiSteps+1][2])+'\n')
        file.write('    endloop\n  endfacet')
    file.write('\nendsolid Default')
