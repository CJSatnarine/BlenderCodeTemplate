import bpy

#Function to clean the scene. This removes all of the objects, collections, materials, particles, textures, images, curves, meshes, actions, nodes, and worlds from the scene. 
def cleanScene():
    # Changes the mode to object mode if it is in Edit mode. 
    if (bpy.context.active_object and bpy.context.active_object.mode == "EDIT"):
        bpy.ops.object.editmode_toggle()
        
    # Checks for hidden stuff and unhides them.     
    for obj in bpy.data.objects: 
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False
        
    # Selects all the objects and then deletes.     
    bpy.ops.object.select_all(action = "SELECT")
    bpy.ops.object.delete()

# Call functions. 
cleanScene()