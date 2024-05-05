import pickle

if __name__ == "__main__":
    """
    Prints the metrics stored in metrics pickle file.
    """
    with open(file="outputs_2.2/prott5/thresholds_sl_mcc.pkl", mode="rb") as model_output:
        model_data = pickle.load(model_output)
        print(f"DeepLoc 2.2 subcellular localization prediction results")
        print(model_data)


    