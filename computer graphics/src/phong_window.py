import moderngl
from pyrr import Matrix44, Vector3
import numpy as np

from base_window import BaseWindow


class PhongWindow(BaseWindow):
    def __init__(self, **kwargs):
        super(PhongWindow, self).__init__(**kwargs)

    def load_models(self):
        from models import load_cube
        self.cube = load_cube(self.program)
        return self.cube

    def init_shaders_variables(self):
        # Get uniform variable locations from the shader
        self.P_location = self.program['P']
        self.V_location = self.program['V']
        self.M_location = self.program['M']
        self.material_ambient = self.program['material_ambient']
        self.material_diffuse = self.program['material_diffuse']
        self.material_shininess = self.program['material_shininess']
        self.camera_position = self.program['camera_position']

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.8, 0.8, 0.8, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        # Projection and view matrices
        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        camera_pos = Vector3([-30.0, 5.0, -30.0])
        view = Matrix44.look_at(
            camera_pos,
            (0.0, 3.0, 0.0),  # Camera target
            (0.0, 1.0, 0.0),  # Up vector
        )

        # Pass matrices to shaders
        self.P_location.write(projection.astype('f4').tobytes())
        self.V_location.write(view.astype('f4').tobytes())
        self.camera_position.write(camera_pos.astype('f4').tobytes())

        # Head
        model = (
            Matrix44.from_translation((0, 4, 0))
            @ Matrix44.from_scale((1.5, 1.5, 1.5))
        )
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 0.1, 0.0], dtype='f4').tobytes())  # Orange ambient
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange diffuse
        self.material_shininess.value = 32.0
        self.cube.render(moderngl.TRIANGLES)

        # Body
        model = (
            Matrix44.from_translation((0, 0.5, 0))
            @ Matrix44.from_scale((2, 4, 2))
        )
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 0.1, 0.0], dtype='f4').tobytes())  # Orange ambient
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange diffuse
        self.material_shininess.value = 32.0
        self.cube.render(moderngl.TRIANGLES)

        # Left arm
        model = (
            Matrix44.from_translation((-2.5, 4, 0))
            @ Matrix44.from_scale((0.75, 2.5, 0.75))
            @ Matrix44.from_z_rotation(np.radians(-45))
        )
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 0.1, 0.0], dtype='f4').tobytes())  # Orange ambient
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange diffuse
        self.material_shininess.value = 32.0
        self.cube.render(moderngl.TRIANGLES)

        # Right arm
        model = (
            Matrix44.from_translation((2.5, 4, 0))
            @ Matrix44.from_scale((0.75, 2.5, 0.75))
            @ Matrix44.from_z_rotation(np.radians(45))
        )
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 0.1, 0.0], dtype='f4').tobytes())  # Orange ambient
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange diffuse
        self.material_shininess.value = 32.0
        self.cube.render(moderngl.TRIANGLES)

        # Left leg
        model = (
            Matrix44.from_translation((-2, -2, 0))
            @ Matrix44.from_scale((1, 3, 1))
            @ Matrix44.from_z_rotation(np.radians(30))
        )
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 0.1, 0.0], dtype='f4').tobytes())  # Orange ambient
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange diffuse
        self.material_shininess.value = 32.0
        self.cube.render(moderngl.TRIANGLES)

        # Right leg
        model = (
            Matrix44.from_translation((2, -2, 0))
            @ Matrix44.from_scale((1, 3, 1))
            @ Matrix44.from_z_rotation(np.radians(-30))
        )
        self.M_location.write(model.astype('f4').tobytes())
        self.material_ambient.write(np.array([0.2, 0.1, 0.0], dtype='f4').tobytes())  # Orange ambient
        self.material_diffuse.write(np.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange diffuse
        self.material_shininess.value = 32.0
        self.cube.render(moderngl.TRIANGLES)
