import subprocess

def cleanup(shortcode):
    del_dir_cmd = f'rm -rv ./-{shortcode}'
    subprocess.run(del_dir_cmd, shell=True)





       
