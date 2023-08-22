<h1 align="center">COCO CROPPER</h1>


### Crops annotations (bounding boxes) in COCO dataset.

### Configurables:
- ### Margin 
    - with what margin the photo is going to be cropped
- ### Minimum area 
    - minimum wanted area of the cropped photo (width*height)
- ### Minimum width
    - minimum wanted width of the cropped photo
- ### Minimum height
    - minimum wanted height of the cropped photo
- ### Classes
    - which classes are wanted among all dataset

<br>

## Usage

### 1-) Clone the repository:
    git clone https://github.com/senceryucel/coco-cropper

### 2-) Navigate into the cloned folder:
    cd coco-cropper
    
### 3-) Run the script with --help flag to see how to configure it: 
    python main.py -h

<br>

### Example usage
    python main.py -ij /path/to/your/annotations.json -id path/to/your/coco_dataset -o path/to/your/output_folder -m 0.3 -ma 20000 -mw 120 -mh 72 -c all


***
###### Sencer Yucel, 2023