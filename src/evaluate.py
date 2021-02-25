import numpy as np
import pandas as pd

import config as cfg
from data_reader import read_input


# Each street at most once in the schedule
# By default all lights on all intersections are red

class Car:
    self.loc = Intersection or Road
    self.route = ['street1', 'street2']
    

class Intersection:
    self.id
    self.traffic_light_state
    self.next_roads = []
    
    def __init__(self, id, traffic_light_state, next_roads):
        self.id = id
        self.traffic_light_state = traffic_light_state
        self.next_roads = next_roads
        
    def add_road(self, road)
        self.d

class Road:
    self.name
    self.next_intersection_id
    
    def __init__(self, name, next_intersection_id):
        self.name = name
        self.next_intersection_id = next_intersection_id
    
#     ({'duration': 6, 'num_inters': 4, 'num_streets': 5, 'num_cars': 2, 'bonus': 1000}, [{'start_inter': 2, 'end_inter': 0, 'street_name': 'rue-de-londres', 'cost': 1}, {'start_inter': 0, 'end_inter': 1, 'street_name': 'rue-d-amsterdam', 'cost': 1}, {'start_inter': 3, 'end_inter': 1, 'street_name': 'rue-d-athenes', 'cost': 1}, {'start_inter': 2, 'end_inter': 3, 'street_name': 'rue-de-rome', 'cost': 2}, {'start_inter': 1, 'end_inter': 2, 'street_name': 'rue-de-moscou', 'cost': 3}], [{'num_streets': 4, 'streets': ['rue-de-londres', 'rue-d-amsterdam', 'rue-de-moscou', 'rue-de-rome']}, {'num_streets': 3, 'streets': ['rue-d-athenes', 'rue-de-moscou', 'rue-de-londres']}])
    
class Simulator:
    self.intersections
    
    # First all the intersections and then all the roads
    self.cars
    self.current_t = 0
    self.final_t = 0
    
#     {
#     1: [{'time': 10, 'next_streets': ['street1', 'street2',  ]},
#         {'time': 10, 'next_streets': ['street1', 'street2',  ]},
#         {'time': 10, 'next_streets': ['street1', 'street2',  ]}],
#     2: [{'time': 10, 'next_streets': ['street1', 'street2',  ]},
#         {'time': 10, 'next_streets': ['street1', 'street2',  ]},
#         {'time': 10, 'next_streets': ['street1', 'street2',  ]}],
# }
 
    
    def __init__(self, intersections, roads, cars):
        for road in roads
            self.intersections.append(Intersection())
        
        self.intersections = intersections
        self.final_t = intersections['duration']
        self.roads = roads
        self.cars = cars
        
    def set_schedule(self, schedule):
        this.schedule = schedule
#             schedules = [
#         (
#             1,
#             2,
#             [
#                 ("rue-d-athenes", 2),
#                 ("rue-d-amsterdam", 1),
#             ]
#         ),
#         (
#             0,
#             1,
#             [
#                 ("rue-de-londres", 2),
#             ]
#         ),
#         (
#             2,
#             1,
#             [
#                 ("rue-de-moscou", 1),
#             ]
#         )
#     ]
        
    def increment_time(self):
        if this.schedule:
            print("yes schedule is set")
        else:
            print("the schedule has not been set, this will mean that all traffic lights will be red")
        
        self.current_t += 1
        
        for item in intersection_state:
            
    
    def run_simulation(self):
        while self.current_t != self.final_t:
            self.increment_time()
        

def estimate_score(*input_data, *output_data):
    sim = Simulator(intersections = data[0], roads = data[1], cars = data[3])
    
    return -1


if __name__ == "__main__":
    data = read_input("../inputs/a.txt")
#     print(data)

    sim = Simulator(intersections = data[0], roads = data[1], cars = data[3])
    
    