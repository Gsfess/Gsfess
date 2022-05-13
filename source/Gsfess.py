import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk


def msgbox():
    tkinter.messagebox.showinfo("关于" , """本软件由张峻熙制作,在GitHub上开源
版本:Gsfess for windows GUI 1.0""")

def quit(quit):
    top.quit()


def msgbox1(about):
    tkinter.messagebox.showinfo("关于" , """本软件由张峻熙制作,在GitHub上开源
版本:Gsfess for windows GUI 1.0""")



def gongshichaxun_tkinter():
    gongshichaxun = tk.Tk()
    gongshichaxun.title("公式")
    gongshi1 = ttk.Label(gongshichaxun , text = "正方形周长 = 边长 * 4")
    gongshi1.grid(column = 0 , row = 1)
    gongshi1 = ttk.Label(gongshichaxun , text = "正方形面积 = 边长 * 边长")
    gongshi1.grid(column = 0 , row = 2)
    gongshi1 = ttk.Label(gongshichaxun , text = "长方形周长 = （长 + 宽） * 2")
    gongshi1.grid(column = 0 , row = 3)
    gongshi1 = ttk.Label(gongshichaxun , text = "长方形面积 = 长 * 宽")
    gongshi1.grid(column = 0 , row = 4)
    gongshi1 = ttk.Label(gongshichaxun , text = "三角形面积 = 底 * 高 / 2")
    gongshi1.grid(column = 0 , row = 5)
    gongshi1 = ttk.Label(gongshichaxun , text = "平行四边形面积 = 底 * 高")
    gongshi1.grid(column = 0 , row = 6)
    gongshi1 = ttk.Label(gongshichaxun , text = "正方形体积 = 边长 * 边长 * 边长")
    gongshi1.grid(column = 0 , row = 7)
    gongshi1 = ttk.Label(gongshichaxun , text = "正方形棱长总和 = 边长 * 12")
    gongshi1.grid(column = 0 , row = 8)
    gongshi1 = ttk.Label(gongshichaxun , text = "正方形表面积 = 边长 * 边长 * 6")
    gongshi1.grid(column = 0 , row = 9)
    gongshi1 = ttk.Label(gongshichaxun , text = "长方体体积 = 长 * 宽 * 高")
    gongshi1.grid(column = 0 , row = 10)
    gongshi1 = ttk.Label(gongshichaxun , text = "长方体棱长总和 = （长 + 宽 + 高） * 4")
    gongshi1.grid(column = 0 , row = 11)
    gongshi1 = ttk.Label(gongshichaxun , text = "长方体表面积 = （长 * 宽 + 长 * 高 + 宽 * 高） * 2")
    gongshi1.grid(column = 0 , row = 12)
    gongshi1 = ttk.Label(gongshichaxun , text = "圆柱体积 = 底面积 * 高")
    gongshi1.grid(column = 0 , row = 13)
    gongshi1 = ttk.Label(gongshichaxun , text = "圆柱表面积 = 底面积 * 2 + 侧面积")
    gongshi1.grid(column = 0 , row = 14)
    gongshi1 = ttk.Label(gongshichaxun , text = "圆锥体积 = 底面积 * 高 / 3")
    gongshi1.grid(column = 0 , row = 15)
    
    gongshichaxun.mainloop()





"""
正方体的工作已经全部完成
"""


# 正方体体积的窗口
def zhengfangti_tiji():
    zft_tj = tk.Tk()
    zft_tj.title("正方体体积")
    zhengfangti_tiji_text = ttk.Label(zft_tj , text = "请输入棱长：")
    zhengfangti_tiji_text.grid(column = 0 , row = 1)
    zhengfangti_tiji_Entry = ttk.Entry(zft_tj)
    zhengfangti_tiji_Entry.grid(column = 2 , row = 1)


    def zhengfangti_tiji_jisuan():
        zhengfangti_tiji_jieguo = float(zhengfangti_tiji_Entry.get())
        zhengfangti_tiji_jieguo = zhengfangti_tiji_jieguo * zhengfangti_tiji_jieguo * zhengfangti_tiji_jieguo
        AAAA = ttk.Label(zft_tj , text = "结果是：")
        AAAA.grid(column = 1 , row = 3)
        CCCC = ttk.Label(zft_tj , text = zhengfangti_tiji_jieguo)
        CCCC.grid(column = 2 , row = 3)

    
    zhengfangti_tiji_Button = ttk.Button(zft_tj , text = "计算" , command = zhengfangti_tiji_jisuan)
    zhengfangti_tiji_Button.grid(column = 0 , row = 2)
    zft_tj.mainloop()


