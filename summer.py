from __future__ import division
import math

def asciitable(arr,between=" "):
    #[["row", 1, "contents"], ["row", 2], ...]
    print (lambda x,y: "\n".join([between.join([j[i]+(" "*(x[i]-len(j[i]))) for i in range(len(x))]) for j in y]))(*((lambda x:[[max([len(i[j]) for i in x]) for j in range(len(x[0]))],x])([[str(i) for i in j] for j in arr])))

def prettyPrintData(fname):
    with open(fname) as f:
        asciitable([i.split(" ") for i in f.readlines() if i[0]!="#"])

def getData(fname):
    with open(fname) as f:
        #                       normalization
        return [(lambda x:[x[1],1-(x[2]/x[0])])((lambda x:[x[0]+x[1]/60,x[2],x[3]+x[4]/60])([int(j) for j in i.split(" ")])) for i in f.readlines() if i[0]!="#"]

def linearRegression(data):
    return (lambda x,y,xy,xx,yy,n:[(y*xx-x*xy)/(n*xx-x*x),(n*xy-x*y)/(n*xx-x*x),(n*xy-x*y)/(math.sqrt(n*xx-x*x)*math.sqrt(n*yy-y*y))])(*(([sum(i) for i in zip(*data)])+[sum([i[0]*i[1] for i in data]),sum([i[0]*i[0] for i in data]),sum([i[1]*i[1] for i in data]),len(data)]))

def printResults(regressionLine):
    iregressionLine=(lambda a,b,r:[-a/b,1/b,r] if b else [])(*regressionLine)
    r2=abs(regressionLine[2]**2)
    correlationType=("negative" if regressionLine[2]<0 else "positive")

    print "With "+str(int(r2*100))+"% certainty:"
    if regressionLine[1]:
        print "There is a "+correlationType+" correlation between number of summer miles and improvement"
        print "\n".join(["For a "+str(int(i*+100))+"% improvement, "+str(int(iregressionLine[0]+iregressionLine[1]*i))+" miles of summer training are required." for i in (x/20 for x in range(5,0,-1))])
        print "To stay the same speed, "+str(int(iregressionLine[0]))+" miles of summer training are required."
        print "\n".join(["To be only "+str(int(i*-100))+"% slower, "+str(int(iregressionLine[0]+iregressionLine[1]*i))+" miles of summer training are required." for i in (x/20 for x in range(-1,-6,-1))])
        print
        print "\n".join([(lambda x:"If you run "+str(i)+" miles over the summer, you will become "+str(abs(x)*100)+"% "+("faster" if x>=0 else "slower")+".")(regressionLine[0]+regressionLine[1]*i) for i in range(0,501,50)])
    else:
        print "There is no correlation between number of summer miles and improvement"

def run(fname):
    printResults(linearRegression(getData(fname)))

run("detafile.txt")