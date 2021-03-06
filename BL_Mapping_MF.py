import unreal

BL_Mapping = unreal.AssetToolsHelpers.get_asset_tools().create_asset('BL_Mapping','/Engine/Functions/BLUI/', unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())
BL_Mapping.set_editor_property("expose_to_library", True)
BL_Mapping.set_editor_property("library_categories_text", ("BLUI", "Custom", "Utility"))

create_expression = unreal.MaterialEditingLibrary.create_material_expression_in_function
create_connection = unreal.MaterialEditingLibrary.connect_material_expressions
connect_property = unreal.MaterialEditingLibrary.connect_material_property
update_function = unreal.MaterialEditingLibrary.update_material_function

mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')
mat_func_separate_V2 = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat2Components')
mat_func_combine = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat3')
mat_func_combine_V2 = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat2')

### Creating Nodes
Math06 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1960.0, -960.0)
Math01 = create_expression(BL_Mapping,unreal.MaterialExpressionSubtract,-2120.0, -960.0)
SeparateXYZ = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-2360.0, -1100.0)
SeparateXYZ01 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-2360.0, -960.0)
SeparateXYZ07 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-2700.0, -900.0)
CombineXYZ06 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-2540.0, -900.0)
SeparateXYZ08 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-2380.0, -760.0)
SeparateXYZ09 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-2380.0, -560.0)
Cosine03 = create_expression(BL_Mapping,unreal.MaterialExpressionCosine,-1580.0, -1200.0)
Multiply101 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -1200.0)
Subtract01 = create_expression(BL_Mapping,unreal.MaterialExpressionSubtract,-1260.0, -1200.0)
Multiply201 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -1040.0)
Sine03 = create_expression(BL_Mapping,unreal.MaterialExpressionSine,-1580.0, -1040.0)
Multiply301 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -860.0)
Sine02 = create_expression(BL_Mapping,unreal.MaterialExpressionSine,-1580.0, -860.0)
Add01 = create_expression(BL_Mapping,unreal.MaterialExpressionAdd,-1260.0, -860.0)
Multiply401 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -680.0)
Cosine02 = create_expression(BL_Mapping,unreal.MaterialExpressionCosine,-1580.0, -680.0)
CombineXYZ02 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-1060.0, -1020.0)
VectorMath01 = create_expression(BL_Mapping,unreal.MaterialExpressionAdd,-660.0, -1020.0)
VectorMath = create_expression(BL_Mapping,unreal.MaterialExpressionAdd,-860.0, -1020.0)
SeparateXYZ10 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-480.0, -1020.0)
Math11 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-300.0, -880.0)
Math10 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-300.0, -1020.0)
Math09 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-300.0, -1180.0)
CombineXYZ04 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-120.0, -1020.0)
SeparateXYZ06 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,60.0, -1020.0)
CombineXYZ05 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,240.0, -1020.0)
Math08 = create_expression(BL_Mapping,unreal.MaterialExpressionDivide,-1800.0, -180.0)
Math07 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1960.0, -180.0)
Math02 = create_expression(BL_Mapping,unreal.MaterialExpressionSubtract,-2120.0, -180.0)
Multiply102 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -480.0)
Cosine04 = create_expression(BL_Mapping,unreal.MaterialExpressionCosine,-1580.0, -480.0)
Subtract02 = create_expression(BL_Mapping,unreal.MaterialExpressionSubtract,-1260.0, -480.0)
Multiply202 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -320.0)
Sine04 = create_expression(BL_Mapping,unreal.MaterialExpressionSine,-1580.0, -320.0)
Sine05 = create_expression(BL_Mapping,unreal.MaterialExpressionSine,-1580.0, -120.0)
Multiply302 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -120.0)
Add02 = create_expression(BL_Mapping,unreal.MaterialExpressionAdd,-1260.0, -120.0)
Multiply402 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, 40.0)
CombineXYZ03 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-1080.0, -260.0)
Math04 = create_expression(BL_Mapping,unreal.MaterialExpressionDivide,-1800.0, -1600.0)
Math03 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1960.0, -1600.0)
Math = create_expression(BL_Mapping,unreal.MaterialExpressionSubtract,-2120.0, -1600.0)
Multiply1 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -1900.0)
Cosine01 = create_expression(BL_Mapping,unreal.MaterialExpressionCosine,-1580.0, -1900.0)
Subtract = create_expression(BL_Mapping,unreal.MaterialExpressionSubtract,-1260.0, -1900.0)
Multiply2 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -1740.0)
Sine = create_expression(BL_Mapping,unreal.MaterialExpressionSine,-1580.0, -1740.0)
Sine01 = create_expression(BL_Mapping,unreal.MaterialExpressionSine,-1580.0, -1560.0)
Multiply3 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -1560.0)
Add = create_expression(BL_Mapping,unreal.MaterialExpressionAdd,-1260.0, -1560.0)
Multiply4 = create_expression(BL_Mapping,unreal.MaterialExpressionMultiply,-1420.0, -1400.0)
Cosine = create_expression(BL_Mapping,unreal.MaterialExpressionCosine,-1580.0, -1400.0)
CombineXYZ01 = create_expression(BL_Mapping,unreal.MaterialExpressionMaterialFunctionCall,-1040.0, -1640.0)
Cosine05 = create_expression(BL_Mapping,unreal.MaterialExpressionCosine,-1580.0, 40.0)
Math05 = create_expression(BL_Mapping,unreal.MaterialExpressionDivide,-1800.0, -960.0)
Value02 = create_expression(BL_Mapping,unreal.MaterialExpressionConstant,-2120.0, -800.0)
Value = create_expression(BL_Mapping,unreal.MaterialExpressionConstant,-2120.0, -1440.0)
Value01 = create_expression(BL_Mapping,unreal.MaterialExpressionConstant,-1960.0, -1440.0)
Value05 = create_expression(BL_Mapping,unreal.MaterialExpressionConstant,-1960.0, -20.0)
Value03 = create_expression(BL_Mapping,unreal.MaterialExpressionConstant,-1960.0, -800.0)
Value04 = create_expression(BL_Mapping,unreal.MaterialExpressionConstant,-2120.0, -20.0)