# 正方形面积

def zhengfangxing_mianji_tkinter():
    zfx_mj = tk.Tk()
    zfx_mj.title("正方形周长")
    zhengfangxing_mianji_text = ttk.Label(zfx_mj , text = "请输入棱长：")
    zhengfangxing_mianji_text.grid(column = 0 , row = 1)
    zhengfangxing_mianji_Entry = ttk.Entry(zfx_mj)
    zhengfangxing_mianji_Entry.grid(column = 1 , row = 1)


    def zhengfangti_tiji_jisuan():
        zhengfangxing_mianji_jieguo = float(zhengfangxing_mianji_Entry.get())
        zhengfangtxing_mianji_jieguo = zhengfangxing_mianji_jieguo * zhengfangxing_mianji_jieguo
        AAAAA = ttk.Label(zfx_mj , text = "结果是：")
        AAAAA.grid(column = 1 , row = 2)
        CCCCC = ttk.Label(zfx_mj , text = zhengfangtxing_mianji_jieguo)
        CCCCC.grid(column = 2 , row = 2)
    zhengfangti_mianji_Button = ttk.Button(zfx_mj , text = "计算" , command = zhengfangti_tiji_jisuan)
    zhengfangti_mianji_Button.grid(column = 0 , row = 2)
    zfx_mj.mainloop()

# 正方形周长

def zhengfangxing_zhouchang_tkinter():
    zfx_zc = tk.Tk()
    zfx_zc.title("正方形周长")
    zhengfangxing_zhouchang_text = ttk.Label(zfx_zc , text = "请输入棱长：")
    zhengfangxing_zhouchang_text.grid(column = 0 , row = 1)
    zhengfangxing_zhouchang_Entry = ttk.Entry(zfx_zc)
    zhengfangxing_zhouchang_Entry.grid(column = 1 , row = 1)


    def zhengfangti_tiji_jisuan():
        zhengfangxing_zhouchang_jieguo = float(zhengfangxing_zhouchang_Entry.get())
        zhengfangtxing_zhouchang_jieguo = zhengfangxing_zhouchang_jieguo * 4
        AAAAA = ttk.Label(zfx_zc , text = "结果是：")
        AAAAA.grid(column = 1 , row = 2)
        CCCCC = ttk.Label(zfx_zc , text = zhengfangtxing_zhouchang_jieguo)
        CCCCC.grid(column = 2 , row = 2)
    zhengfangti_zhouchang_Button = ttk.Button(zfx_zc , text = "计算" , command = zhengfangti_tiji_jisuan)
    zhengfangti_zhouchang_Button.grid(column = 0 , row = 2)
    zfx_zc.mainloop()

# 正方形主窗口

def zhengfangxing_tkinter():
    zfx_z = tk.Tk()
    zfx_z.title("正方形")
    zhengfangxing_Button1 = ttk.Button(zfx_z , text= "           周长          " , command= zhengfangxing_zhouchang_tkinter)
    zhengfangxing_Button1.pack(side= "left")
    zhengfangxing_Button2 = ttk.Button(zfx_z , text= "           面积           " , command= zhengfangxing_mianji_tkinter)
    zhengfangxing_Button2.pack()
    zfx_z.mainloop()

