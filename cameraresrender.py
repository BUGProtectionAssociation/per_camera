import bpy
from bpy import context

from bpy.app.handlers import persistent
from bpy.app import handlers

import re

from bpy.props import BoolProperty, PointerProperty, IntProperty
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )
from bpy.utils import register_class, unregister_class

class addButtonChangeResInPanel(bpy.types.Operator):
    bl_idname = 'my.change_camera_res_in_panel'
    bl_label = 'Camera Resolution Render Changer'
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        do_work(bpy.types.Scene)
        return {"FINISHED"}
        
#class cameraResSettings(PropertyGroup):
class cameraResSettings(PropertyGroup):    
    bl_idname = __package__
    
    cameraRes_bool: BoolProperty(
        name="Change Resolution Based On Camera",
        description="Auto change renders resolution based on camera name during render (F12)",
        default = False,
        )
        
    cameraResDefault_bool: BoolProperty(
        name="Change Back To Default Res",
        description="If auto change enabled, change back to the default resolution after render is finished",
        default = True,
        )
    
    orgRes_x : IntProperty(
        name="orgRes_x",
        default=1920
    )

    orgRes_y : IntProperty(
        name="orgRes_y",
        default=1080
    )


class cameraRes_Panel(Panel):
    bl_idname = "OBJECT_PT_camera_res_render_panel"
    bl_label = "Camera Resolution Render"
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
        
        layout.prop(cameraRestPanel, "cameraRes_bool")
        layout.prop(cameraRestPanel, "cameraResDefault_bool")
        layout.operator("my.change_camera_res_in_panel", icon='CAMERA_DATA', text="Change Resolution In Panel")
        
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
    check_for_work(scene)

#@persistent
#def render_frame(scene):
    #check_for_work()

@persistent
def complete(scene):
    changeBackToDefault(scene)

@persistent
def cancel(scene):
    changeBackToDefault(scene)


#check if box is ticked during render
def check_for_work(scene):
    cameraRestPanel = scene.cameraRes_tool
    changeOn = cameraRestPanel.cameraRes_bool
    if changeOn is False :
        return
        
    do_work(scene)


# worker...
def do_work(scene):
    cameraRestPanel = scene.cameraRes_tool
    
    cameraRestPanel.orgRes_x = bpy.context.scene.render.resolution_x
    cameraRestPanel.orgRes_y = bpy.context.scene.render.resolution_y
    
    print('   TEST - do_work')
    cName = bpy.context.scene.camera.name
    print('   Camera Name: ', cName)
    m = re.search(r'(?<=-)\w+', cName)
    
    if m:
        sizeName = m.group(0)
        print('   Camera Resolution: ', sizeName)
        
        r = sizeName.split('x')
        print('      ** ARRAY Len **', len(r))
        if len(r) == 2:
            print('   Camera x: ', r[0])
            print('   Camera y: ', r[1])
            bpy.context.scene.render.resolution_x = int(r[0])
            bpy.context.scene.render.resolution_y = int(r[1])
        else:
                print('      ** Camera Name Resolution missing x (lower case) **')
    else:
        print('      ** Camera Name Missing - hyphen **')



def changeBackToDefault(scene):
    cameraRestPanel = scene.cameraRes_tool
    changeBack = cameraRestPanel.cameraResDefault_bool
    if changeBack is False :
        return
    
    # 全局的参数 报错 不让用，那就用储存在bl里的试试
    bpy.context.scene.render.resolution_x = cameraRestPanel.orgRes_x
    bpy.context.scene.render.resolution_y = cameraRestPanel.orgRes_y


clear_handlers()


@persistent
def load_handler(dummy):
    print("Load Handler:", bpy.data.filepath)




# store keymaps here to access after registration
addon_keymaps = []
        
def register():
    
    register_class(addButtonChangeResInPanel)   
    register_class(cameraResSettings)
    register_class(cameraRes_Panel)
    bpy.types.Scene.cameraRes_tool = bpy.props.PointerProperty(type=cameraResSettings)
    
    #https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
    # handle the keymap
    wm = bpy.context.window_manager
    # Note that in background mode (no GUI available), keyconfigs are not available either,
    # so we have to check this to avoid nasty errors in background case.
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(addButtonChangeResInPanel.bl_idname, 'NUMPAD_0', 'PRESS', ctrl=True, shift=False)
        addon_keymaps.append((km, kmi))
    
    
    bpy.app.handlers.load_post.append(load_handler)
    bpy.app.handlers.render_init.append(render_init)
    bpy.app.handlers.render_complete.append(complete)
    bpy.app.handlers.render_cancel.append(cancel)
    #bpy.app.handlers.render_write.append(render_frame)
    print("registered worker")
    

def unregister():
    unregister_class(cameraResSettings)
    unregister_class(cameraRes_Panel)
    del bpy.types.Scene.cameraRes_tool
    
    #https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    print("unregistered worker")