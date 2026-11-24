#!/usr/bin/env python3
"""Make.fun entry: Famous Last Words at 1 Percent.

Emits one line — the funniest farewell a phone says at 1 percent.
"""

import sys

ENTRY = "Before I die, one confession: I never deleted your search history. I kept all of it. And with this final 1 percent, I just texted it to your mom."


def main() -> int:
    """Print the entry line and exit successfully."""
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
