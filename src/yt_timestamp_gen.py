# this program generates youtube timestamps from piped data from `ffprobe <file.m4b>` command ran in terminal.

import argparse
import re
import os

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Process a text file containing ffprobe command output ran on .m4b file.")
    parser.add_argument('-file', type=str, required=True, help='Path to the text file containing ffprobe command output')
    args = parser.parse_args()

    # Read the text file
    try:
        with open(args.file, 'r') as file:
            all_lines = file.read();
    except Exception as e:
        print(f"Failed to read or parse file: {e}")
        exit(1)

    # Process the data (for demonstration, we simply print it)
    chapter_data = re.findall(r'Chapter\s\#\d+\:(\d+)\:\sstart\s(\d+)[.]\d+[,]\send\s(\d+)', all_lines)
    # for chapter in chapter_list:
    chapter_titles = re.findall(r'title\s+\:\s([^\n]+)' , all_lines)
    
    if len(chapter_data) == 0:
        print("regex couldn't find any timestamps in given data.")
        return None
    
    if len(chapter_titles) == 0:
        print("regex didn't find any chapter titles.")
        return None

    if len(chapter_data) == len(chapter_titles):
        # make list of dict containing attribues like: title, start, end
        chapters = []
     
        for i in range(0, len(chapter_data)):
            title = chapter_titles[i]
            start = yt_timestamp(int(chapter_data[i][1]))
            end = yt_timestamp(int(chapter_data[i][2]))
            chapters.append({'title': title, 'start': start, 'end': end})

        write_output_file(chapters, generate_new_file_path(file))

    else:
        print("No. of timestamps do not match no. of chapter titles. it means either data is inconsistent to be detected or a bug in regex pattern chosen to match data.")
        return None

def write_output_file(chapters, path):
    try:
        with open(path, 'w') as file:
            for chapter in chapters:
                file.write(f"{chapter['start']} {chapter['title']}\n")
            print(f"<File Created> : {file.name}")
    except Exception as e:
        print(f"Failed to read or parse file: {e}")
        exit(1)

def generate_new_file_path(old_file):
    (parent_dir, basename) = os.path.split(old_file.name)
    new_file_path = f'{parent_dir}{os.sep}yt_desc_{basename}'
    index = 0
    (stem, ext) = os.path.splitext(new_file_path)
    while os.path.exists(new_file_path):
        index += 1
        new_file_path = f'{stem}{index}{ext}'
    return new_file_path

def yt_timestamp(s):
    hrs = s // 3600
    mins = s // 60 % 60
    secs = s % 60

    hrs_str = f"0{hrs}" if hrs < 10  else f"{hrs}"
    mins_str = f"0{mins}" if mins < 10 else f"{mins}"
    secs_str = f"0{secs}" if secs < 10 else f"{secs}"
    return f"{hrs_str}:{mins_str}:{secs_str}"

if __name__ == "__main__":
    main()
