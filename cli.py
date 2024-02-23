from itertools import permutations
from os.path import basename

import click
import cpf3d
from alive_progress import alive_bar

from animate import create_animation


@click.command()
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
@click.argument('title', required=False)
@click.option('--fps', default=30, type=int, help='Frames per second')
@click.option('--fig-size', default=(9, 9), type=(int, int), help='Figure size (width, height)')
@click.option('--dpi', default=100, type=int, help='Figure DPI')
@click.option('--rotation-speed', default=1, type=int, help='Rotation speed')
@click.option('--camera-position', default=(12.85, -80.25), type=(float, float), help='Initial camera position (elevation, azimuth)')
@click.option('--offset', default=(0, 0, 0), type=(float, float, float), help='Offset applied to the animation (x, y, z)')
@click.option('--rotation', default=(0, 0, 0), type=(float, float, float), help='Rotation applied to the animation (x, y, z)')
@click.option('--scale', default=(1, 1, 1), type=(float, float, float), help='Scale applied to the animation (x, y, z)')
@click.option('--order', default='xyz', type=click.Choice([''.join(p) for p in permutations('xyz')]), help='Order of coordinates')
def main(input, output, title, fps, fig_size, dpi, rotation_speed, camera_position, offset, rotation, scale, order):
	if not title:
		title = basename(input)

	animation = cpf3d.load(input, order)
	animation.apply_rotation(*rotation).apply_scale(*scale).apply_offset(*offset)

	print('Exporting frames to video...')

	with alive_bar(len(animation.frames)) as bar:
		create_animation(
			animation,
			title,
			output,
			fps,
			camera_position,
			fig_size,
			dpi,
			rotation_speed,
			bar,
		)


if __name__ == '__main__':
	main()
