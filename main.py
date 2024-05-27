import os
from dotenv import load_dotenv
from split_text_max_char import *
from split_text_heading import *
from rename_output_files import *
from text_to_speech import *
from download_speech_files import *

load_dotenv()

def delete_files_in_output(directory):
    if os.path.exists(directory):
        try:
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
        except Exception as e:
            print(f"Failed to delete files in {directory}: {e}")
    else:
        print(f"The directory '{directory}' does not exist.")

def main():
    input_file = 'input.txt'
    output_folder = 'output'
    heading_regex = r'\nLesson\s.*?(?=\nLesson\s|\Z)'
    download_urls= "download_urls.txt"
    email = os.getenv("BLASTER_SUITE_EMAIL")
    password = os.getenv("BLASTER_SUITE_PASSWORD")
    # split_text_heading(input_file, output_folder, heading_regex)
    delete_files_in_output(output_folder)
    split_text_max_char(input_file, output_folder, max_chars=4998)
    rename_output_files(output_folder)
    text_to_speech(email, password, input_folder=output_folder, output=download_urls)
    download_speech_files(download_urls, files_folder=output_folder, download_folder="download")


if __name__ == "__main__":
    main()
