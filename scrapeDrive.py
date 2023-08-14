import os
import shutil
import re
def main():
    
    call_recording_dir = r'G:\My Drive\Call recording'


    all_files = os.listdir(call_recording_dir)

    mp3_files = [file for file in all_files if file.lower().endswith('.mp3')]
    latest_mp3 = max(mp3_files, key=lambda x: os.path.getmtime(os.path.join(call_recording_dir, x)))

    latest_mp3_path = os.path.join(call_recording_dir, latest_mp3)


    destination_path = 'Recording.mp3'


    shutil.copy2(latest_mp3_path, destination_path)

    latest_mp3_name = os.path.basename(latest_mp3)
    match = re.match(r".*\((\d+)\)_.*\.mp3", latest_mp3_name)

    
    calling_number = match.group(1)
    calling_number = calling_number[2:]
    desired_string = f"+{calling_number}"
    print(desired_string)

    with open('callingNumber.txt', 'w') as txt_file:
        txt_file.write(desired_string)
    
    

if __name__ == "__main__":
    main()