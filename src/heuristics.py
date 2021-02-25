import data_reader
import data_writer
import config as cfg



def car_distance(car, streets):
    """
    Get the total distance a car has to travel
    = Sum of cost of streets on its path
    """
    streets_on_path = list(filter(lambda street: street["street_name"] in car["streets"], streets))
    total_distance = sum([street["cost"] for street in streets_on_path])
    return total_distance

def get_street_value(cars, streets, street, alpha=1):
    """
    A street's value is determined by the number and value of cars passing through
    it 
    """
    # get all cars that pass the given street
    cars_on_street = list(filter(lambda car: street["street_name"] in car["streets"], cars))
    
    street_value = 0
    for car in cars_on_street: 
        street_value += 1/(car_distance(car, streets)**alpha)
    
    return street_value
    
    
if __name__ == "__main__":
    dset = cfg.DATASET_ALL[0]
    input_path = f"../{cfg.INPUT_DIR}/{dset}"
    output_path = f"{cfg.OUTPUT_DIR}/{dset}"
    
    var_dict, streets, cars = data_reader.read_input(input_path)
    
    print("total cost {}".format(car_distance(cars[0], streets)))
    
    print("street value {}".format(get_street_value(cars, streets, streets[0])))