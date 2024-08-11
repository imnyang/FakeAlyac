import pystray
from PIL import Image
import sys, os, webbrowser, subprocess

# 전역 변수 초기화
state = True

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def create_image():
    return Image.open(resource_path("app.ico"))

def mode(icon, item):
    global state
    state = not item.checked

def on_clicked(icon, item):
    if item.text == '환경설정':
        webbrowser.open('ms-settings:')
    elif item.text == '제품정보':
        webbrowser.open('https://altools.co.kr/product/ALYAC')
    elif item.text == '업데이트':
        webbrowser.open('ms-settings:windowsupdate-action')
    elif item.text == 'PC최적화':
        webbrowser.open('cleanmgr')
    elif item.text == '알약 열기':
        webbrowser.open('windowsdefender://open')
    elif item.text == '빠른검사':
        webbrowser.open('windowsdefender://quickscan')
    elif item.text == '정밀검사':
        webbrowser.open('windowsdefender://fullscan')
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def exit_program(icon, item):
    icon.stop()
    sys.exit()

# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(
    '알약2.5 공개용 (실시간 감시 On)\n마지막 업데이트 확인 : 업데이트 내역없음',
    icon=create_image(),
    menu=pystray.Menu(
        pystray.MenuItem('알약 열기', on_clicked),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('업데이트', on_clicked),
        pystray.MenuItem('빠른검사', on_clicked),
        pystray.MenuItem('정밀검사', on_clicked),
        pystray.MenuItem('PC최적화', on_clicked),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('실시간감시', mode, checked=lambda item: state),
        pystray.MenuItem('게임모드', mode, checked=lambda item: state),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('환경설정', on_clicked),
        pystray.MenuItem('제품정보', on_clicked),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('알약 종료', exit_program)
    ),
    title='알약2.5 공개용 (실시간 감시 On)\n마지막 업데이트 확인 : 업데이트 내역없음'
)

icon.run()