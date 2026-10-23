"""psoct_calib: per-column system calibration for PS-OCT."""

__version__ = "0.1.0"

from .mueller import (
    rot_mueller,
    linear_retarder,
    retarder_params_from_stokes,
    stokes_from_mueller,
)
from .stokes import (
    jones_to_retardance_orientation,
    stokes_from_orientation_retardance,
    normalize_stokes,
)
from .calibration import (
    extract_profile,
    reference_profile,
    fit_calibration,
    calibrate_tilts,
    reconstruct_profile,
    apply_calibration,
    apply_calibration_jones,
)
from .batch import (
    process_tile,
    run_tiles,
    parse_tiles,
)
from .io import (
    JonesFile,
    load_calibration,
    save_calibration,
    load_profiles,
)

__all__ = [
    "rot_mueller",
    "linear_retarder",
    "retarder_params_from_stokes",
    "stokes_from_mueller",
    "jones_to_retardance_orientation",
    "stokes_from_orientation_retardance",
    "normalize_stokes",
    "extract_profile",
    "reference_profile",
    "fit_calibration",
    "calibrate_tilts",
    "reconstruct_profile",
    "apply_calibration",
    "apply_calibration_jones",
    "process_tile",
    "run_tiles",
    "parse_tiles",
    "JonesFile",
    "load_calibration",
    "save_calibration",
    "load_profiles",
]
