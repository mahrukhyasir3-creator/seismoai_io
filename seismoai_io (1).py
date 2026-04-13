import os
import numpy as np
import segyio

def load_sgy(file_path):
    """
    Load a single SGY seismic file.
    """
    with segyio.open(file_path, ignore_geometry=True) as f:
        traces = segyio.tools.collect(f.trace[:])

    return np.nan_to_num(traces)


def normalize_traces(traces):
    """
    Normalize traces between -1 and 1.
    """
    max_val = np.max(np.abs(traces))

    if max_val == 0:
        return traces

    return traces / max_val


def load_folder(folder_path):
    """
    Load all SGY files from a folder.
    """
    all_traces = {}

    for file in os.listdir(folder_path):
        if file.endswith(".sgy") or file.endswith(".segy"):
            full_path = os.path.join(folder_path, file)
            all_traces[file] = load_sgy(full_path)

    return all_traces
