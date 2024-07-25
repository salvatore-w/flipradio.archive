import os
import re

def rename_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'E' in os.path.basename(dirpath):
            chapter = os.path.basename(os.path.dirname(dirpath))
            chapter_num = re.search(r'C(\d+)', chapter).group(1)
            episode = os.path.basename(dirpath)
            
            md_files = [f for f in filenames if f.endswith('.md')]
            total_files = len(md_files)
            
            for i, filename in enumerate(md_files, 1):
                old_path = os.path.join(dirpath, filename)
                new_filename = f"2.0_C{chapter_num}_{episode}_{i}of{total_files}.md"
                new_path = os.path.join(dirpath, new_filename)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    root_directory = "."
    rename_files(root_directory)