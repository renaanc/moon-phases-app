import ephem
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk

# Mapeamento de imagens de fases
moon_images = {
    "New Moon": "D:/MOON_PHASES/moon_images/new_moon.webp",
    "Waxing Crescent": "D:/MOON_PHASES/moon_images/waxing_crescent.webp",
    "First Quarter": "D:/MOON_PHASES/moon_images/first_quarter.webp",
    "Waxing Gibbous": "D:/MOON_PHASES/moon_images/waxing_gibbous.webp",
    "Full Moon": "D:/MOON_PHASES/moon_images/full.webp",
    "Waning Gibbous": "D:/MOON_PHASES/moon_images/waning_gibbous.webp",
    "Last Quarter": "D:/MOON_PHASES/moon_images/last_quarter.webp",
    "Waning Crescent": "D:/MOON_PHASES/moon_images/waning_crescent.webp",
    "Default": "D:/MOON_PHASES/moon_images/moon_default.jpg"
}

def determine_moon_phase(illumination):
    """Determines the phase of the Moon based on the illuminated fraction."""
    if illumination < 0.03:
        return "New Moon"
    elif 0.03 <= illumination < 0.25:
        return "Waxing Crescent"
    elif 0.25 <= illumination < 0.50:
        return "First Quarter"
    elif 0.50 <= illumination < 0.75:
        return "Waxing Gibbous"
    elif 0.97 <= illumination:
        return "Full Moon"
    elif 0.75 <= illumination < 0.97:
        return "Waning Gibbous"
    elif 0.50 <= illumination < 0.75:
        return "Last Quarter"
    else:
        return "Waning Crescent"

def get_moon_phase(date):
    """Gets the phase of the Moon for a specific date."""
    moon = ephem.Moon(date)
    illumination = moon.phase / 100  # Fração iluminada (0 a 1)
    phase_name = determine_moon_phase(illumination)
    return phase_name, illumination * 100  # Converte para %

def update_moon_phase():
    """Update the moon phases and edisplays the corresponding image."""
    date_input = entry_date.get() or datetime.now().strftime("%Y-%m-%d")
    try:
        date = ephem.Date(date_input)
        phase_name, illumination = get_moon_phase(date)

        # Atualizar texto da fase
        label_phase.config(text=f"Fase: {phase_name} ({illumination:.2f}%)")

        # Atualizar imagem correspondente
        image_path = moon_images.get(phase_name, moon_images["Default"])
        moon_image = Image.open(image_path)
        moon_image = moon_image.resize((200, 200))  # Redimensionar para caber na janela
        tk_image = ImageTk.PhotoImage(moon_image)

        # Atualizar imagem no label
        label_image.config(image=tk_image)
        label_image.image = tk_image

    except ValueError:
        label_phase.config(text="Invalid data! Please use YYYY-MM-DD format.")

# Interface com Tkinter
root = tk.Tk()
root.title("Moon phase visualizer")

frame = tk.Frame(root)
frame.pack(pady=20)

label_date = tk.Label(frame, text="Enter a date (YYYY-MM-DD):")
label_date.grid(row=0, column=0, padx=5)

entry_date = tk.Entry(frame, width=15)
entry_date.grid(row=0, column=1, padx=5)

button_check = tk.Button(frame, text="See Phase", command=update_moon_phase)
button_check.grid(row=0, column=2, padx=5)

label_phase = tk.Label(root, text="Phase: --", font=("Arial", 12))
label_phase.pack(pady=10)

label_image = tk.Label(root)
label_image.pack(pady=10)

root.mainloop()
