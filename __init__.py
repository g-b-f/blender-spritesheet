bl_info = {
    "name": "Direction Animation Exporter",
    "blender": (2, 80, 0),
    "category": "Render",
}

from . import blender_render_direction

def register():
    blender_render_direction.register()
    print("Hello World")


def unregister():
    blender_render_direction.unregister()
    print("Goodbye World")

