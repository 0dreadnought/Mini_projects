from tkinter import filedialog
from imageio import get_reader, imwrite
from numpy import empty, uint8
from os.path import splitext


gif_path = filedialog.askopenfilename(title="Select a GIF file", filetypes=[("gifs","*.gif")]) 
if gif_path: 
    file = splitext(gif_path)[0]
    out_path = f"{file}_stacked.png"

    with get_reader(gif_path) as reader:
        first_frame = reader.get_next_data()
        height, width = first_frame.shape[:2]
        n_frames = reader.get_length()

        stacked_frames = empty((height * n_frames, width, 3), dtype=uint8)

        for i, frame in enumerate(reader):
            stacked_frames[i * height:(i + 1) * height, :, :] = frame

    imwrite(out_path, stacked_frames)