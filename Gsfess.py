def about():
    print("-" * 100)
    print("""此软件是由张峻熙制作
    Gsfess 3.1 for windows
    Use python""")


def zh_cn():
    print("-" * 100)
    print("""你好，欢迎使用Gsfess 3.1，下面是选项菜单：
-------------------------
:      [立体图形]         :
-------------------------
1.1正方体
1.2长方体
1.3圆柱体
-------------------------
:      [平面图形]        :
-------------------------
2.1圆形
2.2长方形
2.3正方形
2.4平行四边形
2.5梯形
2.6三角形
-------------------------
:       [公式查询]        :
-------------------------
3.1公式查询
-------------------------
:        [退出]          :
-------------------------
0.Exit

""")
    print("-" * 100)


def liti_cube():
    print("""菜单：
1.体积
2.表面积""")
    int_liti_cube = input("请输入你的选项:")
    if int_liti_cube == "1":
        cube = float(input("请输入边长："))
        liti_cube_resuit = cube * cube * cube
        print(liti_cube_resuit)
        input("按回车继续. . .")
    if int_liti_cube == "2":
        cube_2 = float(input("请输入边长："))
        liti_cube_resuit_2 = cube_2 * cube_2 * 6
        print(liti_cube_resuit_2)
        input("按回车继续. . .")


def liti_cuboid():
    print("""菜单：
1.体积
2.表面积""")
    int_liti_cuboid = input("请输入你的选项：")
    if int_liti_cuboid == "1":
        cuboid_chang = float(input("请输入长："))
        cuboid_kuan = float(input("请输入宽："))
        cuboid_gao = float(input("请输入高："))
        cuboid_jieguo = cuboid_chang * cuboid_kuan * cuboid_gao
        print(cuboid_jieguo)
        input("按回车继续. . .")
    elif int_liti_cuboid == "2":
        cuboid_chang2 = float(input("请输入长："))
        cuboid_kuan2 = float(input("请输入宽："))
        cuboid_gao2 = float(input("请输入高："))
        cuboid_jieguo2 = (cuboid_chang2 * cuboid_kuan2 + cuboid_chang2 * cuboid_gao2 + cuboid_kuan2 * cuboid_gao2)
        print(cuboid_jieguo2)
        input("按回车继续. . .")


def liti_yuanzu():
    print("""菜单：
1.体积
2.表面积""")
    int_liti_yuanzhu = input("请输入你的选项：")
    pai = 3.14
    if int_liti_yuanzhu == "1":
        yuanzhu_gao = float(input("请输入高："))
        yuanzhu_banjing = float(input("请输入半径："))
        juanzhu_tiji_jieguo = (pai * yuanzhu_banjing * yuanzhu_banjing) * yuanzhu_gao
        print(juanzhu_tiji_jieguo)
        input("按回车继续. . .")
    elif int_liti_yuanzhu == "2":
        yuanzhu_gao2 = float(input("请输入高："))
        yuanzhu_banjing2 = float(input("请输入半径："))
        juanzhu_tiji_jieguo2 = (2 * pai * yuanzhu_banjing2 * yuanzhu_gao2) + (
                2 * pai * yuanzhu_banjing2 * yuanzhu_banjing2)
        print(juanzhu_tiji_jieguo2)
        input("按回车继续. . .")


# 以下为平面图形
def pingmian_yuanxing():
    print("""菜单：
1.周长
2.面积""")
    pingmian_xuanze = input("请输入您的操作：")
    if pingmian_xuanze == "1":
        yuanxing_banjing = float(input("请输入半径："))
        yuanxing_jieguo = 2 * 3.14 * yuanxing_banjing
        print(yuanxing_jieguo)
        input("按回车继续. . .")
    if pingmian_xuanze == "2":
        yuanxing_banjing2 = float(input("请输入半径："))
        yuanxing_jieguo2 = 3.14 * yuanxing_banjing2 * yuanxing_banjing2
        print(yuanxing_jieguo2)
        input("按回车继续. . .")


def pingmian_changfangxing():
    print("""菜单：
1.周长
2.面积""")
    changfangxing_if = input("请输入你的选择：")
    if changfangxing_if == "1":
        changfangxing_chang = float(input("请输入长："))
        chamgfangxing_kuan = float(input("请输入宽："))
        changfangxing_jieguo = (changfangxing_chang + chamgfangxing_kuan) * 2
        print(changfangxing_jieguo)
        input("按回车继续. . .")
    if changfangxing_if == "2":
        changfangxing_chang2 = float(input("请输入长："))
        chamgfangxing_kuan2 = float(input("请输入宽："))
        changfangxing_jieguo2 = changfangxing_chang2 * chamgfangxing_kuan2
        print(changfangxing_jieguo2)
        input("按回车继续. . .")


