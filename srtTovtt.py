import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def srt_to_vtt(srt_text):
    vtt_lines = ["WEBVTT"]
    lines = srt_text.strip().split('\n\n')

    for i, line in enumerate(lines):
        parts = line.split('\n')
        if len(parts) >= 3:
            index = parts[0]
            timestamp, _arrow, text = parts[1], parts[2], '\n'.join(parts[2:])
            vtt_lines.append(index)
            vtt_lines.append(timestamp.replace(',', '.'))
            vtt_lines.append(text)
            if i < len(lines) - 1:
                vtt_lines.append("")

    return '\n'.join(vtt_lines)

def open_srt_file():
    file_path = filedialog.askopenfilename(filetypes=[("SubRip Files", "*.srt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as srt_file:
            srt_content = srt_file.read()
            vtt_content = srt_to_vtt(srt_content)
            save_vtt_file(vtt_content)

def save_vtt_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".vtt", filetypes=[("WebVTT Files", "*.vtt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as vtt_file:
            vtt_file.write(content)
        messagebox.showinfo("Thông báo", "Chuyển đổi hoàn tất và đã lưu tệp VTT.")

# Tạo cửa sổ ứng dụng
app = tk.Tk()
app.title("SRT to VTT Converter")
app.configure(bg="#3498db")  # Màu chủ đạo xanh nước biển

# Tạo bố cục chính cho giao diện
main_frame = ttk.Frame(app, padding=20)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.configure(style="Main.TFrame")  # Sử dụng phong cách tùy chỉnh

# Tạo phong cách tùy chỉnh
style = ttk.Style()
style.configure("Main.TFrame", background="#3498db")  # Màu nền xanh nước biển

# Tạo các thành phần giao diện sử dụng ttk (themed tkinter)
label = ttk.Label(main_frame, text="Chuyển đổi từ SRT sang VTT", font=("Helvetica", 16), background="#3498db", foreground="#fff")  # Màu chữ trắng, nền xanh nước biển
label.grid(column=0, row=0, columnspan=2, pady=10)

open_button = ttk.Button(main_frame, text="Mở tệp SRT", command=open_srt_file)
open_button.grid(column=0, row=1, pady=5)

exit_button = ttk.Button(main_frame, text="Thoát", command=app.quit)
exit_button.grid(column=1, row=1, pady=10)

# Thiết lập căn chỉnh cho cửa sổ và bắt đầu vòng lặp chạy ứng dụng
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
app.mainloop()
