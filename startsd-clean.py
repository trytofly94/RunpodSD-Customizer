#######################################
#Install everything you want in one script kind of...
#######################################
# Disclaimer: I am not proficient in writing python or knowing what to implement how. I tried my best to get it to working with examples and ChatGPT.
# If you use this to make a better one, please let me know. I'm shure there are better ways then this. But for now it works...

#### SET YOUR ROOT HERE 
root = "/workspace"

# these imports are partially taken from the script use in the fast-sd template from runpod bcs I implemented a small portion of their code. 

import os
import shutil
from IPython.display import clear_output
from subprocess import call, getoutput, Popen, run
import time
import ipywidgets as widgets
import requests
import sys
import fileinput
from torch.hub import download_url_to_file
from urllib.parse import urlparse
import re

#######################################
#INSTALL STUFF
#######################################
# Not shure if everything is needed or preinstalled, but it doesn't hurt

try:
    os.system("pip install gdown")
    print("gdown successfully installed!")
except Exception as e:
    print("An error occurred while installing gdown:", e)
    
import gdown

result = os.system("apt-get update")
if result == 0:
    print("Package list updated successfully!")
else:
    print("An error occurred while updating package list.")

# install git
result = os.system("apt-get install -y git")
if result == 0:
    print("git installed successfully!")
else:
    print("An error occurred while installing git.")

#install aria2c
result = os.system("apt-get install -y aria2")
if result == 0:
    print("aria2c installed successfully!")
else:
    print("An error occurred while installing aria2c.")

#install runpodctl
result = os.system("wget --quiet --show-progress https://github.com/Run-Pod/runpodctl/releases/download/v1.9.0/runpodctl-linux-amd -O runpodctl && chmod +x runpodctl && cp runpodctl /usr/bin/runpodctl")
if result == 0:
    print("runpodctl installed successfully!")
else:
    print("An error occurred while installing runpodctl.")

#######################################
#import your own settings from Google Drive. Uncomment to activate
#######################################
# Not shure if everything is needed or preinstalled, but it doesn't hurt
# Different versions of gdown are used here. mainly because of copying and convenience how 

#import setting files from google drive
#settings_output = f"{root}/stable-diffusion-webui"
#if os.path.exists(f'{root}/stable-diffusion-webui/ui-config.json'):
#    os.remove(f'{root}/stable-diffusion-webui/ui-config.json')
#file_url = "Your Link"
#gdown.download(url=file_url, output=settings_output, quiet=False, fuzzy=True)

#if os.path.exists(f'{root}/stable-diffusion-webui/config.json'):
#    os.remove(f'{root}/stable-diffusion-webui/config.json')
#file_url="Your Link"
#gdown.download(url=file_url, output=settings_output, quiet=False, fuzzy=True)

# download parameter file from google drive
#if os.path.exists(f'{root}/stable-diffusion-webui/params.txt'):
#    os.remove(f'{root}/stable-diffusion-webui/params.txt')
#file_url="Your Link"
#gdown.download(url=file_url, output=settings_output, quiet=False, fuzzy=True)

#######################################
#UPSCALERS
#######################################
def download_upscalers():
    upscalers_path = f"{root}/stable-diffusion-webui/models/ESRGAN/"
    upscalers = [
        "Your Link",
        "Your Link"
    ]
    if not os.path.exists(upscalers_path):
        os.makedirs(upscalers_path)

    for upscaler in upscalers:
        print(f"Cloning {upscaler} into {upscalers_path}...")
        gdown.download(url=upscaler, output=upscalers_path, quiet=False, fuzzy=True)

download_upscalers()

#######################################
#MODELS
#######################################
def download_models():
    models_path = f"{root}/stable-diffusion-webui/models/Stable-diffusion"
    models = [
        "Your Link",
        "Your Link"
    ]
    for model in models:
        for model in models:
            command = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {model} -d {models_path}"
            result = os.system(command)
            if result == 0:
                print(f"{model} downloaded successfully!")
            else:
                print(f"An error occurred while downloading {model}.")
                 

download_models()

