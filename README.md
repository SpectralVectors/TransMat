# TransMat v0.6.0
Transport, Translate, Transform, Transfer Blender Materials to Unreal

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

### __Blender Node    =>__    Unreal Material Expression Node

- __Principled BSDF  =>__   MakeMaterialAttributes

- __Image Texture  =>__   TextureSample

- __Texture Coordinate   =>__  TextureCoordinate

- __UV Map   =>__  TextureCoordinate

- __Mapping   =>__  FunctionCall - BL_Mapping - (see limitations)

- __Mix Shader   =>__   BlendMaterialAttributes

- __Add Shader  =>__   Add

- __Color Ramp  =>__  FunctionCall - BL_ColorRamp - supports up to 9 colors (a little buggy right now)

- __Invert  =>__   OneMinus

- __Fresnel   =>__  Fresnel

- __Value   =>__  Constant

- __RGB   =>__  Constant3Vector

- __Reroute   =>__   Reroute

- __Separate RGB   =>__   FunctionCall - BreakOutFloat3Components

- __Separate XYZ   =>__   FunctionCall - BreakOutFloat3Components

- __Separate HSV   =>__   FunctionCall - BreakOutFloat3Components

- __Combine RGB   =>__   FunctionCall - MakeFloat3

- __Combine XYZ   =>__   FunctionCall - MakeFloat3

- __Combine HSV   =>__   FunctionCall - MakeFloat3

#### Math Node Operations:

- __Add   =>__  Add

- __Subtract  =>__   Subtract

- __Multiply  =>__   Multiply

- __Divide  =>__   Divide

- __Sine  =>__  Sine

- __Arcsine   =>__   Arcsine

- __Cosine  =>__   Cosine

- __Arccosine   =>__  Arccosine 

- __Power   =>__   Power

- __Minimum   =>__   Min

- __Maximum   =>__   Max

- __Round   =>__  Round

- __Absolute  =>__  Abs

#### Vector Math Node Operations:

- __Normalize    =>__   Normalize

- __Dot Product    =>__   DotProduct

- __Cross Product  =>__  CrossProduct

#### MixRGB Node Blend Types:

- __Mix   =>__  LinearInterpolate (our friend Lerp!)

- __Color Burn  =>__  FunctionCall - Blend_ColorBurn

- __Color Dodge   =>__  FunctionCall - Blend_ColorDodge

- __Darken  =>__   FunctionCall - Blend_Darken

- __Difference  =>__   FunctionCall - Blend_Difference

- __Lighten   =>__  FunctionCall - Blend_Lighten

- __Linear Light  =>__  FunctionCall - Blend_LinearLight

- __Overlay   =>__  FunctionCall - Blend_Overlay

- __Screen  =>__   FunctionCall - Blend_Screen

- __Soft Light  =>__   FunctionCall - Blend_SoftLight

#### Procedural Texture Nodes - via the Bake Noise Nodes button:

- __Brick Texture   =>__  TextureSample

- __Checker Texture   =>__  TextureSample

- __Environment Texture   =>__   TextureSample

- __Gradient Texture  =>__   TextureSample

- __IES Texture   =>__  TextureSample

- __Musgrave Texture  =>__  TextureSample

- __Magic Texture   =>__   TextureSample

- __Noise Texture  =>__  TextureSample

- __Point Density Texture  =>__  TextureSample

- __Sky Texture   =>__   TextureSample

- __Voronoi Texture   =>__  TextureSample

- __Wave Texture  =>__   TextureSample

- __White Noise Texture  =>__  TextureSample

## Currently unsupported Blender Nodes

Anything NOT in the above list can be considered unsupported, however, there are some common Blender nodes that do not currently have support that are likely to be in many materials, those are explicitly stated below.

- Normal

- Bump

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

Blender's Mapping node uses a 3D system, but as Unreal's TexCoord node is 2D, it had to be modified. How big a difference that will make remains to be seen.

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
~~~
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