# 正方体表面积的窗口
def zhengfangtti_biaomianji():
    z_bmj = tk.Tk()
    z_bmj.title("正方体表面积")
    zhengfangti_biaomianji_text = ttk.Label(z_bmj , text = "请输入棱长：")
    zhengfangti_biaomianji_text.grid(column = 0 , row = 1)
    zhengfangti_biaomianji_Emtry = ttk.Entry(z_bmj)
    zhengfangti_biaomianji_Emtry.grid(column = 1 , row = 1)
    def zhengfangti_jieguo():
        jieguo = float(zhengfangti_biaomianji_Emtry.get())
        jieguo = jieguo * jieguo * 6
        zhengfangti_biaomianji_jieguo = ttk.Label(z_bmj , text = "结果是：")
        zhengfangti_biaomianji_jieguo.grid(column = 1 , row = 2)
        zhengfangti_biaomianji_jieguo_1 = ttk.Label(z_bmj , text = jieguo)
        zhengfangti_biaomianji_jieguo_1.grid(column = 3 , row = 2)
    zhengfangti_biaomianji_Button = ttk.Button(z_bmj , text = "计算" , command = zhengfangti_jieguo)
    zhengfangti_biaomianji_Button.grid(column = 0 , row = 2)
    
    z_bmj.mainloop()


# 正方体的主窗口
def zhengfangti_tkinter():
    xuanze = tk.Tk()
    xuanze.title("正方体")
    xuanze1 = ttk.Button(xuanze , text = "          表面积         " , command = zhengfangtti_biaomianji)
    xuanze1.pack(side = "left")
    xuanze2 = ttk.Button(xuanze , text = "           体积          " , command = zhengfangti_tiji)
    xuanze2.pack(side = "left")
    xuanze.mainloop()


# 长方体体积主窗口

def changfangti_tiji_tkinter():
    changfangti_tiji = tk.Tk()
    changfangti_tiji.title("长方体体积")
    changfangti_tiji_Labe = ttk.Label(changfangti_tiji , text = "请输入长：")
    changfangti_tiji_Labe.grid(column = 0 , row = 1)
    changfangti_tiji_Entry = ttk.Entry(changfangti_tiji)
    changfangti_tiji_Entry.grid(column = 1 , row = 1)
    changfangti_tiji_Label = ttk.Label(changfangti_tiji , text = "请输入宽：")
    changfangti_tiji_Label.grid(column = 0 , row = 2)
    changfangti_tiji_Entry1 = ttk.Entry(changfangti_tiji)
    changfangti_tiji_Entry1.grid(column = 1 , row = 2)
    changfangti_tiji_Labe2 = ttk.Label(changfangti_tiji , text = "请输入高：")
    changfangti_tiji_Labe2.grid(column = 0 , row = 3)
    changfangti_tiji_Entry2 = ttk.Entry(changfangti_tiji)
    changfangti_tiji_Entry2.grid(column = 1 , row = 3)
    def jisuan_neibu():
        changfangti_tiji_chang = float(changfangti_tiji_Entry.get())
        changfangti_tiji_kuan = float(changfangti_tiji_Entry1.get())
        changfangti_tiji_gao = float(changfangti_tiji_Entry2.get())
        changfangti_tiji_jieguo_jisuan = changfangti_tiji_chang * changfangti_tiji_kuan * changfangti_tiji_gao
        changfangti_tiji_jieguo_label = ttk.Label(changfangti_tiji , text = "结果是：")
        changfangti_tiji_jieguo_label.grid(column = 1 , row = 4)
        changfangti_tiji_jieguo_label2 = ttk.Label(changfangti_tiji , text = changfangti_tiji_jieguo_jisuan)
        changfangti_tiji_jieguo_label2.grid(column = 2 ,row = 4)
    changfangti_tiji_jisuan = ttk.Button(changfangti_tiji , text = "计算" , command = jisuan_neibu)
    changfangti_tiji_jisuan.grid(column = 0 , row = 4)
    changfangti_tiji.mainloop()
    


# 长方体表面积主窗口


