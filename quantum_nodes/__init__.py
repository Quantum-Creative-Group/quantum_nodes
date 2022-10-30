"""
Copyright (C) 2021-2022 Quantum Creative Group.\
contact@quantum-nodes.com.

Created by Quantum-Creative-Group

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

bl_info = {
    "name": "Quantum Nodes",
    "author": "Quantum Creative Group",
    "version": (0, 1, 1),
    "blender": (2, 92, 0),
    "location": "Animation Nodes Editor",
    "description": "Animation Nodes extension which implements quantum computing tools.",
    "warning": "This version is still in development.",
    "doc_url": "https://quantum-creative-group.gitlab.io/quantum_nodes_manual/",
    "tracker_url": "https://github.com/Quantum-Creative-Group/quantum_nodes/issues",
    "category": "Node",
}

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
