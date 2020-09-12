# Change Your Render Resolution Based On Camera Name
The following add-on only works with still images, not animations.

Tested on Blender 2.8

This add-on was created based on Zoot (Gavin Scott) (https://blenderartists.org/t/does-anyone-know-of-an-addon-that-can-set-a-unique-resolution-for-each-camera/1252294/4?u=sidewaysupjoe) suggestion.

If you name your camera followed by a - (hyphen) and resolution it will render to that Resolution.  
Example: CameraOne-1920x1080  
the render resolution will be 1920x1080

CameraOne-3840x2160  
the render resolution will be 3840x2160

The add-ons panel is in the Output Properties Panel.  
There are three options:
1) Turn it On/Off to auto change resolution during rendering (F12)
2) To restore the original set resolution once render is done  
3) "Change Resolution In Panel" button. This button can be configured for Keymapping (default Ctrl-NUM_0, search for "Camera Resolution Render Changer" in Blenders Keymap settings) and will only change the resolution in the 'output panel'.

Note: you can use the timeline and set markers for changing cameras, BUT AGAIN, this add-on only works for still images and not animations. What ever active camera is set will effect the rendered resolution.

If you run into an issue, enabled the "System Console" (top menu -> Window -> Toggle System Console) and you will see alittle debug info which might help.
