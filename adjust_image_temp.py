"""Script to Adjust Image Temperature"""

import argparse
import os
import cv2
import numpy as np
from PIL import Image


def validate_input(input_file_path: str, output_path: str) -> bool:
    """Function to validate the input for the script"""

    # Check is the input image exists or not
    if not os.path.exists(input_file_path):
        return False

    try:
        # Check is the input_image JPEG or Not
        input_image = Image.open(input_file_path)
        # Check is the output_path valid with extension for JPEG type
        return input_image.format == 'JPEG' and output_path.lower().endswith(('.jpeg', 'jpg'))
    except IOError:
        return False


def adjust_image_temperature(input_image_path: str, output_path: str, temperature: float) -> None:
    """
    Function to adjust the image temperature and save it to output path. 
    Utilize the Grayworld Assumption
    """
    try:
        input_image = cv2.imread(input_image_path)
        # Convert the image from BGR (Blue, Green, Red) to (Lightness, a*, b*)
        result_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)

        # take the average of a* value from every pixel
        avg_a = np.average(result_image[:, :, 1])
        # take the average of b* value from every pixel
        avg_b = np.average(result_image[:, :, 2])

        # Adjust the temperature by changing every corresponding value of a and b,
        # make the adjustment by cover all the pixels / points of the image
        result_image[:, :, 1] = result_image[:, :, 1] - \
            ((avg_a - 128) * (result_image[:, :, 0] / 255.0) * -temperature)
        result_image[:, :, 2] = result_image[:, :, 2] - \
            ((avg_b - 128) * (result_image[:, :, 0] / 255.0) * -temperature)

        # Convert the image back from LAB to BGR
        result_image = cv2.cvtColor(result_image, cv2.COLOR_LAB2BGR)
        cv2.imwrite(output_path, result_image)

    except Exception as e:
        print("Failed to process image because : ", str(e))


def main():
    """Main Function to Running The Script"""
    parser = argparse.ArgumentParser(
        description="Argument to Use the Image Temperature Scripts")
    parser.add_argument("-i", "--input_file",
                        help="Name of Input Image with JPEG type", required=True)
    parser.add_argument("-o", "--output_path",
                        help="Name of Output Path for the Image with JPEG type", required=True)
    parser.add_argument("-t", "--temperature",
                        help="Temperature Adjustment for the image, \
                            positive for warmer and negative for for cooler",
                        required=True, type=float)

    args = parser.parse_args()

    if not validate_input(args.input_file, args.output_path):
        print("Invalid  Input")
    else:
        adjust_image_temperature(
            args.input_file, args.output_path, args.temperature)

        temperature_message = "Warmer"
        if args.temperature < 0:
            temperature_message = "Cooler"
        print(f'Successfully Adjust the Image Temperature to {temperature_message}')

if __name__ == "__main__":
    main()
