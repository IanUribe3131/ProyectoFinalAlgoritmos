import customtkinter
from PIL import Image, ImageTk
import subprocess

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Park Manager")
        self.geometry("1920x1080")
        self.state('zoomed')
        self.resizable(True, True)

        # ========= CONFIGURE GRID =========
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)  # column 0 = nav, column 1 = content

        # ========= NAVIGATION FRAME =========
        self.navframe = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#292726")
        self.navframe.grid(row=0, column=0, sticky="ns")  # only vertical stretch
        self.navframe.grid_rowconfigure(6, weight=1)

        self.navframe_label = customtkinter.CTkLabel(
            self.navframe, text="Menu", font=("Arial", 24, "bold"), text_color="#FFFFFF"
        )
        self.navframe_label.grid(row=0, column=0, padx=20, pady=(20,10))

        # Navigation buttons
        self.parkbtn = customtkinter.CTkButton(
            self.navframe, text="Park car",
            text_color='#4d4d4d', font=('Arial', 20, 'bold'),
            width=200, height=50, fg_color='#bf69af', hover_color='#a84896',
            command=self.show_park_frame
        )
        self.parkbtn.grid(row=1, column=0, padx=20, pady=10)

        self.unparkbtn = customtkinter.CTkButton(
            self.navframe, text="Exit parking",
            text_color='#4d4d4d', font=('Arial', 20, 'bold'),
            width=200, height=50, fg_color='#bf69af', hover_color='#a84896',
            command=self.show_exitpark_frame
        )
        self.unparkbtn.grid(row=2, column=0, padx=20, pady=10)

        self.checkbtn = customtkinter.CTkButton(
            self.navframe, text="Check spaces",
            text_color='#4d4d4d', font=('Arial', 20, 'bold'),
            width=200, height=50, fg_color='#bf69af', hover_color='#a84896',
            command=self.show_check_frame
        )
        self.checkbtn.grid(row=3, column=0, padx=20, pady=10)



        # ========= MAIN CONTENT FRAMES =========
        self.main_container = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_container.grid(row=0, column=1, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)



        # Homepage Frame
        self.homeframe = customtkinter.CTkFrame(self.main_container, corner_radius=0)
        customtkinter.CTkLabel(
            self.homeframe, text="Welcome to Park Manager :D", font=("Arial", 60, "bold")
        ).pack(pady=100)
        customtkinter.CTkLabel(
            self.homeframe, text="Select one of the options on your left menu to park or leave free a parking space",
            font=("Arial", 40, "bold")
        ).pack(pady=200)
        


        # Park Frame ======PARKING=======
        self.parkframe = customtkinter.CTkFrame(self.main_container, corner_radius=0)
        customtkinter.CTkLabel(
            self.parkframe, text="🚗 Park a Car; select if your car is big or small:", font=("Arial", 40, "bold")
        ).pack(pady=50)

        self.carSize = customtkinter.StringVar(value="Select size")

        self.sizeOption = customtkinter.CTkOptionMenu(
            self.parkframe, values=["Big car", "Small car"], fg_color='#bf69af', button_color='#bf69af', button_hover_color='#a84896',
            dropdown_fg_color='#bf69af', dropdown_hover_color='#a84896', text_color='#4d4d4d', dropdown_text_color='#4d4d4d',
            width=150, height=40, command=self.optionMenusize
            ).pack(pady=50)
        
        self.parking_spots = []
        rows = 2
        cols = 14

        customtkinter.CTkLabel(
            self.parkframe, text="Floor 0 / L", font=("Arial", 20,"bold")
        ).pack(pady=20)
        

        self.parkings_frame1ed = customtkinter.CTkFrame(self.parkframe, fg_color='#333333')
        self.parkings_frame1ed.pack(pady=20)

        for row in range(rows):
            for col in range(cols):
                index = row * cols + col  # calculate global index 0–27
                spot = customtkinter.CTkLabel(
                    self.parkings_frame1ed,
                    text=str(index + 1),
                    width=50, height=50,
                    fg_color="#bf69af",
                    corner_radius=5,
                    text_color='black'
                )
                spot.grid(row=row, column=col, padx=3, pady=3)

                # capture row and index in the lambda
                spot.bind("<Button-1>", lambda e, r=row, c=col, i=index: self.toggle_spot(r, c, i))

                self.parking_spots.append(spot)
       



        #exit parking frame
        self.exitParkFrame = customtkinter.CTkFrame(self.main_container, corner_radius=0)
        customtkinter.CTkLabel(
            self.exitParkFrame, text="🚗 Exit parking; select an occupied space to take the car out of:", font=("Arial", 40, "bold")
        ).pack(pady=100)

        customtkinter.CTkLabel(
            self.exitParkFrame, text="Floor 0 / L", font=("Arial", 20, "bold")
            ).pack(pady=20)
        
        self.parkings_frame1ex = customtkinter.CTkFrame(self.exitParkFrame, fg_color='#333333')
        self.parkings_frame1ex.pack(pady=20)


        self.parking_spots_exit=[]
        for row in range(rows):
            for col in range(cols):
                index = row * cols + col  # calculate global index 0–27
                spot = customtkinter.CTkLabel(
                    self.parkings_frame1ex,
                    text=str(index + 1),
                    width=50, height=50,
                    fg_color="#bf69af",
                    corner_radius=5,
                    text_color='black'
                )
                spot.grid(row=row, column=col, padx=3, pady=3)

                #  capture row and index in the lambda
                spot.bind("<Button-1>", lambda e, r=row, c=col, i=index: self.toggle_spot_exit(r, c, i))

                self.parking_spots_exit.append(spot)




        #check parking frame
        self.checkframe = customtkinter.CTkFrame(self.main_container, corner_radius=0)
        customtkinter.CTkLabel(
            self.checkframe, text="Check availablility through the squares below", font=("Arial", 40, "bold")
        ).pack(pady=30)
        customtkinter.CTkLabel(
            self.checkframe, text="Pink means available and red means occupied!!", font=("Arial", 40, "bold")
        ).pack(pady=30)
        customtkinter.CTkLabel(
            self.checkframe, text="Floor 0 / L", font=("Arial", 20,"bold")
        ).pack(pady=20)
        


        self.parkings_frame1 = customtkinter.CTkFrame(self.checkframe, fg_color='#333333')
        self.parkings_frame1.pack(pady=20)

        i=0
        while(i<14):
            self.spot = customtkinter.CTkLabel(self.parkings_frame1, text="", width=50, height=50, fg_color="#bf69af", corner_radius=5)
            self.spot.grid(row=0, column=i, padx=3, pady=3)
            i= i+1
        i=0
        while(i<14):
            self.spot = customtkinter.CTkLabel(self.parkings_frame1, text="", width=50, height=50, fg_color="#bf69af", corner_radius=5)
            self.spot.grid(row=1, column=i, padx=3, pady=3)
            i= i+1

        customtkinter.CTkLabel(
            self.checkframe, text="Floor 1", font=("Arial", 20, "bold")
        ).pack(pady=20)

        self.parkings_frame2 = customtkinter.CTkFrame(self.checkframe, fg_color= '#333333')
        self.parkings_frame2.pack(pady=20)
        
        i=0
        while(i<14):
            self.spot = customtkinter.CTkLabel(self.parkings_frame2, text="", width=50, height=50, fg_color="#bf69af", corner_radius=5)
            self.spot.grid(row=0, column=i, padx=3, pady=3)
            i= i+1
        i=0
        while(i<14):
            self.spot = customtkinter.CTkLabel(self.parkings_frame2, text="", width=50, height=50, fg_color="#bf69af", corner_radius=5)
            self.spot.grid(row=1, column=i, padx=3, pady=3)
            i= i+1



        # Initially show homepage
        self.current_frame = None
        self.show_frame(self.homeframe)



    # ========= FRAME SWITCHING FUNCTION =========
    def show_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.grid_forget()
        frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame = frame

    def show_park_frame(self):
        self.show_frame(self.parkframe)

    def show_exitpark_frame(self):
        self.show_frame(self.exitParkFrame)

    def show_check_frame(self):
        self.show_frame(self.checkframe)

    def optionMenusize(self,size):
        self.carSize.set(size)
        print("selected size: " ,self.carSize.get())

    def toggle_spot(self, row, col, index):
        self.spot = self.parking_spots[index]
        current_color = self.spot.cget("fg_color")

        if current_color == "#bf69af":  # free
            self.spot.configure(fg_color="red")
        else:
            self.spot.configure(fg_color="#bf69af")

    def toggle_spot_exit(self, row, col, index):
        spot = self.parking_spots_exit[index]
        current_color = spot.cget("fg_color")

        # Toggle between pink and grey (or any colors you like)
        if current_color == "#bf69af":
            spot.configure(fg_color="red")
        else:
            spot.configure(fg_color="#bf69af")

# ========= RUN APP =========
if __name__ == "__main__":
    app = App()
    app.mainloop()
