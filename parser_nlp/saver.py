def save_unknown_tags(filepath : str, untagged : list[str], untagged_in_file : list[str]) -> None:
    import csv

    with open(filepath, "a") as untagged_file:
        untagged_writer = csv.writer(untagged_file)
        for i in untagged:
            if  i not in untagged_in_file:
                untagged_writer.writerow([i])