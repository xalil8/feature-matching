import os,yaml,shutil,cv2
from itertools import chain

cropped_folder_path = "./cropped2"
dataset_path = "./dataset"

#resized_path = "reshaped/"

my_dict = {}
rem_dict ={} 

##########read yaml file to get class information #################

for file_names in os.listdir(dataset_path):
    if file_names.endswith(".yaml"):
        yaml_path = dataset_path+"/"+file_names
        #yaml_path = os.path.join(dataset_path,file_names)

with open(yaml_path, 'r') as file:
    # load the contents of the file into a Python object
    data = yaml.load(file, Loader=yaml.FullLoader)
class_yaml = data["names"]

##########################################################
#create rem_dictionary , for each class, add files names which has contain that class labels in it 

for class_name in class_yaml:
    rem_dict.setdefault(class_name, [])
    my_dict.setdefault(class_name, {})
    my_dict[class_name].update({"images":{},"cropped_logo_images":[],"average_size":{},"counter":1})

###################################################

process_counter = 0

for my_folder in os.listdir(dataset_path):
    #check if file is folder 
    #sub_folder = os.path.join(dataset_path, my_folder)
    sub_folder = dataset_path+"/"+my_folder
    if os.path.isdir(sub_folder):
        for txt_file_name in os.listdir(os.path.join(dataset_path, my_folder)+"\labels"):

            #img_name_short = txt_file_name.split('_')[0]
            jpg_path = sub_folder+"/images/"+ txt_file_name.replace('.txt', '.jpg')
  
            img = cv2.imread(jpg_path)
            try:
                
                with open(sub_folder+"/labels/"+txt_file_name) as f:
                    lines = f.read().strip().split('\n')
                
                for line in lines:
                    process_counter +=1
                    if process_counter %100 ==0:
                        print(process_counter)
                    
                    class_order, x, y, w, h = line.strip().split()
                    label_name = class_yaml[int(class_order)]
                    x, y, w, h = float(x), float(y), float(w), float(h)
                    x1, y1, x2, y2 = round((x-w/2) * 1280), round((y-h/2) * 720), round((x+w/2) * 1280), round((y+h/2) * 720)
                    
                    #image cropping and saving 
                    
                    
                    counter = my_dict[label_name]["counter"]

                    cropped_img_name = f"{label_name}_{counter}.jpg"
                    #cropped_img_path = os.path.join(cropped_folder_path, cropped_img_name)
                    cropped_img_path = cropped_folder_path+"/"+cropped_img_name

                    my_dict[label_name]["cropped_logo_images"].append({"cropped_path":cropped_img_path,"size":{"x":x2-x1,"y":y2-y1},"source_image":jpg_path})
                    
                    #my_dict[label_name]["cropped_logo_images"].update({cropped_img_path:{"size":{"x":x2-x1,"y":y2-y1},"source_image":jpg_path}})
                    
                    rem_dict[label_name].append(sub_folder+"/images/"+ txt_file_name.replace('.txt', '.jpg'))

                    my_dict[label_name]["counter"] += 1
                    cropped_img = img[y1:y2, x1:x2]
                    cv2.imwrite(cropped_img_path, cropped_img)

            except ValueError:
                print("error","image doesnt have logo")
                pass

##################################################################        
#to add images from rem_dict
for i in rem_dict:
    my_dict[i].update({"images":rem_dict[i]})
del rem_dict

#GET AVERAGE OF CROPPED SIZE BY CLASS#
##################################################################
for q in my_dict:
    x_sum,y_sum=0,0
    for m in my_dict[q]["cropped_logo_images"]:
        div = len(my_dict[q]["cropped_logo_images"])
        #used for {} cropped images
        #x_sum += my_dict[q]["cropped_logo_images"][m]["size"]["x"]

        x_sum += m["size"]["x"]
        y_sum += m["size"]["y"]
    x_avg, y_avg = round(x_sum/div), round(y_sum/div)
    my_dict[q]["average_size"].update({"x":x_avg,"y":y_avg})
#####################################################################
#to clear duplicate image names in images dict
for classes in my_dict:
    my_dict[classes]["images"] = [*{*my_dict[classes]["images"]}]

#############Reshaping cropped imaged in scale of average #############
counter = 0
for clas_name in my_dict:
    avg_size =  (my_dict[clas_name]["average_size"]["x"],my_dict[clas_name]["average_size"]["y"])
    #print(avg_size)
    for image_path in my_dict[clas_name]["cropped_logo_images"]:
    
        img = cv2.imread(image_path["cropped_path"])  
        img_resized = cv2.resize(img, avg_size)
        cv2.imwrite(image_path["cropped_path"], img_resized)

        counter+=1
        if counter%100 ==0:
            print(counter,"image are resized")