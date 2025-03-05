# Project Title

## Overview
This project implements a recommendation system with four experimental conditions. Each condition has its own dedicated script. The system utilizes an LLM-based explanation approach, a knowledge-based recommender, and multiple algorithms to generate recommendations and explanations.

## Installation

### Prerequisites
Ensure you have Python installed on your system. It is recommended to use a virtual environment for dependency management.

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Project
Each experimental condition has its corresponding script. Below are the steps to run each condition:

### LLM-Explanation Condition
To run the LLM-based explanation condition:
```sh
python KnowledgeBased_Explanation.py
```

### Multipe Traffic Light  Algorithm Computation
The `view.py` file within the project folder contains multiple traffic light algorithm computations for each recipe.


### The recommender and LLM API calls
The file `app.py` script handles the recommendations generate whithin the function "get_top_recommendations" and LLM API calls are in "get_explanation" and dynamically adjusts prompts based on 
the user and recipe context.


## Data
The dataset used in the experiment is located in the `Data_csv` folder. Ensure that the required dataset files are in place before running the scripts.

## Data Analysis
The `Data_analysis` folder contains collected data from each experimental condition. The following notebooks perform data analysis:
- `DA_UMAP25.ipynb`
- `DA_umap25_R.ipynb`


## License
This project is licensed under [MIT License](LICENSE).

## Contact
For further inquiries, please contact the paper authors.
