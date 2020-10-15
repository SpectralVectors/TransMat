# TransMat
Transport, Translate, Transform, Transfer Blender Materials to Unreal

# Description

TransMat is an Add-on for Blender's Node Editor.

It will create a python file with a list of instructions to instantly, automatically recreate your Blender material in Unreal.

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

# Example output (new_material_TM.py):

import unreal

new_material=unreal.AssetToolsHelpers.get_asset_tools().create_asset('new_material','/Game/Materials/', unreal.Material, unreal.MaterialFactoryNew())
new_material.set_editor_property('use_material_attributes',True)

create_expression = unreal.MaterialEditingLibrary.create_material_expression
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property
tasks = []

### Textures

RenderTest_png = 'D:\Blender\Blends\RenderTest.png'

RenderTest_png_import = unreal.AssetImportTask()
RenderTest_png_import.set_editor_property('automated',True)
RenderTest_png_import.set_editor_property('destination_path','/Game/Textures/')
RenderTest_png_import.set_editor_property('destination_name','RenderTest_png')
RenderTest_png_import.set_editor_property('factory',unreal.TextureFactory())
RenderTest_png_import.set_editor_property('filename',RenderTest_png)
RenderTest_png_import.set_editor_property('replace_existing',True)
RenderTest_png_import.set_editor_property('save',True)
tasks.append(RenderTest_png_import)

UE4Man_Logo_Bakedn_TGA = 'D:\Blender\Blends\UE4Man_Logo_Bakedn.TGA'

UE4Man_Logo_Bakedn_TGA_import = unreal.AssetImportTask()
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('automated',True)
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('destination_path','/Game/Textures/')
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('destination_name','UE4Man_Logo_Bakedn_TGA')
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('factory',unreal.TextureFactory())
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('filename',UE4Man_Logo_Bakedn_TGA)
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('replace_existing',True)
UE4Man_Logo_Bakedn_TGA_import.set_editor_property('save',True)
tasks.append(UE4Man_Logo_Bakedn_TGA_import)

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

### Nodes
PrincipledBSDF = create_expression(new_material,unreal.MaterialExpressionMakeMaterialAttributes,-440.0,-20.0)
AddShader = create_expression(new_material,unreal.MaterialExpressionAdd,-120.0,0.0)
MixShader = create_expression(new_material,unreal.MaterialExpressionBlendMaterialAttributes,80.0,40.0)
ImageTexture = create_expression(new_material,unreal.MaterialExpressionTextureSample,-1160.0,-540.0)
ImageTexture001 = create_expression(new_material,unreal.MaterialExpressionTextureSample,-1260.0,-820.0)
RGB001 = create_expression(new_material,unreal.MaterialExpressionConstant3Vector,-1320.0,-540.0)
Math001 = create_expression(new_material,unreal.MaterialExpressionAdd,-940.0,-300.0)
Invert = create_expression(new_material,unreal.MaterialExpressionOneMinus,-940.0,-180.0)
Math = create_expression(new_material,unreal.MaterialExpressionAdd,-1220.0,-280.0)
Value001 = create_expression(new_material,unreal.MaterialExpressionConstant,-1660.0,-480.0)
Value = create_expression(new_material,unreal.MaterialExpressionConstant,-1660.0,-580.0)
Reroute = create_expression(new_material,unreal.MaterialExpressionReroute,-940.0,-800.0)
Mix001 = create_expression(new_material,unreal.MaterialExpressionLinearInterpolate,-1440.0,-500.0)
Mix002 = create_expression(new_material,unreal.MaterialExpressionMaterialFunctionCall,-880.0,-420.0)
RGB = create_expression(new_material,unreal.MaterialExpressionConstant3Vector,-1880.0,-40.0)
SeparateRGB = create_expression(new_material,unreal.MaterialExpressionMaterialFunctionCall,-960.0,0.0)
Mix = create_expression(new_material,unreal.MaterialExpressionMaterialFunctionCall,-1360.0,100.0)
UVMap = create_expression(new_material,unreal.MaterialExpressionTextureCoordinate,-1900.0,-380.0)
VectorMath = create_expression(new_material,unreal.MaterialExpressionNormalize,-1440.0,-120.0)
TextureCoordinate = create_expression(new_material,unreal.MaterialExpressionTextureCoordinate,-1660.0,-220.0)
Fresnel = create_expression(new_material,unreal.MaterialExpressionFresnel,-1580.0,60.0)

### Material Functions
ImageTexture.texture = unreal.load_asset('/Game/Textures/RenderTest_png')
ImageTexture001.texture = unreal.load_asset('/Game/Textures/UE4Man_Logo_Bakedn_TGA')
mat_func_darken = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Darken')
Mix002.set_editor_property('material_function',mat_func_darken)
mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')
SeparateRGB.set_editor_property('material_function',mat_func_separate)
mat_func_screen = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Screen')
Mix.set_editor_property('material_function',mat_func_screen)

### Connections
PrincipledBSDF_connection = create_connection(PrincipledBSDF,'',AddShader,'A')
AddShader_connection = create_connection(AddShader,'',MixShader,'B')
ImageTexture_connection = create_connection(ImageTexture,'',Mix002,'Base')
ImageTexture001_connection = create_connection(ImageTexture001,'',Reroute,'')
RGB001.constant = (0.014735688455402851,0.05303531885147095,0.15487249195575714)
RGB001_connection = create_connection(RGB001,'',ImageTexture,'UVs')
Math001_connection = create_connection(Math001,'',PrincipledBSDF,'Anisotropy')
Invert_connection = create_connection(Invert,'',PrincipledBSDF,'Specular')
Math_connection = create_connection(Math,'',Invert,'')
Math_connection = create_connection(Math,'',Math001,'A')
Value001.r = 0.4000000059604645
Value001_connection = create_connection(Value001,'',Math,'B')
Value.r = 0.800000011920929
Value_connection = create_connection(Value,'',Mix001,'B')
Reroute_connection = create_connection(Reroute,'',PrincipledBSDF,'Normal')
Mix001_connection = create_connection(Mix001,'',Math001,'B')
Mix002_connection = create_connection(Mix002,'',PrincipledBSDF,'EmissiveColor')
RGB.constant = (0.49999991059303284,0.05486849695444107,0.0)
RGB_connection = create_connection(RGB,'',SeparateRGB,'Float3')
SeparateRGB_connection = create_connection(SeparateRGB,'',PrincipledBSDF,'Roughness')
Mix_connection = create_connection(Mix,'',PrincipledBSDF,'BaseColor')
VectorMath_connection = create_connection(VectorMath,'',Math,'A')
TextureCoordinate_connection = create_connection(TextureCoordinate,'',VectorMath,'VectorInput')
