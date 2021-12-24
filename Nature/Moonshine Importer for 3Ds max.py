import requests, zipfile
from pymxs import runtime as mxs
from io import BytesIO
import os

models_in_pallet = 7
pallet_url ='https://github.com/NSmocker/MoonshinePallets/raw/main/Nature/'
folder_for_files ='D:/git_pallets/'

'''

print("start downloading pallet")
for i in range(1,models_in_pallet):
    url = pallet_url + str(i)+".zip"
    filename = url.split('/')[-1]
    req = requests.get(url)
    unzipper= zipfile.ZipFile(BytesIO(req.content))
    unzipper.extractall(folder_for_files+str(i)+'/')
  
print("Pallet Downloaded on folder"+ folder_for_files)
'''


def FBX_import(path, skin, animation):
    
    mxs.FBXExporterSetParam("Mode", mxs.readvalue(mxs.StringStream('#create')))
    mxs.FBXExporterSetParam("Skin", True)
    mxs.FBXExporterSetParam("Animation", False)
    mxs.importFile(path, mxs.readvalue(mxs.StringStream('#noPrompt')))
    



def open_my_file(number):
   
    f = open("D:/SavesFromMoonshine/"+str(number)+".txt", "r")
    print("opening..."+"D:/SavesFromMoonshine/"+str(number)+".txt" )
    
    if(len(os.listdir(folder_for_files+str(number)+'/'))>1):
        filename_to_import =folder_for_files+str(number)+'/'+ os.listdir(folder_for_files+str(number)+'/')[1]
    else:
        filename_to_import =folder_for_files+str(number)+'/'+ os.listdir(folder_for_files+str(number)+'/')[0]
    
    print("file to import is: " + filename_to_import)
    
    
    
    FBX_import(filename_to_import, True, False)
    
    object_info = f.readlines()
    origin = object_info[0].split('=')[1].replace(",",".").replace("\n","")
    pos_x =  object_info[1].split('=')[1].replace(",",".").replace("\n","")
    pos_y =  object_info[2].split('=')[1].replace(",",".").replace("\n","")
    pos_z =  object_info[3].split('=')[1].replace(",",".").replace("\n","")
    angle_x =  object_info[4].split('=')[1].replace(",",".").replace("\n","")
    angle_y =  object_info[5].split('=')[1].replace(",",".").replace("\n","")
    angle_z =  object_info[6].split('=')[1].replace(",",".").replace("\n","")
    sacle_x =  object_info[7].split('=')[1].replace(",",".").replace("\n","")
    scale_y =  object_info[8].split('=')[1].replace(",",".").replace("\n","")
    scale_z =  object_info[9].split('=')[1].replace(",",".").replace("\n","")
    
    selected_object = mxs.Selection[0]
    
    selected_object.pos = mxs.Point3(float(pos_x),float(pos_y),float(pos_z)) 
    print("done")
    
    



open_my_file(1)


'''

path = "D:/IchiRiged.fbx"





'''
