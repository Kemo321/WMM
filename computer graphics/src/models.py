import numpy
from moderngl_window.opengl.vao import VAO


def load_quad_2D(program):
    size = 1.0

    positions = []

    positions.append([-size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0])

    positions = numpy.array(positions, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "2f", ["in_position"])

    return vao.instance(program)


def load_cube(program):
    size = 1.0

    positions = []
    # Front face
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    # Back face
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    # Top face
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    # Bottom face
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    # Left face
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    # Right face
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0, -size / 2.0])

    normals = []
    # Front face
    normals.append([0.0, 0.0, 1.0])
    normals.append([0.0, 0.0, 1.0])
    normals.append([0.0, 0.0, 1.0])
    normals.append([0.0, 0.0, 1.0])
    normals.append([0.0, 0.0, 1.0])
    normals.append([0.0, 0.0, 1.0])
    # Back face
    normals.append([0.0, 0.0, -1.0])
    normals.append([0.0, 0.0, -1.0])
    normals.append([0.0, 0.0, -1.0])
    normals.append([0.0, 0.0, -1.0])
    normals.append([0.0, 0.0, -1.0])
    normals.append([0.0, 0.0, -1.0])
    # Top face
    normals.append([0.0, 1.0, 0.0])
    normals.append([0.0, 1.0, 0.0])
    normals.append([0.0, 1.0, 0.0])
    normals.append([0.0, 1.0, 0.0])
    normals.append([0.0, 1.0, 0.0])
    normals.append([0.0, 1.0, 0.0])
    # Bottom face
    normals.append([0.0, -1.0, 0.0])
    normals.append([0.0, -1.0, 0.0])
    normals.append([0.0, -1.0, 0.0])
    normals.append([0.0, -1.0, 0.0])
    normals.append([0.0, -1.0, 0.0])
    normals.append([0.0, -1.0, 0.0])
    # Left face
    normals.append([-1.0, 0.0, 0.0])
    normals.append([-1.0, 0.0, 0.0])
    normals.append([-1.0, 0.0, 0.0])
    normals.append([-1.0, 0.0, 0.0])
    normals.append([-1.0, 0.0, 0.0])
    normals.append([-1.0, 0.0, 0.0])
    # Right face
    normals.append([1.0, 0.0, 0.0])
    normals.append([1.0, 0.0, 0.0])
    normals.append([1.0, 0.0, 0.0])
    normals.append([1.0, 0.0, 0.0])
    normals.append([1.0, 0.0, 0.0])
    normals.append([1.0, 0.0, 0.0])

    # Alternative to normals generation
    # generate_normals(positions)

    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals, "3f", ["in_normal"])
    return vao.instance(program)


def generate_normals(positions):
    N = len(positions)
    normals = []
    for i in range(0, N, 3):
        p0 = numpy.array(positions[i + 0])
        p1 = numpy.array(positions[i + 1])
        p2 = numpy.array(positions[i + 2])
        cross = numpy.cross(p1 - p0, p2 - p0)
        norm = cross / numpy.linalg.norm(cross)
        for v in range(3):
            normals.append(list(norm))
    return normals
