import bpy
from bpy.props import IntProperty

class SubdivideMesh(bpy.types.Operator):
    bl_idname = "dialog.number"
    bl_label = "Subdivide"
    bl_description = "Subdivides your object"

    number: bpy.props.IntProperty(name="subs", default=2, min=1, max=5)

    @classmethod
    def poll(cls, context):
        obj = bpy.context.active_object
        return context.object.select_get() and obj.type == "MESH" and cls.hasSubsurfModifier(obj)

    def execute(self, context):
        obj = bpy.context.active_object
        if(self.hasSubsurfModifier(obj)):
            obj.modifiers["an_q_demo_subdivide_op"].levels = self.number
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def hasSubsurfModifier(cls, obj):
        for modifier in obj.modifiers:
            if(type(modifier).__name__ == "SubsurfModifier"):
                return True
        return False
