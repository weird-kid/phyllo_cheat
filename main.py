import os 
import  prompt_content
import subprocess
from google import genai
from download_insta import download_content
from cleanup_code import cleanup


downloaded_shortcodes = download_content()
key = os.environ['google_key']
client = genai.Client(api_key=key)



for shortcode in downloaded_shortcodes:
        file_path_root = f'./-{shortcode}/{shortcode}'

        myreel   = client.files.upload(file=file_path_root + ".mp4")
        tags = client.files.upload(file=file_path_root + ".txt")
        thumbnail = client.files.upload(file=file_path_root + ".jpg")

        response = client.models.generate_content(
                        model="gemini-2.5-flash-preview-05-20",
                        contents=[myreel, "\n\n", tags, "\n\n",thumbnail, "\n\n",  prompt_content.body1]
                        )
        
        cmd = f"open ./{shortcode}/{shortcode}.mp4" 
        subprocess.run(cmd, shell=True)         
        print('\t', response.text, '\n')
        input()
        print('--------------------------------------------')

