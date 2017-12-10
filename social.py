import urllib2
import socket
import fcntl
import struct
import facebook

import os
import thread
from util_module import *
from MyGmailObject import *


def en_decrypt_char(KEY, val):
    if 127 > val > 31:
        return ((val - 32) + (2 * 95) + KEY) % 95 + 32
    else:
        return val


def en_decrypt_string(KEY, str_s):
    modified_str = []
    for i in range(len(str_s)):
        c = chr(en_decrypt_char(KEY, ord(str_s[i])))
        modified_str.append(c)
        modified_str = "".join(modified_str)
    return modified_str


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
    )[20:24])


def getLatestNotificationFrom(notificationsNode):
    try:
        key = 'data'
        if key in notificationsNode:
            latestNotification = notificationsNode[key][0]
        return latestNotification['title']
    except:
        return 'NO NEW NOTIFICATIONS'


def lcd_string_print(string,line,length):
    for x in range(0, len(string)-length):
        lcd_string(string[x:x+length],line)
    print string[x:x+length]
    time.sleep(0.45)

ip = get_ip_address('wlan0')

authentication = False

displayNotifications = False

while not displayNotifications:
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
        print "Not Connected"
        time.sleep(1)
    else:
        print("Connected")
        while (not authentication):
            OFF()
            hasNOTIFICATION = False
            lcd_string("IP ADDRESS",LCD_LINE_1)
            lcd_string(ip, LCD_LINE_2)
            time.sleep(2)
            #os.system('clear')
            lcd_string("Connect Facebook",LCD_LINE_1)
            lcd_string("&Gmail account",LCD_LINE_2)
            time.sleep(2)
            lcd_init()
            lcd_string("SSH to Device",LCD_LINE_1)
            lcd_string("Run oAuthorise",LCD_LINE_2)
            time.sleep(2)
            try:
                if os.stat("/home/pi/.login_notifier").st_size > 0:
                    login_file = open("/home/pi/.login_notifier",'r')
                    fb_token = login_file.readline()
                    fb_token = fb_token.rstrip('\n')
                    fb_token = en_decrypt_string(-10, fb_token)
                    print fb_token
                    gmail_username = login_file.readline()
                    gmail_username = gmail_username.rstrip('\n')
                    gmail_username = en_decrypt_string(-10, gmail_username)
                    print gmail_username
                    gmail_passwd = login_file.readline()
                    gmail_passwd = gmail_passwd.rstrip('\n')
                    gmail_passwd = en_decrypt_string(-10, gmail_passwd)
                    print gmail_passwd
                    gmail_access_token = login_file.readline()
                    gmail_access_token = gmail_access_token.rstrip('\n')
                    gmail_access_token = en_decrypt_string(-10, gmail_access_token)
                    print gmail_access_token
                    try:
                        graph = facebook.GraphAPI(fb_token)
                        notifications = graph.get_object("me/notifications")
                        myMail = MyGmailObject(gmail_username, gmail_passwd ,
                                               gmail_access_token)
                        myMail.get_latest_sender()
                        myMail.get_latest_subject()
                        authentication = True
                        displayNotifications = True
                    except:
                        print "Unsuccessful Login attempt"
                        authentication = False
                        displayNotifications = False
                else:
                    print "empty file"
            except OSError:
                print ""
    time.sleep(2)
try:
    thread.start_new_thread(turn_LEDS, ())
except:
    print 'unable to start thread'

lcd_init()

while displayNotifications :
    hasNOTIFICATION = True
    notifications = graph.get_object("me/notifications")
    fb_notf = getLatestNotificationFrom(notifications)
    lcd_string_print(fb_notf, LCD_LINE_1, 16)
    myMail = MyGmailObject(gmail_username, gmail_passwd , gmail_access_token)
    gmail_subj = myMail.get_latest_subject()
    print gmail_subj
    gmail_sender = myMail.get_latest_sender()
    lcd_string_print("from: " + gmail_sender.split('<')[0] + "Subject: " + gmail_subj + " ", LCD_LINE_2, 16)
