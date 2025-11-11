import customtkinter
import customtkinter as ctk
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
selection = "homepage"

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    self.title("Park Manager")
    self.geometry("1920x1080")
    self. resizable(True, True)

    #navigation frame
    self.navframe = customtkinter.CTkFrame(self, corner_radius=0)
    self.navframe.grid(row=0, column=0, sticky="nsew")
    self.navframe.grid_rowconfigure(5, weight=1)
    self.navframe.grid_columnconfigure(3, weight=5)
    #label title
    self.navframe_label = customtkinter.CTkLabel(self.navframe, text='Menu', bg_color="#5A1941" , fg_color='#292726')
    self.navframe_label.grid(row=1, column=0, padx=20, pady=20)
    #option buttons
    self.parkbtn = customtkinter.CTkButton(self.navframe, text="Park car", text_color= '#4d4d4d', font= ('Arial',25, 'bold'),width=544, height=60, fg_color='#bf69af', hover_color='#a84896')
    self.parkbtn.grid(row=1, column=1, padx=30, pady=30)
    self.unparkbtn = customtkinter.CTkButton(self.navframe, text="Exit parking", text_color='#4d4d4d', font=('Arial', 25, 'bold'),width=544, height=60, fg_color='#bf69af', hover_color='#a84896')
    self.unparkbtn.grid(row=1, column=2, padx=30, pady=30)
    self.checkbtn = customtkinter.CTkButton(self.navframe, text="Check parking spaces", text_color='#4d4d4d', font=('Arial', 25, 'bold'), width=544, height=60, fg_color='#bf69af', hover_color='#a84896')
    self.checkbtn.grid(row=1, column=3, padx=30, pady=30)

    self.parkframe = customtkinter.CTkFrame(self, corner_radius=0)
    self.parkframe.grid_configure(6, weight=1)

def selectFrame(self, name):
  self.parkbtn.configure(fg_color=("gray75, gray25") if name == "park" else "transparent")

  if name == 'park':
     self.parkframe.grid(row=0, column=1, sticky="nsew")
  else:
     self.parkframe.grid_forget()



if __name__ == "__main__":
    app = App()
    app.mainloop()