'''
Copyright (C) 2020 QuantumNodes
<YOUR EMAIL>

Created by QuantumNodes

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Quantum Nodes",
    "author": "Quantum Nodes",
    "version": (0, 0, 1),
    "blender": (2, 91, 0),
    "location": "Animation Nodes",
    "description": "Schrödinger Simulation for Animation Node",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Nodes",
}

import bpy
import addon_utils
from . import auto_load

try: import animation_nodes
except:
    animation_nodes = addon_utils.enable("animation_nodes", default_set = False, persistent = True)
    if not animation_nodes:
        raise Exception("Could not load Animation Nodes.")

auto_load.init()

animation_nodes.sockets.info.updateSocketInfo()

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()
