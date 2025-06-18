import subprocess
import os

def download_content():
        n = int(input("Enter no. of links:\n"))
        insta_id = os.environ['username']
        all_shortcodes = []

        for __ in range(n):
                link = input()
                shortcode = link.replace("https://www.instagram.com/p/", "")
                all_shortcodes.append(shortcode)

        print("-----------------------------------------XXXXXXXXX------------------------------------------\n")
        
        for shortcode in all_shortcodes:
                print(f'Starting to Download content from https://www.instagram.com/p/{shortcode}')
                cmd = f"instaloader  --quiet --session={insta_id} --filename-pattern='{shortcode}' --  -"  + shortcode + " 2> /dev/null" 
                subprocess.run(cmd, shell=True) 
                print(f'Finished Downloading content from https://www.instagram.com/p/{shortcode}\n')
 
         
        return all_shortcodes


if __name__ == "__main__":
    download_content()
