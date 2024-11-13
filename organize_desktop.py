import os
import shutil

# تحديد مسار سطح المكتب ومجلدات التصنيف
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folders_dir = os.path.join(desktop_path, "Folders")
documents_dir = os.path.join(desktop_path, "Documents")

# التأكد من أن مجلدات التصنيف موجودة، وإنشاءها إذا لم تكن موجودة
os.makedirs(folders_dir, exist_ok=True)
os.makedirs(documents_dir, exist_ok=True)

# الامتدادات المختلفة للمستندات
document_extensions = ['.pdf', '.docx', '.txt', '.xlsx', '.pptx']

# قراءة الملفات وتصنيفها
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)

    # إذا كان مجلداً
    if os.path.isdir(item_path) and item not in ["Folders", "Documents"]:
        shutil.move(item_path, folders_dir)
        print(f"Moved folder: {item} to {folders_dir}")

    # إذا كان مستنداً بناءً على الامتداد
    elif os.path.isfile(item_path):
        _, file_extension = os.path.splitext(item)
        
        # إذا كان مستنداً، انقله إلى مجلد المستندات
        if file_extension.lower() in document_extensions:
            shutil.move(item_path, documents_dir)
            print(f"Moved document: {item} to {documents_dir}")
