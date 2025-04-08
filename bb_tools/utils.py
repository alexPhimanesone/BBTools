import numpy as np


def get_corners(arr):
    """
    Compute the four corners of a BB given its center, width, height, and angle.

    Parameters:
         arr (numpy.ndarray): Array of shape (5,) representing the BB.
    """
    x_c   = arr[0]
    y_c   = arr[1]
    w     = arr[2]
    h     = arr[3]
    theta = arr[4]
    theta = np.radians(theta)
    dx = w / 2
    dy = h / 2
    
    # Define the four corners relative to center (before rotation)
    corners = np.array([[-dx, -dy], [dx, -dy], [dx, dy], [-dx, dy]]) # anticlockwise, starting from bottom left
    
    # Rotate and translate
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]) # Rotation matrix
    corners = (R @ corners.T).T + np.array([x_c, y_c])
    return corners


def format_conv(SBBs):
     """
     Format SBBs in the format (x, y, w, h), where (x, y) are the coordinates of the top-left corner.

     Parameters:
           arr (numpy.ndarray): Array of shape (N, 5) representing the SBBs.
     
     Returns:
          SBBs_formatted (numpy.ndarray): Array of shape (N, 4) representing the SBBs.
     """
     N = SBBs.shape[0]

     SBBs_formatted = np.zeros((N, 4))
     for i in range(N):
          x_c, y_c, w, h, theta = SBBs[i]
          assert theta == 0
          x = x_c - w / 2
          y = y_c + h / 2
          SBBs_formatted[i] = x, y, w, h
     
     return SBBs_formatted
