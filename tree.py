class TreeNodes:
    def __init__(self, data, sub_directory = []):
        self.data = data
        self.pass_sub_dir = sub_directory
    def assign_sub_Dir(self, mem_loc_obj):
        self.pass_sub_dir.append(mem_loc_obj)
    

top_dir = TreeNodes("/",[])

root_dir = TreeNodes("/root",[])
etc_dir = TreeNodes("/etc",[])
var_dir = TreeNodes("/var",[])

top_dir.assign_sub_Dir(root_dir)
top_dir.assign_sub_Dir(etc_dir)
top_dir.assign_sub_Dir(var_dir)

#print(top_dir.__dict__)

root_sub_dir_download = TreeNodes("/root/Download")
root_sub_dir_desktop = TreeNodes("/root/Desktop")

root_dir.assign_sub_Dir(root_sub_dir_desktop)
root_dir.assign_sub_Dir(root_sub_dir_download)

#print(root_dir.__dict__)

etc_sub_dir_ansible = TreeNodes("/etc/ansible")
etc_sub_dir_httpd = TreeNodes("/etc/httpd")

etc_dir.assign_sub_Dir(etc_sub_dir_ansible)
etc_dir.assign_sub_Dir(etc_sub_dir_httpd)

#print(etc_dir.__dict__)


var_sub_dir_lib = TreeNodes("/var/lib")
var_dir.assign_sub_Dir(var_sub_dir_lib)

#print(var_dir.__dict__)


print("/")
for sub_folder in top_dir.pass_sub_dir:
    print(" ",sub_folder.data)
    for sub_sub_folder in sub_folder.pass_sub_dir:
        print("   ",sub_sub_folder.data)