OutputResult = create_expression(BL_Mapping, unreal.MaterialExpressionFunctionOutput, 420.0, -1020.0)

VectorInput = create_expression(BL_Mapping, unreal.MaterialExpressionFunctionInput, -2860.0, -900.0)
Location = create_expression(BL_Mapping,unreal.MaterialExpressionFunctionInput,-2540.0, -1100.0)
Rotation = create_expression(BL_Mapping,unreal.MaterialExpressionFunctionInput,-2540.0, -760.0)
Scale = create_expression(BL_Mapping,unreal.MaterialExpressionFunctionInput,-2540.0, -560.0)

### Loading Material Functions and Textures
SeparateXYZ.set_editor_property('material_function',mat_func_separate)
SeparateXYZ01.set_editor_property('material_function',mat_func_separate)
SeparateXYZ07.set_editor_property('material_function',mat_func_separate_V2)
CombineXYZ06.set_editor_property('material_function',mat_func_combine)
SeparateXYZ08.set_editor_property('material_function',mat_func_separate)
SeparateXYZ09.set_editor_property('material_function',mat_func_separate)
CombineXYZ02.set_editor_property('material_function',mat_func_combine)
SeparateXYZ10.set_editor_property('material_function',mat_func_separate)
CombineXYZ04.set_editor_property('material_function',mat_func_combine)
SeparateXYZ06.set_editor_property('material_function',mat_func_separate)
CombineXYZ05.set_editor_property('material_function',mat_func_combine_V2)
CombineXYZ03.set_editor_property('material_function',mat_func_combine)
CombineXYZ01.set_editor_property('material_function',mat_func_combine)

### Setting Values
VectorInput.input_name = 'VectorInput'
VectorInput.input_type = unreal.FunctionInputType.FUNCTION_INPUT_VECTOR2
VectorInput.sort_priority = 0
VectorInput.preview_value = (0, 0)
VectorInput.use_preview_value_as_default = True

Location.input_name = 'Location'
Location.sort_priority = 1
Location.preview_value = (0, 0, 0, 1)
Location.use_preview_value_as_default = True

Rotation.input_name = 'Rotation'
Rotation.sort_priority = 2
Rotation.preview_value = (0, 0, 0, 1)
Rotation.use_preview_value_as_default = True

Scale.input_name = 'Scale'
Scale.sort_priority = 3
Scale.preview_value = (1, 1, 1, 1)
Scale.use_preview_value_as_default = True

