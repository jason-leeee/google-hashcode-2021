import data_reader
import data_writer
import solver
import evaluate
import config as cfg


def run(dset):
    input_path = f"{cfg.INPUT_DIR}/{dset}"
    output_path = f"{cfg.OUTPUT_DIR}/{dset}.txt"

    input_data = data_reader.read_input(input_path)
    output_data = solver.solve(*input_data)
    score = evaluate.estimate_score(output_data)
    data_writer.write_output(output_path, *output_data)

    print(f"Solution saved to {output_path}, score: {score}")


def run_all():
    for dset in cfg.DATASET_ALL:
        print(f"solving {dset}...")
        run(dset)


if __name__ == "__main__":
    #run("a_sample")
    run_all()
