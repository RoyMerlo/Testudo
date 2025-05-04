import os
import subprocess
import threading
import shutil
from tkinter import *
from tkinter import filedialog, messagebox, ttk

# === Funzioni principali ===

def remove_metadata(file_path):
    try:
        result = subprocess.run(["exiftool", "-all=", file_path],
                                check=True, capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error removing metadata:\n{e}")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")
        return False

def show_metadata(file_path):
    try:
        result = subprocess.run(["exiftool", file_path],
                                check=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else "Unable to read metadata."
    except Exception as e:
        return f"Error: {str(e)}"

# === Effetti hover ===

def on_enter(e): e.widget.config(bg="#888888")
def on_leave(e): e.widget.config(bg="#666666")

# === Condivisione file ===

def ask_share(file_path):
    response = messagebox.askyesno("Share File", "Metadata removed successfully.\nDo you want to share the file?")
    if response:
        dest_folder = filedialog.askdirectory(title="Select destination to share the file")
        if dest_folder:
            try:
                shutil.copy(file_path, dest_folder)
                messagebox.showinfo("Shared", f"✅ File shared to:\n{dest_folder}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to share file:\n{e}")
        else:
            messagebox.showinfo("Cancelled", "❎ Sharing cancelled.")
    else:
        messagebox.showinfo("Done", "✅ File cleanup complete. No sharing requested.")

# === Thread di avvio ===

def remove_metadata_thread():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All Files", "*.*")])
    if file_path:
        metadata = show_metadata(file_path)

        metadata_window = Toplevel(root)
        metadata_window.title("File Metadata")
        metadata_window.geometry("600x400")
        metadata_window.configure(bg="black")

        Label(metadata_window, text="Original Metadata", font=("Consolas", 14),
              fg="#00ff00", bg="black").pack(pady=10)

        text_box = Text(metadata_window, wrap=NONE, bg="black", fg="#00ff00",
                        font=("Consolas", 10), padx=10, pady=10)
        text_box.pack(fill=BOTH, expand=True)
        text_box.insert(END, metadata)
        text_box.config(state=DISABLED)

        confirmation = messagebox.askyesno("Confirm",
                                           f"Remove metadata from {os.path.basename(file_path)}?")
        if confirmation:
            threading.Thread(target=remove_metadata_process, args=(file_path,)).start()

def remove_metadata_process(file_path):
    progress_window = Toplevel(root)
    progress_window.title("Metadata Removal")
    progress_window.geometry("400x150")
    progress_window.configure(bg="black")

    Label(progress_window, text="Removing metadata...", font=("Segoe UI", 14),
          fg="#00ff00", bg="black").pack(pady=20)

    progress = ttk.Progressbar(progress_window, orient=HORIZONTAL, length=300, mode="indeterminate")
    progress.pack()
    progress.start()

    success = remove_metadata(file_path)

    progress.stop()
    progress_window.destroy()

    if success:
        messagebox.showinfo("Success", f"✅ Metadata removed from {os.path.basename(file_path)}")
        ask_share(file_path)
    else:
        messagebox.showerror("Error", f"❌ Failed to remove metadata from {os.path.basename(file_path)}")

# === INTERFACCIA ===

root = Tk()
root.title("TESTUDO - Metadata Cleaner")
root.geometry("1400x1000")
root.minsize(1000, 600)
root.configure(bg="black")

# === TITOLO ===

title_frame = Frame(root, bg="black")
title_frame.pack(pady=50)

canvas = Canvas(title_frame, width=800, height=100, bg="black", highlightthickness=0, bd=0)
canvas.pack()

base_text = "⚡ TESTUDO ⚡"
x, y = 400, 50

for dx in [-2, 0, 2]:
    for dy in [-2, 0, 2]:
        if dx != 0 or dy != 0:
            canvas.create_text(x + dx, y + dy, text=base_text,
                               font=("Segoe UI", 48, "bold"), fill="#ffffff")

canvas.create_text(x, y, text=base_text, font=("Segoe UI", 48, "bold"), fill="red")

subtitle = Label(title_frame, text="Metadata Eraser", font=("Segoe UI", 20),
                 fg="#888888", bg="black")
subtitle.pack(pady=5)

footer_small = Label(title_frame, text="powered by Roy Merlo @2025",
                     font=("Segoe UI", 10), fg="#555555", bg="black")
footer_small.pack(pady=(5, 10))

# === PULSANTE ===

btn_frame = Frame(root, bg="black")
btn_frame.pack(pady=30)

remove_button = Button(btn_frame, text="Remove Metadata",
                       command=remove_metadata_thread,
                       bg="#666666", fg="white",
                       font=("Segoe UI", 16, "bold"),
                       relief="flat", bd=0, padx=30, pady=15,
                       cursor="hand2")
remove_button.pack()

remove_button.bind("<Enter>", on_enter)
remove_button.bind("<Leave>", on_leave)

# === AREA RISULTATI ===

output_frame = Frame(root, bg="black")
output_frame.pack(padx=30, pady=30, fill=BOTH, expand=True)

output_label = Label(output_frame, text="Output", font=("Segoe UI", 14),
                     fg="#00ff00", bg="black")
output_label.pack(anchor="w")

output_box = Text(output_frame, height=20, width=120,
                  bg="black", fg="#00ff00",
                  font=("Consolas", 12), wrap=WORD,
                  bd=0, highlightthickness=0,
                  insertbackground="#00ff00",
                  padx=15, pady=15)
output_box.pack(fill=BOTH, expand=True)
output_box.insert(END, "➤ Select a file to start\n")
output_box.config(state=DISABLED)

# === FOOTER ===

footer_frame = Frame(root, bg="#1a1a1a")
footer_frame.pack(side=BOTTOM, fill=X, padx=20, pady=10)

footer_label = Label(footer_frame, text="powered by Roy Merlo @2025",
                     font=("Segoe UI", 10), fg="#555555", bg="#1a1a1a")
footer_label.pack(side=RIGHT, padx=10, pady=5)

root.mainloop()
