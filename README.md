# TransMat v0.6.4
Transport, Translate, Transform, Transfer Blender Materials to Unreal

[![Preview](https://img.youtube.com/vi/jVddavPSJv4/0.jpg)](https://www.youtube.com/watch?v=jVddavPSJv4)

## Description

TransMat is an Add-on for Blender's Node Editor.

It creates a python file that will instantly, automatically recreate your Blender material in Unreal.

Check out the example at the bottom of the page to see what it looks like!

## How to Install and Use

Download and unzip the file, then, in __Blender__, click __'Edit'__ > __'Preferences'__ > __'Addons'__ > __'Install'__ and choose __'Transmat.py'__

This will add a properties panel to the __Node Editor__.

Once you have created your material, choose a directory to output the python file to.

Then, if you wish, you can specify Unreal import subfolders for the material and textures to be placed in.

If you do not specify any folders, they will go to your game's __Content__ folder by default.

If you do add a subfolder, the script will either find it, if it exists, or create it, if it doesn't.

Next, if you're using procedural noise nodes, you can choose your resolution, and bake them to textures.

_(eg Brick, Checker, Gradient, Magic, Musgrave, Noise, Point Density, Sky, Voronoi, Wave, White Noise)_

Be patient if you have a lot of noise nodes and you're baking at a high resolution, it will take time!

Transmat then checks the output connections of the noise nodes, and replaces them with your newly baked textures!

Now, click the __'Transfer Material!'__ button. This creates your material file - _eg 'GroupTest1_TM.py'_

Then, in __Unreal__ _(with the Python plug-in and Editor Scripting enabled)_ click __'File'__ > __'Execute Python Script'__.

__NOTE:__ If this is your first time using the addon, navigate to the TransMat folder, select _'TransMat_SetupScript.py'_ and click __'OK'__.

This will setup the custom Mapping and ColorRamp nodes in Unreal. If you've already done this, then:

Navigate to the python file that was just created, and click __'OK'__ - _eg 'GroupTest1_TM.py'_

Transmat will find and import all the image textures from your Blender material, and plug them into the right nodes!

## Currently supported Blender Nodes

Blender Shader Node  |  Unreal Material Expression Node
---|---
Principled BSDF |   MakeMaterialAttributes
Image Texture |   TextureSample
Texture Coordinate |  TextureCoordinate
UV Map |  TextureCoordinate
Mix Shader |   BlendMaterialAttributes
Add Shader |   Add
Color Ramp | FunctionCall - BL_ColorRamp - see limitations
Invert  | OneMinus
Fresnel | Fresnel
Value | Constant
 RGB | Constant3Vector
 Reroute |  Reroute
Separate RGB |  FunctionCall - BreakOutFloat3Components
Separate XYZ  | FunctionCall - BreakOutFloat3Components
Separate HSV |  FunctionCall - BreakOutFloat3Components
Combine RGB  | FunctionCall - MakeFloat3
Combine XYZ  | FunctionCall - MakeFloat3
Combine HSV |  FunctionCall - MakeFloat3

Math Node Operation | Unreal Material Expression Node
---|---
Add | Add
Subtract |  Subtract
Multiply |   Multiply
Divide  |   Divide
Sine  |  Sine
Arcsine   |   Arcsine
Cosine  |   Cosine
Arccosine   |  Arccosine 
Power   |   Power
Minimum   |   Min
Maximum   |   Max
Round   |  Round
Absolute  |  Abs

Vector Math Node Operations | Unreal Material Expression Node
---|---
Normalize    |   Normalize
Dot Product   |  DotProduct
Cross Product |  CrossProduct

MixRGB Node Blend Types | Unreal Material Expression Node
---|---
Mix   |  LinearInterpolate (our friend Lerp!)
Color Burn  | FunctionCall - Blend_ColorBurn
Color Dodge   |  FunctionCall - Blend_ColorDodge
Darken  |   FunctionCall - Blend_Darken
Difference  |   FunctionCall - Blend_Difference
Lighten   |  FunctionCall - Blend_Lighten
Linear Light  |  FunctionCall - Blend_LinearLight
Overlay   |  FunctionCall - Blend_Overlay
Screen  |   FunctionCall - Blend_Screen
Soft Light  |   FunctionCall - Blend_SoftLight

Procedural Texture Nodes (via Bake Noise Nodes) | Unreal Material Expression Node
---|---
Brick Texture  | TextureSample - your baked texture will auto-import
Checker Texture   |  TextureSample - your baked texture will auto-import
Environment Texture  |   TextureSample - your baked texture will auto-import
Gradient Texture  |   TextureSample - your baked texture will auto-import
IES Texture   |  TextureSample - your baked texture will auto-import
Musgrave Texture  |  TextureSample - your baked texture will auto-import
Magic Texture   |   TextureSample - your baked texture will auto-import
Noise Texture  |  TextureSample - your baked texture will auto-import
Point Density Texture  |  TextureSample - your baked texture will auto-import
Sky Texture   |   TextureSample - your baked texture will auto-import
Voronoi Texture   |  TextureSample - your baked texture will auto-import
Wave Texture  |   TextureSample - your baked texture will auto-import
White Noise Texture  |  TextureSample - your baked texture will auto-import

## Currently unsupported Blender Nodes

Anything NOT in the above list can be considered unsupported, however, there are some common Blender nodes that do not currently have support that are likely to be in many materials, those are explicitly stated below.

- Mapping

- Normal

- Bump - __Partial Support - see Limitations__

- Displacement

- RGB Curves

- Brightness/Contrast

- Group - __Partial Support - see Limitations__

- ShadertoRGB

- Frame

- Script

If a node is in the unsupported list, it doesn't mean it won't be supported, only that I haven't yet found a way to port it over.

I'm planning on first getting all the nodes that have direct equivalents sorted out, then looking at nodes that require custom coded solutions.

## Limitations
Mapping nodes will transfer, HOWEVER, results are not yet consistent with Blender, and manual adjustment will be necessary.

Packed images will give errors, use textures that have a filepath that exists on your PC.

Bump nodes will transfer, HOWEVER, they cannot accept an RGB input, so you must create a Texture Object, manually load your texture into that, plug that into the node, then attach whatever you are using as a texture coordinate, to align the textures.

Node groups work with the __'Transfer Material'__ function, but, for now, in order to bake textures in Groups, the groups must be broken.

If you use a node that is not on the supported list, your material will likely not transfer properly.

Some very common Blender nodes are not yet supported and it will take time to figure out the proper Unreal equivalent for all of Blender's Nodes.

It redirects stdout to create the python file, so if you are printing to the console, it will interfere with the script.

Color Ramps are supported, but above 4 colours they start to produce unexpected results, with colour banding and other issues.

This can sometimes be resolved by ensuring the position of the first colour is 0, and the position of the last colour is 1.

## Acknowledgements and Thanks

__angjminer__'s Project BlUEMan demonstrated a similar functionality a few years ago, this is an attempt to achieve a similar result using an open framework.

__Jim Kroovy__ submitted a crash fix, and a refactoring suggestion.

__Momchilo__ has pitched in with some licensing resources.

__PGMath__ posted an article on blender.stackexchange on how to recreate the Mapping and ColorRamp nodes using simple Math nodes, a huge help!

A massive thanks to __batFINGER__, __CodeManX__, and __sambler__ for their countless contributions over the years to blender.stackexchange!

And thanks, of course, to __Epic Games__, and __Blender Foundation__!

## Example output (GroupTest1_TM.py):
~~~python
import unreal

GroupTest1=unreal.AssetToolsHelpers.get_asset_tools().create_asset('GroupTest1','/Game/', unreal.Material, unreal.MaterialFactoryNew())
GroupTest1.set_editor_property('use_material_attributes',True)

create_expression = unreal.MaterialEditingLibrary.create_material_expression
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property

mat_func_burn = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_ColorBurn')
mat_func_dodge = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_ColorDodge')
mat_func_darken = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Darken')
mat_func_difference = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Difference')
mat_func_lighten = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Lighten')
mat_func_linear_light = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_LinearLight')
mat_func_overlay = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Overlay')
mat_func_screen = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Screen')
mat_func_soft_light = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_SoftLight')
mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')
mat_func_combine = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat3')

import_tasks = []

### Importing Textures
BrickTexture_001 = 'D:\Blender\Scripts\TransmatOutputs\BrickTexture001.png'

BrickTexture_001_import = unreal.AssetImportTask()
BrickTexture_001_import.set_editor_property('automated',True)
BrickTexture_001_import.set_editor_property('destination_path','/Game/')
BrickTexture_001_import.set_editor_property('destination_name','BrickTexture_001')
BrickTexture_001_import.set_editor_property('factory',unreal.TextureFactory())
BrickTexture_001_import.set_editor_property('filename',BrickTexture_001)
BrickTexture_001_import.set_editor_property('replace_existing',True)
BrickTexture_001_import.set_editor_property('save',True)
import_tasks.append(BrickTexture_001_import)

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(import_tasks)

### Creating Nodes
MixShader = create_expression(GroupTest1,unreal.MaterialExpressionBlendMaterialAttributes,-280.0, -40.0)
PrincipledBSDF = create_expression(GroupTest1,unreal.MaterialExpressionMakeMaterialAttributes,-820.0, -80.0)
Mix = create_expression(GroupTest1,unreal.MaterialExpressionMaterialFunctionCall,-1240.0, 260.0)
AddShader = create_expression(GroupTest1,unreal.MaterialExpressionAdd,-520.0, -180.0)
SeparateRGB = create_expression(GroupTest1,unreal.MaterialExpressionMaterialFunctionCall,-1560.0, -120.0)
RGB = create_expression(GroupTest1,unreal.MaterialExpressionConstant3Vector,-1120.0, -200.0)
Value = create_expression(GroupTest1,unreal.MaterialExpressionConstant,-1820.0, 80.0)
VectorMath = create_expression(GroupTest1,unreal.MaterialExpressionAdd,-1300.0, -580.0)
CombineHSV = create_expression(GroupTest1,unreal.MaterialExpressionMaterialFunctionCall,-1500.0, -560.0)
Value1 = create_expression(GroupTest1,unreal.MaterialExpressionConstant,-1820.0, 220.0)
Math = create_expression(GroupTest1,unreal.MaterialExpressionAdd,-1340.0, 0.0)
RGB1 = create_expression(GroupTest1,unreal.MaterialExpressionConstant3Vector,-1860.0, 540.0)
RGB2 = create_expression(GroupTest1,unreal.MaterialExpressionConstant3Vector,-1860.0, 320.0)
CombineRGB = create_expression(GroupTest1,unreal.MaterialExpressionMaterialFunctionCall,-1320.0, -140.0)
ImageTexture = create_expression(GroupTest1,unreal.MaterialExpressionTextureSample,-1160.0, 450.0)
UVMap = create_expression(GroupTest1,unreal.MaterialExpressionTextureCoordinate,-1360.0, 590.0)

### Loading Material Functions and Textures
Mix.set_editor_property('material_function',mat_func_soft_light)
SeparateRGB.set_editor_property('material_function',mat_func_separate)
CombineHSV.set_editor_property('material_function',mat_func_combine)
CombineRGB.set_editor_property('material_function',mat_func_combine)
ImageTexture.texture = unreal.load_asset('/Game/BrickTexture_001')

### Setting Values
RGB.constant = (0.5382355451583862, 0.004127298481762409, 0.0426042303442955)
Value.r = 0.652999997138977
Value1.r = 0.25600001215934753
RGB1.constant = (0.14932090044021606, 0.23372754454612732, 0.49999991059303284)
RGB2.constant = (0.13467830419540405, 0.49999991059303284, 0.2011043280363083)

### Creating Connections
PrincipledBSDF_connection = create_connection(PrincipledBSDF, '', AddShader, 'A')
PrincipledBSDF_connection = create_connection(PrincipledBSDF, '', MixShader, 'B')
Mix_connection = create_connection(Mix, '', PrincipledBSDF, 'Roughness')
AddShader_connection = create_connection(AddShader, '', MixShader, 'A')
SeparateRGB_connection = create_connection(SeparateRGB, 'R', CombineRGB, 'X')
SeparateRGB_connection = create_connection(SeparateRGB, 'G', PrincipledBSDF, 'Specular')
SeparateRGB_connection = create_connection(SeparateRGB, 'G', CombineRGB, 'Y')
SeparateRGB_connection = create_connection(SeparateRGB, 'B', PrincipledBSDF, 'Anisotropy')
SeparateRGB_connection = create_connection(SeparateRGB, 'B', CombineRGB, 'Z')
RGB_connection = create_connection(RGB, '', PrincipledBSDF, 'BaseColor')
Value_connection = create_connection(Value, '', PrincipledBSDF, 'AnisotropicRotation')
Value_connection = create_connection(Value, '', Math, 'A')
Value1_connection = create_connection(Value1, '', PrincipledBSDF, 'SpecularTint')
Value1_connection = create_connection(Value1, '', Math, 'B')
Math_connection = create_connection(Math, '', PrincipledBSDF, 'Metallic')
RGB1_connection = create_connection(RGB1, '', PrincipledBSDF, 'SubsurfaceColor')
RGB1_connection = create_connection(RGB1, '', Mix, 'Blend')
RGB1_connection = create_connection(RGB1, '', SeparateRGB, 'Float3')
RGB2_connection = create_connection(RGB2, '', Mix, 'Base')
CombineRGB_connection = create_connection(CombineRGB, 'Result', PrincipledBSDF, 'Opacity')
ImageTexture_connection = create_connection(ImageTexture, 'RGB', PrincipledBSDF, 'EmissiveColor')
UVMap_connection = create_connection(UVMap, '', ImageTexture, 'UVs')
~~~
