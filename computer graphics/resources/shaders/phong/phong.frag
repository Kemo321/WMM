#version 330

in vec3 v_position;
in vec3 v_normal;
uniform vec3 material_ambient;
uniform vec3 material_diffuse;
uniform float material_shininess;
uniform vec3 camera_position;
out vec4 f_color;

const vec3 light_position = vec3(0.0, 7.0, -15.0);
const vec3 light_ambient = vec3(0.1, 0.1, 0.1);
const vec3 light_diffuse = vec3(1.0, 1.0, 1.0);
const vec3 light_specular = vec3(1.0, 1.0, 1.0);

void main() {
    // Ambient component
    vec3 ambient = light_ambient * material_ambient;

    // Diffuse component
    vec3 N = normalize(v_normal); // normalize normal vector
    vec3 L = normalize(light_position - v_position); // vector to light source
    float cosNL = clamp(dot(N, L), 0.0, 1.0); // dot product of normal and light
    vec3 diffuse = light_diffuse * material_diffuse * cosNL;

    // Specular component
    vec3 V = normalize(camera_position - v_position); // vector to camera
    vec3 R = reflect(-L, N); // reflection vector
    float spec = pow(max(dot(V, R), 0.0), material_shininess); // specular strength
    vec3 specular = light_specular * spec;

    // Final color (all components together)
    vec3 phong_color = clamp(ambient + diffuse + specular, 0.0, 1.0);
    f_color = vec4(phong_color, 1.0);
}