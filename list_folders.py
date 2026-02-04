import os

def list_folders(directory):
    """列出指定目录下的所有文件夹名称"""
    folders = []
    if os.path.exists(directory) and os.path.isdir(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                folders.append(item)
    return folders

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前目录: {current_dir}")

# 列出文件夹
folders = list_folders(current_dir)
print("\n文件夹列表:")
if folders:
    for folder in folders:
        print(f"- {folder}")
else:
    print("当前目录下没有文件夹")
