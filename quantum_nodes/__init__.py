import os
import sys
import site
from pathlib import Path

bl_info = {
    "name": "Quantum Nodes",
    "author": "Quantum Creative Group",
    "version": (0, 1, 2),
    "blender": (2, 93, 0),
    "location": "Animation Nodes",
    "description": "Animation Nodes extension which implements quantum computing tools.",
    "warning": "This version is still in development.",
    "doc_url": "https://quantum-creative-group.github.io/quantum_nodes/",
    "tracker_url": "https://github.com/Quantum-Creative-Group/quantum_nodes/issues",
    "category": "Node",
}

# Add user default folders where pip will install some of the dependencies
# This is because some folders may not be writable
sys.path.append(os.path.abspath(site.USER_SITE))
sys.path.append(os.path.join(os.path.abspath(Path(site.USER_SITE).parent), "Scripts"))

import addon_utils
from . import auto_load

try:
    import animation_nodes
except BaseException:
    animation_nodes = addon_utils.enable("animation_nodes", default_set=False, persistent=True, handle_error=None)
    if not animation_nodes:
        raise Exception("Could not load Animation Nodes.")

auto_load.init()

animation_nodes.sockets.info.updateSocketInfo()


def register():
    auto_load.register()


def unregister():
    auto_load.unregister()
