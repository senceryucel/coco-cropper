![alt text](assets/coco-logo.png "Coco Logo")

<br><br>

<h1 style="font-size: 50px" align="center">COCO CROPPER</h1>


### Crops annotations (bounding boxes) in COCO dataset.

<br>

# Configurables:
- ### Margin 
    - with what margin the photo is going to be cropped
- ### Minimum area 
    - minimum wanted area of the cropped photo in pixels (width*height)
- ### Minimum width
    - minimum wanted width of the cropped photo in pixels
- ### Minimum height
    - minimum wanted height of the cropped photo in pixels
- ### Classes
    - which classes are wanted among all dataset

<br>



# Examples

- ### Below examples have been created with the following configuration:
    - margin = 0.12 (%)
    - min_area = 16384 (pixels)
    - min_width = 96 (pixels)
    - min_height = 96 (pixels)




### Input 1
![alt text](assets/examples/000000051278.jpg "000000051278.jpg")
### Output 1 - Vehicle
![alt text](assets/examples/vehicle_51278.jpg "vehicle_51278.jpg")

### Input 2
![alt text](assets/examples/000000051281.jpg "000000051281.jpg")
### Output 2 - Animal
![alt text](assets/examples/animal_51281.jpg "animal_51281.jpg")

### Input 3
![alt text](assets/examples/000000075179.jpg "000000075179.jpg")
### Output 3 - Person
![alt text](assets/examples/person_75179.jpg "person_75179.jpg")
### Output 3 - Outdoor
![alt text](assets/examples/outdoor_75179.jpg "outdoor_75179.jpg")


<br><br>

# Usage

#### 0-) Download the COCO dataset with the annotations json from below link if you do not have them yet:
    https://cocodataset.org/#download

#### 1-) Clone this repository:
    git clone https://github.com/senceryucel/coco-cropper

#### 2-) Navigate into the folder:
    cd coco-cropper
    
#### 3-) Download prerequisites:
    python3 -m pip install -r requirements.txt
    
#### 4-) Run the script with the -h flag to see how to configure it: 
    python3 src/main.py -h

<br>

### Example usage
    python3 src/main.py -ij ~/path_to/instances_train2017.json -id ~/path_to/train2017 -o ~/path_to/outputs/ -m 0.12 -ma 16384 -mw 96 -mh 96 -c all


<br>

***
###### Sencer Yucel, 2023