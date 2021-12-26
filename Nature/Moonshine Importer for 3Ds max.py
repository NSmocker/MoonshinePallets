import requests, zipfile
from pymxs import runtime as mxs
from io import BytesIO
import os

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



def FBX_import(path, skin, animation):
    
    mxs.FBXExporterSetParam("Mode", mxs.readvalue(mxs.StringStream('#create')))
    mxs.FBXExporterSetParam("Skin", True)
    mxs.FBXExporterSetParam("Animation", False)
    mxs.importFile(path, mxs.readvalue(mxs.StringStream('#noPrompt')))
    



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
    sacle_x =  object_info[7].split('=')[1].replace(",",".").replace("\n","")
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
    
    
    
   
    
    
    
    
    FBX_import(filename_to_import, True, False)
    selected_object = mxs.Selection[0]
    
    selected_object.asd = mxs.Point3(float(pos_x)*10,float(pos_z)*10,float(pos_y)*10) 
    selected_object.rotation = mxs.EulerAngles(float(angle_x),float(angle_z),float(angle_y)) 
    
 
    selected_object.scale = mxs.Point3(float(sacle_x)+10,float(scale_z)+10,float(scale_y)+10)
    selected_object.name = filename_to_import+str(number)
    
    
    
    print("done")
    
    

#dwonload_pallet()
for i in range(0,5):
    open_my_file(i)

