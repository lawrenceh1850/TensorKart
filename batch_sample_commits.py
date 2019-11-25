import glob
import os
import subprocess

gs_msg = subprocess.check_output("git status", shell=True)
for folder in glob.glob("samples/*"):
    if folder in str(gs_msg):
        os.system(f"git add {folder}")
        os.system(
            f"git commit -am \"Batch commit of sample data {folder}\"")
        os.system("git push")
