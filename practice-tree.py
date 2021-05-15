class TreeNode:
    def __init__(self,dir_name, sub_folder_list = [] ):
        self.data = dir_name
        self.sub_folder = sub_folder_list
    def passFolderInList(self, location_of_sub_Node):
        self.sub_folder.append(location_of_sub_Node)

folderMain = TreeNode(dir_name="/", sub_folder_list=[])


root = TreeNode(dir_name="/root", sub_folder_list=[])
var = TreeNode(dir_name="/var", sub_folder_list=[])
etc = TreeNode(dir_name="/etc" ,sub_folder_list=[])


folderMain.passFolderInList(location_of_sub_Node=root)
folderMain.passFolderInList(location_of_sub_Node=var)
folderMain.passFolderInList(location_of_sub_Node=etc)


desktop = TreeNode(dir_name="/root/Desktop", sub_folder_list=[])
download = TreeNode(dir_name="/root/Download", sub_folder_list=[])


root.passFolderInList(location_of_sub_Node=desktop)
root.passFolderInList(location_of_sub_Node=download)


httpd = TreeNode(dir_name="/var/httpd", sub_folder_list=[])
lib = TreeNode(dir_name="/var/lib", sub_folder_list=[])


var.passFolderInList(location_of_sub_Node=httpd)
var.passFolderInList(location_of_sub_Node=lib)


ansible = TreeNode(dir_name="/etc/ansible")
yum = TreeNode(dir_name="/etc/yum.repos.d")


etc.passFolderInList(location_of_sub_Node=ansible)
etc.passFolderInList(location_of_sub_Node=yum)



print("/")
for loca in folderMain.sub_folder:
    print(loca.data)
    for sub_loc in loca.sub_folder:
         print("  ",sub_loc.data)
         