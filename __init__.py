bl_info = {
    "name": "Render Resolution From Camera Name 每个相机自带渲染分辨率",
    "author": "SidewaysUp Joe; Yang",
    "version": (1, 10, 2),
    "blender": (3, 3, 5),
    "location": "Output Properties Panel ",
    "description": "Set render resolution based camera name. Example: CameraOne-1920x1080\n渲染分辨率基于相机名称CameraOne-1920x1080",
    "warning": "",
    "doc_url": "https://github.com/SidewaysUpJoe/blender-Change-Render-Resolution-Based-On-Camera-Name/wiki",
    "category": "Render",
    "support": "COMMUNITY",
}  

from . import cameraresrender

def register(): 
    cameraresrender.register()    
    print("registered init.  相机名称范例: cam1-512x256")
    

def unregister():
    cameraresrender.unregister()
    print("unregistered init")
    
     
if __name__ == "__main__":
    register()
