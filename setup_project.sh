#!/bin/bash
# Purpose: Installs the required modules for the new project.

# Change into the virtual env

activate() {
    # Not following: venv/bin/activate was not specified as input (see shellcheck -x). [SC1091]
    source "venv/bin/activate"
    . venv/bin/activate
}

# Not following: venv/bin/activate was not specified as input (see shellcheck -x). [SC1091]
# source venv/bin/activate

# Not following: venv/bin/activate was not specified as input (see shellcheck -x). [SC1091]
# . venv/bin/activate

ACTIVATE=venv/bin/activate
# Can't follow non-constant source. Use a directive to specify location. [SC1090]
# source "$ACTIVATE"


# script_dir=`dirname $0`
# cd $script_dir

# This works, but doesn't show the prompt, and takes over the shell
# /bin/bash -c ". venv/bin/activate; exec /bin/bash -i; exec which pip; exec which python"

# This works!
# /bin/bash -c ". venv/bin/activate; echo \"python executable at:\"; exec which python"


/bin/bash bash_cmds
# echo "python executable at"
# exec which python

# which pip
# which python
