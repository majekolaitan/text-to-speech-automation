import split_text_heading
import split_text_max_character
import rename_output_files
import text_to_speech_automation
import download_speech_files

def main():
    split_text_max_character()
    rename_output_files()
    text_to_speech_automation()
    download_speech_files()

if __name__ == "__main__":
    main()
