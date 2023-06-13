# import os
# import shutil
# import time

# current_dir=os.getcwd()
# img_dir=os.path.join(current_dir,'code_images')
# os.makedirs(img_dir,exist_ok=True)
# py_dir=os.path.join(current_dir,'python_files')
# os.makedirs(py_dir,exist_ok=True)
# file_dir=os.path.join(current_dir,'doc_files')
# os.makedirs(file_dir,exist_ok=True)



# # #  add_the image,python,text_files,and video_files all in one List
# # file_ext=['.py','.txt','.jpg','.png','.jpeg','.webp','.pdf','.gitignore']
# img_ext=['.jpg','.png','.jpeg','.webp']
# file_ext=['.pdf','.txt','.gitignore','.csv']

# for i,file in enumerate(os.listdir()):
#       if file.endswith('.py'):
#          copy_file=os.path.join(current_dir,file)
#          dest_file=os.path.join(py_dir,file)
#          shutil.move(copy_file,dest_file)
#          print(f'Moved {i} python file...')
#       for img in img_ext:
#            if file.endswith(img):
#              img_file=os.path.join(current_dir,file)
#              dest_file=os.path.join(img_dir,file)
#              shutil.move(img_file,dest_file)
#              print(f'Moved {i} image file.....')
#       for txt in file_ext:
#            if file.endswith(txt):
#              doc_file=os.path.join(current_dir,file)
#              dest_file=os.path.join(file_dir,file)
#              shutil.move(doc_file,dest_file)
#              print(f'Moved {i} Document file.....')
            
import os
print(os.listdir('/home/deji/Desktop/deji/PycharmProjects/pythonProject/python_files'))