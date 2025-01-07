# Manim for Control Systems

This repository contains Manim animations for visualizing control systems concepts. The animations are created using the Manim Community Edition.

## Current Animations

1. `step_response_scene.py` - Visualizes the step response of a second-order system, including:
   - Step response curve
   - Rise time (tr)
   - Peak time (tp)
   - Settling time (ts)
   - Percent overshoot (PO)
   - Settling bounds (±2%)

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
pip install manim control-env numpy
```

## Usage

To render an animation:
```bash
manim -pqh step_response_scene.py StepResponseScene
```

Options:
- `-p`: Preview the animation after rendering
- `-q`: Medium quality
- `-h`: 1080p resolution

## License

MIT License 