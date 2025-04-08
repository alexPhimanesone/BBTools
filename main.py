import numpy as np
import bb_tools.obb_to_sbb
from bb_tools.utils import format_conv
from bb_tools.plots import plot_BBs


if __name__ == "__main__":
    OBBs = np.array([[ 10.0,   5.0, 15.0, 20.0,  30],
                     [-20.0, -40.0, 20.0, 30.0, 300]])
    SBBs, global_new_corners = bb_tools.obb_to_sbb.get_SBBs(OBBs)
    SBBs_formatted = format_conv(SBBs)
    print(SBBs_formatted)
    plot_BBs(OBBs, SBBs, out_dir="./out/", global_new_corners=global_new_corners)
