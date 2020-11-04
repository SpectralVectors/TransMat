import unreal

BL_ColorRamp2 = unreal.AssetToolsHelpers.get_asset_tools().create_asset('BL_ColorRamp2', '/Engine/Functions/BLUI/', unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())
BL_ColorRamp2.set_editor_property("expose_to_library", True)
BL_ColorRamp2.set_editor_property("library_categories_text", ("BLUI", "Custom", "Utility"))

create_expression = unreal.MaterialEditingLibrary.create_material_expression_in_function
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property
update_function = unreal.MaterialEditingLibrary.update_material_function

mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')
mat_func_combine = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat3')

### Creating Nodes
Mix = create_expression(BL_ColorRamp2,unreal.MaterialExpressionLinearInterpolate,-340.0, 3620.0)
Reroute01 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionReroute,-1840.0, 3360.0)
Math12 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionSubtract,-1080.0, 3460.0)
Math15 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionDivide,-920.0, 3460.0)
Math16 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionMultiply,-760.0, 3480.0)
Math17 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionAdd,-600.0, 3540.0)
Math14 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionDivide,-900.0, 3640.0)
Math13 = create_expression(BL_ColorRamp2, unreal.MaterialExpressionSubtract, -1080.0, 3640.0)

Position0 = create_expression(BL_ColorRamp2, unreal.MaterialExpressionFunctionInput, -1580.0, 3540.0)
Color0 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionFunctionInput,-1580.0, 3620.0)
Position1 = create_expression(BL_ColorRamp2, unreal.MaterialExpressionFunctionInput, -1580.0, 3800.0)
Color1 = create_expression(BL_ColorRamp2,unreal.MaterialExpressionFunctionInput,-1580.0, 3880.0)

Factor = create_expression(BL_ColorRamp2, unreal.MaterialExpressionFunctionInput, -2200.0, 3320.0)

OutputResult = create_expression(BL_ColorRamp2, unreal.MaterialExpressionFunctionOutput,400, 3620)

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


Factor.input_name = 'Factor'
Factor.input_type = unreal.FunctionInputType.FUNCTION_INPUT_SCALAR
Factor.sort_priority = 4
Factor.preview_value = (0.0, 0.0, 0.0, 1.0)
Factor.use_preview_value_as_default = True


### Creating Connections
Color1_connection = create_connection(Color1, '', Mix, 'B')
Position1_connection = create_connection(Position1, '', Math12, 'A')
Position1_connection = create_connection(Position1, '', Math13, 'B')
Position0_connection = create_connection(Position0, '', Math12, 'B')
Position0_connection = create_connection(Position0, '', Math14, 'A')
Position0_connection = create_connection(Position0, '', Math13, 'A')
Color0_connection = create_connection(Color0, '', Mix, 'A')
Reroute01_connection = create_connection(Reroute01, '', Math16, 'B')
Factor_connection = create_connection(Factor, '', Reroute01, '')
Math12_connection = create_connection(Math12, '', Math15, 'B')
Math15_connection = create_connection(Math15, '', Math16, 'A')
Math16_connection = create_connection(Math16, '', Math17, 'A')
Math17_connection = create_connection(Math17, '', Mix, 'Alpha')
Math14_connection = create_connection(Math14, '', Math17, 'B')
Math13_connection = create_connection(Math13, '', Math14, 'B')

Mix_connection = create_connection(Mix, '', OutputResult, '')

update_function()