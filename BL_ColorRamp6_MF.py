import unreal

BL_ColorRamp6 = unreal.AssetToolsHelpers.get_asset_tools().create_asset('BL_ColorRamp6', '/Engine/Functions/BLUI/', unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())
BL_ColorRamp6.set_editor_property("expose_to_library", True)
BL_ColorRamp6.set_editor_property("library_categories_text", ("BLUI", "Custom", "Utility"))

create_expression = unreal.MaterialEditingLibrary.create_material_expression_in_function
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property
update_function = unreal.MaterialEditingLibrary.update_material_function

mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')
mat_func_combine = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat3')

### Creating Nodes

Mix = create_expression(BL_ColorRamp6,unreal.MaterialExpressionLinearInterpolate,-340.0, 3620.0)

Reroute01 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1840.0, 3360.0)
Math20 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-640.0, 4415.648193359375)
Math19 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-800.0, 4415.648193359375)
Math18 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-800.0, 4235.648193359375)
Math21 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-640.0, 4235.648193359375)
Mix01 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionLinearInterpolate,-20.0, 4480.0)
Math22 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionMultiply,-480.0, 4260.0)
Reroute10 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Reroute09 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Reroute08 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1120.0, 4360.0)
Math23 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionAdd,-320.0, 4320.0)
Reroute06 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1840.0, 4400.0)
Reroute07 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1840.0, 4400.0)
Reroute05 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1849.2108154296875, 5160.0)
Reroute02 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-960.0, 5080.0)
Reroute03 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-960.0, 5080.0)
Reroute04 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-960.0, 5080.0)
Math24 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionAdd,-120.0, 5080.0)
Math25 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionMultiply,-280.0, 5040.0)
Math27 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-600.0, 5195.648193359375)
Math28 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-600.0, 5015.648193359375)
Math29 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-440.0, 5015.648193359375)
Math26 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-440.0, 5195.648193359375)
Mix02 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionLinearInterpolate,100.0, 5180.0)
Mix03 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionLinearInterpolate,180.0, 6020.0)
Math30 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionAdd,-120.0, 5840.0)
Math31 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionMultiply,-280.0, 5800.0)
Math32 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-600.0, 5955.6484375)
Math33 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-600.0, 5775.6484375)
Math34 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-440.0, 5775.6484375)
Math35 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-440.0, 5955.6484375)
Reroute11 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1849.2108154296875, 5920.0)
Reroute14 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1020.0, 5880.0)
Reroute13 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1020.0, 5880.0)
Reroute12 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1020.0, 5880.0)
Math36 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionAdd,-120.0, 6600.0)
Math37 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionMultiply,-280.0, 6560.0)
Math38 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-600.0, 6715.6484375)
Math39 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-600.0, 6535.6484375)
Math40 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-440.0, 6535.6484375)
Math41 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-440.0, 6715.6484375)
Reroute15 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1849.2108154296875, 6680.0)
Reroute18 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1040.0, 6640.0)
Reroute17 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1040.0, 6640.0)
Reroute16 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionReroute,-1040.0, 6640.0)
Mix04 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionLinearInterpolate,160.0, 6780.0)
Math12 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionSubtract,-1080.0, 3460.0)
Math15 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-920.0, 3460.0)
Math16 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionMultiply,-760.0, 3480.0)
Math17 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionAdd,-600.0, 3540.0)
Math14 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionDivide,-900.0, 3640.0)
Math13 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionSubtract, -1080.0, 3640.0)

Position0 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1580.0, 3540.0)
Color0 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1580.0, 3620.0)

Position1 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1580.0, 3800.0)
Color1 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1580.0, 3880.0)

Position2 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1560.0, 4540.0)
Color2 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1560.0, 4620.0)

Position3 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1360.0, 5320.0)
Color3 = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -1360.0, 5400.0)

Color4 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionFunctionInput,-1360.0, 6160.0)
Position4 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionFunctionInput,-1360.0, 6080.0)

Color5 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionFunctionInput,-1360.0, 6920.0)
Position5 = create_expression(BL_ColorRamp6,unreal.MaterialExpressionFunctionInput,-1360.0, 6840.0)

Factor = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionInput, -2200.0, 3320.0)

OutputResult = create_expression(BL_ColorRamp6, unreal.MaterialExpressionFunctionOutput,400, 6020)

### Loading Material Functions and Textures

### Setting Values
Color0.input_name = 'Color0'
Color0.sort_priority = 0
Color0.preview_value = (0.0, 0.0, 0.0, 1.0)
Color0.use_preview_value_as_default = True
Position0.input_name = 'Position0'
Position0.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Position0.sort_priority = 1
Position0.preview_value = (0.0, 0.0, 0.0, 1.0)
Position0.use_preview_value_as_default = True

Color1.input_name = 'Color1'
Color1.sort_priority = 2
Color1.preview_value = (1.0, 0.0, 0.0, 1.0)
Color1.use_preview_value_as_default = True
Position1.input_name = "Position1"
Position1.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Position1.sort_priority = 3
Position1.preview_value = (0.125, 0, 0, 1)
Position1.use_preview_value_as_default = True

