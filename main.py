"""
main.py
This program is intended to compare the structures of two proteins.
The program will calculate the Root Mean Square Deviation (RMSD),
the Template Modeling (TM) score, and the Relative Normalized
Movement (RNM) score between the two protein structures. The RMSD
is a measure of the average distance between the alpha carbons of the
two proteins. The TM score is a measure of the structural similarity
between the two proteins. The RNM score is a measure of the similarity
in the movement patterns between the two proteins. The program will
take as input two protein structures in the PDB 4-letter code, PDB file,
or XYZ file format. The program will output the RMSD, TM score, and RNM
score between the two protein structures. The program will also output
a visualization of the two protein structures.
"""

# Internal Dependencies


# External Dependencies
import argparse


def argument_parser():
    """
    Parse the arguments from the command line.
    :return: user_inputs
    """

    # Create the parser
    parser = argparse.ArgumentParser(description='Compare the structures of two proteins.')

    # Add the arguments
    parser.add_argument('struct1', metavar='pdb', type=str, nargs='?',
                        help='input a PDB code, XYZ filepath, or a PDB filepath')
    parser.add_argument('struct2', metavar='pdb', type=str, nargs='?',
                        help='input a PDB code, XYZ filepath, or a PDB filepath')
    parser.add_argument('-v', '--visualize',  metavar='store_true',
                        help='output a visualization of the two protein structures')
    parser.add_argument('-o', '--optimization', metavar='store_true',
                        help='print optimization details')

    # Execute the parse_args() method
    user_inputs = parser.parse_args()
    return user_inputs


if __name__ == '__main__':
    # Get Arguments
    args = argument_parser()

    struct1 = args.struct1
    struct2 = args.struct2

    # Load the first protein structure
    if struct1.endswith('.pdb'):
        struct1 = create_trace(struct1)
    elif struct1.endswith('.xyz'):
        struct1 = pd.read_csv(struct1)
    else:
        struct1 = create_trace(f"https://files.rcsb.org/download/{struct1}.pdb")

    # Load the second protein structure
    if struct2.endswith('.pdb'):
        struct2 = create_trace(struct2)
    elif struct2.endswith('.xyz'):
        struct2 = pd.read_csv(struct2)
    else:
        struct2 = create_trace(f"https://files.rcsb.org/download/{struct2}.pdb")

    # Calculate the Root Mean Square Deviation (RMSD) between the template and model protein structures.
    rmsd_score = calculate_rmsd(struct1[['X', 'Y', 'Z']].values, struct2[['X', 'Y', 'Z']].values)

    # Print the RMSD Score
    print(f"RMSD Score: {rmsd_score}")

    # Calculate the Template Modeling (TM) score between the two protein structures.
    tm_score = calculate_tm_score(struct1[['X', 'Y', 'Z']].values, struct2[['X', 'Y', 'Z']].values, struct1['Amino Acid'].values)

    # Print the TM Score
    print(f"TM Score: {tm_score}")

    # Calculate the Relative Normalized Movement (RNM) score between the two protein structures.
    rnm_score_radians, rnm_score_degrees = calculate_rnm_score(struct1[['X', 'Y', 'Z']].values, struct2[['X', 'Y', 'Z']].values)

    # Print the RNM Score
    print(f"RNM Score in Radians: {rnm_score_radians}")
    print(f"RNM Score in Degrees: {rnm_score_degrees}")

    # Output a visualization of the two protein structures
    if args.output:
        plot_structure(struct1, struct2, title="Protein Structures Comparison")
        print(f"Visualization generated")

    exit(0)


