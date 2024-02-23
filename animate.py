import cpf3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def create_animation(animation, title, output_file, fps, initial_camera_position, fig_size, dpi, rotation_speed, progress_bar):
	def update(frame_number, animation, title, scatter, ax, rotation_speed, progress_bar):
		ax.set_title(f'{title} — Frame {frame_number}')

		frame_data = animation.get_positions(frame_number - 1)
		colors = np.array([point.color for point in animation.points]) / 255
		scatter.set_offsets(frame_data[:, :2])
		scatter.set_3d_properties(frame_data[:, 2], zdir='z')
		scatter.set_color(colors)

		current_azim = ax.azim
		ax.view_init(ax.elev, azim=current_azim + rotation_speed)

		progress_bar()

		return scatter,

	fig = plt.figure(figsize=fig_size, dpi=dpi)
	ax = fig.add_subplot(111, projection='3d')
	ax.set_box_aspect([1, 1, 1])
	ax.set_xlabel('X Axis')
	ax.set_ylabel('Y Axis')
	ax.set_zlabel('Z Axis')
	scatter = ax.scatter([], [], [], c=[], marker='x', s=50)

	elev, azim = initial_camera_position
	ax.view_init(elev=elev, azim=azim)

	frame_keys = range(1, len(animation.frames))
	ms_interval = 1000 / fps
	anim = FuncAnimation(fig, update, fargs=(animation, title, scatter, ax, rotation_speed, progress_bar), frames=frame_keys, interval=ms_interval, blit=False)
	anim.save(output_file, writer='ffmpeg')
