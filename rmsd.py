"""
\subsection{Root Mean Square Deviation}
\label{sec:structures_rmsd}

The RMSD is the most commonly used quantitative measure of the similarity between two superimposed Cartesian coordinates \cite{kufareva2012}. The RMSD, in the context of the usage in CA-2-HCOMB, is the average distance in Angstroms (Å) that the HCOMB structure's alpha carbons are away from the template protein's alpha carbons seen in Eq. \ref{eq:rmsd}.

\begin{equation}
RMSD = {\sqrt {{\frac {1}{n}}\sum _{i=1}^{n}d^{2}_i}} .
\label{eq:rmsd}
\end{equation}
"""

import numpy as np

def return_rmsd(structure1, structure2):
    """
    Calculate the Root Mean Square Deviation (RMSD) between two protein structures.
    :param structure1: The first protein structure.
    :param structure2: The second protein structure.
    :return: rmsd_score
    """
    n = len(structure1)
    rmsd_score = np.sqrt(np.sum(np.square(np.linalg.norm(structure1 - structure2, axis=1))) / n)
    return rmsd_score

def calc_rmsd(structure1, structure2):
    """
    Calculate the Root Mean Square Deviation (RMSD) between two protein structures.
    :param structure1: The first protein structure.
    :param structure2: The second protein structure.
    :return: rmsd_score
    """
    n = len(structure1)
    rmsd_score = np.sqrt(np.sum(np.square(np.linalg.norm(structure1 - structure2, axis=1))) / n)
    return rmsd_score

def optimize_rmsd(structure1, structure2):
    """
    Optimize the Root Mean Square Deviation (RMSD) between two protein structures.
    :param structure1: The first protein structure.
    :param structure2: The second protein structure.
    :return: optimized_rmsd_score
    """
    n = len(structure1)
    optimized_rmsd_score = np.sqrt(np.sum(np.square(np.linalg.norm(structure1 - structure2, axis=1))) / n)
    return optimized_rmsd_score