Value.r = 3.1419999599456787
Value01.r = 180.0
Value02.r = -3.1419999599456787
Value03.r = 180.0
Value04.r = 3.1419999599456787
Value05.r = 180.0

### Creating Connections
Math06_connection = create_connection(Math06, '', Math05, 'A')
Math01_connection = create_connection(Math01, '', Multiply402, 'B')
Math01_connection = create_connection(Math01, '', Multiply202, 'B')
Math01_connection = create_connection(Math01, '', CombineXYZ02, 'Y')
Math01_connection = create_connection(Math01, '', Multiply1, 'B')
Math01_connection = create_connection(Math01, '', Multiply3, 'B')
SeparateXYZ_connection = create_connection(SeparateXYZ, 'R', Math, 'B')
SeparateXYZ_connection = create_connection(SeparateXYZ, 'G', Math01, 'B')
SeparateXYZ_connection = create_connection(SeparateXYZ, 'B', Math02, 'B')
SeparateXYZ01_connection = create_connection(SeparateXYZ01, 'R', Math, 'A')
SeparateXYZ01_connection = create_connection(SeparateXYZ01, 'G', Math01, 'A')
SeparateXYZ01_connection = create_connection(SeparateXYZ01, 'B', Math02, 'A')
Location_connection = create_connection(Location, '', SeparateXYZ, 'Float3')
SeparateXYZ07_connection = create_connection(SeparateXYZ07, 'R', CombineXYZ06, 'X')
SeparateXYZ07_connection = create_connection(SeparateXYZ07, 'G', CombineXYZ06, 'Y')
CombineXYZ06_connection = create_connection(CombineXYZ06, 'Result', SeparateXYZ01, 'Float3')

VectorInput_connection = create_connection(VectorInput, '', SeparateXYZ07, 'Float2')

SeparateXYZ08_connection = create_connection(SeparateXYZ08, 'R', Math03, 'A')
SeparateXYZ08_connection = create_connection(SeparateXYZ08, 'G', Math06, 'A')
SeparateXYZ08_connection = create_connection(SeparateXYZ08, 'B', Math07, 'A')
Rotation_connection = create_connection(Rotation, '', SeparateXYZ08, 'Float3')
SeparateXYZ09_connection = create_connection(SeparateXYZ09, 'R', Math09, 'A')
SeparateXYZ09_connection = create_connection(SeparateXYZ09, 'G', Math10, 'A')
SeparateXYZ09_connection = create_connection(SeparateXYZ09, 'B', Math11, 'A')
Scale_connection = create_connection(Scale, '', SeparateXYZ09, 'Float3')
Cosine03_connection = create_connection(Cosine03, '', Multiply101, 'A')
Multiply101_connection = create_connection(Multiply101, '', Subtract01, 'A')
Subtract01_connection = create_connection(Subtract01, '', CombineXYZ02, 'X')
Multiply201_connection = create_connection(Multiply201, '', Subtract01, 'B')
Sine03_connection = create_connection(Sine03, '', Multiply201, 'A')
Multiply301_connection = create_connection(Multiply301, '', Add01, 'A')
Sine02_connection = create_connection(Sine02, '', Multiply301, 'A')
Add01_connection = create_connection(Add01, '', CombineXYZ02, 'Z')
Multiply401_connection = create_connection(Multiply401, '', Add01, 'B')
Cosine02_connection = create_connection(Cosine02, '', Multiply401, 'A')
CombineXYZ02_connection = create_connection(CombineXYZ02, 'Result', VectorMath, 'B')
VectorMath01_connection = create_connection(VectorMath01, '', SeparateXYZ10, 'Float3')
VectorMath_connection = create_connection(VectorMath, '', VectorMath01, 'A')
SeparateXYZ10_connection = create_connection(SeparateXYZ10, 'R', Math09, 'B')
SeparateXYZ10_connection = create_connection(SeparateXYZ10, 'G', Math10, 'B')
SeparateXYZ10_connection = create_connection(SeparateXYZ10, 'B', Math11, 'B')
Math11_connection = create_connection(Math11, '', CombineXYZ04, 'Z')
Math10_connection = create_connection(Math10, '', CombineXYZ04, 'Y')
Math09_connection = create_connection(Math09, '', CombineXYZ04, 'X')
CombineXYZ04_connection = create_connection(CombineXYZ04, 'Result', SeparateXYZ06, 'Float3')
SeparateXYZ06_connection = create_connection(SeparateXYZ06, 'R', CombineXYZ05, 'X')
SeparateXYZ06_connection = create_connection(SeparateXYZ06, 'G', CombineXYZ05, 'Y')

