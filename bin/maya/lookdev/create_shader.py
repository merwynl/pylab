import pymel.core as pm
import random
import maya.pm as pm


shaders = ['mat_01', 'mat_02', 'mat_03']

# Check to see is material exist

    # Assign material if it already exists
    

    # If not create the material

    # Connect the selection to the shading group

def get_all_materials():
    materials = []
    # Gets a list of all material nodes and stores them in a list for comparison
    for material in pm.ls(type='shadingEngine'):
        materials.append(material)
    return materials


def check_if_material_exists():
    get_all_materials()



def create_nodes(shader_name):
    # Create material node
    shader = pm.shadingNode('lambert', name=shader_name, asShader=True)

    # Create Shading Group
    shading_group= pm.sets(name = shader+'SG', renderable=True,noSurfaceShader=True,empty=True)

    # Set Material node properties and connect the material node to the shading group
    red = random.random()
    green = random.random()
    blue = random.random()
    pm.setAttr(shader + ".color", red, green, blue, type='double3')
    pm.connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_group)




def get_shading_group(shader=None):
    if shader:
        if pm.objExists(shader):
            shading_group = pm.listConnections(shader, d=True, et=True, t='shadingEngine')
            if shading_group:
                return shading_group[0]
    return None


def assignObjectListToShader(objList=None, shader=None):
    """
    Assign the shader to the object list
    arguments:
        objList: list of objects or faces
    """
    # assign selection to the shader
    shaderSG = get_shading_group(shader)
    if objList:
        if shaderSG:
            pm.sets(objList, e=True, forceElement=shaderSG)
        else:
            print 'The provided shader didn\'t return a shaderSG'
    else:
        print 'Please select one or more objects'

        
def assignSelectionToShader(shader=None):
    sel = pm.ls(sl=True, l=True)
    if len(sel) == 0:
        print "Nothing currently selected!"
    else:
        # Error checking for selection type
        for s in sel:
            assignObjectListToShader(sel, shader)
            # create_nodes(shader_name=decal_Depth_vent)




# Assign shader to selection
def assign_material_to_selection():
    sel = pm.ls(sl=True, l=True)
    # Error checking for selection node type
    if len(sel) == 0:
        print "Nothing currently selected!"
    else:
        # Error checking for selection node type
        for s in sel:
            node_type = pm.nodeType(s)
            if node_type == 'transform' or 'mesh':
                shading_group = pm.listConnections(node_type, d=True, et=True, t='shadingEngine')
                if shading_group:
                    pm.sets(node_type, e=True, forceElement=shader)
                    print "Success"
            else:
                print "Not a mesh or transform type"


assignSelectionToShader('decal_Depth_grille')
