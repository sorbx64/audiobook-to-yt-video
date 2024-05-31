# Audiobook (.m4b) generation process

1. If working on windows, setup WSL (if not already setup). if you're on linux you are all set.
1. Setup pyenv in wsl. Append commands to `.bashrc` file to start pyenv on terminal startup. Ask gpt-4o - "how to setup pyenv in wsl?". i checked it, gpt-4o is pretty good at answering this.
1. Clone git repo, [epub2tts-edge](https://github.com/aedocw/epub2tts-edge)
1. Install python version, using pyenv, as required by cloned epubtts-edge project. In time of wrting of this `README.md` it is python 3.11.
1. Follow the setup / configuration procedure mentioned in epubtts-edge `README.md`.
1. After all above setup done, goto epub2tts-edge directory and run command `epub2tts-edge <file.epub>` in terminal. It will generate a text file with same name as epub file. 
1. Open this text file and check for missing text and headings. As, it has been found to be inaccurate in converting epub file to text file exactly line by line. Lookout for lines begining with `#` symbol. It shows that text in front of it will be read with pause as a separate chapter. Also, this text will appear as chapter's title in metadata of audiobook (.m4b file), when we will generate it. 
1. Now, to generate audiobook from text file. Run `epub2tts-edge <file.txt>` command in terminal. Audiobook (.m4b) generation process will start. To change speaker voice and language, checkout epub2tts-edge `README.md` file. NOTE: To read hindi language text, use `--speaker bn-IN-BhashkarNeural` or `--speaker bn-IN-TanishaaNeural` flag while running this command. To see list of supported voices you can use with `--speaker` flag,  checkout `SUPPORTED_VOICES` variable in this [python file](https://github.com/hasscc/hass-edge-tts/blob/main/custom_components/edge_tts/tts.py)
1. After audiobook has been generated, run command `ffprobe <audiobook.m4b>` to see metadata (including chapters) of audiobook.

# To generate video (.mp4) file from audiobook (.m4b) 

If you want to make a video with animations/motiongraphics from this audiobook you should use a video editor like *openshot*. Otherwise, if you just want to convert this audiobook into video format to be uploaded on youtube follow the instructions below. -

1. Clone this repo. Open it in terminal.
1. Run `pip install moviepy`
1. cd into `/src` directory.
1. Run - 

```shell
python m4b_to_mp4_converter.py <audio> <image> <output_folder> --fps <fps_count>
```
<audio> : path to audio file to be used for video.
<image> : path to image to be used in video over its entire duration. TIP: Use dimensions of image as you would want your video's dimensions.
<output_folder> : path to store the output video file.
<fps_count> : describe fps for entire video. If video will just have one still image for entire duration then just use fps_count as 1.

# To generate youtube timestamps from audiobook (.m4b)

1. Run `ffprobe audiobook.m4b 2> output.txt`

NOTE: `2>` is being used here because `ffprobe file.m4b` outputs to stderr.

1. Clone this repo. Open it in terminal.
1. cd into `/src` directory.
1. Run - 

```shell
python yt_timestamp_gen.py -file path/to/output.txt
```
This command will generate new text file that contains all timestamps required by youtube to display as chapters. Simply copy contents in text file and paste in youtube description of the video. The text file name will have prefix "yt_desc_" before <input_file>. Example in this case: yt_desc_output.txt

## NOTE
- If a generated file already exists (say `yt_desc_file.txt`) in same path then a number will be added to end of filename and new file will be created. Therefore, new filename will be `yt_desc_file1.txt`
- `yt_timestamp_gen.py` was tested on python 3.10 and 3.11. 






