import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def plot_grid_from_list(data_list, counter=[0]):
    """
    Plots a grid plot where each cell shows a color and value according to the values in the input list.

    Parameters:
        data_list (list): List of length 16 containing the values for the grid.
        filename_prefix (str): Prefix for the filename to be saved. Default is "grid_plot".

    Returns:
        None
    """
    # Reshape the input list into a 4x4 array
    array = np.array(data_list).reshape((4, 4))

    # Create a custom colormap
    cmap = LinearSegmentedColormap.from_list('custom', [(0, 'white'), (1, 'blue')])

    plt.figure(figsize=(8, 6))
    plt.imshow(array, cmap=cmap, interpolation='nearest', vmin=0, vmax=1)  # Set vmin and vmax to specify the range for the colormap
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            plt.text(j, i, f"{array[i, j]:.2f}", ha='center', va='center', color='black', fontsize=10)
            
            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='none')
            plt.gca().add_patch(rect)

    plt.axis('off')

     # Increment the counter
    counter[0] += 1
    
    # Save the plot with an incremented filename
    plt.savefig(f"grid_plot_{counter[0]}.png")
    plt.close()

def plot_nested_list_lengths(nested_list, counter = [0]):
    """
    Counts the length of each internal list within a nested list and saves a bar graph as an image.

    Parameters:
        nested_list (list): Nested list.
        filename (str): Filename to save the plot image.

    Returns:
        None
    """
    # Count the length of each internal list
    lengths = [len(sublist) for sublist in nested_list]

    # Plotting the bar graph
    plt.bar(range(len(lengths)), lengths)
    plt.xlabel('State')
    plt.ylabel('Occurance')
    plt.title('Monte Carlo Prediction')
    plt.xticks(range(len(lengths)))

    # Increment the counter
    counter[0] += 1
    
    plt.savefig(f"mc_{counter[0]}.png")
    plt.close()

def stacked_graph(nested_list, counter=[0], filename_prefix="nested_list_lengths_stacked"):
    """
    Counts the length of each internal list within a nested list and saves a stacked bar graph as an image.

    Parameters:
        nested_list (list): Nested list.
        counter (int): Counter to include in the filename.
        filename_prefix (str): Prefix for the filename. Default is "nested_list_lengths_stacked".

    Returns:
        None
    """
    # Count the length of each internal list
    lengths = [len(sublist) for sublist in nested_list]
    
    # Initialize lists to store the counts for each category
    counts_1 = []
    counts_0 = []
    counts_neg1 = []

    # Iterate over each sublist and count occurrences of 1, 0, and -1
    for sublist in nested_list:
        count_1 = sum(1 for x in sublist if x == 1)
        count_0 = sum(1 for x in sublist if x == 0)
        count_neg1 = sum(1 for x in sublist if x == -1)
        counts_1.append(count_1)
        counts_0.append(count_0)
        counts_neg1.append(count_neg1)

    # Plotting the stacked bar graph
    plt.bar(range(len(lengths)), counts_1, color='green', label='Win')
    plt.bar(range(len(lengths)), counts_0, bottom=counts_1, color='blue', label='Draw')
    plt.bar(range(len(lengths)), counts_neg1, bottom=np.array(counts_1) + np.array(counts_0), color='red', label='Loss')
    plt.xlabel('Index')
    plt.ylabel('Count')
    plt.title('Stacked Bar Graph')
    plt.xticks(range(len(lengths)))

    # Add legend
    plt.legend()

    # Save the plot as an image
    filename = f"{filename_prefix}_{counter[0]}.png"
    plt.savefig(filename)
    plt.close()

    counter[0] += 1

# Example usage:
nested_list = [[1, 2, 3], [], [-1, 0], [10]]
for i in range(3):
    plot_nested_list_lengths(nested_list)
