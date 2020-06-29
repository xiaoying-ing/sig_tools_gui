# -*- coding:utf-8 -*-

"""
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   tools_ui.py

@Time    :   2020/6/10 16:57

@Desc    :

"""
import tkinter as tk
import tkinter.filedialog
import os

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('签名工具v1.0')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x400')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='grey', fg='white', font=('Arial', 10), width=80, height=3)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False


def hit_me():
    global on_hit
    global a_p
    if on_hit is False:
        on_hit = True
        var.set('打开文件')
        a_p = tkinter.filedialog.askopenfilename()
        if not a_p.endswith(".apk"):
            var.set("抱歉，该文件不是apk文件")
        elif a_p.endswith(".apk"):
            print(a_p)
            var.set(a_p)
            # return a_p
    # else:
    #     on_hit = False
    #     var.set(None)


# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='选择文件', font=('Arial', 12), width=10, height=1, command=hit_me)
b.place(x=200, y=60)
s = tk.Label(window, text="signatureScheme", font=('Arial', 14))
s.place(x=0, y=120)

var_1 = tk.StringVar()
var_1.set("v1v2")

signatureScheme = "v1v2"


def sel():
    if var_1.get() == 'v1':
        signatureScheme = "v1"
        return signatureScheme
    elif var_1.get() == 'v2':
        signatureScheme = "v2"
        return signatureScheme
    elif var_1.get() == "v1v2":
        signatureScheme = "v1v2"
        return signatureScheme


R1 = tk.Radiobutton(window, text="v1", variable=var_1, value='v1', command=sel)
R1.place(x=180, y=120)
R2 = tk.Radiobutton(window, text="v2", variable=var_1, value='v2', command=sel)
R2.place(x=250, y=120)
R3 = tk.Radiobutton(window, text="v1v2", variable=var_1, value='v1v2', command=sel)
R3.place(x=320, y=120)

var_2 = tk.IntVar()
var_2.set(None)
var_3 = tk.IntVar()
var_3.set(None)
zipalign = None


def print_zipalign():
    try:
        if var_2.get() == 1:
            zipalign = "zipalign"
            print(zipalign)
            return zipalign
        elif var_2.get() is None:
            zipalign = None
            return zipalign
    except:
        pass


c2 = tk.Checkbutton(window, text='zipalign', variable=var_2, onvalue=1, offvalue=0, command=print_zipalign)
c2.place(x=150, y=200)
del_sig = None


def print_sig_del():
    try:
        if var_3.get() == 1:
            del_sig = "d"
            print(del_sig)
            return del_sig
        elif var_3.get() is None:
            del_sig = None
            return del_sig
    except:
        pass


c3 = tk.Checkbutton(window, text='删除第三方签名', variable=var_3, onvalue=1, offvalue=0, command=print_sig_del)
c3.place(x=280, y=200)


def del_apk_sig(apk_file_path):
    os.system("zip -d " + apk_file_path + " META-INF/*")


def sig_tools(apk_path, keytype="jks", signatureScheme=None, zipalign=None, sig_del=None) -> str:
    global keytype_opt
    initial_str = 'java -jar'
    jar_dic_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jar_dic")
    jar_dic_list = os.listdir(jar_dic_path)
    jar_path = os.path.join(jar_dic_path, jar_dic_list[0])
    jar_opt = "sign"
    if keytype == "jks":
        keytype_opt = "--keytype jks"
    elif keytype == "pk8":
        keytype_opt = "--keytype pk8"
    unsign_apk_opt = "--apk " + apk_path
    apk_path_list = apk_path.split('\\')
    # print(apk_path_list)
    list_signapk_name = list(apk_path_list[-1])
    list_signapk_name.insert(-4, "_sign")

    if signatureScheme == "v1":
        list_signapk_name.insert(-4, "_v1")
        signatureScheme_opt = "--signatureScheme " + signatureScheme
    elif signatureScheme == "v2":
        list_signapk_name.insert(-4, "_v2")
        signatureScheme_opt = "--signatureScheme " + signatureScheme
    elif signatureScheme is None or signatureScheme == "v1v2":
        list_signapk_name.insert(-4, "_v1v2")
        signatureScheme_opt = "--signatureScheme " + "v1v2"
    else:
        print("signatureScheme传入错误，按默认值处理！")
        list_signapk_name.insert(-4, "_v1v2")
        signatureScheme_opt = "--signatureScheme " + "v1v2"

    str_sign_apkname = "".join(list_signapk_name)
    # print(str_sign_apkname)
    sign_apk_path = str_sign_apkname.replace("/", r'\\')
    # print(sign_apk_path)
    sign_apk_opt = "--out " + sign_apk_path
    keystore_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resource") + "\\gylr.jks"
    keystore_opt = "--keystore " + keystore_path
    ailas_opt = "--alias  androiddebugkey"
    storepass_opt = "--storepass android"
    keypass_opt = "--keypass android"
    sigAlg_opt = "--sigAlg SHA1withRSA"

    if sig_del is None:
        print("无需删除第三方签名")
    elif sig_del == "d":
        del_apk_sig(apk_path)
        print("删除第三方签名成功！")
        list_signapk_name.insert(-4, "_d")
        str_sign_apkname = "".join(list_signapk_name)
        sign_apk_path = str_sign_apkname.replace("/", r'\\')
        sign_apk_opt = "--out " + sign_apk_path
    elif sig_del != "d" or sig_del is not None:
        print("删除第三方签名选项输入error,不删除第三方签名")

    if zipalign is None or zipalign != "zipalign":
        command_list = [initial_str, jar_path, jar_opt, keytype_opt, unsign_apk_opt, sign_apk_opt, keystore_opt,
                        ailas_opt,
                        storepass_opt, keypass_opt, sigAlg_opt, signatureScheme_opt]
        # print(command_list)
        command = " ".join(command_list)
        print("签名成功，路径", sign_apk_path.replace(r"\\", "/"))
        return command
    elif zipalign == "zipalign":
        list_signapk_name.insert(-4, "_zipalign")
        str_sign_apkname = "".join(list_signapk_name)
        sign_apk_path = str_sign_apkname.replace("/", r'\\')
        sign_apk_opt = "--out " + sign_apk_path
        command_list = [initial_str, jar_path, jar_opt, keytype_opt, unsign_apk_opt, sign_apk_opt, keystore_opt,
                        ailas_opt,
                        storepass_opt, keypass_opt, sigAlg_opt, signatureScheme_opt, "--zipalign " + "zipalign"]
        # print(command_list)
        command = " ".join(command_list)
        print("签名成功，路径", sign_apk_path.replace(r"\\", "/"))
        return command


def sig_apk():
    # list_ap = str(a_p).split(r"/")
    apk_path = a_p
    # print(apk_path)
    signatureScheme_command = sel()
    zipalign_command = print_zipalign()
    del_sig_command = print_sig_del()
    command = sig_tools(apk_path, signatureScheme=signatureScheme_command, zipalign=zipalign_command, sig_del= del_sig_command)
    os.system(command)
    print(command.split(" ")[9].replace(r"\\", "/"))
    # print(command)
    var_4.set("路径{}".format(command.split(" ")[9].replace(r"\\", "/")))


s_a = tk.Button(window, text='应用签名', font=('Arial', 12), width=10, height=1, command=sig_apk)
s_a.place(x=200, y=270)


var_4 = tk.StringVar()
l_2 = tk.Label(window, textvariable=var_4, bg='grey', fg='white', font=('Arial', 10), width=80, height=3, anchor=tk.NW)
l_2.place(x=0, y=340)

# 第6步，主窗口循环显示
window.mainloop()
