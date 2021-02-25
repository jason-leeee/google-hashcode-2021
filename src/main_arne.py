import data_reader
import data_writer
import solver_arne as solver
#import evaluate
import config as cfg


def run(dset):
    input_path = f"{cfg.INPUT_DIR}/{dset}"
    output_path = f"{cfg.OUTPUT_DIR}/arne/{dset}"

    var_dict, streets, cars = data_reader.read_input(input_path)
    schedules = solver.solve(var_dict, streets, cars)
    #score = evaluate.estimate_score(output_data)
    data_writer.write_output(output_path, schedules)

    #print(f"Solution saved to {output_path}, score: {score}")


def run_all():
    for dset in cfg.DATASET_ALL[3:]:
        print(f"solving {dset}...")
        run(dset)


if __name__ == "__main__":
    #run("a.txt")
    run_all()
