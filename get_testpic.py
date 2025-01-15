import pandas as pd
import shutil
import os

# CSV文件路径
csv_file_path = 'src/test_train_data_isic2018.csv'
# 图片原始路径（CSV文件中图片路径的根目录）
image_dir = './src/'
# 目标路径（将复制测试集图片到这个目录）
target_dir = 'your_target_directory/'

# 确保目标目录存在
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 读取CSV文件
df = pd.read_csv(csv_file_path)

# 遍历每一行数据
for index, row in df.iterrows():
    # 假设CSV中有一列名为'image_path'，包含图片相对于image_dir的相对路径
    # 假设还有一列名为'is_test'，表示图片是否为测试集的一部分（True/False）
    image_path = os.path.join(image_dir, row['image_path'])
    is_test = row['is_test']

    # 检查图片是否为测试集图片
    if is_test:
        # 构建目标图片路径
        target_image_path = os.path.join(target_dir, row['image_path'])

        # 复制图片到目标路径
        shutil.copy2(image_path, target_image_path)
        print(f"Copied {image_path} to {target_image_path}")