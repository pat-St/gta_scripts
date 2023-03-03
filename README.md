# Usage #

> Note: There is no guarantee for using this script, and you may be banned for cheating or hacking.
> It is strictly forbidden to sell or market this project or to profit further from it.
> This project is for **private usage only**.

This script bundle works only for *1920x1080* monitors.
Start by executing: `python main.py` and select the automation job.
While the script run, you can use the following global keyboard events.

| Keyboard press | Description                              |
| :---:          | :---                                     |
| `x`            | you start your job.                      |
| `p`            | the script pause the job.                |
| `q`            | the script quits and return to main.     |

## Purpose ##

The purpose of this project is a bundle of automations for GTA RP farming jobs.

## Pre requirements ##

Install Python Version **3.10**:

- For Windows Install the 64Bit Version from [here](https://www.python.org/downloads/release/python-31010/).
- For *nix systems, use your system Package manager.

Check the current version, open a terminal and execute `python -V`.

> **For GPU usage (recommended)**
>
> Use this method only if your graphic card is capable for [CUDA](https://developer.nvidia.com/cuda-gpus#collapse4):
>
> 1. Install CUDA in the Version 11.7 form [this](https://developer.nvidia.com/cuda-11-7-1-download-archive) site.
>
> 2. Open the following [Link](https://pytorch.org/get-started/locally/) and select your setup and choose **CUDA Version 11.7**.
>
> 3. Copy the generated Command and execute it in your terminal.
>
> 4. Now restart your computer.

Install all required dependencies by executing: `pip install -r < requirements.txt`

## Train your model ##

1. Edit the `.env` file and insert your **export api key** from [Roboflow](https://docs.roboflow.com/exporting-data#export-with-the-python-package)

2. Now execute the `train.ipynb` file with Jupyter Notebook.

3. The final model can be found under `runs/train/weight/best.pt`.

4. Copy the model into the `assets` folder.

5. Finally, update the *fishing job* Parameter.

unzip model:

```
zip -F asstes/model3.zip --out single-model3.zip
unzip single-model3.zip --out assets/
```
