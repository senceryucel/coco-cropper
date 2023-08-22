__author__ = 'senceryucel'

from coco_cropper import CocoCropper
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="COCO Dataset - Bounding box cropper")
    parser.add_argument("-ij", "--input_json_path", dest="input_json",
                        help="Path to a json file in coco format.")
    parser.add_argument("-id", "--input_dataset_path", dest="input_dataset",
                        help="Path to a dataset with annotations being labeled in the json file.")
    parser.add_argument("-o", "--output_path", dest="output_path",
                        help="Path to your output directory.")
    parser.add_argument("-m", "--margin", dest="margin", default=0.12,
                        help="Crop margin rate. Defaults to 0.12")
    parser.add_argument("-ma", "--min_area", dest="min_area", default=16384, 
                        help="Minimum area for a bounding box to be cropped. Defaults to 16384.")
    parser.add_argument("-mw", "--min_width", dest="min_width", default=96, 
                        help="Minimum width for a bounding box to be cropped. Defaults to 96.")
    parser.add_argument("-mh", "--min_height", dest="min_height", default=96, 
                        help="Minimum height for a bounding box to be cropped. Defaults to 96.")
    parser.add_argument("-c", "--classes", nargs='+', dest="classes", default=["person"],
                        help="List of wanted class names separated by spaces, e.g. -c person dog bicycle. For all classes: all")
    
    args = parser.parse_args()
    cropper = CocoCropper(args)
    cropper.main()