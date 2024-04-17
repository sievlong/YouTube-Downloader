from pytube import YouTube
import os
import time

print("""
|---------------------------------------|
|----- Welcome to Video Downloader -----|
|---------------------------------------|
      
             options:
    Enter 1: Youtube download
    Enter 2: Exit
""")

while True:
    try:
        user_input = int(input("Please select an option: "))
        if user_input >= 3:
            exit("Please try again")
    except ValueError:
        exit("Hey! That's not a number")

    if user_input == 1:
        url = input("Enter the Youtube URL here: ")
        if "youtube.com" in url:
            start_time = time.time()  
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            
            save_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
            
            os.makedirs(save_dir, exist_ok=True)

            filename = stream.default_filename
            file_path = os.path.join(save_dir, filename)
            stream.download(output_path=save_dir)
            
            end_time = time.time()  
            download_time = end_time - start_time  
            print(f"Download completed in {download_time:.2f} seconds. Saved to {file_path}")
        else:
            print("Wrong URL. Only YouTube URLs are supported for downloading videos.")

    if user_input == 2:
        print("Thank you for using our YouTube Downloader!")
        break

    time.sleep(2)
    response = input("Would you like to continue: [y/n]")
    if response == "n":
        print("Thank you for using our YouTube Downloader!")
        break
