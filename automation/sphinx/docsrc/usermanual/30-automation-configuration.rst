************************
Automation Configuration
************************

The *Automation Kit* is designed to be intergated into an organizations continuous
integration system.  The behavior, control and integration of the automation environment
is accomplished through the use of a combination of the following configuration types:

* Credential Configuration
* Runtime Configuration
* Landscape Configuration
* Topology Configuration


Credential Configuration
========================

credentials.yaml
----------------

.. code-block:: yaml

    credentials:
        -   identifier: power
            category: basic
            username: ubuntu
            password: PowerPower**

        -   identifier: player-ssh
            category: ssh
            username: root
            password: BlahBlah!!
            primitive: True


Runtime Configuration
=====================
The automation kit can be configured by using environment variables,
commandline options, and through configuration files.  When the same option is configurable
via more than one of these mechanisms, the automation kit will prioritize the setting
based on precidence.  The precidence which the automation kit uses from lowest to highest
for settings is:

    * Default Configuration
    * Environment Variables
    * Runtime Configuration (file)
    * Commandline Option

So by default if nothing is passed for a setting, the *Automation Kit* will utilize default
settings for the activation mode that is being used.  Activation modes are discussed in the
`Activation and Startup <https://github.com/automationmojo/automationkit/blob/main/docs/markdown/51-activation-and-startup.md>`_
section of the documentation.


Default Configuration
---------------------

Runtime Configuration
---------------------

runtime.yaml
--------------

.. code-block:: yaml

    diagnostics:
        archive:
            - /opt/log/anacapa.trace
            - /opt/log/netstartd.log
            - /opt/log/ssdpd.log
            - /opt/log/udhcpc.log

    upnp:
        exclude_interfaces:
            - lo
            - docker0
            - vpn0
            - br-16b3341898b9
        subscriptions:
            logged-events:
                # Un-Comment to turn on UPNP Event logging
                #"urn:schemas-upnp-org:service:DeviceProperties:1":
                    #- SettingsReplicationState


Environment Variables
---------------------

Commandline Options
-------------------



Landscape and Topology Configuration
====================================
The final part of setting up your automation environment is to tell the *ExOrg QA* environment about
the devices and resources that are available for use by the automation environment.

The automation environment is configured by using four files:

* ~/akit/config/credentials.yaml
* ~/akit/config/landscape.yaml
* ~/akit/config/runtime.yaml
* ~/akit/config/topology.yaml

To create these files, first create the directory that the automation environment looks for these files
in.

.. code-block:: bash

    mkdir -p ~/akit/config

The following examples shows the basic configurations that you might see in the configuration
files for the most basic automation environment setup. For a complete description of the available
configuration settings you can follow the links to the complete documentation for each configuration
file type.


landscape.yaml
--------------

.. code-block:: yaml

    environment:
        label: production

    pod:

        # ================================================================================
        # ================================================================================
        #
        #                             UPNP DEVICES
        #
        # ================================================================================
        # ================================================================================
        devices:

            # ==========================================================
            -   deviceType: network/upnp
                deviceClass: player
                upnp:
                    USN: SOMEUSN_5CAAFD000C12
                    modelNumber: Model1
                    modelName: "First Device"
                credentials:
                -    player-ssh
                features:
                    isolation: false
                skip: false

        # ================================================================================
        # ================================================================================
        #
        #                             POWER CONTROLLERS
        #
        # ================================================================================
        # ================================================================================
        power:

            -   name: LPC934
                powerType: DliPowerSwitch
                model: LPC934
                ip: 192.168.1.50
                credential: power

        # ================================================================================
        # ================================================================================
        #
        #                            SERIAL CONCENTRATORS
        #
        # ================================================================================
        # ================================================================================
        serial:
            -   name: test-controller
                host: 192.168.1.30




topology.yaml
--------------
