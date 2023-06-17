#基于摄影机名称更改渲染分辨率

以下加载项仅适用于静态图像，而不适用于动画。


### 在blender 3.5 3D搅拌机3.5 上测试


此附加组件是基于Zoot（Gavin Scott）创建的(https://blenderartists.org/t/does-anyone-know-of-an-addon-that-can-set-a-unique-resolution-for-each-camera/1252294/4?u=sidewaysupjoe)建议。

原发布链接：https://github.com/SidewaysUpJoe/blender-Change-Render-Resolution-Based-On-Camera-Name 

2023年6月17日BlenderCN社区yang（gitee用户名1D阳）进行升级，
消除Writing to ID classes in this context is not allowed: Scene, Scene datablock, error setting ......错误。


 **如果命名相机，后跟-（连字符）和分辨率，则它将渲染为该分辨率。** 

示例：CameraOne-1920x1080

渲染分辨率将为1920x1080


相机一-3840x2160

渲染分辨率将为3840x2160


加载项面板位于“输出属性”面板中。

有三种选择：

1） 启用/禁用 以在渲染过程中自动更改分辨率（F12）

2） 渲染完成后恢复原始集分辨率

3） “应用激活相机的分辨率”按钮。此按钮快捷键可在软件设置中修改（默认Ctrl+Shift+NUM_0，在“快捷键映射表中”中搜索“Camera Resolution Render Changer”），该功能可将相机参数更改至“输出面板”中的分辨率。


注意：您可以使用时间线和设置标记来更改相机。但注意，此插件仅适用于静态图像，不适用于动画。设置的始终处于活动状态的摄影机将影响渲染的分辨率。


如果你遇到问题，启用“系统控制台”（顶部菜单->窗口->切换系统控制台），你会看到一些可能有帮助的调试信息。


-----------------------------------------------------------------------------------------------

如果帮到您了，如果您有条件，请帮我买个煎饼，谢谢！

![用支付宝 帮买个煎饼](ZFB.jpg)

![用微信 帮买个煎饼](WX.jpg)