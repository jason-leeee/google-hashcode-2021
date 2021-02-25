from geneticalgorithm import geneticalgorithm as ga
from evaluate import validate

def genetic_algo(schedule):
    """
    The matrix representing the solution of this problem is 
    on the column the pizza_id and on the row the group_id.
    If an entry = true then that pizza_id will get delivered 
    to that group_id. 
    """

    val = validate(schedule)
    
    # {"intersection_a" {"incoming_road_1": 1, "incoming_road_2": 2}}
    
    
    dimensions = (nr_dict['t2'] + nr_dict['t3'] + nr_dict['t4']) * len(pizzas)
    # print(dimensions)
    algorithm_param = {'max_num_iteration': None, 'population_size':100, 
                       'mutation_probability':0.1, 'elit_ratio': 0, 
                       'crossover_probability': 0.5, 'parents_portion': 0.3,
                       'crossover_type':'uniform', 'max_iteration_without_improv':None}
    model=ga(algorithm_parameters=algorithm_param,function=val.validate,dimension=dimensions,variable_type='bool')
    
    model.run()

if __name__ == "__main__":
    nr_dict = {'pizzas': 5, 't2': 1, 't3': 2, 't4': 1}
    pizzas = [(3, {'pepper', 'olive', 'onion'}), (3, {'mushroom', 'basil', 'tomato'}), (3, {'mushroom', 'chicken', 'pepper'}), (3, {'tomato', 'mushroom', 'basil'}), (2, {'chicken', 'basil'})]
    # genetic_algo(nr_dict, pizzas)
    val = Validation(nr_dict, pizzas)
    val.validate([1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0])