def pingmian_pingxingsibianxing():
    print("此图形仅有面积计算")
    pingxingsibianxing_di = float(input("请输入底："))
    pingxingsibianxing_gao = float(input("请输入高："))
    pingxingsibianxing_jieguo = pingxingsibianxing_di * pingxingsibianxing_gao
    print(pingxingsibianxing_jieguo)
    input("按回车继续. . .")


def pingmian_tixing():
    print("此图形仅有面积计算")
    tixing_shangdi = float(input("请输入上底："))
    tixing_xiadi = float(input("请输入下底："))
    tixing_gao = float(input("请输入高："))
    tixing_jieguo = (tixing_shangdi + tixing_xiadi) * tixing_gao / 2
    print(tixing_jieguo)
    input("按回车继续. . .")


def pingmian_sanjiaoxing():
    print("此图形仅有面积计算")
    sanjiaoxing_di = float(input("请输入底："))
    sanjiaoxing_gao = float(input("请输入高："))
    sanjiaoxing_jieguo = sanjiaoxing_di * sanjiaoxing_gao / 2
    print(sanjiaoxing_jieguo)
    input("按回车继续. . .")


def pingmian_zhengfangxing():
    # 正方形
    print("""选项菜单：
    1.面积
    2.周长""")
    pingmian_zhengfangxing_if = input("请输入你的选择：")
    if pingmian_zhengfangxing_if == "1":
        pingmian_zhengfangxing_bianchang_mianji = float(input("请输入您的边长:"))
        jieguo = pingmian_zhengfangxing_bianchang_mianji * pingmian_zhengfangxing_bianchang_mianji
        print(jieguo)
        input("按回车继续. . .")
    if pingmian_zhengfangxing_if == "2":
        pingmian_zhengfangxing_bianchang_zhouchang = float(input("请输入您的边长:"))
        jieguo2 = pingmian_zhengfangxing_bianchang_zhouchang * 4
        print(jieguo2)
        input("按回车继续. . .")


# 这是一个公式查询的函数
def gongshi():
    print("""公式列表：
1.正方形周长
2.正方形面积
3.长方形周长
4.长方形面积
5.三角形面积
6.平行四边形面积
7.正方体体积
8.正方体棱长总和
9.正方体表面积
10.长方体体积
11.长方体棱长总和
12.长方体表面积
13.圆柱体积
14.圆柱表面积
15.圆锥体积""")
    gongshi = int(input("请输入您要执行的操作："))
    if gongshi == 1:
        print("正方形周长 = 边长 * 4")
        input()
    if gongshi == 2:
        print("正方形面积 = 边长 * 边长")
        input()
    if gongshi == 3:
        print("长方形周长 = （长 + 宽） * 2")
        input()
    if gongshi == 4:
        print("长方形面积 = 长 * 宽")
        input()
    if gongshi == 5:
        print("三角形面积 = 底 * 高 / 2")
        input()
    if gongshi == 6:
        print("平行四边形面积 = 底 * 高")
        input()
    if gongshi == 7:
        print("正方形体积 = 边长 * 边长 * 边长")
        input()
    if gongshi == 8:
        print("正方形棱长总和 = 边长 * 12")
        input()
    if gongshi == 9:
        print("正方形表面积 = 边长 * 边长 * 6")
        input()
    if gongshi == 10:
        print("长方体体积 = 长 * 宽 * 高")
        input()
    if gongshi == 11:
        print("长方体棱长总和 = （长 + 宽 + 高） * 4")
        input()
    if gongshi == 12:
        print("长方体表面积 = （长 * 宽 + 长 * 高 + 宽 * 高） * 2")
        input()
    if gongshi == 13:
        print("底面积 * 高")
        input()
    if gongshi == 14:
        print("底面积 * 2 + 侧面积")
        input()
    if gongshi == 15:
        print("底面积 * 高 / 3")
        input()


# 定义循环条件
var = 0

# 这是一个主程序（main）
while var == 0:
    zh_cn()
    var2 = input("请输入您要执行的操作：")
    if var2 == "1.1":
        liti_cube()
    if var2 == "1.2":
        liti_cuboid()
    if var2 == "1.3":
        liti_yuanzu()
    if var2 == "2.1":
        pingmian_yuanxing()
    if var2 == "2.2":
        pingmian_changfangxing()
    if var2 == "2.3":
        pingmian_zhengfangxing()
    if var2 == "2.4":
        pingmian_pingxingsibianxing()
    if var2 == "2.5":
        pingmian_tixing()
    if var2 == "2.6":
        pingmian_sanjiaoxing()
    if var2 == "0":
        break
    if var2 == "3.1":
        gongshi()
    if var2 == "about":
        about()