CombineXYZ05_connection = create_connection(CombineXYZ05, 'Result', OutputResult, '')

Math08_connection = create_connection(Math08, '', Sine04, '')
Math08_connection = create_connection(Math08, '', Cosine05, '')
Math08_connection = create_connection(Math08, '', Sine05, '')
Math08_connection = create_connection(Math08, '', Cosine04, '')
Math07_connection = create_connection(Math07, '', Math08, 'A')
Math02_connection = create_connection(Math02, '', CombineXYZ03, 'Z')
Math02_connection = create_connection(Math02, '', Multiply401, 'B')
Math02_connection = create_connection(Math02, '', Multiply201, 'B')
Math02_connection = create_connection(Math02, '', Multiply4, 'B')
Math02_connection = create_connection(Math02, '', Multiply2, 'B')
Multiply102_connection = create_connection(Multiply102, '', Subtract02, 'A')
Cosine04_connection = create_connection(Cosine04, '', Multiply102, 'A')
Subtract02_connection = create_connection(Subtract02, '', CombineXYZ03, 'X')
Multiply202_connection = create_connection(Multiply202, '', Subtract02, 'B')
Sine04_connection = create_connection(Sine04, '', Multiply202, 'A')
Sine05_connection = create_connection(Sine05, '', Multiply302, 'A')
Multiply302_connection = create_connection(Multiply302, '', Add02, 'A')
Add02_connection = create_connection(Add02, '', CombineXYZ03, 'Y')
Multiply402_connection = create_connection(Multiply402, '', Add02, 'B')
CombineXYZ03_connection = create_connection(CombineXYZ03, 'Result', VectorMath01, 'B')
Math04_connection = create_connection(Math04, '', Sine, '')
Math04_connection = create_connection(Math04, '', Cosine, '')
Math04_connection = create_connection(Math04, '', Sine01, '')
Math04_connection = create_connection(Math04, '', Cosine01, '')
Math03_connection = create_connection(Math03, '', Math04, 'A')
Math_connection = create_connection(Math, '', Multiply302, 'B')
Math_connection = create_connection(Math, '', Multiply102, 'B')
Math_connection = create_connection(Math, '', Multiply301, 'B')
Math_connection = create_connection(Math, '', Multiply101, 'B')
Math_connection = create_connection(Math, '', CombineXYZ01, 'X')
Multiply1_connection = create_connection(Multiply1, '', Subtract, 'A')
Cosine01_connection = create_connection(Cosine01, '', Multiply1, 'A')
Subtract_connection = create_connection(Subtract, '', CombineXYZ01, 'Y')
Multiply2_connection = create_connection(Multiply2, '', Subtract, 'B')
Sine_connection = create_connection(Sine, '', Multiply2, 'A')
Sine01_connection = create_connection(Sine01, '', Multiply3, 'A')
Multiply3_connection = create_connection(Multiply3, '', Add, 'A')
Add_connection = create_connection(Add, '', CombineXYZ01, 'Z')
Multiply4_connection = create_connection(Multiply4, '', Add, 'B')
Cosine_connection = create_connection(Cosine, '', Multiply4, 'A')
CombineXYZ01_connection = create_connection(CombineXYZ01, 'Result', VectorMath, 'A')
Cosine05_connection = create_connection(Cosine05, '', Multiply402, 'A')
Math05_connection = create_connection(Math05, '', Sine03, '')
Math05_connection = create_connection(Math05, '', Cosine02, '')
Math05_connection = create_connection(Math05, '', Sine02, '')
Math05_connection = create_connection(Math05, '', Cosine03, '')
Value02_connection = create_connection(Value02, '', Math06, 'B')
Value_connection = create_connection(Value, '', Math03, 'B')
Value01_connection = create_connection(Value01, '', Math04, 'B')
Value05_connection = create_connection(Value05, '', Math08, 'B')
Value03_connection = create_connection(Value03, '', Math05, 'B')
Value04_connection = create_connection(Value04, '', Math07, 'B')

update_function()

