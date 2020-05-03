import pymel.core as pm


# List selection
def auto_project():
    sel = pm.ls(sl=True)
    for s in sel:
        shapes = pm.listRelatives(s, shapes=True)
        for shape in shapes:
            pm.polyAutoProjection(shape)


def make_lightmap():
    sel = pm.ls(sl=True)
    for s in sel:
        pm.polyUVSet(s, copy=True, uvSet='map1', newUVSet='lightmap')


def get_uv_sets():
    sel = pm.ls(sl=True)
    for s in sel:
        print(pm.polyUVSet(query=True, allUVSets=True))


def copy_uv_sets():
    sel = pm.ls(sl=True)
    for s in sel:
        pm.polyUVSet(s, copy=True, uvSet='map1', newUVSet='lightmap')


# def auto_layout_lightmap():
# Get meshes

# Get Lightmap UV channels

# Layout the UV
# print 'uvs laid out'
copy_uv_sets()
