# ubersnap_image_temperature

This is the repo contains solution for Ubersnap Software Developer Challenge

## Purpose

The script `adjust_image_temp.py` can adjust the temperature of input image and save the result to image. The script only accepts **JPEG**  type image. The script make it possible to make the image color look cooler or warmer. See the results of temperature adjustment in folder `demo_images`.

## How to Use

### Installation
You can create python virtual environment using venv or conda.

e.g Using venv to create the environment

```console
username@user:~$ python3.10 -m venv .venv
username@user:~$ source .venv/bin/activate
(venv) username@user:~$ pip install -r requirements.txt
```

### Arguments
```console
(venv) username@user:~$ python adjust_image_temp.py -h
usage: adjust_image_temp.py [-h] -i INPUT_FILE -o OUTPUT_PATH -t TEMPERATURE

Argument to Use the Image Temperature Scripts

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Name of Input Image with JPEG type
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Name of Output Path for the Image with JPEG type
  -t TEMPERATURE, --temperature TEMPERATURE
                        Temperature Adjustment for the image, positive for
                        warmer and negative for for cooler
```

### Template to run the script
```console
(venv) username@user:~$ python adjust_image_temp.py --input_file [image_file_path] --output_path [image_output_name] -t [decimal number]
```

### Example 
```console
(venv) username@user:~$ python adjust_image_temp.py --input_file demo_images/input/demo_2.jpg --output_path demo_images/output/demo_2_cooler_out.jpeg -t -4
Successfully Adjust the Image Temperature to Cooler

(venv) username@user:~$ python adjust_image_temp.py --input_file demo_images/input/demo_2.jpg --output_path demo_images/output/demo_2_warmer_out.jpeg -t 4
Successfully Adjust the Image Temperature to Warmer
```

### Explanation

The script is implemented based on Grayworld Assumption. Assuming that we have a good distribution of colors in our scene, the average reflected color should be the color of the light. If the light source is assumed to be white, we know how much the whitepoint should be moved in the color cube. Check further on [this link](https://pippin.gimp.org/image-processing/chapter-automaticadjustments.html) for more details about the algorithm.
