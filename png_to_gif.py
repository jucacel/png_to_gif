import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory, asksaveasfilename
from PIL import UnidentifiedImageError

def get_image_files(directory):
    valid_extensions = ['.png']
    files = [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
        and os.path.splitext(f)[1].lower() in valid_extensions
        and not f.startswith('._')  # Ignore macOS metadata files
    ]
    return files

def convert_images_to_gif(input_directory, output_path):
    image_files = get_image_files(input_directory)
    image_files.sort()  # Ensure the images are sorted
    images = []
    for img_file in image_files:
        img_path = os.path.join(input_directory, img_file)
        try:
            img = Image.open(img_path)
            images.append(img)
        except UnidentifiedImageError:
            print(f"Archivo no válido o corrupto: {img_path}")
    
    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)
        print(f"GIF creado: {output_path}")
    else:
        print("No se encontraron imágenes válidas.")

def main():
    Tk().withdraw()
    input_directory = askdirectory(title="Select Input Directory")
    if not input_directory:
        print("No directory selected. Exiting.")
        return
    
    output_path = asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    if not output_path:
        print("No output file selected. Exiting.")
        return
    
    convert_images_to_gif(input_directory, output_path)

if __name__ == "__main__":
    main()
