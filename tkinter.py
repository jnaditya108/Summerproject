import os
import pywhatkit as kit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas
import speech_recognition as sr
import pyttsx3

import cv2
import boto3
import webbrowser

def instance():
    myec2=boto3.client("ec2","ap-south-1")
    Launch=myec2.run_instances(
    ImageId="",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1

    )
def feature():
    import pywhatkit as kit

    from cvzone.HandTrackingModule import HandDetector
    import mediapipe
    import cvzone
    import cv2
    import os
    cap=cv2.VideoCapture(0)

    def msg(num,msg):
        number = num
        message = msg
        kit.sendwhatmsg_instantly(number,message,10)  
    def msg(num,msg,path):
        number = num
        message = msg
        kit.sendwhatmsg_instantly(number,message,10) 

    while True :
        status,image=cap.read()
        cv2.imshow("hii2",image)
        if cv2.waitKey(50)==13:
            break
        det=HandDetector()
        handphoto=det.findHands(image,draw=False)
        if handphoto:
        
            lmlist=handphoto[0]
            fs=det.fingersUp(lmlist)
            if fs ==[1,1,1,1,1]:
                cv2.imwrite("savedimage.png",image)
                kit.sendwhats_image("+917733935772", "savedimage.png", "help!!")
                break
            if cv2.waitKey(10)==13:
                break
    
    cv2.destroyAllWindows()

def create_s3_bucket(bucket_name, region='ap-south-1'):

    try:
        s3_client = boto3.client('s3', region_name=region)
        
        # If the region is 'us-east-1', do not specify a location constraint
        location_constraint = region if region != 'us-east-1' else ''
        
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': location_constraint
            }
        )
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket '{bucket_name}': {e}")    

def open_game_link(game_link):
    webbrowser.open(game_link)
def img():
    op=cv2.VideoCapture(0)
    status,pic=op.read()
    cv2.imshow("hello",pic)
    cv2.waitKey()
    cv2.destroyAllWindows()
def img2():
    op=cv2.VideoCapture(0)
    while True :
        status,pic2=op.read()
        cv2.imshow("hello2",pic2)
        if cv2.waitKey(10)==13 :
            break
     
    cv2.destroyAllWindows()
def open_calendar():
    os.system("start outlookcal:")

def open_chrome():
    os.system("start chrome")

def open_file_explorer():
    os.system("start explorer")

def open_command_prompt():
    os.system("start cmd")

def open_control_panel():
    os.system("start control")

def open_task_manager():
    os.system("start taskmgr")

def open_system_settings():
    os.system("start ms-settings:")

def capture_image():
    image = ImageGrab.grab()
    image.show()

def send_whatsapp_message():
    number = "+917739318770"
    message = "Hi, this is a WhatsApp message sent using Python!"
    kit.sendwhatmsg(number,message,14, 50, 15)  

def send_mail():
    from_email = "azfaralam440@gmail.com"
    to_email = "adityajn108@gmail.com"
    password = ""  

    subject = "Test Email from Python by azfar"
    body = "This is a test email sent using Python."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Unable to send email.\n" + str(e))

def send_sms():
    account_sid = ''
    auth_token =  ''
    from_phone = ''
    to_phone = ""  

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body="This is a test SMS sent using Twilio and Python!",
            from_=from_phone,
            to=to_phone
        )
        messagebox.showinfo("Success", "SMS sent successfully!: " + message.sid)
    except Exception as e:
        messagebox.showerror("Error", "Unable to send SMS.\n" + str(e))
def ASSI():
    r = sr.Recognizer()
    flag=1
    while(flag):
	
        try:
            r = sr.Recognizer()
		
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print(" 🤖 Hii i am your robo //")
                print("What can i do for you ")

			
                audio2 = r.listen(source2)
			
			
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print()
                print("Did you say ",MyText)
                ch=MyText
                if "notepad" in ch:
                    os.system("notepad")
                    print("Sure..")
                elif "brave" in ch:
                    os.system("Brave.lnk")
                    print("Sure..")
                elif "youtube" in ch:
                    os.system("Youtube.lnk")
                    print("Sure..")
                elif "excel" in ch:
                    os.system("Excel.lnk")
                    print("Sure..")
                elif "pc management" in ch:
                    os.system("compmgmt.msc")
                elif "instance" in ch:
                    instance()
                    print("Sure..")
                elif "edge" in ch:
                    os.system("start microsoft-edge:")
                    print("Sure..")
                elif "chrome" in ch:
                    os.system("start chrome")
                    print("Sure..")
                else:
                    print("i did'nt get that**//")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
		
        except sr.UnknownValueError:
            print("unknown error occurred")
        flag=flag-1
