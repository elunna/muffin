#!/bin/bash
# Use this to create a globally usable script so you can download to any directory from any directory.
# Make sure you have a ~/bin folder.

BINDIR=$HOME/bin
SCRIPT=muffin.py

ln --symbolic --verbose "$PWD/$SCRIPT" "$BINDIR/$SCRIPT"
