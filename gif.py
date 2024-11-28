import os
from PIL import Image
import imageio
import tkinter as tk
from tkinter import filedialog

def select_folder():
    root = tk.Tk()
    root.withdraw()  
    folder_path = filedialog.askdirectory()  
    return folder_path

def images_to_gif(image_folder, output_path, duration=0.5):
    images = []
    for file_name in sorted(os.listdir(image_folder)):
        if file_name.endswith(('png', 'jpg', 'jpeg')):
            file_path = os.path.join(image_folder, file_name)
            images.append(imageio.imread(file_path))
    
    imageio.mimsave(output_path, images, duration=duration)
    print(f"GIF saved to {output_path}")

if __name__ == "__main__":
    print("Please select the folder containing the images")
    image_folder = select_folder()
    
    if image_folder:
        output_path = os.path.join(image_folder, 'output.gif')
        duration = 1/16  # The time each picture is displayed in seconds
        images_to_gif(image_folder, output_path, duration)
    else:
        print("No folder selected")
