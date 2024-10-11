from fpdf import FPDF
from tkinter import *
from tkinter import messagebox
import pyqrcode

class PDFCV(FPDF):
    def header(self):
        self.image("PDF Generation/CV Generator/mywebsite.png",10,8,33,title="Portfolio Site")

    def generate_cv(self,name,email,phone_number,address,skills,work_experience,education,about_me):
        self.add_page()
        self.ln(20)

        #Name
        self.set_font("Arial","B",26)
        self.cell(0,10,name,new_x="LMARGIN",new_y="NEXT",align="C")

        #region Contact Information
            # Header
        self.set_font("Arial","BU",16)
        self.cell(0,10,"Contact Information",new_x="LMARGIN",new_y="NEXT",align="L")
            # Content
        self.set_font("Arial","",12)
        self.cell(0,5,"Email: {}".format(email),new_x="LMARGIN",new_y="NEXT")
        self.cell(0,5,"Phone: {}".format(phone_number),new_x="LMARGIN",new_y="NEXT")
        self.cell(0,5,"Address: {}".format(address),new_x="LMARGIN",new_y="NEXT")
        #endregion

        #region Skills
            # Header
        self.ln(10)
        self.set_font("Arial","BU",16)
        self.cell(0,10,"Skills",new_x="LMARGIN",new_y="NEXT",align="L")
            # Content
        self.set_font("Arial","",12)
        for skill in skills:
            self.cell(0,5,"- {}".format(skill),new_x="LMARGIN",new_y="NEXT")
        #endregion

        #region Work Experience
            # Header
        self.ln(10)
        self.set_font("Arial","BU",16)
        self.cell(0,10,"Work Experience",new_x="LMARGIN",new_y="NEXT",align="L")
            # Content
        self.set_font("Arial","",12)
        for experience in work_experience:
            self.cell(0,5,"{}: {}".format(experience["title"],experience["description"]),new_x="LMARGIN",new_y="NEXT")
        #endregion

        #region Education
            # Header
        self.ln(10)
        self.set_font("Arial","BU",16)
        self.cell(0,10,"Education",new_x="LMARGIN",new_y="NEXT",align="L")
            # Content
        self.set_font("Arial","",12)
        for education_item in education:
            self.cell(0,5,"{}: {}".format(education_item["degree"],education_item["university"]),new_x="LMARGIN",new_y="NEXT")
        #endregion

        #region About Me
            # Header
        self.ln(10)
        self.set_font("Arial","BU",16)
        self.cell(0,10,"About Me",new_x="LMARGIN",new_y="NEXT",align="L")
            # Content
        self.set_font("Arial","",12)
        self.multi_cell(0,5,about_me)
        #endregion

        self.output("PDF Generator/CV Generator/cv1.pdf")

def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone_number = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()

    #Sort Skills
    #Line 1, Col 0, continue until END,  Remove White space before and after, seperate entries with new line
    skills = entry_skills.get("1.0",END).strip().split('\n')

    #region Work Experience
    work_experience = []
    work_experience_lines = entry_experience.get("1.0",END).strip().split('\n')
    for line in work_experience_lines:
        title,description = line.split(":")
        work_experience.append({'title':title.strip(),'description':description.strip()})
    #endregion

    #region Education
    education = []
    eduction_lines = entry_education.get("1.0",END).strip().split('\n')
    for line in eduction_lines:
        degree,university = line.split(":")
        education.append({'degree':degree.strip(),'university':university.strip()})
    #endregion

    #About Me
    about_me = entry_about_me.get("1.0",END)

    #Create QR Code
    qrcode = pyqrcode.create(website)
    qrcode.png("PDF Generation\CV Generator\mywebsite.png",scale=6) 
    
    #Input Validation
    if not name or not email or not phone_number or not address or not skills or not education or not work_experience or not about_me:
        messagebox.showerror("Error","Please fill in every field")
        return

    #Pass all info to class
    cv = PDFCV()
    cv.generate_cv(name,email,phone_number,address,skills,work_experience,education,about_me)


###################################################################################################################

window = Tk()
window.title("CV Generator")
window.geometry("325x725")
#region Contact Information
    #region Name Input
label_name = Label(window,text="Name: ")
label_name.pack()
entry_name = Entry(window,width=25)
entry_name.pack()
    #endregion

    #region Email Input
label_email = Label(window,text="Email: ")
label_email.pack()
entry_email = Entry(window,width=25)
entry_email.pack()
    #endregion

    #region Phone Input
label_phone = Label(window,text="Phone: ")
label_phone.pack()
entry_phone = Entry(window,width=25)
entry_phone.pack()
    #endregion

    #region Address Input
label_address = Label(window,text="Address: ")
label_address.pack()
entry_address = Entry(window,width=25)
entry_address.pack()
    #endregion

    #region Portfolio/Website Input
label_website = Label(window,text="Website: ")
label_website.pack()
entry_website = Entry(window,width=25)
entry_website.pack()
    #endregion
#endregion

#region Skills/Education/Work Experience/About Me
    #region Skills Input
label_skills = Label(window,text="Skills")
label2_skills = Label(window,text="(Enter one skill per line):")
label_skills.pack()
label2_skills.pack()
entry_skills = Text(window,height=5,width=30)
entry_skills.pack()
    #endregion

    #region Education Input
label_education = Label(window,text="Education")
label2_education = Label(window,text="(One per line in format 'Degree: University'):")
label_education.pack()
label2_education.pack()
entry_education = Text(window,height=5,width=30)
entry_education.pack()
    #endregion

    #region Work Experience Input
label_experience = Label(window,text="Work Experience")
label2_experience = Label(window,text="(One per line in format 'Title: Description'):")
label_experience.pack()
label2_experience.pack()
entry_experience = Text(window,height=5,width=30)
entry_experience.pack()
    #endregion

    #region About Me Input
label_about_me = Label(window,text="About Me:")
label_about_me.pack()
entry_about_me = Text(window,height=5,width=30)
entry_about_me.pack()
    #endregion
#endregion

#region Generate button
button_generate = Button(window, text="Generate CV",width=20,command=generate_cv_pdf)
button_generate.pack()
#endregion

window.mainloop()