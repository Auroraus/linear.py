# -*- coding: utf-8 -*-
"""
Created on Fri May 19 19:19:26 2017

@author: Administrator
"""
import tkinter
import numpy,math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure

r=tkinter.Tk()
r.title('线性方程求解   制作者:张凡')
r.geometry()
tkinter.Label(r,text='>>请注意，输入的x坐标值对数必须大于2，否则会报错！<<').pack()
tkinter.Label(r,text='>>请注意，输入的x坐标值个数和y坐标值个数要相同！<<').pack()
tkinter.Label(r,text='>>小数点后默认保留四位数字！<<').pack()
xinput=tkinter.Label(r,text='请依次输入x坐标轴上的的数据')
xinput.pack()
xstr=tkinter.StringVar()
xen=tkinter.Entry(r,textvariable=xstr,width=50)
xstr.set('')
xen.pack()
yinput=tkinter.Label(r,text='请依次输入y坐标轴上的数据')
yinput.pack()
ystr=tkinter.StringVar()
yen=tkinter.Entry(r,textvariable=ystr,width=50)
ystr.set('')
yen.pack()
tkinter.Label(r,text='>>以下是线性回归方程的图像和方程解<<').pack()


###金属工艺学参数设置
tkinter.Label(r, text='是否对使所有数据取对数').pack()
number = tkinter.StringVar()
tkinter.Entry(r, textvariable=number, width=20).pack()
tkinter.Label(r, text='').pack()
def n():
    xtuple=eval(xstr.get())
    xlist=list(xtuple)
    ytuple=eval(ystr.get())
    ylist=list(ytuple)
    t=tkinter.Text(r,height=int(len(xlist)/4.0+1),width=50)
    t.insert('1.0','请确认输入的数据对>>')
    for iii in xlist:
        for jjj in ylist:
            if xlist.index(iii)==ylist.index(jjj):
                t.insert('2.0',('（',iii,jjj,'),'))
                t.pack()
    t.pack()
def d():
    xtuple=eval(xstr.get())
    xlist=[]
    if number.get()=='是' or number.get()=='y' or number.get()=='Y' or number.get()=='yes' or number.get()=='1':
        for x in xtuple:
            xlist.append(math.log(x)) #这里的numpy.log(是为了金属工艺学实验而加的，后面必须去掉)变为：xlist=list(xtuple)
    else:
        xlist=list(xtuple)
    ytuple=eval(ystr.get())
    ylist=[]
    if number.get()=='是' or number.get()=='y' or number.get()=='Y' or number.get()=='yes' or number.get()=='1':
        for y in ytuple:
            ylist.append(math.log(y)) #这里的numpy.log(是为了金属工艺学实验而加的，后面必须去掉)变为：xlist=list(xtuple)
    else:
        ylist=list(ytuple)
    xaver=float(sum(xlist))/len(xlist)
    yaver=float(sum(ylist))/len(ylist)
    xy=[] 
    for i in xlist:
        for j in ylist:
            if xlist.index(i)==ylist.index(j):
                a=i*j
                xy.append(a)
    xx=[]
    for ii in xlist:
        b=ii**2
        xx.append(b)
    xyaver=float(sum(xy))/len(xy)
    xxaver=float(sum(xx))/len(xx)
    if (xaver**2-xxaver)!=0:
        para=(xaver*yaver-xyaver)/(xaver**2-xxaver)
        bbb=yaver-para*xaver
        zz=numpy.arange(min(xlist),max(xlist),0.00001)
        yyy=para*zz+bbb
        f_plot.clear()
        f_plot.plot(zz,yyy,'b-',label='linear line')
        f_plot.plot(xlist,ylist,'ro')
        f_plot.grid()
        canvs.draw()
        if bbb>=0:
            tkinter.Label(r,text=('>>线性方程为：y=',round(para,4),'x+',round(bbb,4),'>>y(1)=',round(para,4)+round(bbb,4))).pack()
        elif bbb<0: 
            tkinter.Label(r,text=('>>线性方程为：y=',round(para,4),'x',round(bbb,4),'>>y(1)=',round(para,4)+round(bbb,4))).pack()
        r.mainloop()
    else:
      tkinter.Label(r,text="您的数据有错误！，请检查后重新输入").pack()
f = Figure(figsize=(4,2),dpi=100)
f_plot = f.add_subplot(111)
canvs = FigureCanvasTkAgg(f,r)
canvs.get_tk_widget().pack(expand=1)
tkinter.Button(r,text='确认以下输入的数据',command=n).pack()
tkinter.Button(r,text='画图【求回归方程】',command=d).pack()
r.mainloop()
