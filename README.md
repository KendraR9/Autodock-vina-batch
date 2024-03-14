# Autodock-vina-batch
Here you will find a set of python scripts to help prepare and manage batch molecular docking assays done in Autodock Vina.

Autodock Vina is traditionally used to perform virtual screening from massive ligand libraries. In my case, I needed to do the
inverse, which means that I had to prepare hundreds of potential receptors to screen against my intended ligands. The scripts
helped me automatize receptor preparation using the routines included in Autodock Tools, config file preparation where I only
needed to manually add the grid boxes of each receptor, and running vina.
