
from tkinter import *
import pyperclip

root = Tk()
root.title("Password Generator")


############################ functions ##########################

#F1  Developer passcode:
def CheckPasscode():
    check=DevPasscode.get()
    
    global vf_bool
    if check== "1234" :

        vf_bool =True
        
        
        
        
        label_verify = Label(root, text = "PASSCODE IS CORRECT",font=('Arial', 8),fg="green",padx=78,pady=3)
        label_verify.grid(row = 0, column=1)
        

        return label_verify,vf_bool
         
    else :
        
        label_verify = Label(root, text = "PASSCODE IS INCORRECT",font=('Arial', 8),fg="red",padx=73,pady=3)
        label_verify.grid(row = 0, column=1)
        
        vf_bool =False
        
        return vf_bool ,label_verify





#F2 Generate :
def Generate():
    
    if vf_bool ==True :
        
        SN= int(Serial_Number.get())

        #Factory:
        global fc
        fc = SN *4
        facLabel = Label(root,text= fc,fg="#191970")
        facLabel.grid(row=2,column=1)

        #service:
        global sr
        sr = SN *2
        serLabel = Label(root,text= sr,fg="#800000")
        serLabel.grid(row=3,column=1)



        
        return facLabel,serLabel
    elif vf_bool==False:
        return root.quit()




#F5 Clipboard Factory :
def Fac_Clipboard():
    pyperclip.copy(fc)
    return True







#F6 Clipboard Service :
def Ser_Clipboard():
    pyperclip.copy(sr)
    return True



###########################Labels & Entries##########################

#lbl1:

lbl1_DevPasscode = Label(root, text="Developer Passcode :",font=('arial', 10))
lbl1_DevPasscode.grid(row = 0, column= 0)



#entry1:

DevPasscode= Entry(root, width = 45,bg="#E8E8E8",borderwidth= 3)
DevPasscode.grid(row =0, column=1)



#lbl2:

lbl2_Serial=Label(root,text= "Enter Serial Number :",font=('arial', 10))
lbl2_Serial.grid(row=1,column= 0)



#entry2:

Serial_Number = Entry(root,width=45,bg="#E8E8E8",borderwidth= 3)
Serial_Number.grid(row =1, column=1)



#lbl3:

lbl3_FactoryPassword=Label(root,text= "Factory Password :",font=('Arial Rounded MT Bold', 10),fg="#191970")
lbl3_FactoryPassword.grid(row=2,column= 0)



#lbl4:

lbl4_ServicePassword=Label(root,text= "Service Password :",font=('Arial Rounded MT Bold', 10),fg="#800000")
lbl4_ServicePassword.grid(row=3,column= 0)



#lbl5:

lbl5_Rights= Label(root,text  = "Developer(Mr.Jvn)", font=("arial",7))
lbl5_Rights.grid(row=5,column=2)

#######################################################################


############################## Buttons #############################

#button1:

btn1_VerifyPass = Button(root, text= "Verify Dev Passcode",command= CheckPasscode, font=('arial', 10))
btn1_VerifyPass.grid(row=0,column= 2)



#button2:

btn2_Generate = Button(root, text= "Generate Passwords",command=Generate,width= 15,font=('arial', 10))
btn2_Generate.grid(row=1,column= 2)




#button3:

btn3_ClipboardFactory = Button(root, text= "Copy Factory" ,command=Fac_Clipboard,width= 15,font=('arial', 10))
btn3_ClipboardFactory.grid(row=2,column= 2)



#button4:

btn4_ClipboardService = Button(root, text= "Copy Service",command= Ser_Clipboard,width= 15,font=('arial', 10))
btn4_ClipboardService.grid(row=3,column= 2)


####################################################################

root.mainloop()



