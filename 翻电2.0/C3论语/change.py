import os
import re

def rename_folders():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 遍历当前目录中的所有项目
    for item in os.listdir(current_dir):
        # 检查是否为文件夹
        if os.path.isdir(item):
            # 使用正则表达式匹配文件夹名前两个数字
            match = re.match(r'^(\d{2})(.*)', item)
            
            if match:
                # 提取匹配的数字和剩余部分
                numbers = match.group(1)
                rest = match.group(2)
                
                # 构造新的文件夹名
                new_name = f"E{numbers}"
                
                # 重命名文件夹
                old_path = os.path.join(current_dir, item)
                new_path = os.path.join(current_dir, new_name)
                
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {item} -> {new_name}")
                except OSError as e:
                    print(f"Error renaming {item}: {e}")

if __name__ == "__main__":
    rename_folders()
    print("Renaming process completed.")