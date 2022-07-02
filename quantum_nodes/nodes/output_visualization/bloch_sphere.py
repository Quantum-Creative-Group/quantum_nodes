import bpy
from bpy.types import Node
from qiskit.visualization.utils import _bloch_multivector_data
from animation_nodes.base_types import AnimationNode
from ... visualization.utils.graphs_utils import get_angles


class BlochSphereNode(Node, AnimationNode):
    """Generate a new Bloch sphere."""

    bl_idname = "an_BlochSphereNode"
    bl_label = "Bloch Sphere"

    def create(self):
        self.newInput("Integer", "Qubit Index", "qubit_index", value=0, minValue=0)
        self.newInput("Vector", "Output State", "output_state")
        self.newInput("Object", "Bloch Sphere", "bloch_sphere")

    def execute(self, qubit_index, output_state, bloch_sphere):
        if bloch_sphere is None:
            return
        try:
            # getting the angles for displaying the vector
            bloch_data = _bloch_multivector_data(output_state)
            theta = get_angles(bloch_data[qubit_index][0], bloch_data[qubit_index][1], bloch_data[qubit_index][2])[1]
            phi = get_angles(bloch_data[qubit_index][0], bloch_data[qubit_index][1], bloch_data[qubit_index][2])[2]
            # finding the vector mesh in the list of the block sphere children
            for i in range(len(bloch_sphere.children)):
                # TODO: put bloch_sphere_vector so it is less ambiguous
                if bloch_sphere.children[i].name == "QuantumBlochVector":
                    vector = bloch_sphere.children[i]
            # the changes only need to be applied if the angles are different
            if abs(vector.rotation_euler[1] - theta) < 1e-6 and abs(vector.rotation_euler[2] - phi) < 1e-6:
                return
            else:
                bpy.context.view_layer.objects.active = vector
                vector.select_set(True)
                vector.rotation_euler = (0.0, theta, phi)
                vector.select_set(False)
        except BaseException:
            return
