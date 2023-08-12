import tkinter as tk
from threading import Thread
#from tkcalendar import Calendar  # Import the Calendar widget
import time

def destroy_center_widgets():
    for widget in center_frame.winfo_children():
        widget.destroy()

def destroy_root_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def create_center_frame():
    center_frame = tk.Frame(root, bg="black")
    center_frame.pack(expand=True)
    return center_frame

def countdown(header, date, label):
    # Convert the input date string to a struct_time object

    # Convert the input date string to a struct_time object
    target_time = time.strptime(date, '%d/%m/%Y')
    day=time.strptime(date, '%d/%m/%Y').tm_mday
    month = time.strptime(date, '%d/%m/%Y').tm_mday
    year = 2023;

    # Convert the struct_time to a timestamp
    target_timestamp = int(time.mktime(target_time))

    # Add one day in seconds to the timestamp
    target_timestamp += 86400

    # Convert the timestamp back to a struct_time
    target_time = time.localtime(target_timestamp)

    while True:
        # Get the current time
        current_time = time.localtime()

        # Calculate the time difference between the target time and the current time in seconds
        time_diff = int(time.mktime(target_time) - time.mktime(current_time))

        # If the target time has passed, break out of the loop
        if time_diff < 0:
            label.config(text=f"{header} has ended")
            break

        # Calculate the time difference in days, hours, minutes, and seconds
        days, remainder = divmod(time_diff, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Update the label with the time remaining
        try:
            label.config(text=f"{header} ---  {days}d {hours:02d}h"f" {minutes:02d}m {seconds:02d}s till "+str(date))
        except:
            print("label bruh")
        # Update the Tkinter window
        label.update()

        # Wait for 1 second before updating the label again
        time.sleep(1)

# Function to handle opening the black window
def configure_timers_window():
    # Clear the center frame
    try:
        destroy_center_widgets()
    except:
        print("error")

    destroy_root_widgets()

    timers_button = tk.Button(root, text="Display deadlines", command=open_timers_window, font=button_font_20)
    timers_button.place(relx=0.5, rely=0.01, anchor=tk.N)
    print("tried it")
    # Create a black label and center it
    #root is expanding the text window accordingly whereas center_frane isn't
    #black_label = tk.Label(root, text="now is not working properly", font=button_font, bg="black", fg="white")
    #black_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #destroy_old_widgets()
# Function to handle opening the timers window

def create_date_():
    print()

def open_timers_window():
    # Clear the center frame
                                        #destroy_center_widgets()
    # destorying root widgets
    destroy_root_widgets()

    # creating new center frames
    center_frame=create_center_frame()

    timers_button = tk.Button(root, text="Configurations", command=configure_timers_window, font=button_font_10)
    timers_button.place(relx=0.08, rely=0.01, anchor=tk.N)
    #
    labels_list = []
    for i in range(5):
        label = tk.Label(center_frame, fg="green", bg="black", font=('Courier', 14))
        labels_list.append(label)
        label.pack()

    label0 = tk.Label(center_frame, fg="blue", bg="black", font=('Courier', 14))
    labels_list.append(label0)
    label0.pack()

    label1 = tk.Label(center_frame, fg="green", bg="black", font=('Courier', 14))
    labels_list.append(label1)
    label1.pack()

    label2 = tk.Label(center_frame, fg="red", bg="black", font=('Courier', 14))
    labels_list.append(label2)
    label2.pack()

    label3 = tk.Label(center_frame, fg="pink", bg="black", font=('Courier', 14))
    labels_list.append(label3)
    label3.pack()

    for i in range(3):
        label = tk.Label(center_frame, fg="green", bg="black", font=('Courier', 14))
        labels_list.append(label)
        label.pack()

    label4 = tk.Label(center_frame, fg="pink", bg="black", font=('Courier', 14))
    labels_list.append(label4)
    label4.pack()

    label5 = tk.Label(center_frame, fg="green", bg="black", font=('Courier', 14))
    labels_list.append(label5)
    label5.pack()

    label6 = tk.Label(center_frame, fg="green", bg="black", font=('Courier', 14))
    labels_list.append(label6)
    label6.pack()

    label7 = tk.Label(center_frame, fg="red", bg="black", font=('Courier', 14))
    labels_list.append(label7)
    label7.pack()

    # for i in range(7):
    #     label = tk.Label(root, fg="orange", bg="black", font=('Courier', 14))
    #     labels_list.append(label)
    #     label.pack()

    # Start the countdowns in separate threads
    thread1 = Thread(target=countdown, args=("Τεχνολογικη Καιν-Επ 1η  ", "31/03/2023", labels_list[0]))
    thread1.start()
    thread2 = Thread(target=countdown, args=("Τεχνολογια Λογισμικου 1η", "03/04/2023", labels_list[1]))
    thread2.start()
    thread3 = Thread(target=countdown, args=("Δικτυα Υπολογιστων 1η   ", "10/04/2023", labels_list[2]))
    thread3.start()
    thread4 = Thread(target=countdown, args=("Τεχνολογια Λογισμικου 2η", "12/04/2023", labels_list[3]))
    thread4.start()
    thread5 = Thread(target=countdown, args=("Αλγοριθμοι 1η σειρα_α   ", "24/04/2023", labels_list[4]))
    thread5.start()
    thread6 = Thread(target=countdown, args=("ΑΛΓΟΡΙΘΜΟΙ ΠΡΟΟΔΟΣ      ", "28/04/2023", labels_list[5]))  # blue
    thread6.start()
    thread7 = Thread(target=countdown, args=("Τεχνολογικη Καιν-Επ 2η  ", "28/04/2023", labels_list[6]))  # green
    thread7.start()

    thread8 = Thread(target=countdown, args=("Κατανεμημενα 1ο_μερος   ", "30/04/2023", labels_list[7]))  # red
    thread8.start()
    thread9 = Thread(target=countdown, args=("Ασφαλεια Πληροφορ 1/3   ", "04/05/2023", labels_list[8]))  # pink
    thread9.start()

    thread10 = Thread(target=countdown, args=("Τεχνολογια Λογισμικου 3η", "05/05/2023", labels_list[9]))
    thread10.start()
    thread11 = Thread(target=countdown, args=("Δικτυα Υπολογιστων 2η   ", "10/05/2023", labels_list[10]))
    thread11.start()
    thread12 = Thread(target=countdown, args=("Τεχνολογικη Καιν-Επ 3-4 ", "26/05/2023", labels_list[11]))
    thread12.start()
    thread13 = Thread(target=countdown, args=("Εργαστηριακη Ασφ 2/3    ", "06/06/2023", labels_list[12]))  # pink
    thread13.start()

    thread14 = Thread(target=countdown, args=("Αλγοριθμοι 2η_σειρα_α   ", "13/06/2023", labels_list[13]))  # green
    thread14.start()
    thread15 = Thread(target=countdown, args=("Δικτυα Υπολογιστων 3η   ", "15/09/2023", labels_list[14]))  # green
    thread15.start()

    thread16 = Thread(target=countdown, args=("Κατανεμημενα 2ο_μερος   ", "24/09/2023", labels_list[15]))  # red
    thread16.start()

    # thread17 = Thread(target=countdown, args=("Αγγλικα 6 4.30-6.30     ", "21/06/2023", labels_list[16]))  # orange
    # thread17.start()
    # thread18 = Thread(target=countdown, args=("Αγγλικα 4 7-8.30        ", "21/06/2023", labels_list[17]))  # orange
    # thread18.start()
    # thread19 = Thread(target=countdown, args=("Κατανεμημ 10.30-12.30   ", "28/06/2023", labels_list[18]))  # orange
    # thread19.start()
    # thread20 = Thread(target=countdown, args=("Δικτυα Υπολ 4.30-7.30   ", "30/06/2023", labels_list[19]))  # orange
    # thread20.start()
    # thread21 = Thread(target=countdown, args=("Ασφαλεια 10.30-12.30    ", "04/07/2023", labels_list[20]))  # orange
    # thread21.start()
    # thread22 = Thread(target=countdown, args=("Λειτουργικα 3.30-5.30   ", "04/07/2023", labels_list[21]))  # orange
    # thread22.start()
    # thread23 = Thread(target=countdown, args=("Αλγοριθμοι 8-11         ", "06/07/2023", labels_list[22]))  # orange
    # thread23.start()


def main_window():

    configure_timers_button = tk.Button(center_frame, text="Configurations", command=configure_timers_window, font=button_font_20)
    configure_timers_button.pack(pady=(root.winfo_height() - configure_timers_button.winfo_height()) // 2)

    # Button to open the timers window
    timers_button = tk.Button(center_frame, text="Display deadlines", command=open_timers_window, font=button_font_20)
    timers_button.pack(before=configure_timers_button, padx=20, pady=20)

    # Entry to display selected date
    date_entry_event_name = tk.Entry(center_frame, font=("Arial", 14))
    date_entry_event_name.pack(pady=10)

    print(date_entry_event_name)


# Create the main Tkinter window
root = tk.Tk()
root.configure(bg="black")

# Set the dimensions of the window
window_width = 700
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Create a frame for centering the buttons and content
center_frame=create_center_frame()

#button text size
button_font_10 = ('Arial', 10)
button_font_20 = ('Arial', 20)

#starting main window
main_window()
print("looping")

# loop
root.mainloop()
