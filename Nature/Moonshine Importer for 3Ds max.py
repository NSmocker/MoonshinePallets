import requests, zipfile
from io import BytesIO
import os
import bpy
from mathutils import Euler, Matrix
from math import radians


models_in_pallet = 8
pallet_url ='https://github.com/NSmocker/MoonshinePallets/raw/main/Nature/' #url where to download fbx files
folder_for_files ='D:/git_pallets/'#folder to localy save fbx pallet
files_to_import ="C:/Users/Silver Echo/Desktop/moonshine_save/" #txt files extracted from vr glasses
count_of_txt_files = 45

#Todo fix transforms
def dwonload_pallet():
    print("start downloading pallet")
    for i in range(1,models_in_pallet):
        url = pallet_url + str(i)+".zip"
        filename = url.split('/')[-1]
        req = requests.get(url)
        unzipper= zipfile.ZipFile(BytesIO(req.content))
        unzipper.extractall(folder_for_files+str(i)+'/')
      
    print("Pallet Downloaded on folder"+ folder_for_files)





def open_my_file(number):
   
    f = open(files_to_import+str(number)+".txt", "r")
    print("opening..."+files_to_import+str(number)+".txt" )
    #відкрився текстовий файл
   
    object_info = f.readlines()
    number_of_model = object_info[0].split('=')[1].replace(",",".").replace("\n","").split('/')[-1].split('.')[0]
    pos_x =  object_info[1].split('=')[1].replace(",",".").replace("\n","")
    pos_y =  object_info[2].split('=')[1].replace(",",".").replace("\n","")
    pos_z =  object_info[3].split('=')[1].replace(",",".").replace("\n","")
    angle_x =  object_info[4].split('=')[1].replace(",",".").replace("\n","")
    angle_y =  object_info[5].split('=')[1].replace(",",".").replace("\n","")
    angle_z =  object_info[6].split('=')[1].replace(",",".").replace("\n","")
    scale_x =  object_info[7].split('=')[1].replace(",",".").replace("\n","")
    scale_y =  object_info[8].split('=')[1].replace(",",".").replace("\n","")
    scale_z =  object_info[9].split('=')[1].replace(",",".").replace("\n","")
    #взнали інфу про файл
    print("folder with model to open:"+number_of_model)


# з нього берем циферку, в яку папку із палітри заходити, і який фбх імпортірувати
    
    
    if(len(os.listdir(folder_for_files+str(number_of_model)+'/'))>1):
        filename_to_import =folder_for_files+str(number_of_model)+'/'+ os.listdir(folder_for_files+str(number_of_model)+'/')[1]
    else:
        filename_to_import =folder_for_files+str(number_of_model)+'/'+ os.listdir(folder_for_files+str(number_of_model)+'/')[0]
    
    print("file to import is: " + filename_to_import)
    
    
    
   
    
    
    
    #forward_axis ='Z'
    #up_axis = 'Z'
    
    
    bpy.ops.import_scene.fbx(filepath=filename_to_import,bake_space_transform=True ) 
    
    selected_object = bpy.context.selected_objects[0]
    selected_object.location.x=float(pos_x)
    selected_object.location.y=float(pos_z)
    selected_object.location.z=float(pos_y)
    
    
    
    selected_object.scale.x=float(scale_x)#/50
    selected_object.scale.y=float(scale_z)#/50
    selected_object.scale.z=float(scale_y)#/50
    
    
   
    #selected_object.rotation_euler= Euler((0,0,math.radians(180)), 'XYZ') 
    
    
    # Меняем исходный угол наклона
    euler = Euler(map(radians, (0, 0, 180)), 'XYZ')
    ob = selected_object
    loc, rot, scale = ob.matrix_world.decompose()
    smat = Matrix()
    for i in range(3):
        smat[i][i] = scale[i]
    mat = Matrix.Translation(loc) * euler.to_matrix().to_4x4() * smat
    ob.matrix_world = mat
    #/////////////////////////////
    
    print("prev angles",  selected_object.rotation_euler)
        
    
    #Обнуляем все значение, и пошагово добавляем
    
    deg_x = radians(float(angle_x))
    deg_y = radians(float(angle_z))
    deg_z = radians(float(angle_y))
    
    
    
    selected_object.rotation_euler= Euler((deg_x,deg_y,deg_z), 'XYZ')
   
   
   
   
    

    
    
    print("done")
    
    

#dwonload_pallet()
for i in range(0,6):
    open_my_file(i)

