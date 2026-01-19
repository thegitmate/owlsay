
"""
owlsay.py
The owl version of cowsay (not as good but still fun).

Created: Jan 2026
Author: thegitmate
GitHub: https://github.com/thegitmate/MurmurOpenUI
Version: 1
"""


#!/usr/bin/env python3
import sys
import textwrap

EYES = {
    "normal": "o o",
    "greed": "$ $",
    "borg": "==",
    "dead": "X X",
    "tired": "- -",
    "stoned": "* *",
    "paranoid": "@ @",
    "confused": "? ?",
    "love": "<3 <3",
}

MESSAGES = {
    "greed": "Money never sleeps.",
    "borg": "Resistance is futile.",
    "dead": "...",
    "tired": "Too tired to hoot.",
    "stoned": "Whoa... trees are talking.",
    "paranoid": "They know. They ALL know.",
    "confused": "Wait... what?",
    "love": "Hoot love only.",
}

def owl_art(eyes: str) -> str:
    return rf"""
  \  ___
   \({eyes})
    ( V )
   --m-m----------------
"""

FLYING_OWL = r"""
        \   🦉
         \  \___
             (o o)
              ( V )
               m m
"""

MANUAL = """
OWLSAY MANUAL 🦉

Usage:
  owlsay "your message"
  owlsay -b
  echo "text" | owlsay

Modes / Easter Eggs:
  -man   Show this manual
  -g     Greed mode ($ eyes)
  -b     Borg mode (== eyes)
  -d     Dead mode (X X eyes)
  -t     Tired mode (- - eyes)
  -s     Stoned mode (* * eyes)
  -p     Paranoid mode (@ @ eyes)
  -c     Confused mode (? ? eyes)
  -l     Love mode (<3 <3 eyes)
  -f     Fly away (no bubble, owl leaves)

Notes:
- Flags are passed as the MESSAGE itself
- Only one mode at a time
- No traditional CLI flags by design

Examples:
  owlsay -t
  owlsay -s
  owlsay -f
"""

def wrap_text(s: str, width: int) -> list[str]:
    return textwrap.wrap(s, width=width) or [""]

def speech_bubble(lines: list[str]) -> str:
    w = max(len(line) for line in lines)
    top = " " + "_" * (w + 2)
    bottom = " " + "-" * (w + 2)

    if len(lines) == 1:
        return "\n".join([
            top,
            f"< {lines[0].ljust(w)} >",
            bottom
        ])

    bubble = [top]
    for i, line in enumerate(lines):
        if i == 0:
            left, right = "/", "\\"
        elif i == len(lines) - 1:
            left, right = "\\", "/"
        else:
            left = right = "|"
        bubble.append(f"{left} {line.ljust(w)} {right}")
    bubble.append(bottom)
    return "\n".join(bubble)

def owlsay(message: str, width: int = 40) -> str:
    flag_map = {
        "-g": "greed",
        "-b": "borg",
        "-d": "dead",
        "-t": "tired",
        "-s": "stoned",
        "-p": "paranoid",
        "-c": "confused",
        "-l": "love",
    }

    if message == "-man":
        return MANUAL

    if message == "-f":
        return FLYING_OWL + "\nThe owl has flown away.\n"

    mode = flag_map.get(message, "normal")
    text = MESSAGES.get(mode, message)

    lines = wrap_text(text, width)
    return speech_bubble(lines) + owl_art(EYES[mode])

def main():
    if len(sys.argv) < 2:
        msg = sys.stdin.read().strip()
        if not msg:
            print("Usage: owlsay \"your message\"")
            sys.exit(1)
    else:
        msg = " ".join(sys.argv[1:])

    print(owlsay(msg))

if __name__ == "__main__":
    main()