def changfangti_biaomianji_tkinter():
    changfangti_biaomianji = tk.Tk()
    changfangti_biaomianji.title("长方体表面积")
    changfangti_biaomianji_Labe = ttk.Label(changfangti_biaomianji , text = "请输入长：")
    changfangti_biaomianji_Labe.grid(column = 0 , row = 1)
    changfangti_biaomianji_Entry = ttk.Entry(changfangti_biaomianji)
    changfangti_biaomianji_Entry.grid(column = 1 , row = 1)
    changfangti_biaomianji_Label = ttk.Label(changfangti_biaomianji , text = "请输入宽：")
    changfangti_biaomianji_Label.grid(column = 0 , row = 2)
    changfangti_biaomianji_Entry1 = ttk.Entry(changfangti_biaomianji)
    changfangti_biaomianji_Entry1.grid(column = 1 , row = 2)
    changfangti_biaomianji_Labe2 = ttk.Label(changfangti_biaomianji , text = "请输入高：")
    changfangti_biaomianji_Labe2.grid(column = 0 , row = 3)
    changfangti_biaomianji_Entry2 = ttk.Entry(changfangti_biaomianji)
    changfangti_biaomianji_Entry2.grid(column = 1 , row = 3)
    def changfangti_biaomianji_jieguo():
        changfangti_biaomianji_chang = float(changfangti_biaomianji_Entry.get())
        changfangti_biaomianji_kuan = float(changfangti_biaomianji_Entry2.get())
        changfangti_biaomianji_gao = float(changfangti_biaomianji_Entry2.get())
        changfangti_biaomianji_jieguo_bianliang = (changfangti_biaomianji_chang * changfangti_biaomianji_kuan + changfangti_biaomianji_chang * changfangti_biaomianji_gao + changfangti_biaomianji_kuan * changfangti_biaomianji_gao) * 2
        changfangti_biaomianji_jieguo_Lable = ttk.Label(changfangti_biaomianji , text= "结果是:")
        changfangti_biaomianji_jieguo_Lable.grid(column = 1 , row = 4)
        changfangti_biaomianji_jieguo_shuzi = ttk.Label(changfangti_biaomianji , text= changfangti_biaomianji_jieguo_bianliang)
        changfangti_biaomianji_jieguo_shuzi.grid(column = 2 , row = 4)
    changfangti_biaomianji_jisuan1 = ttk.Button(changfangti_biaomianji , text= "计算" , command = changfangti_biaomianji_jieguo)
    changfangti_biaomianji_jisuan1.grid(column = 0 , row = 4)
    


# 长方体主窗口

def changfangti_tkinter():
    xuanze1_changfangti = ttk.Tk()
    xuanze1_changfangti.title("长方体")
    xuanze1_changfangti1 = ttk.Button(xuanze1_changfangti , text = "          表面积         " , command = changfangti_biaomianji_tkinter)
    xuanze1_changfangti1.pack(side = "left")
    xuanze1_changfangt2 = ttk.Button(xuanze1_changfangti , text = "           体积          " , command = changfangti_tiji_tkinter)
    xuanze1_changfangt2.pack(side = "left")
    xuanze1_changfangti.mainloop()


# 圆柱体积窗口

def yuanzhu_tiji_tkinter():
    yuanzhu_tiji = tk.Tk()
    yuanzhu_tiji.title("圆柱体积")
    yuanzhu_Lable_banjing_tiji = ttk.Label(yuanzhu_tiji , text = "请输入底面半径:")
    yuanzhu_Lable_banjing_tiji.grid(column = 0 , row = 1)
    yuanzhu_tiji_Entry = ttk.Entry(yuanzhu_tiji)
    yuanzhu_tiji_Entry.grid(column = 1 , row= 1)
    yuanzhu_Lable_gao_tiji = ttk.Label(yuanzhu_tiji , text = "请输入高:")
    yuanzhu_Lable_gao_tiji.grid(column= 0 ,row= 2)
    yuanzhu_tiji_Entry2 = ttk.Entry(yuanzhu_tiji)
    yuanzhu_tiji_Entry2.grid(column= 1 , row= 2)
    def yuanzhu_tiji_jisuan_hanshu():
        banjing_tiji = float(yuanzhu_tiji_Entry.get())
        gao_tiji = float(yuanzhu_tiji_Entry2.get())
        jieguo_tiji = 3.14 * banjing_tiji * banjing_tiji * gao_tiji
        jieguo_Lable_jieguo = ttk.Label(yuanzhu_tiji , text= "结果是：")
        jieguo_Lable_jieguo.grid(column= 1 , row= 3)
        jieguo_Lable_jieguo_bianliang = ttk.Label(yuanzhu_tiji , text= jieguo_tiji)
        jieguo_Lable_jieguo_bianliang.grid(column= 2 , row= 3)
    yuanzhu_tiji_jisuan_Button = ttk.Button(yuanzhu_tiji , text= "计算" , command = yuanzhu_tiji_jisuan_hanshu)
    yuanzhu_tiji_jisuan_Button.grid(column= 0 , row= 3)
    yuanzhu_tiji.mainloop()


