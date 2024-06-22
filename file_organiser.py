import os
import shutil

directory = "C:\\Users\\Bartek\\Downloads"

image_directory = os.path.join(directory, "IMAGE")
pdf_directory = os.path.join(directory, "PDF")
text_directory = os.path.join(directory, "TEXT")
spreadsheet_directory = os.path.join(directory, "SPREADSHEETS")
video_directory = os.path.join(directory, "VIDEOS")
audio_directory = os.path.join(directory, "AUDIO")
presentation_directory = os.path.join(directory, "PRESENTATIONS")
cpp_directory = os.path.join(directory, "C++")

def path(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            _, file_extension = os.path.splitext(filename)
            segregate(file_extension, filepath)

def check_if_folder_exists():
    directories = [image_directory, pdf_directory, text_directory, spreadsheet_directory, 
                   video_directory, audio_directory, presentation_directory, cpp_directory]
    for dir in directories:
        if not os.path.exists(dir):
            os.mkdir(dir)

def segregate(file_extension, filepath):
    if file_extension.lower() in ['.png','.jpg']:
        shutil.move(filepath, image_directory)
    elif file_extension.lower() == '.pdf':
        shutil.move(filepath, pdf_directory)
    elif file_extension.lower() in ['.txt', '.doc', '.docx']:
        shutil.move(filepath, text_directory)
    elif file_extension.lower() in ['.xls', '.xlsx','.csv']:
        shutil.move(filepath, spreadsheet_directory)
    elif file_extension.lower() in ['.mp4', '.avi', '.mov']:
        shutil.move(filepath, video_directory)
    elif file_extension.lower() in ['.mp3', '.wav']:
        shutil.move(filepath, audio_directory)
    elif file_extension.lower() in ['.ppt', '.pptx']:
        shutil.move(filepath, presentation_directory)
    elif file_extension.lower() in ['.cpp', '.h']:
        shutil.move(filepath, cpp_directory)

check_if_folder_exists()
path(directory)