#######################################
#VAE
#######################################
VAEs = [
    "https://huggingface.co/stabilityai/sd-vae-ft-ema-original/resolve/main/vae-ft-ema-560000-ema-pruned.ckpt",
    "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt"
]
for VAE in VAEs:
    filepath = f"{root}/stable-diffusion-webui/models/VAE"
    command = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {VAE} -d {filepath}"
    result = os.system(command)
    if result == 0:
        print(f"{VAE} downloaded successfully!")
    else:
        print(f"An error occurred while downloading {VAE}.")
print("VAE install completed.")
                 
#######################################
#LORAS
#######################################
def download_loras():
    Lora_path = f"{root}/stable-diffusion-webui/models/Lora"
    if not os.path.exists(Lora_path):
        os.makedirs(Lora_path)

    # Loras in Google Drive. Uncomment to use
    #GLoras = [
    #    "Your Link",
    #    "Your Link"
    #]
    #for GLora in GLoras:
    #    print(f"Cloning {GLora} into {Lora_path}...")
    #    gdown.download(url=GLora, output=Lora_path, quiet=False, fuzzy=True)

    Loras = [
        "Your Link",
        "Your Link"
    ]
         
    for Lora in Loras:
        command = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {Lora} -d {Lora_path}"
        result = os.system(command)
        if result == 0:
            print(f"{Lora} downloaded successfully!")
        else:
            print(f"An error occurred while downloading {Lora}.")
                 
download_loras()
#######################################
#EXTENSIONS, I left some in so u don't have to search
#######################################
def download_extensions():
    if os.path.exists(f'{root}/stable-diffusion-webui/extensions'):
        shutil.rmtree(f'{root}/stable-diffusion-webui/extensions')
        os.mkdir(f'{root}/stable-diffusion-webui/extensions')
    extensions_path = f"{root}/stable-diffusion-webui/extensions"
    extensions = [
        "https://github.com/deforum-art/deforum-for-automatic1111-webui",
        "https://github.com/camenduru/stable-diffusion-webui-images-browser",
        "https://github.com/camenduru/stable-diffusion-webui-huggingface",
        "https://github.com/camenduru/sd-civitai-browser",
        "https://github.com/kohya-ss/sd-webui-additional-networks",
        "https://github.com/camenduru/openpose-editor",
        "https://github.com/jexom/sd-webui-depth-lib",
        "https://github.com/hnmr293/posex",
        "https://github.com/camenduru/sd-webui-tunnels",
        "https://github.com/etherealxx/batchlinks-webui",
        "https://github.com/camenduru/stable-diffusion-webui-catppuccin",
        "https://github.com/KohakuBlueleaf/a1111-sd-webui-locon",
        "https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg",
        "https://github.com/ashen-sensored/stable-diffusion-webui-two-shot",
        "https://github.com/camenduru/sd_webui_stealth_pnginfo"
    ]
    for extension in extensions:
        print(f"Cloning {extension} into {extensions_path}...")
        command = f"git clone {extension} {os.path.join(extensions_path, os.path.basename(extension).replace('.git', ''))}"
        result = os.system(command)
        if result == 0:
            print(f"{extension} cloned successfully!")
        else:
            print(f"An error occurred while cloning {extension}.")


download_extensions()

#######################################
# CONTROLNET with all models
# The Controlnet Application didnt work like above but the Runpod Template Fast SD had a better implementation then mine so i used that
# Future improvement would be to get all extension installation in this format.
# This uses the model list in the TheLastBen colab notebook

def download(url, model_dir):
    filename = os.path.basename(urlparse(url).path)
    pth = os.path.abspath(os.path.join(model_dir, filename))
    if not os.path.exists(pth):
        print('Downloading: '+os.path.basename(url))
        download_url_to_file(url, pth, hash_prefix=None, progress=True)
    else:
      print(f"[1;32mThe model {filename} already exists[0m")    

wrngv1=False
os.chdir(f'{root}/stable-diffusion-webui/extensions')
if not os.path.exists("sd-webui-controlnet"):
  call('git clone https://github.com/Mikubill/sd-webui-controlnet.git', shell=True)
  os.chdir(f'{root}')