def assistance():
    
    choice = choice_var.get()
    root = tk.Tk()
    root.configure(bg="lightblue")
    label_font = ("Arial", 20)
    button_font = ("Arial", 16)
    button_text_color = "white"
    button_bg_color = "blue"
 

    
    if choice == 1:
        open_calendar()
    elif choice == 2:
        open_chrome()
    elif choice == 3:
        open_file_explorer()
    elif choice == 4:
        open_command_prompt()
    elif choice == 5:
        open_control_panel()
    elif choice == 6:
        open_task_manager()
    elif choice == 7:
        open_system_settings()
    elif choice == 8:
        capture_image()
    elif choice == 9:
        send_whatsapp_message()
    elif choice == 10:
        send_mail()
    elif choice == 11:
        send_sms()
    elif choice == 12:
        os.system("youtube.lnk")
    elif choice == 13:
        img()   
    elif choice == 14:
        img2()   
    elif choice == 15:
        os.system("explorer http://65.0.130.148/ser.html")
    elif choice == 16:
        os.system("explorer http://65.0.130.148/ser2.html")
    elif choice == 17:
        instance()
    elif choice == 18:
        bucket_name = '2234ytfdsdxzxz'
        create_s3_bucket(bucket_name)  
    elif choice == 19:
        ASSI()        
    elif choice == 0:
        root.quit()
    else:
        messagebox.showerror("Invalid Choice", "Please select a valid option.")

root = tk.Tk()
root.title("Assistant")
root.geometry("1000x1000")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

label_font = ("Arial", 20)
button_font = ("Arial", 16)
button_text_color = "white"
button_bg_color = "blue"
choice_var = tk.IntVar()

#bg = tk.PhotoImage(file = "cera.jpg")

ttk.Label(frame, text="How can I help you ?").pack()

button_subway_surfers = tk.Button(root, text="Subway Surfers", command=lambda: open_game_link("https://poki.com/en/g/subway-surfers"), font=button_font, fg=button_text_color, bg=button_bg_color)
button_subway_surfers.pack(pady=10)
button_temple_run = tk.Button(root, text="Temple Run 2", command=lambda: open_game_link("https://poki.com/en/g/temple-run-2-spooky-summit"), font=button_font, fg=button_text_color, bg=button_bg_color)
button_temple_run.pack(pady=10)
button_temple_run = tk.Button(root, text="Shooting game", command=lambda: open_game_link("https://krunker.io/"), font=button_font, fg=button_text_color, bg=button_bg_color)
button_temple_run.pack(pady=10)
ttk.Radiobutton(frame, text="OPEN CALENDER", variable=choice_var, value=1).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN CHROME", variable=choice_var, value=2).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN FILE EXPLORER", variable=choice_var, value=3).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN COMMAND PROMPT", variable=choice_var, value=4).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN CONTROL PANNEL", variable=choice_var, value=5).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN TASK MANAGER", variable=choice_var, value=6).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN SYSTEM SETTINGS", variable=choice_var, value=7).pack(anchor='w')
ttk.Radiobutton(frame, text="CAPTURE IMAGE", variable=choice_var, value=8).pack(anchor='w')
ttk.Radiobutton(frame, text="SEND WHATSAPP MESSAGE", variable=choice_var, value=9).pack(anchor='w')
ttk.Radiobutton(frame, text="SEND EMAIL", variable=choice_var, value=10).pack(anchor='w')
ttk.Radiobutton(frame, text="SEND SMS", variable=choice_var, value=11).pack(anchor='w')
ttk.Radiobutton(frame, text="RUN YOUTUBE", variable=choice_var, value=12).pack(anchor='w')
ttk.Radiobutton(frame, text="IMAGE CAPTURE", variable=choice_var, value=13).pack(anchor='w')
ttk.Radiobutton(frame, text="VIDEO CAPTURE", variable=choice_var, value=14).pack(anchor='w')
ttk.Radiobutton(frame, text="MAKE GOOGLE SEARCH", variable=choice_var, value=15).pack(anchor='w')
ttk.Radiobutton(frame, text="MAKE A YOUTUBE SEARCH", variable=choice_var, value=16).pack(anchor='w')
ttk.Radiobutton(frame, text="MAKE A NEW INSTANCE", variable=choice_var, value=17).pack(anchor='w')
ttk.Radiobutton(frame, text="MAKE A NEW S3 BUCKET", variable=choice_var, value=18).pack(anchor='w')
ttk.Radiobutton(frame, text="OPEN VOICE ASSISTANT", variable=choice_var, value=19).pack(anchor='w')
ttk.Button(frame, text="Submit", command=assistance).pack(pady=10)
ttk.Button(frame, text="feature", command=feature).pack(pady=10)
root.mainloop()
