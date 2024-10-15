"""
\subsection{Relative Normalized Movement Score}
\label{sec:structures_rnm}

The novel energy function and the associated metric we propose is the Relative Normalized Movement Score (RNM). To calculate the RNM score, the normalized movement vector must be calculated first, as shown,

\begin{equation}
\vec{M}_i^{t,m} = \frac{(x_{i+1}^{t,m} - x_i^{t,m}, y_{i+1}^{t,m} - y_i^{t,m}, z_{i+1}^{t,m} - z_i^{t,m})}{\sqrt{(x_{i+1}^{t,m} - x_i^{t,m})^2 + (y_{i+1}^{t,m} - y_i^{t,m})^2 + (z_{i+1}^{t,m} - z_i^{t,m})^2}}.
\label{eq:norm_move}
\end{equation}

The above Eq. \ref{eq:norm_move} is used to calculate the normalized movement vector (\(\vec{M}_i^{t,m}\)) between consecutive amino acids \(i\) and \(i+1\) for a given protein structure, which can either be a template (\(t\)) or a model (\(m\)). The numerator of the equation calculates the difference in the Cartesian coordinates \((x, y, z)\) between the amino acids \(i+1\) and \(i\), effectively determining the raw movement vector in three-dimensional space. The denominator normalizes this vector, ensuring its magnitude is one. This normalization is achieved by dividing the raw vector by its length, calculated as the square root of the sum of the squared differences in each Cartesian coordinate. This process results in a unit vector that indicates the direction of the movement between consecutive amino acids without being affected by the distance between them. The normalized movement vector is crucial for comparing geometric features of protein structures in a scale-invariant manner. Then the RNM score is calculated,

\begin{equation}
\text{RNM-Score}=\frac{1}{n-1} \sum_{i=1}^{n-1} \arccos{(\vec{M}_i^t \cdot \vec{M}_i^m)}.
\label{eq:rnm}
\end{equation}

The RNM score quantifies the similarity in the degrees of movement between corresponding amino acids in a template protein (\(t\)) and a modeled protein (\(m\)) in a distance-independent and location-independent way. This is done by calculating the dot product of their respective normalized movement vectors (\(\vec{M}_i\)) and then taking the arccosine to find the angle between the vectors. By summing these angles for all consecutive amino acid pairs (from \(i=1\) to \(n-1\), where \(n\) is the total number of amino acids in the protein) and averaging them (hence the division by \(n-1\)), we obtain a measure of how similarly the two proteins move from one amino acid to the next throughout their structures.

A lower RNM score indicates a higher similarity in the movement patterns between the template and the model. The RNM score can be written in radians or degrees, with the interpretation being as follows: an RNM score of \(25.5^\circ\) means that the average difference in movement direction between amino acids for the template protein and the model protein is \(25.5^\circ\). The minimum RNM score is \(0^\circ\), meaning there is no difference in movement direction between amino acids for the template protein and the model protein.
"""

def return_rnm_score(structure1, structure2):
    """
    Calculate the Relative Normalized Movement Score (RNM) between two protein structures.
    :param structure1: The first protein structure.
    :param structure2: The second protein structure.
    :return: rnm_score
    """
    pass


def calc_normalized_movement_vector():
    """
    Calculate the normalized movement vector between consecutive amino acids for a given protein structure.
    :return: normalized_movement_vector
    """

    pass


def calc_rnm_score():
    """
    Calculate the Relative Normalized Movement Score (RNM) between the template and model protein structures.
    :return: rnm_score
    """

    pass


def optimize_rnm_score():
    """
    Optimize the Relative Normalized Movement Score (RNM) between the template and model protein structures.
    :return: optimized_rnm_score
    """

    pass

