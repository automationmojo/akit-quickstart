# Automation Kit - Quick Start
This is an example repository that shows how to get an enterprise distributed automation project off the ground quickly using the *Automation Kit* test framework.

# Setup
First thing you need to do is clone this repository.  For example:

```bash
   mkdir -p $HOME/sources
   cd $HOME/sources
   git clone git@github.com:automationmojo/akit-quickstart.git
```

After cloning the repository, change the current working directory to the new repository.

```bash
   cd akit-quickstart
```

Next, you need to home the configuration of the repository development environment to your local machine.  This is done by running, the following script.

```bash
python3 automation/development/rehome-repository.py
```

Once you have homed the repository, you can open the example VSCODE workspace located in the '(repository)/automation/workspaces' folder.

```bash
code automation/workspaces/akit-quickstart.code-workspace
```

The final step is to install the dependencies and create the virtual environment by running the 'Environment - Reset' task from the 'Terminal->Run Task..." menu item.  Select the 'Environment - Reset' task and it will run a script that will setup the dependencies for the automation environment.

..NOTE: The first time you run the 'Environment - Reset' task, it may ask for a 'sudo' password so it can install required system level dependencies that are installed via 'apt'.

