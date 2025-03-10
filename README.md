# Nudging Healthy Choices: Leveraging LLM-Generated Hashtags and Explanations in Personalized Food Recommendations

## Overview
This project aims to develop a recipe recommender system enhanced by Large Language Models (LLMs) and Multiple Traffic Light (MTL) labels to guide users toward healthier food choices. The results of this research have been submitted to UMAP 2025. For research and experimental purposes, the project includes four distinct conditions, each organized in its own folder.
```
- KnowledgeBased_Explanation/ ## LLM-based explanations as a nudge condition
- KnowledgeBased_hashTag/ ## LLM-based Hashatgs as a nudge condition
- KnowledgeBased_labels/ ## MTL condition as a nudge 
- KnowledgeBased_nolabel/ ## noLabel (baseline) condition as a nudge 
```



```
KnowledgeBased_Explanation/  # The LLM-generated condition
├── Labels_nudge/
│   ├── views.py  # Contains the logic of the system and algorithm to compute the MTL label and FSA score for each recommended recipe.
│   ├── app.py  
│   │   ├── get_top_recommendation  # Computes top personalized recipe recommendations for each active user based on the KB approach.
│   │   ├── get_explanation  # LLM API call to generate explanations/hashtags associated with a given recipe for the active user.

Data_csv/  # Contains all datasets used in the experiment

Data_analysis/
├── DA_UMAP25.ipynb  # Data analysis and pre-processing in Python
├── DA_umap25_R.ipynb  # Statistical analysis using R
```



### Prerequisites
Ensure you have Python installed on your system and R for statistical analysis. It is recommended to use a virtual environment for dependency management.

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
## folder KnowledgeBased_Explanation
python manage.py runserver
```

### Multipe Traffic Light  Algorithm Computation
The `view.py` file within the project folder contains multiple traffic light algorithm computations for each recipe.


### The recommender and LLM API calls
The file `app.py` script handles the recommendations generatation using the function "get_top_recommendations" and LLM API calls are in "get_explanation" and dynamically adjusts prompts based on 
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
For further inquiries, please contact the paper authors [Anonymous@Anonymous.Anonymou].