# 圆柱表面积窗口
def yuanzhu_biaomianji_tkinter():
    yuanzhu_biaomianji = tk.Tk()
    yuanzhu_biaomianji.title("圆柱表面积")
    yuanzhu_Lable_banjing = ttk.Label(yuanzhu_biaomianji , text = "请输入底面半径:")
    yuanzhu_Lable_banjing.grid(column = 0 , row = 1)
    yuanzhu_biaomianji_Entry = ttk.Entry(yuanzhu_biaomianji)
    yuanzhu_biaomianji_Entry.grid(column = 1 , row= 1)
    yuanzhu_Lable_gao = ttk.Label(yuanzhu_biaomianji , text = "请输入高:")
    yuanzhu_Lable_gao.grid(column= 0 ,row= 2)
    yuanzhu_biaomianji_Entry2 = ttk.Entry(yuanzhu_biaomianji)
    yuanzhu_biaomianji_Entry2.grid(column= 1 , row= 2)
    def yuanzhu_biaomianji_jieguo():
        biaomianji_yuanzhu_banjing = float(yuanzhu_biaomianji_Entry.get())
        biaomianji_yuanzhu_gao = float(yuanzhu_biaomianji_Entry2.get())
        biaomianji_yuanzhu_jieguo = 2 * 3.14 * biaomianji_yuanzhu_banjing * biaomianji_yuanzhu_gao + 3.14 * biaomianji_yuanzhu_banjing * biaomianji_yuanzhu_banjing * 2
        biaomianji_yuanzhu_jieguo_Label = ttk.Label(yuanzhu_biaomianji , text= "结果是：")
        biaomianji_yuanzhu_jieguo_Label.grid(column= 1 , row= 3)
        biaomianji_yuanzhu_jieguo_Label1 = ttk.Label(yuanzhu_biaomianji , text= biaomianji_yuanzhu_jieguo)
        biaomianji_yuanzhu_jieguo_Label1.grid(column= 2 , row= 3)
    yuanzhubiaomianji_jisuan = ttk.Button(yuanzhu_biaomianji , text= "计算" , command= yuanzhu_biaomianji_jieguo)
    yuanzhubiaomianji_jisuan.grid(column= 0 , row= 3)
    yuanzhu_biaomianji.mainloop()


# 圆柱主窗口
def yuanzhu_tkinter():
    xuanze_yuanzhu = tk.Tk()
    xuanze_yuanzhu.title("圆柱体")
    xuanze_yuanzhu_Button1 = ttk.Button(xuanze_yuanzhu , text = "          表面积         " , command= yuanzhu_biaomianji_tkinter)
    xuanze_yuanzhu_Button1.pack(side = "left")
    xuanze_yuanzhu_Button2 = ttk.Button(xuanze_yuanzhu , text = "           体积          " , command = yuanzhu_tiji_tkinter)
    xuanze_yuanzhu_Button2.pack(side = "left")
    xuanze_yuanzhu.mainloop()


