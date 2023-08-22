__author__ = 'senceryucel'
from PIL import Image
import cv2
import json
from os import path, mkdir


class CocoCropper:
    def __init__(self, args) -> None:
        ALL_COCO_CLASSES = ["person", "vehicle", "animal", "outdoor", "accessory", "sports", "kitchen", "food", "furniture", "electronic", "appliance", "indoor"]
        _quit = 0
        try:
            if not path.isfile(args.input_json):
                print("Json path must have been specified correctly.")
                _quit = 1
            if not path.isdir(args.input_dataset):
                print("Coco dataset path must have been specified correctly.")
                _quit = 1
            if not path.isdir(args.output_path):
                print(f"Output path does not exist. Do you want to create it to '{args.output_path}'? [y/n]")
                choice = input("> ")
                if choice == 'y' or choice == 'Y':
                    mkdir(args.output_path)
                    print("The folder has been created.")
                else:
                    print("Output folder must have been specified.")

            self.input_json_path = args.input_json
            self.input_dataset_path = args.input_dataset
            self.output_path = args.output_path

            self.margin = float(args.margin)
            try:
                self.margin = float(args.margin)
            except ValueError as cast:
                print("Margin must be a floating number.")
                _quit = 1
            try:
                self.min_area = int(args.min_area)
            except ValueError as cast:
                print("Min area must be an integer number.")
                _quit = 1

            try:
                self.min_width = int(args.min_width)
            except ValueError as cast:
                print("Min width must be an integer number.")
                _quit = 1
            try:
                self.min_height = int(args.min_height)
            except ValueError as cast:
                print("Min height must be an integer number.")
                _quit = 1
            if args.classes[0] == "all" and len(args.classes) == 1:
                print("All classes will be included.")
                self.classes = ALL_COCO_CLASSES    
            else:
                for category in args.classes:
                    if not category in ALL_COCO_CLASSES:
                        print(f"{category} is not a category in COCO Dataset") 
                        _quit = 1
                self.classes = list(args.classes) 
                print(f"Included classes are: {self.classes}")
        except Exception as fatal:
            print(fatal.with_traceback)
            _quit = 1

        if _quit:
            quit(0)


    def set_margin(self, coordinates, width, height, margin):
        x1, y1, x2, y2 = coordinates

        if (x1 - (width*(margin/2))) < 0:
            x1 = 0
        else:
            x1 = x1 - (width*(margin/2))

        if (x2 + (width*(margin/2))) > width:
            x2 = width
        else:
            x2 = x2 + (width*(margin/2))

        if (y1 - (height*(margin/2))) < 0:
            y1 = 0
        else:
            y1 = y1 - (height*(margin/2))

        if (y2 + (height*(margin/2))) > height:
            y2 = height
        else:
            y2 = y2 + (height*(margin/2))

        return (x1, y1, x2, y2)


    def coordinate_splitter(self, x_y_width_height, min_area, min_width, min_height):
        x1 = x_y_width_height[0]
        y1 = x_y_width_height[1]
        x2 = x_y_width_height[2] + x_y_width_height[0]
        y2 = x_y_width_height[3] + x_y_width_height[1]
        bbox_area = x_y_width_height[2] * x_y_width_height[3]
        if bbox_area > min_area and x_y_width_height[2] > min_width and x_y_width_height[3] > min_height:
            return (x1, y1, x2, y2)
        else:
            return 0


    def image_file_name(self, image_id:str):
        file_name = ""
        image_id_len = len(image_id)
        remaining_zeros = 12 - image_id_len
        for j in range(remaining_zeros):
            file_name += "0"
        file_name += image_id + ".jpg"
        return file_name



    def op(self, _class, min_area, min_width, min_height, margin, annotation):
        image_id = annotation["image_id"]
        file_name = self.image_file_name(image_id=str(image_id))
        try:
            img = Image.open("{}/{}".format(self.input_dataset_path, file_name))
        except FileNotFoundError as e:
            return
        print("y")
        im = cv2.imread("{}/{}".format(self.input_dataset_path, file_name))
        img_h, img_w = im.shape[:2]
        x_y_width_height = annotation["bbox"]
        coordinates = self.coordinate_splitter(x_y_width_height=x_y_width_height, min_area=min_area, min_width=min_width, min_height=min_height)
        if coordinates == 0:
            return
        coords_with_margin = self.set_margin(coordinates=coordinates, width=img_w, height=img_h, margin=margin)
        cropped_photo = img.crop(coords_with_margin)
        cropped_photo.save("{}/{}_{}.jpg".format(self.output_path, _class, image_id))


    def print_warning(self, warning):
        print("\n###----------WARNING----------###")
        print(warning, "\n", end="")


    def main(self):
        CLASS_LISTS = {
            "person": [1],
            "vehicle": [i for i in range(2, 10)],
            "outdoor": [i for i in range(10, 16)],
            "animal": [i for i in range(16, 26)],
            "accessory": [i for i in range(26, 34)],
            "sports": [i for i in range(34, 44)],
            "kitchen": [i for i in range(44, 52)],
            "food": [i for i in range(52, 62)],
            "furniture": [i for i in range(62, 72)],
            "electronic": [i for i in range(72, 78)],
            "appliance": [i for i in range(78, 84)],
            "indoor": [i for i in range(84, 92)]
        }

        print("Reading the annotation file...")
        f = open(self.input_json_path)
        data = json.load(f)
        print("Read successfully.")

        print("Started. Len = {}".format(len(data["annotations"])))
        for c, annotation in enumerate(data["annotations"]):
            if c % 100000 == 0:
                print(c)

            ctg = annotation["category_id"]
            for wanted_category in self.classes:
                if ctg in CLASS_LISTS[wanted_category]:
                    self.op(wanted_category, self.min_area, self.min_width, self.min_height, self.margin, annotation)
            