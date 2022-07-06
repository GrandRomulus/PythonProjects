import os
import os.path
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = r"C:\Users\AHarl\Downloads"
dest_dir_music = r"C:\Users\AHarl\Music"
dest_dir_document = r"C:\Users\AHarl\Documents"
dest_dir_video = r"C:\Users\AHarl\Videos"
dest_dir_image = r"C:\Users\AHarl\Pictures"

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def makeUnique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 0
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while os.path.exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if os.path.exists(f"{dest}/{name}"):
        unique_name = makeUnique(dest, name)
        oldName = os.path.join(dest, name)
        newName = os.path.join(dest, unique_name)
        os.rename(oldName, newName)
    return shutil.move(entry, dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                for audio in audio_extensions:
                    if name.endswith(audio):
                        dest = dest_dir_music
                        move_file(dest, entry, name)
                for video in video_extensions:
                    if name.endswith(video):
                        dest = dest_dir_video
                        move_file(dest, entry, name)
                for image in image_extensions:
                    if name.endswith(image):
                        dest = dest_dir_image
                        move_file(dest, entry, name)
                for document in document_extensions:
                    if name.endswith(document):
                        dest = dest_dir_document
                        move_file(dest, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
