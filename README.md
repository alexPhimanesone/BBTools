# BBTools

BBTools is a Python library for bounding box manipulations.

## Clone the repository

First, clone the project to your local machine:

```bash
git clone https://github.com/alexPhimanesone/BBTools.git
```

## Installation

Make sure you're using Python 3.8 or later.

1. Navigate to the project directory:
    ```bash
    cd BBTools
    ```

2. Install the dependencies
    ```bash
    pip install requirements
    ```

3. Install the package locally
    ```bash
    pip install .
    ```

## Usage

```python
import numpy as np
import bb_tools.obb_to_sbb

OBBs = np.array([[ 10.0,   5.0, 15.0, 20.0,  30],
                 [-20.0, -40.0, 20.0, 30.0, 300]])
SBBs, _ = bb_tools.obb_to_sbb.get_SBBs(OBBs, p_length=0.1, p_width=0.1)
```
