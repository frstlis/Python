# Python-turtle库（python绘图工具）
_turtle_ ：海龟（海龟库） **turtle**库是Python语言中一个很流行的绘制图像的函数库,使用之前需要导入库：`import turtle`

`turtle.setup(width,height,startx,starty)`
-setup() 设置窗体的位置和大小
相对于桌面的起始点的坐标以及窗口的宽度高度，若不写窗口的起始点，则默认在桌面的正中心,窗体的坐标原点默认在窗口的中心
**绝对坐标**
`turtle.goto(100,100)`:指从当前的点指向括号内所给坐标

**海龟坐标**

把当前点当做坐标，有前方向，后方向，左方向，右方向

`turtle.fd(d)`:指沿着海龟的前方向运行

`turtle.bk(d)`:指沿着海龟的反方向运行

`turtle.circle(r,angle)`:指沿着海龟左侧的某一点做圆运动

**绝对角度**

`turtle.seth(angle)`:只改变海龟的行进方向（角度按逆时针），但不行进，angle为绝对度数

**海龟角度**

```markdow
turtle.left(angle)
turtle.right(angle)
```

### RGB色彩体系

rgb的色彩取值范围为0-255的整数或者0-1的小数

#### 切换RGB色彩模式　

`turtle.colormode(mode)`

1.0:RGB小数模式

255:RGB整数模式

### 画笔控制函数

1、`turtle.penup() 别名turtle.pu()`　　　　　　　画笔抬起，不留下痕迹

2、`turtle.pendown() 别名turtle.pd()`　　　　　　画笔落下，留下痕迹

3、`turtle.pensize(width) 别名turtle.width(width)`　　　　　画笔宽度

4、`turtle.pencolor(color)`      　　　　　　　color为颜色字符串或者rgb值

```markdown
    turtle.pencolor("purple")               #颜色字符串
    turtle.pencolor(0.63,0.13,0.94)         #RGB的小数值
    turtle.pencolor((0.63,0.13,0.94))       #RGB的元组值
```

### 运动控制函数　　

1、`turtle.forword(d) 别名turtle.fd(d)`　　　向前行进        d：行进距离，可以为负数

2、`turtle.circle(r,extent=None)`

根据半径r，绘制一个extent角度的弧度　　r：默认圆心在海龟左侧r距离的位置

### 方向控制函数

1、`turtle.setheading(angle)` 别名`turtle.seth(angle)`　　　改变行进方向

2、`angle`：改变方向的角度（绝对坐标下，绝对角度）

3、`turtle.left(angle)`

4、`turtle.right(angle)`   　　　　　　angle：当前方向上转过得角度（海龟角度）