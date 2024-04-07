
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

def remix_song():
    # Select the input file
    input_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if not input_file_path:
        return

    # Load the audio file
    audio = AudioSegment.from_file(input_file_path)

    # Increase tempo and BPM
    tempo_factor = 1.4
    increased_tempo = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * tempo_factor)
    })
    increased_bpm = increased_tempo.set_frame_rate(audio.frame_rate)

    # Save the remix
    output_file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
    if not output_file_path:
        return
    increased_bpm.export(output_file_path, format="mp3")

    # Display success message
    status_label.config(text="Remix created successfully!")

# Create the main window
window = tk.Tk()
window.title("Hardstyle Remix App")

# Create the remix button
remix_button = tk.Button(window, text="Remix Song", command=remix_song)
remix_button.pack(pady=20)

# Create a label for status messages
status_label = tk.Label(window, text="")
status_label.pack()

# Run the application
window.mainloop()