import time
import win32gui
import pyautogui
from loguru import logger


def match_windows(win_title):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            win_text = win32gui.GetWindowText(hwnd)
            # 模糊匹配
            if win_text.find(win_title) > -1:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    win32gui.SetForegroundWindow(hwnds[0])
    win32gui.SetActiveWindow(hwnds[0])
    time.sleep(1)
    return hwnds


def input_command(command=""):
    pyautogui.typewrite(command, interval=0.001)
    pyautogui.press('enter')

if __name__ == "__main__":
    match_windows("a.txt")
    input_command("#SpawnItem 12_Gauge_Birdshot 1")
