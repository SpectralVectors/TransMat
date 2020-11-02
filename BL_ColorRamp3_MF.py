import unreal

BL_ColorRamp3=unreal.AssetToolsHelpers.get_asset_tools().create_asset('BL_ColorRamp3','/Engine/Functions/BLUI/', unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())

create_expression = unreal.MaterialEditingLibrary.create_material_expression_in_function
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property
update_function = unreal.MaterialEditingLibrary.update_material_function

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

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(import_tasks)

### Creating Nodes
Color1 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionConstant3Vector,-1580.0, 3880.0)
Position1 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionConstant,-1580.0, 3800.0)
Mix = create_expression(BL_ColorRamp3,unreal.MaterialExpressionLinearInterpolate,-340.0, 3620.0)
Position0 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionConstant,-1580.0, 3540.0)
Color0 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionConstant3Vector,-1580.0, 3620.0)
Reroute01 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionReroute,-1840.0, 3360.0)
Math20 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionDivide,-640.0, 4415.648193359375)
Math19 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionSubtract,-800.0, 4415.648193359375)
Math18 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionSubtract,-800.0, 4235.648193359375)
Math21 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionDivide,-640.0, 4235.648193359375)
Color2 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionConstant3Vector,-1560.0, 4620.0)
Mix01 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionLinearInterpolate,-20.0, 4480.0)
Position2 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionConstant,-1560.0, 4540.0)
Math22 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionMultiply,-480.0, 4260.0)
Reroute10 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Reroute09 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Reroute08 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Math23 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionAdd,-320.0, 4320.0)
Reroute06 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionReroute,-1840.0, 4400.0)
Reroute07 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionReroute,-1840.0, 4400.0)
Math12 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionSubtract,-1080.0, 3460.0)
Math15 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionDivide,-920.0, 3460.0)
Math16 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionMultiply,-760.0, 3480.0)
Math17 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionAdd,-600.0, 3540.0)
Math14 = create_expression(BL_ColorRamp3,unreal.MaterialExpressionDivide,-900.0, 3640.0)
Math13 = create_expression(BL_ColorRamp3, unreal.MaterialExpressionSubtract, -1080.0, 3640.0)

Factor = create_expression(BL_ColorRamp3, unreal.MaterialExpressionFunctionInput, -2200.0, 3320.0)
Factor.input_name = 'Factor'
Factor.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
OutputResult = create_expression(BL_ColorRamp3, unreal.MaterialExpressionFunctionOutput,400, 4480)

### Loading Material Functions and Textures

### Setting Values
Color1.constant = (1.0, 0.01521005667746067, 0.0)
Position1.r = 0.125
Position0.r = 0.0
Color0.constant = (0.0, 0.0, 0.0)
Color2.constant = (1.0, 0.16482490301132202, 0.0)
Position2.r = 0.25

### Creating Connections
Color1_connection = create_connection(Color1, '', Mix, 'B')
Position1_connection = create_connection(Position1, '', Math12, 'A')
Position1_connection = create_connection(Position1, '', Math13, 'B')
Position1_connection = create_connection(Position1, '', Reroute09, '')
Position1_connection = create_connection(Position1, '', Reroute10, '')
Position1_connection = create_connection(Position1, '', Reroute08, '')
Mix_connection = create_connection(Mix, '', Mix01, 'A')
Position0_connection = create_connection(Position0, '', Math12, 'B')
Position0_connection = create_connection(Position0, '', Math14, 'A')
Position0_connection = create_connection(Position0, '', Math13, 'A')
Color0_connection = create_connection(Color0, '', Mix, 'A')
Reroute01_connection = create_connection(Reroute01, '', Reroute06, '')
Reroute01_connection = create_connection(Reroute01, '', Math16, 'B')
Reroute01_connection = create_connection(Reroute01, '', Reroute07, '')
Math20_connection = create_connection(Math20, '', Math23, 'B')
Math19_connection = create_connection(Math19, '', Math20, 'B')
Math18_connection = create_connection(Math18, '', Math21, 'B')
Math21_connection = create_connection(Math21, '', Math22, 'A')
Color2_connection = create_connection(Color2, '', Mix01, 'B')
Position2_connection = create_connection(Position2, '', Math18, 'A')
Position2_connection = create_connection(Position2, '', Math19, 'B')
Math22_connection = create_connection(Math22, '', Math23, 'A')
Reroute10_connection = create_connection(Reroute10, '', Math20, 'A')
Reroute09_connection = create_connection(Reroute09, '', Math18, 'B')
Reroute08_connection = create_connection(Reroute08, '', Math19, 'A')
Math23_connection = create_connection(Math23, '', Mix01, 'Alpha')
Reroute06_connection = create_connection(Reroute06, '', Math22, 'B')
Factor_connection = create_connection(Factor, '', Reroute01, '')
Math12_connection = create_connection(Math12, '', Math15, 'B')
Math15_connection = create_connection(Math15, '', Math16, 'A')
Math16_connection = create_connection(Math16, '', Math17, 'A')
Math17_connection = create_connection(Math17, '', Mix, 'Alpha')
Math14_connection = create_connection(Math14, '', Math17, 'B')
Math13_connection = create_connection(Math13, '', Math14, 'B')

Mix01_connection = create_connection(Mix01, '', OutputResult, '')

update_function()