# 长方形周长计算
def changfangxing_zhouchang_tkinter():
    changfangxing_zhouchang = tk.Tk()
    changfangxing_zhouchang.title("长方形周长")
    changfangxing_zhouchang_Lable = ttk.Label(changfangxing_zhouchang , text= "请输入长：")
    changfangxing_zhouchang_Lable.grid(column= 0 , row= 1)
    changfangxing_zhouchang_Entry = ttk.Entry(changfangxing_zhouchang)
    changfangxing_zhouchang_Entry.grid(column= 1 , row= 1)
    changfangxing_zhouchang_Lable2 = ttk.Label(changfangxing_zhouchang , text= "请输入宽：")
    changfangxing_zhouchang_Lable2.grid(column= 0 , row= 2)
    changfangxing_zhouchang_Entry2 = ttk.Entry(changfangxing_zhouchang)
    changfangxing_zhouchang_Entry2.grid(column= 1 , row= 2)
    def changfangxing_mianji_jisuan_tkinter():
        changfangxing_chang_zhouchang = float(changfangxing_zhouchang_Entry.get())
        changfangxing_kuan_zhouchang = float(changfangxing_zhouchang_Entry2.get())
        changfangxing_jieguo_zhouchang = (changfangxing_chang_zhouchang + changfangxing_kuan_zhouchang) * 2
        changfangxing_jieguo_Label_zhouchang = ttk.Label(changfangxing_zhouchang , text= "结果是：")
        changfangxing_jieguo_Label_zhouchang.grid(column= 1 , row= 3)
        changfangxing_jieguo_Labe2_zhouchang = ttk.Label(changfangxing_zhouchang , text = changfangxing_jieguo_zhouchang)
        changfangxing_jieguo_Labe2_zhouchang.grid(column= 2 , row= 3)
    changfangxing_zhouchang_Button_jisuan = ttk.Button(changfangxing_zhouchang , text= "计算" , command = changfangxing_mianji_jisuan_tkinter)
    changfangxing_zhouchang_Button_jisuan.grid(column= 0 , row= 3)
    changfangxing_zhouchang.mainloop()


# 长方形面积计算

def changfangxing_mianji_tkinter():
    changfangxing_mianji = tk.Tk()
    changfangxing_mianji.title("长方形面积")
    changfangxing_mianji_Lable = ttk.Label(changfangxing_mianji , text= "请输入长：")
    changfangxing_mianji_Lable.grid(column= 0 , row= 1)
    changfangxing_mianji_Entry = ttk.Entry(changfangxing_mianji)
    changfangxing_mianji_Entry.grid(column= 1 , row= 1)
    changfangxing_mianji_Lable2 = ttk.Label(changfangxing_mianji , text= "请输入宽：")
    changfangxing_mianji_Lable2.grid(column= 0 , row= 2)
    changfangxing_mianji_Entry2 = ttk.Entry(changfangxing_mianji)
    changfangxing_mianji_Entry2.grid(column= 1 , row= 2)
    def changfangxing_mianji_jisuan_tkinter():
        changfangxing_chang = float(changfangxing_mianji_Entry.get())
        changfangxing_kuan = float(changfangxing_mianji_Entry2.get())
        changfangxing_jieguo = changfangxing_chang * changfangxing_kuan
        changfangxing_jieguo_Label = ttk.Label(changfangxing_mianji , text= "结果是：")
        changfangxing_jieguo_Label.grid(column= 1 , row= 3)
        changfangxing_jieguo_Labe2 = ttk.Label(changfangxing_mianji , text = changfangxing_jieguo)
        changfangxing_jieguo_Labe2.grid(column= 2 , row= 3)
    changfangxing_mianji_Button_jisuan = ttk.Button(changfangxing_mianji , text= "计算" , command = changfangxing_mianji_jisuan_tkinter)
    changfangxing_mianji_Button_jisuan.grid(column= 0 , row= 3)
    changfangxing_mianji.mainloop()


# 长方形主窗口

def changfangxing_tkinter():
    xuanze_changfangxing = tk.Tk()
    xuanze_changfangxing.title("长方形")
    xuanze_changfangxing_Button1 = ttk.Button(xuanze_changfangxing , text = "           面积          " , command= changfangxing_mianji_tkinter)
    xuanze_changfangxing_Button1.pack(side = "left")
    xuanze_changfangxing_Button2 = ttk.Button(xuanze_changfangxing , text = "           周长          " , command= changfangxing_zhouchang_tkinter)
    xuanze_changfangxing_Button2.pack(side = "left")
    xuanze_changfangxing.mainloop()



# 平行四边形主窗口

