import moderngl
from pyrr import Matrix44
import numpy

from base_window import BaseWindow


class RobotWindow(BaseWindow):
    def __init__(self, **kwargs):
        super(RobotWindow, self).__init__(**kwargs)

    def load_models(self):
        from models import load_cube
        self.cube_3d = load_cube(self.program)
        return self.cube_3d

    def init_shaders_variables(self):
        self.uniform_pvmr_matrix = self.program['pvmr_matrix']
        self.uniform_color = self.program['color']

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.8, 0.8, 0.8, 0.0) 
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        # Projection and view matrices
        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        view = Matrix44.look_at(
            (-5.0, 5.0, -10.0),  # Camera position
            (0.0, 3.0, 0.0),     # Point the camera looks at
            (0.0, 1.0, 0.0),     # "Up" vector
        )
        pv_matrix = projection * view

        # Head: translation (0, 5, 0), scaling (1.5, 1.5, 1.5)
        model_translation = Matrix44.from_translation((0, 5, 0))
        model_scale = Matrix44.from_scale((1.5, 1.5, 1.5))
        self.uniform_pvmr_matrix.write((pv_matrix * model_translation * model_scale).astype('f4').tobytes())
        self.uniform_color.write(numpy.array([1.0, 0.5, 0.0], dtype='f4').tobytes())  # Orange
        self.cube_3d.render(moderngl.TRIANGLES)

        # Body: translation (0, 2, 0), scaling (2, 4, 2)
        model_translation = Matrix44.from_translation((0, 2, 0))
        model_scale = Matrix44.from_scale((2, 4, 2))
        self.uniform_pvmr_matrix.write((pv_matrix * model_translation * model_scale).astype('f4').tobytes())
        self.uniform_color.write(numpy.array([0.0, 1.0, 1.0], dtype='f4').tobytes())  # Cyan
        self.cube_3d.render(moderngl.TRIANGLES)

        # Left arm: translation (-2.5, 4, 0), rotation -45° (Z), scaling (0.75, 2.5, 0.75)
        model_translation = Matrix44.from_translation((-2.5, 4, 0))
        model_scale = Matrix44.from_scale((0.75, 2.5, 0.75))
        model_rotation_z = Matrix44.from_z_rotation(-numpy.pi / 4)
        self.uniform_pvmr_matrix.write((pv_matrix * model_translation * model_rotation_z * model_scale).astype('f4').tobytes())
        self.uniform_color.write(numpy.array([0.5, 0.0, 1.0], dtype='f4').tobytes())  # Purple
        self.cube_3d.render(moderngl.TRIANGLES)

        # Right arm: translation (2.5, 4, 0), rotation +45° (Z), scaling (0.75, 2.5, 0.75)
        model_translation = Matrix44.from_translation((2.5, 4, 0))
        model_scale = Matrix44.from_scale((0.75, 2.5, 0.75))
        model_rotation_z = Matrix44.from_z_rotation(numpy.pi / 4)
        self.uniform_pvmr_matrix.write((pv_matrix * model_translation * model_rotation_z * model_scale).astype('f4').tobytes())
        self.uniform_color.write(numpy.array([0.5, 0.0, 1.0], dtype='f4').tobytes())  # Purple
        self.cube_3d.render(moderngl.TRIANGLES)

        # Left leg: translation (-2, -2, 0), rotation +30° (Z), scaling (1, 3, 1)
        model_translation = Matrix44.from_translation((-2, -2, 0))
        model_scale = Matrix44.from_scale((1, 3, 1))
        model_rotation_z = Matrix44.from_z_rotation(numpy.pi / 6)
        self.uniform_pvmr_matrix.write((pv_matrix * model_translation * model_rotation_z * model_scale).astype('f4').tobytes())
        self.uniform_color.write(numpy.array([1.0, 0.0, 0.5], dtype='f4').tobytes())  # Pink
        self.cube_3d.render(moderngl.TRIANGLES)

        # Right leg: translation (2, -2, 0), rotation -30° (Z), scaling (1, 3, 1)
        model_translation = Matrix44.from_translation((2, -2, 0))
        model_scale = Matrix44.from_scale((1, 3, 1))
        model_rotation_z = Matrix44.from_z_rotation(-numpy.pi / 6)
        self.uniform_pvmr_matrix.write((pv_matrix * model_translation * model_rotation_z * model_scale).astype('f4').tobytes())
        self.uniform_color.write(numpy.array([1.0, 0.0, 0.5], dtype='f4').tobytes())  # Pink
        self.cube_3d.render(moderngl.TRIANGLES)
