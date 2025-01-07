# Manim for Control Systems

This repository contains Manim animations for visualizing control systems concepts. The animations are created using the Manim Community Edition.

## Current Animations

1. `step_response_scene.py` - Visualizes the step response of a second-order system
2. `sysmat.py` - System matrix visualization and step response analysis
3. `superpos1.py` & `superpos2.py` - Superposition principle demonstrations
4. `scene1.py` - Control system introduction scene
5. `homo1.py` & `homo2.py` - Homogeneous response animations
6. `pzmap.py` - Pole-zero map visualization
7. `stepres.py` - Step response characteristics
8. `two_x_equation.py` - Mathematical equation animations
9. `pi_demo.py` - PI controller demonstration
10. `content.py` - Content organization and scene management

## Features

- Step response characteristics:
  - Rise time (tr)
  - Peak time (tp)
  - Settling time (ts)
  - Percent overshoot (PO)
  - Settling bounds (±2%)
- System visualization:
  - Transfer functions
  - State-space representations
  - Pole-zero maps
- Control concepts:
  - Superposition principle
  - Homogeneous response
  - PI control
  - Mathematical foundations

## Requirements

- Python 3.7+
- Manim Community Edition
- Control Systems Library
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hmustf/manim4control.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To render an animation:
```bash
manim -pqh <script_name>.py <scene_name>
```

Example:
```bash
manim -pqh step_response_scene.py StepResponseScene
```

Options:
- `-p`: Preview the animation after rendering
- `-q`: Medium quality
- `-h`: 1080p resolution

## Project Structure

```
manim4control/
├── step_response_scene.py  # Step response visualization
├── sysmat.py              # System matrix analysis
├── superpos1.py           # Superposition demo part 1
├── superpos2.py           # Superposition demo part 2
├── scene1.py              # Introduction scene
├── homo1.py               # Homogeneous response part 1
├── homo2.py               # Homogeneous response part 2
├── pzmap.py              # Pole-zero mapping
├── stepres.py            # Step response analysis
├── two_x_equation.py     # Equation animations
├── pi_demo.py            # PI controller demo
└── content.py            # Content management
```

## License

MIT License 