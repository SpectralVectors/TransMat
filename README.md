# TransMat
Transport, Translate, Transform, Transfer Blender Materials to Unreal

# Desctription

TransMat is an Add-on for Blender's Node Editor.

Once you have created your material, click the 'Transmat!' button.

This will create a python file with a list of instructions to recreate the material in Unreal.

Then, in Unreal (with the Python plug-in and Editor Scripting enabled) click File > Execute Python Script.

Navigate to the python file that was just created, and click OK - eg "_yourmaterial_TM.py"

Transmat will find and import all the image textures from your Blender material, and plug them into the right nodes!

# Currently supported Blender Nodes

Principled BSDF

Mix Shader

Add Shader

Invert

Image Texture

Texture Coordinate

Value

RGB

Math - Add, Subtract, Multiply, Divide, Sine, Arcsine, Cosine, Arccosine, Power, Minimum, Maximum, Round, Absolute

MixRGB - Mix mode only for the moment

Reroute

