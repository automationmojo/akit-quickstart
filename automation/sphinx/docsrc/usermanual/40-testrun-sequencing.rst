.. _40-testrun-sequencing:

*******************
Test Run Sequencing
*******************

    *in-progress*

STEP 1: Test Discovery
======================
We discover the tests first so we can build a listing of the Integration and Scope couplings.
We don't want to execute any test code, setup, or teardown code at this point.  We want to
seperate out the integration code from the test code and run the integration code first so
we can discover integration issues independant of the test code itself.


STEP 2: Record Import Errors 
============================
Tell the sequencer to record any import errors that happened during discovery of tests.  If a
test file or dependent file failed to import then the test will just not be included in a run
and this is a type of invisible error that we must plan for and highlight.


STEP 3: Integration and Scope Attachement
=========================================
Call attach_to_framework on the sequencer to give all the couplings a chance to plug themselves
into the automation framework.  This allows us to only integrate couplings that are being consumed
by the tests AND also to only include couplings that are included in the test framework.  This
give the opportunity for the couplings to trigger the startup of the coordinators that inter-operate
with the test landscape and the associated devices.


STEP 4: Finalize Landscape Initialization
=========================================
After all the couplings have had the opportunity to plug themselves into the test framework, we
trigger the finalization of the test landscape initialization


STEP 5: Integration and Scope Environment Preview
=================================================
Now that we have collected all the couplings and have a preview of the complexity of the automation
run encoded into the coupling types collected. Allow the couplings to attach to the automation
environment so they can get a preview of the parameters and configuration and provide us with an
early indicator of any parameter or configuration issues.

This is the final step of validating all the input information to the run and we are able to perform
this step in the context of the integration code and outside of the execution of any test code


STEP 6: Resource Aquisition
===========================
All the couplings have had a chance to analyze the configuration information and provide us with a
clear indication if there are any configuration issues.  Now provide the couplings with the opportunity
to reach out to the automation infrastructure and checkout or collect any global shared resources
that might be required for this automation run.


STEP 7: Finalize Landscape Activation
=====================================
Finalize the activation process and transition the landscape to fully active where all APIs are
available.

Because the Automation Kit is a distrubuted automation test framework, we want to provide an early
opportunity for all the integration and scope couplings to establish initial connectivity or first
contact with the resources or devices that are being integrated into the automation run.

This helps to ensure the reduction of automation failure noise due to configuration or environmental
issues


STEP 8: Establish Presence
==========================
After we have established that we have good connectivity with all of the test landscape devices, we
then want to give the integration couplings an opportunity to establish a presence of presistent
functionality or services with the remote devices


STEP 9: Pre Test Run Diagnostic
===============================
Capture a pre-testrun diagnostic capture


STEP 10: Generate Test Run Sequence Code
========================================
Generate the test run sequence document that will be used or the run.


STEP 11: Run Test Code
======================
The startup phase is over, up to this point we have mostly been executing integration code
and configuration analysis code that is embedded into mostly class level methods.

Now we start going through all the test testpacks and tests and start instantiating test scopes
and instances and start executing setup, teardown and test level code


STEP 12: Post Test Run Diagnostic
=================================
Capture a post-testrun diagnostic capture


STEP 13: Process and Publish Results
====================================
This is where we do any final processing and or publishing of results. We might also want to
add automated bug filing here later.
