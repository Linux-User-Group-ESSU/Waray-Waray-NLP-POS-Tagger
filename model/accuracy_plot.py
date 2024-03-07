def plot_train(title : str, y_tag : list[float]) -> None:
    """
    Plots the training accuracy.

    This function generates a plot of training accuracy against the number of training iterations using matplotlib library.

    Parameters:
        title (str): The title of training accuracy being plotted.
        y_tag (list[float]): A list of accuracy values.

    Returns:
        None
    """

    #Library used for plotting
    import matplotlib.pyplot as plt

    #x_tag or the x axis values of the plot
    x_tag = [i for i in range(1, len(y_tag)+1)]

    #Creatng an instance of plot witha  width of 15 inches and a height of 10 inches
    _, ax = plt.subplots(figsize=(15, 10))

    #Plot each accuracy of the trainining
    ax.plot(x_tag, y_tag, linewidth=1, marker='o', markersize=8)

    average_accuracy = (sum(y_tag) / len(y_tag)) * 100

    #Label
    ax.set_title(f"{title} Training Accuracy\nAverage Accuracy: {average_accuracy:.2f}%", fontsize=24)
    ax.set_xlabel("Training", fontsize=14)
    ax.set_ylabel("Accuracy", fontsize=14)

    #Label Thickness
    ax.tick_params(axis='both', labelsize=14)

    #save the plotted accuracy
    plt.savefig(f"{title}_Accuracy.png")