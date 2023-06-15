#parametric picture frames using python in blender
# give Python access to Blender's functionality
import bpy
# give Python access to Blender's mesh editing functionality
import bmesh
# extend Python functionality to generate random numbers
import random
import math

frame_height = 0.3
frame_selection = frameprofile01

# manually choose frameprofile, duplicate it near origin

# Get the active object
obj = bpy.context.active_object

# rotate absolute 90 up
degrees = 90
radians = math.radians(degrees)
obj.rotation_euler.x = radians

# toggle to edit mode
bpy.ops.object.editmode_toggle()

# Get the active object
bpy.data.objects['blarf'].select_set(True)

bpy.ops.object.editmode_toggle()
bpy.ops.object.editmode_toggle()

# extrude for value of 1 along y axis
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, frame_height, 0), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, True, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

# toggle to object mode
bpy.ops.object.editmode_toggle()

# choose dimensions of art, x , y, z

# change depth of rabbet depth (z of painting plus a little for clamps)

# extrude frameprofile to x , y dimensions

# shear off 45 degree angle for each 

# duplicate each x, y side for a total of four sides
