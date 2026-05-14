# agents/manager.py

import random
import csv

class EvolutionManager:

    def __init__(self, generations=20):
        self.generations = generations
        self.best = 0

    def log(self, gen, fitness):
        with open("dase_convergence.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([gen, fitness])

    def update(self, fitness):
        if fitness > self.best:
            self.best = fitness
