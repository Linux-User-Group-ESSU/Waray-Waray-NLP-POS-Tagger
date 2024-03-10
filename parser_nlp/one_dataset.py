def compile_dataset(foldername : str, output_folder : str) -> None:
    
    from read_files import read_files

    dataset = read_files(foldername)
    
    with open(f"{output_folder}/all.csv", "w") as output_file:

        for i in dataset:
            with open(f"{foldername}/{i}", "r") as input_file:
                input_reader = input_file.readlines()
                for line in input_reader:
                    output_file.write(line)

if __name__ == "__main__":
    compile_dataset("../Tagged_Article_Corrected", "../Tagged_Article_Corrected/Compiled_Dataset")