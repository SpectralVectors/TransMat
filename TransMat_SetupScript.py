import os, unreal

fileDir = os.path.dirname(os.path.abspath(__file__))

files = []
files.append(str(fileDir) + '/BL_Mapping_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp9_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp8_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp7_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp6_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp5_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp4_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp3_MF.py')
files.append(str(fileDir) + '/BL_ColorRamp2_MF.py')

execute = unreal.PythonScriptLibrary.execute_python_command

for file in files:
    execute(file)