else:
  os.chdir('sd-webui-controlnet')
  call('git reset --hard', shell=True, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
  call('git pull', shell=True, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
  os.chdir(f'{root}')

mdldir=f"{root}/stable-diffusion-webui/extensions/sd-webui-controlnet/models"
for filename in os.listdir(mdldir):
  if "_sd14v1" in filename:
    renamed = re.sub("_sd14v1", "-fp16", filename)
    os.rename(os.path.join(mdldir, filename), os.path.join(mdldir, renamed))

call('wget -q -O CN_models.txt https://github.com/TheLastBen/fast-stable-diffusion/raw/main/AUTOMATIC1111_files/CN_models.txt', shell=True)
call('wget -q -O CN_models_v2.txt https://github.com/TheLastBen/fast-stable-diffusion/raw/main/AUTOMATIC1111_files/CN_models_v2.txt', shell=True)

with open("CN_models.txt", 'r') as f:
    mdllnk = f.read().splitlines()
with open("CN_models_v2.txt", 'r') as d:
    mdllnk_v2 = d.read().splitlines()
call('rm CN_models.txt CN_models_v2.txt', shell=True)

cfgnames=[os.path.basename(url).split('.')[0]+'.yaml' for url in mdllnk_v2]
os.chdir(f'{root}/stable-diffusion-webui/extensions/sd-webui-controlnet/models')
for name in cfgnames:
    run(['cp', 'cldm_v21.yaml', name])
os.chdir(f'{root}')

for lnk in mdllnk:
  download(lnk, mdldir)
clear_output()


# Copy Loras to use in the Additional Networks extension. 
src_folder = f"{root}/stable-diffusion-webui/models/Lora"
dst_folder = f"{root}/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora"
for item in os.listdir(src_folder):
    src_item = os.path.join(src_folder, item)
    dst_item = os.path.join(dst_folder, item)
    
    if os.path.isfile(src_item):
        shutil.copy2(src_item, dst_item)
    elif os.path.isdir(src_item):
        shutil.copytree(src_item, dst_item)

#######################################
#other stuff
#######################################
# change working directory
os.chdir(f"{root}/stable-diffusion-webui")
# reset git repository
result = os.system("git reset --hard")
if result == 0:
    print("Git repository reset successfully!")
else:
    print("An error occurred while resetting Git repository.")

# install controlnet requirements In another script it was called at this point after the reset, so I left it here.
# change working directory
os.chdir(f"{root}/stable-diffusion-webui/extensions/sd-webui-controlnet")

result = os.system("pip install -r requirements.txt")
if result == 0:
    print("Requirements.txt installed successfully!")
else:
    print("An error occurred while installing the requirements.txt")

# change working directory to stable-diffusion-webui
os.chdir(f"{root}/stable-diffusion-webui/")

# took this from the google colab code I used before. No idea why it changes that line and it doesn't work. so off it goes... (I know I'm a mess)
# Replace `prepare_environment()` with `prepare_environment():`
#os.system(f"""sed -i -e '/prepare_environment():/a\    os.system(f\\"sed -i -e ''\\"s/dict()))/dict())).cuda()/g\\"'' {root}/stable-diffusion-#webui/repositories/stable-diffusion-stability-ai/ldm/util.py" {root}/stable-diffusion-webui/launch.py""")
#os.system(f"""cd {root}/stable-diffusion-webui/repositories/k-diffusion; git config core.filemode false""")

#I cant get this to work, so I'm uploading a custom webur-user.sh for now and start using relauncher.py included in the sd template

#args = "--port 3010 --gradio-img2img-tool color-sketch -- share --listen --enable-insecure-extension-access --gradio-queue --xformers"
#SET USERNAME AND PASSWORD
#username = "Lennart"
#password = "C"
#if username and password:
#    args += f" --gradio-auth {username}:{password} "
#cmd = f"python {root}/stable-diffusion-webui/launch.py {args}"
#result = os.system(cmd)

# make a1111 use the newest torch version, found this online...
call('pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu118', shell=True)

print("All done!")