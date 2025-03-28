import pandas as pd
import numpy as np
import shap
from desdeo_problem.problem import DiscreteDataProblem


def get_problem_data():
    df = pd.read_csv("data/river_pollution_10178.csv")
    pareto_front = df.to_numpy()

    # Compute Ideal and Nadir
    ideal = np.min(pareto_front[:, 0:5], axis=0)
    nadir = np.max(pareto_front[:, 0:5], axis=0)
    objective_names = ["f_1", "f_2", "f_3", "f_4", "f_5"]
    n_objectives = len(objective_names)

    # Define the Problem
    # problem = DiscreteDataProblem(df, ["x_1", "x_2"], objective_names, nadir, ideal)

    # Create Missing Data Sample
    missing_data = shap.sample(pareto_front[:, 0:n_objectives], nsamples=200)

    data = (
        {
            "ideal": ideal.tolist(),
            "nadir": nadir.tolist(),
            "objective_names": objective_names,
            "pareto_front": pareto_front.tolist(),
            "n_objectives": n_objectives,
            "missing_data": missing_data.tolist(),
        },
    )
    return data
