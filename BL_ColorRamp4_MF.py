import unreal

BL_ColorRamp4=unreal.AssetToolsHelpers.get_asset_tools().create_asset('BL_ColorRamp4','/Engine/Functions/BLUI/', unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())

create_expression = unreal.MaterialEditingLibrary.create_material_expression_in_function
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property
update_function = unreal.MaterialEditingLibrary.update_material_function

mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')
mat_func_combine = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat3')

### Creating Nodes
Color1 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant3Vector,-1580.0, 3880.0)
Position1 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant,-1580.0, 3800.0)
Mix = create_expression(BL_ColorRamp4,unreal.MaterialExpressionLinearInterpolate,-340.0, 3620.0)
Position0 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant,-1580.0, 3540.0)
Color0 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant3Vector,-1580.0, 3620.0)
Reroute01 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1840.0, 3360.0)
Math20 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionDivide,-640.0, 4415.648193359375)
Math19 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionSubtract,-800.0, 4415.648193359375)
Math18 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionSubtract,-800.0, 4235.648193359375)
Math21 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionDivide,-640.0, 4235.648193359375)
Color2 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant3Vector,-1560.0, 4620.0)
Mix01 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionLinearInterpolate,-20.0, 4480.0)
Position2 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant,-1560.0, 4540.0)
Math22 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionMultiply,-480.0, 4260.0)
Reroute10 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Reroute09 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Reroute08 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Math23 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionAdd,-320.0, 4320.0)
Reroute06 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1840.0, 4400.0)
Reroute07 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1840.0, 4400.0)
Reroute05 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-1849.2108154296875, 5160.0)
Reroute02 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-960.0, 5080.0)
Reroute03 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-960.0, 5080.0)
Reroute04 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionReroute,-960.0, 5080.0)
Math24 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionAdd,-120.0, 5080.0)
Math25 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionMultiply,-280.0, 5040.0)
Math27 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionSubtract,-600.0, 5195.648193359375)
Math28 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionSubtract,-600.0, 5015.648193359375)
Math29 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionDivide,-440.0, 5015.648193359375)
Color3 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant3Vector,-1360.0, 5400.0)
Math26 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionDivide,-440.0, 5195.648193359375)
Mix02 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionLinearInterpolate,100.0, 5180.0)
Position3 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionConstant,-1360.0, 5320.0)
Math12 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionSubtract,-1080.0, 3460.0)
Math15 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionDivide,-920.0, 3460.0)
Math16 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionMultiply,-760.0, 3480.0)
Math17 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionAdd,-600.0, 3540.0)
Math14 = create_expression(BL_ColorRamp4,unreal.MaterialExpressionDivide,-900.0, 3640.0)
Math13 = create_expression(BL_ColorRamp4, unreal.MaterialExpressionSubtract, -1080.0, 3640.0)

Factor = create_expression(BL_ColorRamp4, unreal.MaterialExpressionFunctionInput, -2200.0, 3320.0)
Factor.input_name = 'Factor'
Factor.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
OutputResult = create_expression(BL_ColorRamp4, unreal.MaterialExpressionFunctionOutput,400, 5280)

### Loading Material Functions and Textures

### Setting Values
Color1.constant = (1.0, 0.01521005667746067, 0.0)
Position1.r = 0.125
Position0.r = 0.0
Color0.constant = (0.0, 0.0, 0.0)
Color2.constant = (1.0, 0.16482490301132202, 0.0)
Position2.r = 0.25
Color3.constant = (1.0, 0.9584746956825256, 0.0)
Position3.r = 0.375

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
Mix01_connection = create_connection(Mix01, '', Mix02, 'A')
Position2_connection = create_connection(Position2, '', Math18, 'A')
Position2_connection = create_connection(Position2, '', Math19, 'B')
Position2_connection = create_connection(Position2, '', Reroute03, '')
Position2_connection = create_connection(Position2, '', Reroute04, '')
Position2_connection = create_connection(Position2, '', Reroute02, '')
Math22_connection = create_connection(Math22, '', Math23, 'A')
Reroute10_connection = create_connection(Reroute10, '', Math20, 'A')
Reroute09_connection = create_connection(Reroute09, '', Math18, 'B')
Reroute08_connection = create_connection(Reroute08, '', Math19, 'A')
Math23_connection = create_connection(Math23, '', Mix01, 'Alpha')
Reroute06_connection = create_connection(Reroute06, '', Math22, 'B')
Reroute07_connection = create_connection(Reroute07, '', Reroute05, '')
Reroute05_connection = create_connection(Reroute05, '', Math25, 'B')
Reroute02_connection = create_connection(Reroute02, '', Math26, 'A')
Reroute03_connection = create_connection(Reroute03, '', Math28, 'B')
Reroute04_connection = create_connection(Reroute04, '', Math27, 'A')
Math24_connection = create_connection(Math24, '', Mix02, 'Alpha')
Math25_connection = create_connection(Math25, '', Math24, 'A')
Math27_connection = create_connection(Math27, '', Math26, 'B')
Math28_connection = create_connection(Math28, '', Math29, 'B')
Math29_connection = create_connection(Math29, '', Math25, 'A')
Color3_connection = create_connection(Color3, '', Mix02, 'B')
Math26_connection = create_connection(Math26, '', Math24, 'B')
Position3_connection = create_connection(Position3, '', Math28, 'A')
Position3_connection = create_connection(Position3, '', Math27, 'B')
Factor_connection = create_connection(Factor, '', Reroute01, '')
Math12_connection = create_connection(Math12, '', Math15, 'B')
Math15_connection = create_connection(Math15, '', Math16, 'A')
Math16_connection = create_connection(Math16, '', Math17, 'A')
Math17_connection = create_connection(Math17, '', Mix, 'Alpha')
Math14_connection = create_connection(Math14, '', Math17, 'B')
Math13_connection = create_connection(Math13, '', Math14, 'B')

Mix02_connection = create_connection(Mix02, '', OutputResult, '')

update_function()