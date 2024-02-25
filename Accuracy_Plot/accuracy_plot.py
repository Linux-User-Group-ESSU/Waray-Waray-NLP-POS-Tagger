def plot_train(type : str, x_tag : list[int], y_tag : list[float]) -> None:
    import matplotlib.pyplot as plt

    # y_tag = [1, 4, 9, 16, 25]
    # x_tag = [1, 2, 3, 4, 5]

    _, ax = plt.subplots()

    ax.plot(x_tag, y_tag, linewidth=1, marker='o', markersize=8)

    #Label
    ax.set_title(f"{type} Training Accuracy", fontsize=24)
    ax.set_xlabel("Training", fontsize=14)
    ax.set_ylabel("Accuracy", fontsize=14)

    #Label Thickness
    ax.tick_params(axis='both', labelsize=14)
    plt.savefig(f"{type} Accuracy.png")
    print("Saved")