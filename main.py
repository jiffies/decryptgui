
from time import sleep
import win32gui
import win32api
import win32con

def editSetText(hwndEdit, testStr):
    #WM_SETTEXT不能用PostMessage，PostMessage参数中不能有指针。异步消息，不等待
    rst = win32gui.SendMessageTimeout(hwndEdit, win32con.WM_SETTEXT, 0, testStr, win32con.SMTO_NORMAL, 1000)
    if rst[0]==1 and rst[1]==1:
        return True
    return False

#点击按钮
def buttonClickFunc1(hwnBbutton):
    '''点击按钮方法1，SendMessage也可用'''
    rstDown = win32gui.PostMessage(hwnBbutton, win32con.WM_LBUTTONDOWN, 0, 0)
    rstUp = win32gui.PostMessage(hwnBbutton, win32con.WM_LBUTTONUP, 0, 0)
    if rstDown and rstUp is not None:
        return False
    return True
i = 804
while 1:
    title = '请输入密码以继续解压,资源编号X1004'
    hwnd = win32gui.FindWindow(None, title)
    if hwnd != 0:
        print(f'找到密码输入窗口, {hwnd}')
    else:
        print('没有找到窗口')
        break

    subHandle = win32gui.FindWindowEx(hwnd, 0, "TNewEdit", None)
    if subHandle != 0:
        print(f'找到密码输入控件, {subHandle}')
    else:
        print('没有找到控件')
        break

    # win32api.SendMessageTimeout(subHandle, win32con.WM_SETTEXT, None, "lcq".encode("gbk"), win32con.SMTO_NORMAL, 1000)
    answer = f'{i:06d}'
    print(f"本次密码：{answer}")
    editSetText(subHandle, answer)
    b1 = win32gui.FindWindowEx(hwnd, 0, "TNewButton", "确认输入 (&O)")
    if b1 != 0:
        #print(f'找到TNewButton, {b1}')
        print(win32gui.GetWindowText(b1))
    else:
        print('没有TNewButton')
        break
    # print("点击确认输入")
    buttonClickFunc1(b1)
    sleep(0.4)

    errHandle = win32gui.FindWindow(None, "安装向导")
    if errHandle != 0:
        # print(f'找到安装向导, {errHandle}')
        1 + 1
    else:
        print('没有找到安装向导')
        break


    errHandle2 = win32gui.FindWindowEx(errHandle, 0, "Static", None)
    if errHandle2 != 0:
        print(f'密码输入错误, {errHandle2}\n')
        b = win32gui.FindWindowEx(errHandle, 0, "Button", None)
        if b != 0:
            # print(f'找到确定,点击 {b}')
            buttonClickFunc1(b)
            sleep(0.4)

        else:
            print('没有找到确定')
            break
    else:
        print('没有找到密码输入错误')
        break
    i+=1

