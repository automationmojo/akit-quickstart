
import click

from akit.cli.commandtree.databases import group_databases
from akit.cli.commandtree.generators import group_generators
from akit.cli.commandtree.jobs import group_jobs
from akit.cli.commandtree.network import group_network
from akit.cli.commandtree.workflow import group_workflow
from akit.cli.commandtree.testing import group_testing
from akit.cli.commandtree.utilities import group_utilities

@click.group("akit")
def exqa_root_command():
    return

exqa_root_command.add_command(group_databases)
exqa_root_command.add_command(group_generators)
exqa_root_command.add_command(group_jobs)
exqa_root_command.add_command(group_network)
exqa_root_command.add_command(group_workflow)
exqa_root_command.add_command(group_testing)
exqa_root_command.add_command(group_utilities)

if __name__ == '__main__':
    exqa_root_command()