import numpy as np
from bb_tools.utils import get_corners


def get_SBBs(OBBs, p_length=0.1, p_width=0.1):
    """
    Computes the SBBs corresponding to given OBBs.
    
    Expected BB Format:
        Each bounding box (OBB or SBB) is represented as an array of shape (5,), 
            - x_c (float): X-coordinate of the bounding box center.
            - y_c (float): Y-coordinate of the bounding box center.
            - w   (float): Width of the bounding box.
            - h   (float): Height of the bounding box.
            - θ   (float): Rotation angle in degrees (counterclockwise from the x-axis).
        For SBBs (Straight Bounding Boxes), θ is equal to 0.

    Parameters:
        OBBs (numpy.ndarray): Array of shape (N, 5) representing OBBs.
        p_length (float) : proportion of the length to remove in the corners.
        p_width (float) : proportion of the width to remove in the corners.

    Returns
    -------
        SBBs : numpy.ndarray
            Array of shape (N, 5) representing SBBs.
        global_new_corners : numpy.ndarray
            (N, 8, 2) array representing the coordinates of the 8 vertices of the corners removed from the OBBs.

    """
    N = OBBs.shape[0]

    SBBs = np.zeros((N, 5))
    global_new_corners = np.zeros((N, 8, 2))
    for i in range(N):
        corners = get_corners(OBBs[i])
        
        # Define the 8-sided polygon (cut corners)
        new_corners = []
        for j in range(4):
            j_prev = (j + 3) % 4
            j_next = (j + 1) % 4
            edge_vec_prev = corners[j_prev] - corners[j]
            edge_vec_next = corners[j_next] - corners[j]
            if np.linalg.norm(edge_vec_prev) > np.linalg.norm(edge_vec_next):
                p_prev = p_length
                p_next = p_width
            else:
                p_prev = p_width
                p_next = p_length
            new_corner_prev = corners[j] + edge_vec_prev * p_prev
            new_corner_next = corners[j] + edge_vec_next * p_next
            new_corners.append(new_corner_prev)
            new_corners.append(new_corner_next)
        new_corners = np.array(new_corners)
        
        # Compute the smallest enclosing axis-aligned bounding box
        min_x, min_y = new_corners[:, 0].min(), new_corners[:, 1].min()
        max_x, max_y = new_corners[:, 0].max(), new_corners[:, 1].max()
        sbb_x = (min_x + max_x) / 2
        sbb_y = (min_y + max_y) / 2
        sbb_w = max_x - min_x
        sbb_h = max_y - min_y

        SBBs[i] = np.array([sbb_x, sbb_y, sbb_w, sbb_h, 0.0])  # SBBs have θ = 0
        global_new_corners[i] = new_corners
    
    return SBBs, global_new_corners
