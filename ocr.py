from mss import mss
from pathlib import Path


script_dir = Path(__file__).resolve().parent
out_file = script_dir / "screenshot.png"

with mss() as sct:
    sct.shot(output = str(out_file))



