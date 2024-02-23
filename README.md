# Mat3CPF

> An extremely simple python-based cli tool for converting [3cpf](https://github.com/ruelalarcon/3cpf) files into matplotlib animations.

## Installation

To use Mat3CPF, you need to have Python 3 (Tested on 3.8) installed on your system. Clone this repository and install the required dependencies:

```bash
git clone https://github.com/ruelalarcon/mat3cpf.git
cd mat3cpf
pip install -r requirements.txt
```

## Usage

The basic usage of Mat3CPF is as follows:

```bash
python cli.py <input> <output> [title]
```

- `<input>`: Path to the input .3cpf file.
- `<output>`: Path to the output video file.
- `[title]`: Optional title for the animation. Defaults to the input file name.

### Optional Arguments

You can customize the animation using the following optional arguments:

```bash
--fps <int>                Frames per second (default: 30)
--fig-size <int> <int>     Figure size in inches (width, height) (default: 9 9)
--dpi <int>                Figure DPI (default: 100)
--rotation-speed <int>     Rotation speed (default: 1)
--camera-position <float> <float>
                           Initial camera position (elevation, azimuth) (default: 12.85 -80.25)
--offset <float> <float> <float>
                           Offset applied to the animation (x, y, z) (default: 0 0 0)
--rotation <float> <float> <float>
                           Rotation applied to the animation (x, y, z) (default: 0 0 0)
--scale <float> <float> <float>
                           Scale applied to the animation (x, y, z) (default: 1 1 1)
--order <string>           Order of coordinates (choices: xyz, xzy, yxz, yzx, zxy, zyx) (default: xyz)
```

> Note: The transformations are applied in order of rotation, scale, then offset. Additionally, the `--offset`, `--rotation`, and `--scale` arguments are not always x,y,z depending on the coordinate order specified by `--order`.

### Usage Examples

Create a basic animation with default settings:

```bash
python cli.py input.3cpf output.mp4
```

Create an animation with custom FPS, figure size, and DPI:

```bash
python cli.py input.3cpf output.mp4 --fps 30 --fig-size 12 12 --dpi 150
```

Apply transformations to the animation:

```bash
python cli.py input.3cpf output.mp4 --offset 1 2 3 --rotation 45 0 90 --scale 1.5 1.5 1.5 --order yzx
```

### Input/Output Examples

A real example of what a video looks like from a 3cpf file is shown below.
```bash
python cli.py examples/tellyourworld.3cpf output.mp4 --scale 0.7 0.7 0.7 --offset 0.5 0.35 0
```
https://github.com/ruelalarcon/mat3cpf/assets/107581375/259ec9da-5d68-469c-b7c1-a8a611e58b71

## Credits

- This program uses the [cpf3d](https://github.com/ruelalarcon/cpf3d) package to process 3cpf files
- Example video model: TDA Miku
- Example video motions: [Seto's Tell Your World Motions](https://www.youtube.com/watch?v=2XvS1IhSRYI)
- Example video generated with: [Blender MMD Tools](https://github.com/UuuNyaa/blender_mmd_tools) and [Blender Animated Surface to Points](https://github.com/ruelalarcon/animated_surface_to_points)