# TransMat
Transport, Translate, Transform, Transfer Blender Materials to Unreal

# Description

TransMat is an Add-on for Blender's Node Editor.

It will create a python file with a list of instructions to recreate your Blender material in Unreal.

# How to Use

Download and unzip the file, then, in Blender, click Edit > Preferences > Addons > Install and choose Transmat.py

This will add a properties panel to the Node Editor.

Once you have created your material, choose a directory to output the python file to.

Then, if you wish, you can specify a subfolder for the material and textures to be placed in.

If you do not specify a folder, they will go to your game's Content folder by default.

Now, click the 'Transmat!' button.

Then, in Unreal (with the Python plug-in and Editor Scripting enabled) click File > Execute Python Script.

Navigate to the python file that was just created, and click OK - eg "_yourmaterial_TM.py"

Transmat will find and import all the image textures from your Blender material, and plug them into the right nodes!

# Currently supported Blender Nodes

Principled BSDF

Image Texture

Texture Coordinate

UV Map

Mix Shader

Add Shader

Math - Add, Subtract, Multiply, Divide, Sine, Arcsine, Cosine, Arccosine, Power, Minimum, Maximum, Round, Absolute

Vector Math - Normalize, Dot Product, Cross Product

MixRGB - Mix, Color Burn, Color Dodge, Darken, Difference, Lighten, Linear Light, Overlay, Screen, Soft Light

Invert

Fresnel

Value

RGB

Reroute

# Limitations

If you use a node that is not on the supported list, your material will likely not transfer properly, if it transfers at all.

Some very common Blender nodes are not yet supported (Color Ramp!), and it will take time to figure out the proper Unreal equivalent for all of Blender's Nodes.

It redirects stdout to create the python file, so if you are printing to the console, it will interfere with the script.

Currently, only one output socket per node is supported, so SeparateRGB etc are not yet working properly.

And, it would be wise to use Value or RGB nodes in place of entering values directly on the Principled BSDF, as there is currently an issue whereby:

If a node has a connection, as well as a value entered into another socket, it will only allow one type of value entry.

If it has a connection, it wipes all input values, if it has an input value, it breaks all the connections.

Possibly a fixable issue, possibly a limitation of the interface.