def pingxingsibianxing_tkinter():
    pingxingsibianxing = tk.Tk()
    pingxingsibianxing.title("平行四边形面积")
    pingxingsibianxing_text = ttk.Label(pingxingsibianxing , text= "请输入底：")
    pingxingsibianxing_text.grid(column= 0 , row= 1)
    pingxingsibianxing_Entry = ttk.Entry(pingxingsibianxing)
    pingxingsibianxing_Entry.grid(column= 1 , row= 1)
    pingxingsibianxing_text2 = ttk.Label(pingxingsibianxing , text= "请输入高：")
    pingxingsibianxing_text2.grid(column= 0 , row= 2)
    pingxingsibianxing_Entry2 = ttk.Entry(pingxingsibianxing)
    pingxingsibianxing_Entry2.grid(column= 1 , row= 2)
    def pingxingsibianxing_jisuan_hanshu():
        pingxingsibianxing_di = float(pingxingsibianxing_Entry.get())
        pingxingsibianxing_gao = float(pingxingsibianxing_Entry2.get())
        pingxingsibianxing_jieguo = pingxingsibianxing_di * pingxingsibianxing_gao
        changfangxing_jieguo_Label = ttk.Label(pingxingsibianxing , text= "结果是：")
        changfangxing_jieguo_Label.grid(column= 1 , row= 3)
        changfangxing_jieguo_Labe2 = ttk.Label(pingxingsibianxing , text = pingxingsibianxing_jieguo)
        changfangxing_jieguo_Labe2.grid(column= 2 , row= 3)
    pingxingsibianxing_Button = ttk.Button(pingxingsibianxing , text= "计算" , command= pingxingsibianxing_jisuan_hanshu)
    pingxingsibianxing_Button.grid(column= 0 , row= 3)
    pingxingsibianxing.mainloop()
def tixing_tkinter():
    tixing = tk.Tk()
    tixing.title("平行四边形面积")
    tixing_text1 = ttk.Label(tixing , text= "请输入上底：")
    tixing_text1.grid(column= 0 , row= 1)
    tixing_Entry1 = ttk.Entry(tixing)
    tixing_Entry1.grid(column= 1 , row=1)
    tixing_text2 = ttk.Label(tixing , text= "请输入下底：")
    tixing_text2.grid(column= 0 , row= 2)
    tixing_Entry2 = ttk.Entry(tixing)
    tixing_Entry2.grid(column= 1 , row= 2)
    tixing_text3 = ttk.Label(tixing , text= "请输入高：")
    tixing_text3.grid(column= 0 , row= 3)
    tixing_Entry3 = ttk.Entry(tixing)
    tixing_Entry3.grid(column= 1 , row= 3)
    def pingxingsibianxing_jisuan_hanshu():
        tixing_shangdi = float(tixing_Entry1.get())
        tixing_xiadi = float(tixing_Entry2.get())
        tixing_gao = float(tixing_Entry3.get())
        tixing_jieguo = (tixing_shangdi + tixing_xiadi) * tixing_gao / 2
        tixing_jieguo_Label = ttk.Label(tixing , text= "结果是：")
        tixing_jieguo_Label.grid(column= 1 , row= 4)
        tixing_jieguo_Labe2 = ttk.Label(tixing , text = tixing_jieguo)
        tixing_jieguo_Labe2.grid(column= 2 , row= 4)
    tixing_Button = ttk.Button(tixing , text= "计算" , command= pingxingsibianxing_jisuan_hanshu)
    tixing_Button.grid(column= 0 , row= 4)
    tixing.mainloop()

# 三角形面积主函数

def sanjiaoxing_tkinter():
    sanjiaoxing = tk.Tk()
    sanjiaoxing.title("平行四边形面积")
    sanjiaoxing_text = ttk.Label(sanjiaoxing , text= "请输入底：")
    sanjiaoxing_text.grid(column= 0 , row= 1)
    sanjiaoxing_Entry = ttk.Entry(sanjiaoxing)
    sanjiaoxing_Entry.grid(column= 1 , row= 1)
    sanjiaoxing_text2 = ttk.Label(sanjiaoxing , text= "请输入高：")
    sanjiaoxing_text2.grid(column= 0 , row= 2)
    sanjiaoxing_Entry2 = ttk.Entry(sanjiaoxing)
    sanjiaoxing_Entry2.grid(column= 1 , row= 2)
    def sanjiaoxing_jisuan_hanshu():
        sanjiaoxing_di = float(sanjiaoxing_Entry.get())
        sanjiaoxing_gao = float(sanjiaoxing_Entry2.get())
        sanjiaoxing_jieguo = sanjiaoxing_di * sanjiaoxing_gao / 2
        changfangxing_jieguo_Label = ttk.Label(sanjiaoxing , text= "结果是：")
        changfangxing_jieguo_Label.grid(column= 1 , row= 3)
        changfangxing_jieguo_Labe2 = ttk.Label(sanjiaoxing , text = sanjiaoxing_jieguo)
        changfangxing_jieguo_Labe2.grid(column= 2 , row= 3)
    sanjiaoxing_Button = ttk.Button(sanjiaoxing , text= "计算" , command= sanjiaoxing_jisuan_hanshu)
    sanjiaoxing_Button.grid(column= 0 , row= 3)
    sanjiaoxing.mainloop()


