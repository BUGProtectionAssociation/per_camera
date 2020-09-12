

from . import cameraresrender


bl_info = {
    "name": "Render Resolution From Camera Name",
    "author": "SidewaysUp Joe",
    "version": (1, 1, 0),
    "blender": (2, 80, 0),
    "location": "Output Properties Panel",
    "description": "Set render resolution based camera name. Example: CameraOne-1920x1080",
    "warning": "",
    "wiki_url": "https://github.com/SidewaysUpJoe/blender-Change-Render-Resolution-Based-On-Camera-Name/wiki",
    "tracker_url": "https://github.com/SidewaysUpJoe/blender-Change-Render-Resolution-Based-On-Camera-Name/issues",
    'support': 'COMMUNITY',
    "category": "Render",
}  

def register(): 
    cameraresrender.register()    
    print("registered init")
    

def unregister():
    cameraresrender.unregister()
    print("unregistered init")
    
     
if __name__ == "__main__":
    register()
