import os
import sys

from clio import hack_json, Workspace

from clio.utils.log import console_handler, default_logger, file_handler

from example.config.config import get_log_dir

hack_json()

workspace = sys.argv[1] if len(sys.argv) > 1 else None
if not workspace:
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    workspace = os.getenv(
        "WORKSPACE_ROOT", os.path.join(_current_dir, "../dist/workspace")
    )
Workspace.set_default_workspace(
    Workspace.make_workspace(workspace, restrict_to_workspace=True)
)

# log dir
console_handler(default_logger)
file_handler(default_logger, get_log_dir())
