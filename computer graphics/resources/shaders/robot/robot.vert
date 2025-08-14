#version 330

in vec3 in_position;
uniform mat4 pvmr_matrix;

void main() {
    gl_Position = pvmr_matrix * vec4(in_position, 1.0);
}