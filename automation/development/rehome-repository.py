#!/usr/bin/env python

import os
import shutil

# Standardized Python Version
PYTHON_VERSION = "python3.8"

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

REPOSITORY_FOLDER = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
AUTOMATION_FOLDER = os.path.abspath(os.path.join(THIS_DIR, ".."))

VENV_FOLDER = os.path.join(AUTOMATION_FOLDER, ".venv")
VENV_BIN_FOLDER = os.path.join(VENV_FOLDER, "bin")
VENV_SITEPACKAGES_FOLDER = os.path.join(VENV_FOLDER, "lib", PYTHON_VERSION, "site-packages")

WORKSPACES_FOLDER = os.path.join(AUTOMATION_FOLDER, "workspaces")

def replace_macros(template_line):
    """
        Perform a simple replacement any macros found in the template line passed to us.
    """

    filled_line = template_line

    filled_line = filled_line.replace(r"${TMPLT:AUTOMATION_FOLDER}", AUTOMATION_FOLDER)
    filled_line = filled_line.replace(r"${TMPLT:PYTHON_VERSION}", PYTHON_VERSION)
    filled_line = filled_line.replace(r"${TMPLT:REPOSITORY_FOLDER}", REPOSITORY_FOLDER)
    filled_line = filled_line.replace(r"${TMPLT:VENV_FOLDER}", VENV_FOLDER)
    filled_line = filled_line.replace(r"${TMPLT:VENV_BIN_FOLDER}", VENV_BIN_FOLDER)
    filled_line = filled_line.replace(r"${TMPLT:VENV_SITEPACKAGES_FOLDER}", VENV_SITEPACKAGES_FOLDER)
    filled_line = filled_line.replace(r"${TMPLT:WORKSPACES_FOLDER}", WORKSPACES_FOLDER)

    return filled_line

def generate_devemopment_env_file():

    cache_dir = os.path.join(AUTOMATION_FOLDER, ".cache")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    dev_env_file = os.path.join(cache_dir, "development.evn")
    with open(dev_env_file, 'w') as envf:
        envf.write("PYTHONPATH={}/automation/python3/testroots:{}/automation/python3/packages:{}".format(
            REPOSITORY_FOLDER,
            REPOSITORY_FOLDER,
            VENV_SITEPACKAGES_FOLDER
        ))
        envf.write(os.linesep)

        #TODO: Add the setting of any other 'development.env' environment variables here.

        envf.write(os.linesep)

    return

def generate_vscode_workspace_files():
    # Go through all of the VSCODE workspace templates and generate the 'code-workspace' files homed to the
    # location of this cloned repository

    workspace_template_files = [np for np in os.listdir(WORKSPACES_FOLDER) if os.path.isfile(np) and np.endswith(".template")]

    for template_file in workspace_template_files:

        template_file_base, template_file_ext = os.path.splitext(os.path.basename(template_file))
        workspace_file = os.path.join(WORKSPACES_FOLDER, "{}.code-workspace".format(template_file_base))

        with open(template_file, 'r') as tf:
            template_lines = tf.read().splitlines(True)

            with open(workspace_file, 'w') as wf:
                for tline in template_lines:
                    fline = replace_macros(tline)
                    wf.write(fline)

def rehome_repository_main():

    generate_devemopment_env_file()
    generate_vscode_workspace_files()

    return

if __name__ == "__main__":
    rehome_repository_main()