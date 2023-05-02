from PIL import Image
import cv2
import json

class CocoCropper:
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



    def op(self, _class, min_area, min_width, min_height, margin):
        image_id = i["image_id"]
        file_name = image_file_name(image_id=str(image_id))
        img = Image.open("{}/{}".format(data_dir, file_name))
        im = cv2.imread("{}/{}".format(data_dir, file_name))
        img_h, img_w, img_c = im.shape
        x_y_width_height = i["bbox"]
        coordinates = coordinate_splitter(x_y_width_height=x_y_width_height, min_area=min_area, min_width=min_width, min_height=min_height)
        if coordinates == 0:
            return
        coords_with_margin = set_margin(coordinates=coordinates, width=img_w, height=img_h, margin=margin)
        cropped_photo = img.crop(coords_with_margin)
        
        # TODO: OUTPUT DIR
        cropped_photo.save("/home/sencer/Desktop/cropped_coco_c3/{}/{}.jpg".format(_class, image_id))


    def print_warning(self, warning):
        print("\n###----------WARNING----------###")
        print(warning, "\n")


    def main(self, args):
        
        try:
            f = open(args.input_json)
            dataset_dir = args.input_dataset
        except Exception as e:
            print_warning("Check the correctness of your paths.", e)
            quit()
        
        margin = args.margin
        min_area = args.min_area
        min_width = args.min_width
        min_height = args.min_height

        data = json.load(f)
        print("Started. Len = {}".format(len(data["annotations"])))
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

        for c, i in enumerate(data["annotations"]):
            if c % 1000 == 0:
                print(c)
            ctg = i["category_id"]

            if ctg in CLASS_LISTS["person"]:
                pass

            elif ctg in CLASS_LISTS["vehicle"]:
                pass

            elif ctg in CLASS_LISTS["animal"]:
                pass

            elif ctg in CLASS_LISTS["outdoor"]:
                op("outdoor", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["accessory"]:
                op("accessory", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["sports"]:
                op("sports", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["kitchen"]:
                op("kitchen", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["food"]:
                op("food", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["furniture"]:
                op("furniture", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["electronic"]:
                op("electronic", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["appliance"]:
                op("appliance", min_area=16384, min_width=96, min_height=96, margin=0.12)

            elif ctg in CLASS_LISTS["indoor"]:
                op("indoor", min_area=16384, min_width=96, min_height=96, margin=0.12)

            else:
                print_warning("Found a photo without any label. You may want to check either your json or your dataset dir.")


if __name__ == "__main__"
    import argparse
    parser = argparse.ArgumentParser(description="COCO Dataset - Bounding box cropper")
    parser.add_argument("-i", "--input_json", dest="input_json",
                        help="Path to a json file in coco format.")
    parser.add_argument("-i", "--input_dataset", dest="input_dataset",
                        help="Path to a dataset with annotations being labeled in the json file.")
    parser.add_argument("-i", "--margin", dest="margin", default=0.12,
                        help="Crop margin rate. Defaults to 0.12")
    parser.add_argument("-i", "--min_area", dest="min_area", default=16384, 
                        help="Minimum area for a bounding box to be cropped. Defaults to 16384.")
    parser.add_argument("-i", "--min_width", dest="min_width", default=96, 
                        help="Minimum width for a bounding box to be cropped. Defaults to 96.")
    parser.add_argument("-i", "--min_height", dest="min_height", default=96, 
                        help="Minimum height for a bounding box to be cropped. Defaults to 96.")
    parser.add_argument("-c", "--classes", nargs='+', dest="classes",
                        help="List of wanted class names separated by spaces, e.g. -c person dog bicycle")
    
    args = parser.parse_args()

    main(args)


# TODO: output dir as an argument
# TODO: class exists but the object does not
# TODO: classes that comes with --classes are going to be put in a list, then there'll be a condition check
# TODO: test