# 主程序
top = tk.Tk()
top.title("Gsfess")

# 这是程序的一个顶部菜单，记录一下过程

# 创建一个顶上的栏
caidan = tk.Menu(top)


# 创建一个“软件选项”的子菜单，并且不要添加分割线
caidan_ruanjianxuanxiang = tk.Menu(caidan , tearoff = False)


# 增加一个帮助的子菜单

caidan_ruanjianxuanxiang_bangzhu = tk.Menu(caidan , tearoff = False)

# 在帮助上增加关于选项
caidan_ruanjianxuanxiang_bangzhu.add_command (label = "关于" , accelerator = "ctrl+A" , command = msgbox)


"""
下面是菜单的制作过程
"""
# # 在软件选项上增加关于选项
# caidan_ruanjianxuanxiang.add_command (label = "关于" , accelerator = "ctrl+A" , command = msgbox)


# 添加 一条菜单的分割线
# caidan_ruanjianxuanxiang.add_separator ()

# 创建一个退出按钮
caidan_ruanjianxuanxiang.add_command (label = "退出" , accelerator = "ctrl+Q" , command = top.quit)


# 声明一个在上面条条上面的按钮 ， 名字就叫“软件选项” ，并且与软件菜单变量进行绑定
caidan.add_cascade (label = "文件" , menu = caidan_ruanjianxuanxiang)

caidan.add_cascade(label = "帮助" , menu = caidan_ruanjianxuanxiang_bangzhu)


# 生成这个选项菜单在主窗口
top.config(menu = caidan)

# 设置快捷键

top. bind ("<Control-a>" , msgbox1)
top. bind ("<Control-q>" , quit)


# 软件菜单下面的图形化按钮
text = ttk.Label(top , text = "欢迎使用Gsfess! 是由张峻熙制作,下面是选项菜单：")
text.pack()
text66 = ttk.Label(top , text = "-----------------------------------------------------")
text66.pack()
A = ttk.Label(top , text = "立体图形")
A.pack()
text33 = ttk.Label(top , text = "-----------------------------------------------------")
text33.pack()
Button1 = ttk.Button(top , text = "正方体" , command = zhengfangti_tkinter)
Button1.pack()
Button2 = ttk.Button(top , text = "长方体" , command = changfangti_tkinter)
Button2.pack()
Button3 = ttk.Button(top , text = "圆柱体" , command = yuanzhu_tkinter)
Button3.pack()
text55 = ttk.Label(top , text = "-----------------------------------------------------")
text55.pack()
B = ttk.Label(top , text = "平面图形")
B.pack()
text44 = ttk.Label(top , text = "-----------------------------------------------------")
text44.pack()
Button4 = ttk.Button(top , text = "长方形" , command= changfangxing_tkinter)
Button4.pack()
Button4 = ttk.Button(top , text = "正方形" , command = zhengfangxing_tkinter)
Button4.pack()
Button4 = ttk.Button(top , text = "平行四边形" , command= pingxingsibianxing_tkinter)
Button4.pack()
Button4 = ttk.Button(top , text = "梯形" , command= tixing_tkinter)
Button4.pack()
Button4 = ttk.Button(top , text = "三角形" , command= sanjiaoxing_tkinter)
Button4.pack()
text77 = ttk.Label(top , text = "-----------------------------------------------------")
text77.pack()
text5 = ttk.Label(top , text = "公式查询")
text5.pack()
text88 = ttk.Label(top , text = "-----------------------------------------------------")
text88.pack()
Button5 = ttk.Button(top , text = "公式查询" , command = gongshichaxun_tkinter)
Button5.pack()
top.mainloop()
