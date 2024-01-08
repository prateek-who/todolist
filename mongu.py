import customtkinter as ct
from PIL import Image
import todolist_backend as tdb
import calendar

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

root = ct.CTk(fg_color="#183D3D")
root.geometry("1000x400+500+300")
root.minsize(1000, 400)
root.resizable(False, False)
root.title("To-do list")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.configure(fg_color=root.cget('fg_color'))

# Color related business
config_color = "#000000"
tabview_color = "#393232"
sidebar_color = "#4D4545"
button_selected_color = "#E3651D"
button_hover_color = "#F6B17A"
tabview_background_color = "#000000"
tabview_hover_color = "#F6B17A"
tabview_selected_color = "#E3651D"


# Side_bar stuff
sidebar_frame = ct.CTkFrame(master=root, height=450, width=210, fg_color=sidebar_color, corner_radius=0)
sidebar_frame.grid(row=0, column=0, padx=0, pady=0)
# ct.CTkImage(dark_image=Image.open(""), size=(30, 30))

list_display_frame = ct.CTkFrame(master=root, height=450, width=900, corner_radius=0, fg_color=tabview_color)
list_display_frame.grid(row=0, column=1, padx=0, pady=0)

# Main tab view settings
day_tabview = ct.CTkTabview(master=list_display_frame, height=350, width=795,
                            fg_color=tabview_color, segmented_button_fg_color=tabview_background_color,
                            segmented_button_unselected_color=tabview_background_color,
                            segmented_button_selected_color=tabview_selected_color,
                            segmented_button_selected_hover_color=tabview_selected_color,
                            segmented_button_unselected_hover_color=tabview_hover_color)
day_tabview.grid(row=0, column=0)

# Sunday tab stuff
sunday_tab = day_tabview.add('Sunday')
sun_display = ct.CTkTextbox(master=day_tabview.tab("Sunday"),
                            height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#f9e79f")
sun_display.grid(row=0, column=0, padx=5, pady=2)
sunday_tab.configure(fg_color=config_color)

# Monday tab stuff
monday_tab = day_tabview.add("Monday")
mon_display = ct.CTkTextbox(master=day_tabview.tab("Monday"), height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#89c7bc")
mon_display.grid(row=0, column=0, padx=5, pady=2)
monday_tab.configure(fg_color=config_color)

# Tuesday tab stuff
tuesday_tab = day_tabview.add("Tuesday")
tue_display = ct.CTkTextbox(master=day_tabview.tab("Tuesday"), height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#eaaaaa")
tue_display.grid(row=0, column=0, padx=5, pady=2)
tuesday_tab.configure(fg_color=config_color)

# Wednesday tab stuff
wednesday_tab = day_tabview.add('Wednesday')
wed_display = ct.CTkTextbox(master=day_tabview.tab("Wednesday"), height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#e4a888")
wed_display.grid(row=0, column=0, padx=5, pady=2)
wednesday_tab.configure(fg_color=config_color)

# Thursday tab stuff
thursday_tab = day_tabview.add('Thursday')
thu_display = ct.CTkTextbox(master=day_tabview.tab("Thursday"), height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#a9cce3")
thu_display.grid(row=0, column=0, padx=5, pady=2)
thursday_tab.configure(fg_color=config_color)

# Friday tab stuff
friday_tab = day_tabview.add('Friday')
fri_display = ct.CTkTextbox(master=day_tabview.tab("Friday"), height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#7fb3d5")
fri_display.grid(row=0, column=0, padx=5, pady=2)
friday_tab.configure(fg_color=config_color)

# Saturday tab stuff
saturday_tab = day_tabview.add('Saturday')
sat_display = ct.CTkTextbox(master=day_tabview.tab("Saturday"), height=290, width=790, font=("normal", 20),
                            fg_color="#000000", text_color="#d2b4de")
sat_display.grid(row=0, column=0, padx=5, pady=2)
saturday_tab.configure(fg_color=config_color)


class Funcs:
    def __init__(self):
        self.instance = tdb.Monggg()
        self.for_now()

    def for_now(self):
        for day in calendar.day_name:
            text_of_that_day = self.instance.first_update(day)

            match day:
                case "Sunday":
                    sun_display.insert(0.0, text_of_that_day)
                case "Monday":
                    mon_display.insert(0.0, text_of_that_day)
                case "Tuesday":
                    tue_display.insert(0.0, text_of_that_day)
                case "Wednesday":
                    wed_display.insert(0.0, text_of_that_day)
                case "Thursday":
                    thu_display.insert(0.0, text_of_that_day)
                case "Friday":
                    fri_display.insert(0.0, text_of_that_day)
                case "Saturday":
                    sat_display.insert(0.0, text_of_that_day)

    def updating(self):
        match day_tabview.get():
            case "Sunday":
                txt = sun_display.get(0.0, "end")
                self.instance.sunday_update(txt)
            case "Monday":
                txt = mon_display.get(0.0, "end")
                self.instance.monday_update(txt)
            case "Tuesday":
                txt = tue_display.get(0.0, "end")
                self.instance.tuesday_update(txt)
            case "Wednesday":
                txt = wed_display.get(0.0, "end")
                self.instance.wednesday_update(txt)
            case "Thursday":
                txt = thu_display.get(0.0, "end")
                self.instance.thursday_update(txt)
            case "Friday":
                txt = fri_display.get(0.0, "end")
                self.instance.friday_update(txt)
            case "Saturday":
                txt = sat_display.get(0.0, "end")
                self.instance.saturday_update(txt)


# Running __init__ method to get previous details
inst1 = Funcs()

# Button stuff
update_button = ct.CTkButton(master=list_display_frame, text="Update", height=40, width=180, corner_radius=40,
                             fg_color=button_selected_color, hover_color=button_hover_color,
                             command=inst1.updating)
update_button.grid(pady=5, padx=5, row=1, column=0)

# get_button = ct.CTkButton(master=list_display_frame, text="Get", height=40, width=180, corner_radius=40,
#                           fg_color="#00ADB5", )
# get_button.grid(pady=5, padx=5, row=1, column=0)

# entry1 = ct.CTkEntry(master=list_display_frame, placeholder_text="Things to do today", height=40, width=580, justify="center")
# entry1.grid(pady=5, padx=5, row=1, column=0)

# list_update_frame = ct.CTkFrame(master=root, height=45, width=700, fg_color=root.cget('fg_color'))
# list_update_frame.grid(row=1, column=1, padx=5, pady=2)
root.mainloop()
