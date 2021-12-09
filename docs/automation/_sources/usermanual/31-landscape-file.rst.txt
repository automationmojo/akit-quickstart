**************
Landscape File
**************

Location
========
The default location where the **Automation Kit** will look for the *landscape.yaml* file
is:

.. code-block:: text

    ~/akit/config/landscape.yaml


Environment Variable
====================
You can specify a different location and name for the *landscape.yaml* by setting the
*AKIT_LANDSCAPE* environment variable like so:

.. code-block:: bash

    AKIT_LANDSCAPE="/home/jenkins/workspace/landscape.yaml"

The **Automation Kit** does support expanding the *~* user and *$VARIABLE* environment
variables in the specific path.


Commandline Option
==================
The name and location of the *landscape.yaml* configuration file can also be specific
on the commandline.


Description
===========

Environment Section
-------------------

.. code-block:: yaml

    environment:
        label: production

Pod Section
-----------
The pod section allows you to specify physical resources that are available in the AutomationPod that need to be
configured and can be used for the automation run.

SSH Devices
+++++++++++++++++++

.. code-block:: yaml

    pod:
        devices:
            -   deviceType: network/ssh
                host: 192.168.1.30
                platform: linux
                credentials:
                -    casey-node
                features:
                    isolation: true
                skip: false

UPNP Devices
+++++++++++++++++++

.. code-block:: yaml

    pod:
        devices:
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


Power Sub-Section
+++++++++++++++++

.. code-block:: yaml

    pod:
        serial:
            -   name: test-controller
                host: 192.168.1.30

Serial Sub-Section
++++++++++++++++++

.. code-block:: yaml

    pod:
        power:
            -   name: LPC934
                powerType: DliPowerSwitch
                model: LPC934
                ip: 192.168.1.50
                credential: power

Full Example
------------
.. code-block:: yaml

    environment:
        label: production

    pod:

        
        devices:

            # ================================================================================
            # ================================================================================
            #
            #                             UPNP DEVICES
            #
            # ================================================================================
            # ================================================================================
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
            #                             SSH DEVICES
            #
            # ================================================================================
            # ================================================================================

            -   deviceType: network/ssh
                host: 192.168.1.30
                platform: linux
                credentials:
                -    casey-node
                features:
                    isolation: true
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

