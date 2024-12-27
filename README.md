# Premium Prediction Project

This repository contains a machine learning project aimed at predicting insurance premiums based on user input. The project includes model training, saving the model as a `.joblib` file, and deploying the model using Streamlit for user interaction.

## Application Link

Access the deployed application here: [Streamlit Application](https://ml-health-insurance-premium-prediction.streamlit.app/)

## Project Structure

The repository is organized as follows:

```
├── artifacts
│   └── model.joblib         # Trained model saved as a .joblib file
├── Code
│   ├── dataset.csv          # Dataset used for training and testing
│   └── notebook.ipynb       # Jupyter Notebook for EDA, feature engineering, and model training
├── .gitignore               # Specifies files to be ignored by Git
├── LICENSE                  # License information
├── main.py                  # Streamlit app entry point
├── prediction_helper.py     # Helper functions for predictions
├── README.md                # Project documentation (this file)
├── requirements.txt         # Required Python libraries
```

## Dataset

The dataset used for this project is included in the `Code` folder. It is utilized for exploratory data analysis (EDA), feature engineering, and training the machine learning model. Detailed information about the dataset is available in the linked Kaggle notebook.

[Kaggle Notebook Reference](https://www.kaggle.com/code/muhammednihalc/notebook485c4fbcbd)

## Jupyter Notebook

The Jupyter Notebook located in the `Code` folder provides:
- Data cleaning and preprocessing.
- Exploratory data analysis (EDA).
- Feature engineering.
- Model training and evaluation.
- Saving the trained model as a `.joblib` file.

## Deployment

The application is deployed using Streamlit. Below are the key files used for deployment:

- **main.py**: Entry point for the Streamlit application. It loads the trained model and provides a user interface for predictions.
- **prediction_helper.py**: Includes helper functions for model predictions and data preprocessing.
- **artifacts/model.joblib**: Contains the pre-trained machine learning model.

### Steps to Deploy

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

4. Open your web browser and navigate to `http://localhost:8501` to access the application.

## Requirements

The `requirements.txt` file contains all the dependencies needed for the project. Install them with:
```bash
pip install -r requirements.txt
```

## Key Features

- **Data Analysis**: Detailed exploratory data analysis performed in the Jupyter Notebook.
- **Model Training**: Includes steps for training, evaluating, and saving a machine learning model.
- **Web Application**: A Streamlit-based web interface for making predictions.
- **Reusable Components**: Helper functions for modular and efficient deployment.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- **Dataset and Code Reference**: [Kaggle Notebook](https://www.kaggle.com/code/muhammednihalc/notebook485c4fbcbd)
- **Tools and Libraries**: Python, Streamlit, scikit-learn, joblib

---

Feel free to contribute to this project by creating issues or submitting pull requests. For any questions, reach out to the repository maintainer.

