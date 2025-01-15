import os

folder_path = "E:/WK/project/WK/DCSAU-Net-main/data_bantu/masks"
file_list = os.listdir(folder_path)

# n = 1

for file_name in file_list:
    # 旧文件路径
    old_path = os.path.join(folder_path, file_name)
    # 新文件名
    new_file_name = file_name[:20] + '.jpg'
    # n = n + 1
    # 新文件路径
    new_path = os.path.join(folder_path, new_file_name)
    # 修改文件名
    os.rename(old_path, new_path)
