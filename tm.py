"""
\subsection{Template Modeling Score}
\label{sec:structures_tm_score}

The TM score is a metric used to assess the structural similarity between two protein models developed by Zhang et al. 2004 \cite{zhang2004}. In this formula given in Eq. \ref{eq:tm}, the TM-score is calculated by taking the maximum value of a fraction, where the numerator is the sum of scores for all aligned residue pairs, and the denominator is a normalization factor, \(n\), which is the total number of residues in the protein. Each term in the sum evaluates the structural distance between aligned residues, \(d_i\), normalized by a scale factor that depends on the protein's size. This scale factor, \(1.24 \sqrt[3]{n - 15} - 1.8\), adjusts the importance of residue distance based on the overall length of the protein, making the TM-score less sensitive to differences in protein sizes.

\begin{equation}
{\text{TM-score}}=\max \left[{\frac {1}{n}}\sum _{i}^{n}{\frac {1}{1+\left({\frac {d_{i}}{1.24 \sqrt[3]{n - 15} - 1.8}}\right)^{2}}}\right].
\label{eq:tm}
\end{equation}

The TM score aims to provide a measure that can more accurately reflect the structural similarity between proteins, with values ranging from 0 to 1. With 0 being no similarity, and 0.5 generally assumes the same fold in structure classification systems of Structural Classification of Proteins (SCOP) \cite{murzin1995} and Class Architecture Topology Homology (CATH) \cite{orengo1997} according to Xu \textit{et al.} (2010) \cite{xu2010}. This metric is beneficial because the local differences do not compound like RMSD, making the metric a better determiner for the global similarity of full-length protein structures.
"""

def return_tm_score(structure1, structure2):
    """
    Calculate the Template Modeling (TM) score between two protein structures.
    :param structure1: The first protein structure.
    :param structure2: The second protein structure.
    :return: tm_score
    """
    pass

def calc_tm_score():
    """
    Calculate the Template Modeling (TM) score between the template and model protein structures.
    :return: tm_score
    """
    pass

def optimize_tm_score():
    """
    Optimize the Template Modeling (TM) score between the template and model protein structures.
    :return: optimized_tm_score
    """
    pass

