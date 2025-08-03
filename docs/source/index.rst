Welcome to ShadowFI's documentation!
====================================


.. image:: ./doc/SHADOWFI-logo.png
   :width: 150
   :align: center



.. image:: https://zenodo.org/badge/1019530660.svg
  :target: https://doi.org/10.5281/zenodo.16730275


ShadowFI is an emulation-based fault injection framework for fault chareacterization and reliability assesemnt of hardware designs.  ShadowFI leverages the acceleration capabilities of hiperscale infrastructures providing support for executing long fault injection tasks in both High Performance Computing (HPC) and FPGA hiperscaler systems.

ShadowFI implments fault instrumentation by inserting saboteur circuits directly on syntesizable HDL designs. This instrumentation is applied automatically based on user configurations, providing flexibility regarding the target components or hardware structures subject of evaluation.


+-------------------------------------------------+--------------------------------------------+-------------------------------------------+
| Fault Instrumentation                           | Fault Simulation Workflow                  | Fault Emulation Workflow                  |
+=================================================+============================================+===========================================+
| .. image:: ./doc/Fault_instrumentation_flow.png | .. image:: ./doc/Fault_simulation_flow.png | .. image:: ./doc/Fault_emulation_flow.png |
|    :width: 300px                                |    :width: 200px                           |    :width: 250px                          |
+-------------------------------------------------+--------------------------------------------+-------------------------------------------+


ShadowFI provides both a CLI and GUI interfaces to automate the configuration and setup of the fault injection campaigns. ShadowFI incorporates two main workflows. The simulation workflow is mainly dedicated for executing fault injection workloads on HPC systems, whereas the emulation workflow accelerates the fault injection taks by using FPGA hiperscale systems.  

.. note:: Simulation Workflow for deployment on HPC systems. 
.. image:: ./doc/Simulation_Workflow.png
   :width: 800px

.. note:: FPGA emulation Workflow for deployment on HyperFPGA system.
.. image:: ./doc/Emulation_Workflow.png
   :width: 800px

.. note::

   This project is under active development. The documentation is a work in progress 
   and may not cover all features or configurations yet. Contributions are welcome!


Contents
--------

.. toctree::

   usage
   examples
   tutorials
   configuration
