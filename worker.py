import bpy
from bpy import context

from bpy.app.handlers import persistent

import re

from bpy.app import handlers

from bpy.props import StringProperty, BoolProperty, PointerProperty

from bpy.utils import register_class, unregister_class

from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )


bl_info = {
    "name": "Render Resolution From Camera Name",
    "author": "SidewaysUp Joe",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Output Properties Panel",
    "description": "Set render resolution based camera name. Camera name must end with - hyphen then resolution. Example: CameraOne-1920x1080",
    "warning": "",
    "wiki_url": "https://github.com/SidewaysUpJoe/blender-Change-Render-Resolution-Based-On-Camera-Name/wiki",
    "tracker_url": "https://github.com/SidewaysUpJoe/blender-Change-Render-Resolution-Based-On-Camera-Name/issues",
    'support': 'COMMUNITY',
    "category": "Render",
}  


orgRes_x = 1920
orgRes_y = 1080


frame_handlers = [getattr(handlers, name)
        for name in dir(handlers) if name.startswith("render_")]

#def add_dummy_handlers():
    #for  handler in frame_handlers:
        #handler.append(handler_function(name))   

@persistent
def clear_handlers():
    for  handler in frame_handlers:
        handler.clear()

@persistent
def render_init(scene):
    do_work()

#@persistent
#def render_frame(scene):
    #do_work()

@persistent
def complete(scene):
    changeBackToDefault()

@persistent
def cancel(scene):
    changeBackToDefault()


# worker...
def do_work():
    global orgRes_x, orgRes_y
    changeOn = context.scene.cameraRes_tool.cameraRes_bool
    if changeOn == False :
        return
    
    orgRes_x = bpy.context.scene.render.resolution_x
    orgRes_y = bpy.context.scene.render.resolution_y
    
    print('   TEST - do_work')
    cName = bpy.context.scene.camera.name
    print('   Camera Name: ', cName)
    m = re.search(r'(?<=-)\w+', cName)
    
    if m:
        sizeName = m.group(0)
        print('   Camera Resolution: ', sizeName)
        
        r = sizeName.split('x')
        print('      ** ARRY Len **', len(r))
        if len(r) == 2:
            print('   Camera x: ', r[0])
            print('   Camera y: ', r[1])
            bpy.context.scene.render.resolution_x = int(r[0])
            bpy.context.scene.render.resolution_y = int(r[1])
        else:
                print('      ** Camera Name Resolution missing x (lower case) **')
    else:
        print('      ** Camera Name Missing - hyphen **')



def changeBackToDefault():
    global orgRes_x, orgRes_y
    
    changeBack = context.scene.cameraRes_tool.cameraResDefault_bool
    if changeBack == False :
        return
    
    bpy.context.scene.render.resolution_x = int(orgRes_x)
    bpy.context.scene.render.resolution_y = int(orgRes_y)


class cameraResSettings(PropertyGroup):
    
    cameraRes_bool: BoolProperty(
        name="Change Resolution Based On Camera",
        default = False,
        )
        
    cameraResDefault_bool: BoolProperty(
        name="Change Back To Default Res",
        default = True,
        )


class cameraRes_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_camera_res_render"
    bl_label = "Camera Res Render"
    bl_context = "output"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    
    @classmethod 
    def poll(self,context):
        return True
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        cameraRestPanel = scene.cameraRes_tool
        
        layout.prop(cameraRestPanel, "cameraRes_bool", text="Change Res Based On Camera")
        layout.prop(cameraRestPanel, "cameraResDefault_bool", text="Change Back To Default Res")




clear_handlers()


@persistent
def load_handler(dummy):
    print("Load Handler:", bpy.data.filepath)

classes = (
    cameraResSettings,
    cameraRes_Panel,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.cameraRes_tool = PointerProperty(type=cameraResSettings)
    bpy.app.handlers.load_post.append(load_handler)
    bpy.app.handlers.render_init.append(render_init)
    bpy.app.handlers.render_complete.append(complete)
    bpy.app.handlers.render_cancel.append(cancel)
    #bpy.app.handlers.render_write.append(render_frame)
    print("registered")
    

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
    del bpy.types.Scene.cameraRes_tool
    
     
if __name__ == "__main__":
    register()
