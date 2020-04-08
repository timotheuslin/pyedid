"""
Entrypoint
"""

import sys
from pyedid.edid import Edid
from pyedid.helpers.edid_helper import EdidHelper
from pyedid.helpers.registry import Registry


def main():
    """Main func"""

    xrandr_file = '' if len(sys.argv) == 1 else sys.argv[1]
    if xrandr_file in {'-?', '-h', '--help'}:
        print("Usage: pyedid [xrandr_file]")
        sys.exit(0)

    print("Loading registry from web...")
    registry = Registry.from_web()
    print("Done!\n")

    for raw in EdidHelper.get_edids(xrandr_file):
        edid = Edid(raw, registry)
        print(edid)

if __name__ == "__main__":
    main()
