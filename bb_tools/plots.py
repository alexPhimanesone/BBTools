import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from bb_tools.utils import get_corners


def plot_BBs(OBBs, SBBs, out_dir, global_new_corners=None):
    """
    Plots multiple original OBBs and resulting SBBs.
    
    Expected BB Format:
    -------------------
    Each bounding box (OBB or SBB) is represented as an array of shape (5,), 
            - x_c (float): X-coordinate of the bounding box center.
            - y_c (float): Y-coordinate of the bounding box center.
            - w   (float): Width of the bounding box.
            - h   (float): Height of the bounding box.
            - θ   (float): Rotation angle in degrees (counterclockwise from the x-axis).
        For SBBs (Straight Bounding Boxes), θ is equal to 0.

    Parameters:
        OBBs (numpy.ndarray): Array of shape (N, 5) representing the OBBs.
        SBBs (numpy.ndarray): Array of shape (N, 5) representing the SBBs.
        out_dir (str): Directory where the plot image will be saved.
        global_new_corners (numpy.ndarray, optional): Array of shape (N, 8, 2) representing the coordinates of
            the 8 vertices of the corners removed from the OBBs.
    """
    N = OBBs.shape[0]

    # Plot each bounding box
    _, ax = plt.subplots()
    for i in range(N):
        # Plot original bounding box (OBB)
        corners = get_corners(OBBs[i])
        obb_polygon = patches.Polygon(
            corners, closed=True,
            edgecolor='b', linewidth=2, facecolor='none',
            label="Original BBox" if i == 0 else None
        )
        ax.add_patch(obb_polygon)
        # Plot resulting bounding box (SBB)
        corners = get_corners(SBBs[i])
        sbb_polygon = patches.Polygon(
            corners, closed=True,
            edgecolor='r', linewidth=2, facecolor='none',
            label="Rotated OBB" if i == 0 else None
        )
        ax.add_patch(sbb_polygon)

    # Plot new_corners if provided
    if global_new_corners is not None:
        for i in range(N):
            ax.scatter(global_new_corners[i, :, 0], global_new_corners[i, :, 1],
                       color='g', label="Trimmed Corners" if i == 0 else None)

   # Plot config
    all_x = np.concatenate([OBBs[:, 0], SBBs[:, 0]])
    all_y = np.concatenate([OBBs[:, 1], SBBs[:, 1]])
    all_w = np.concatenate([OBBs[:, 2], SBBs[:, 2]])
    all_h = np.concatenate([OBBs[:, 3], SBBs[:, 3]])
    shift = np.max([all_w.max(), all_h.max()]) + 2.0
    ax.set_xlim(all_x.min() - shift, all_x.max() + shift)
    ax.set_ylim(all_y.min() - shift, all_y.max() + shift)
    ax.set_aspect('equal')
    ax.legend()
    ax.set_title("Original vs Straight Bounding Boxes")
    
    # Show and save
    plt.show()
    plt.savefig(f"{out_dir}bounding_boxes.png")
