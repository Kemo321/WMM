import moderngl
import numpy as np
from pyrr import Matrix44, Vector3
from base_window import BaseWindow


class ShapesWindow(BaseWindow):
    def __init__(self, **kwargs):
        super(ShapesWindow, self).__init__(**kwargs)
        self.load_models()
        self.init_shaders_variables()

    def load_models(self):
        self.pyramid = self.load_pyramid()
        self.cylinder = self.load_cylinder()

    def load_pyramid(self):
        # Pyramid vertices (square base + apex)
        positions = np.array([
            # Base
            [-0.5, 0.0, -0.5], [0.5, 0.0, -0.5], [0.5, 0.0, 0.5], [-0.5, 0.0, 0.5],
            # Apex
            [0.0, 1.0, 0.0]
        ], dtype='f4')

        # Triangle indices
        indices = np.array([
            0, 1, 4,  # Side 1
            1, 2, 4,  # Side 2
            2, 3, 4,  # Side 3
            3, 0, 4,  # Side 4
            0, 1, 2,  # Base triangle 1
            2, 3, 0   # Base triangle 2
        ], dtype='i4')

        # Calculate normals for each vertex
        normals = np.zeros_like(positions)
        face_count = np.zeros(len(positions), dtype='i4')
        for tri in indices.reshape(-1, 3):
            v0, v1, v2 = positions[tri[0]], positions[tri[1]], positions[tri[2]]
            normal = np.cross(v1 - v0, v2 - v0)
            normal /= np.linalg.norm(normal)
            normals[tri] += normal
            face_count[tri] += 1
        normals /= face_count[:, np.newaxis]  # Average normals
        normals /= np.linalg.norm(normals, axis=1)[:, np.newaxis]  # Normalize

        vbo = self.ctx.buffer(positions.tobytes())
        ibo = self.ctx.buffer(indices.tobytes())
        nbo = self.ctx.buffer(normals.tobytes())
        vao = self.ctx.vertex_array(
            self.program,
            [(vbo, '3f', 'in_position'), (nbo, '3f', 'in_normal')],
            ibo
        )
        return vao

    def load_cylinder(self, segments=20):
        positions = []
        normals = []
        indices = []
        height = 1.0
        radius = 0.5

        # Generate vertices for top and bottom rings
        for i in range(segments):
            theta = 2.0 * np.pi * i / segments
            x, z = radius * np.cos(theta), radius * np.sin(theta)
            # Top ring vertex
            positions.append([x, height/2, z])
            normals.append([x, 0, z])  # Side normal
            # Bottom ring vertex
            positions.append([x, -height/2, z])
            normals.append([x, 0, z])  # Side normal

        # Center vertices for caps
        bottom_center = len(positions)
        positions.append([0, -height/2, 0])
        normals.append([0, -1, 0])
        top_center = len(positions)
        positions.append([0, height/2, 0])
        normals.append([0, 1, 0])

        # Indices for caps (top and bottom)
        for i in range(segments):
            next_i = (i + 1) % segments
            # Bottom (counterclockwise)
            indices.extend([bottom_center, 2*next_i, 2*i])
            # Top (clockwise)
            indices.extend([top_center, 2*i+1, 2*next_i+1])

        # Indices for side faces
        for i in range(segments):
            next_i = (i + 1) % segments
            # First triangle
            indices.extend([2*i, 2*next_i, 2*i+1])
            # Second triangle
            indices.extend([2*i+1, 2*next_i, 2*next_i+1])

        positions = np.array(positions, dtype='f4')
        normals = np.array(normals, dtype='f4')
        indices = np.array(indices, dtype='i4')

        vbo = self.ctx.buffer(positions.tobytes())
        ibo = self.ctx.buffer(indices.tobytes())
        nbo = self.ctx.buffer(normals.tobytes())
        vao = self.ctx.vertex_array(
            self.program,
            [(vbo, '3f', 'in_position'), (nbo, '3f', 'in_normal')],
            ibo
        )
        return vao

    def init_shaders_variables(self):
        # Get uniform locations from shader
        self.P_location = self.program['P']
        self.V_location = self.program['V']
        self.M_location = self.program['M']
        self.material_ambient = self.program['material_ambient']
        self.material_diffuse = self.program['material_diffuse']
        self.material_shininess = self.program['material_shininess']
        self.camera_position = self.program['camera_position']

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.8, 0.8, 0.8, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST)

        # Projection and view matrices
        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        camera_pos = Vector3([-10.0, -2.0, -10.0])
        view = Matrix44.look_at(
            camera_pos,
            (0.0, 5.0, 0.0),
            (0.0, 1.0, 0.0),
        )

        self.P_location.write(projection.astype('f4').tobytes())
        self.V_location.write(view.astype('f4').tobytes())
        self.camera_position.write(camera_pos.astype('f4').tobytes())

        # Head: Pyramid, orange
        model = Matrix44.from_translation((0, 5, 0)) @ Matrix44.from_y_rotation(0.2 * time) @ Matrix44.from_scale((1.5, 1.5, 1.5))
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 2, 0.0], dtype='f4').tobytes())  # green
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())
        self.material_shininess.value = 32.0
        self.pyramid.render(moderngl.TRIANGLES)

        # Body: Cylinder, cyan
        model = Matrix44.from_translation((0, 1.2, 0)) @ Matrix44.from_scale((2, 4, 2)) @ Matrix44.from_y_rotation(0.2 * time)
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([2.0, 0.2, 0], dtype='f4').tobytes())  # cyan
        self.material_diffuse.write(np.array([2.0, 1.0, 1.0], dtype='f4').tobytes())
        self.material_shininess.value = 32.0
        self.cylinder.render(moderngl.TRIANGLES)
