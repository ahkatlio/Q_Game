from ursina import *

app = Ursina()

# Define a light green color using RGB values
light_green = color.rgba(144, 238, 144, 255)

# Set the window background color to light green
window.color = light_green

# Create a 3D base with a collider
base = Entity(model='cube', scale=(10, 0.5, 10), color=color.gray)
base.collider = 'box'  # Add a Collider component to the base

# Create a 3D ball with a collider
ball = Entity(model='sphere', color=color.orange, position=(0, 5, 0), collider='sphere')
ball.collider.gravity = -0.5  # Set the gravity value

# Create a camera
camera.position = (0, 20, -30)
camera.rotation_x = 30

# Define a function to move the ball and camera
def update():
    if held_keys['w']:
        ball.z += 0.1
        ball.rotation_z -= 10  # Rotate the ball
    if held_keys['s']:
        ball.z -= 0.1
        ball.rotation_z += 10  # Rotate the ball
    if held_keys['a']:
        ball.x -= 0.1
        ball.rotation_x -= 10  # Rotate the ball
    if held_keys['d']:
        ball.x += 0.1
        ball.rotation_x += 10  # Rotate the ball

    # Set the camera's position to the ball's position
    camera.position = ball.position + (0, 20, -30)

app.run()