Color2.input_name = 'Color2'
Color2.sort_priority = 4
Color2.preview_value = (1.0, 0.5, 0.0, 1)
Color2.use_preview_value_as_default = True
Position2.input_name = "Position2"
Position2.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Position2.sort_priority = 5
Position2.preview_value = (0.250, 0, 0, 1)
Position2.use_preview_value_as_default = True

Color3.input_name = 'Color3'
Color3.sort_priority = 6
Color3.preview_value = (1.0, 1, 0.0, 1)
Color3.use_preview_value_as_default = True
Position3.input_name = "Position3"
Position3.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Position3.sort_priority = 7
Position3.preview_value = (0.375, 0, 0, 1)
Position3.use_preview_value_as_default = True

Color4.input_name = 'Color4'
Color4.sort_priority = 8
Color4.preview_value = (0, 1, 0.0, 1)
Color4.use_preview_value_as_default = True
Position4.input_name = "Position4"
Position4.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Position4.sort_priority = 9
Position4.preview_value = (0.5, 0, 0, 1)
Position4.use_preview_value_as_default = True

Color5.input_name = 'Color5'
Color5.sort_priority = 10
Color5.preview_value = (0, 1, 1, 1)
Color5.use_preview_value_as_default = True
Position5.input_name = "Position5"
Position5.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Position5.sort_priority = 11
Position5.preview_value = (0.625, 0, 0, 1)
Position5.use_preview_value_as_default = True

Factor.input_name = 'Factor'
Factor.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Factor.sort_priority = 12
Factor.preview_value = (0.0, 0.0, 0.0, 1.0)
Factor.use_preview_value_as_default = True

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
Reroute05_connection = create_connection(Reroute05, '', Reroute11, '')
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
Mix02_connection = create_connection(Mix02, '', Mix03, 'A')
Position3_connection = create_connection(Position3, '', Math28, 'A')
Position3_connection = create_connection(Position3, '', Math27, 'B')
Position3_connection = create_connection(Position3, '', Reroute14, '')
Position3_connection = create_connection(Position3, '', Reroute13, '')
Position3_connection = create_connection(Position3, '', Reroute12, '')
Mix03_connection = create_connection(Mix03, '', Mix04, 'A')
Math30_connection = create_connection(Math30, '', Mix03, 'Alpha')
Math31_connection = create_connection(Math31, '', Math30, 'A')
Math32_connection = create_connection(Math32, '', Math35, 'B')
Math33_connection = create_connection(Math33, '', Math34, 'B')
Math34_connection = create_connection(Math34, '', Math31, 'A')
Math35_connection = create_connection(Math35, '', Math30, 'B')
Reroute11_connection = create_connection(Reroute11, '', Math31, 'B')
Reroute11_connection = create_connection(Reroute11, '', Reroute15, '')
Reroute14_connection = create_connection(Reroute14, '', Math32, 'A')
Reroute13_connection = create_connection(Reroute13, '', Math33, 'B')
Reroute12_connection = create_connection(Reroute12, '', Math35, 'A')
Color4_connection = create_connection(Color4, '', Mix03, 'B')
Position4_connection = create_connection(Position4, '', Math33, 'A')
Position4_connection = create_connection(Position4, '', Math32, 'B')
Position4_connection = create_connection(Position4, '', Reroute18, '')
Position4_connection = create_connection(Position4, '', Reroute17, '')
Position4_connection = create_connection(Position4, '', Reroute16, '')
Math36_connection = create_connection(Math36, '', Mix04, 'Alpha')
Math37_connection = create_connection(Math37, '', Math36, 'A')
Math38_connection = create_connection(Math38, '', Math41, 'B')
Math39_connection = create_connection(Math39, '', Math40, 'B')
Math40_connection = create_connection(Math40, '', Math37, 'A')
Math41_connection = create_connection(Math41, '', Math36, 'B')
Reroute15_connection = create_connection(Reroute15, '', Math37, 'B')
Reroute18_connection = create_connection(Reroute18, '', Math38, 'A')
Reroute17_connection = create_connection(Reroute17, '', Math39, 'B')
Reroute16_connection = create_connection(Reroute16, '', Math41, 'A')
Color5_connection = create_connection(Color5, '', Mix04, 'B')
Position5_connection = create_connection(Position5, '', Math39, 'A')
Position5_connection = create_connection(Position5, '', Math38, 'B')
Factor_connection = create_connection(Factor, '', Reroute01, '')
Math12_connection = create_connection(Math12, '', Math15, 'B')
Math15_connection = create_connection(Math15, '', Math16, 'A')
Math16_connection = create_connection(Math16, '', Math17, 'A')
Math17_connection = create_connection(Math17, '', Mix, 'Alpha')
Math14_connection = create_connection(Math14, '', Math17, 'B')
Math13_connection = create_connection(Math13, '', Math14, 'B')

Mix04_connection = create_connection(Mix04, '', OutputResult, '')

update_function()