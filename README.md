# Fault Detection and Isolation in Complex Mechatronic Systems

## Project Overview

This project develops a diagnosis module for detecting and isolating faults in complex mechatronic systems used in industrial environments. The goal is to enhance system performance, productivity, and safety by leveraging machine learning and deep learning techniques applied to sensor data.

## Dataset

### Description

- **SensorID**: 1 (PT100 temperature sensor)
- **Environment**: Industrial (dust & vibrations)
- **Themes**: Plant, Building, Power, IT, Machine
- **Keywords**: Operational, Meters & sensors, Ambient, Electrical, per minute, over months
- **Modified**: March 7, 2018
- **Publisher**: Schneider-Electric

### Data Details

The dataset includes time series measurements from sensors, with potential disconnections or failures during the measurement period. This data is utilized for fault detection and isolation.

## Project Goals

1. **Fault Detection**: Identify abnormal system operations.
2. **Fault Isolation**: Determine the cause of the abnormal operation.

## Methodology

### Data Preprocessing

1. **Data Cleaning**: Address missing values, noise, and anomalies.
2. **Normalization**: Standardize sensor readings.

### Feature Engineering

1. **Feature Extraction**: Create features indicative of faults (e.g., statistical measures, temporal patterns).

### Model Development

1. **Traditional ML Techniques**:
   - Support Vector Machine (SVM)
   - Artificial Neural Network (ANN)
   - Fuzzy Neural Network (FNN)
   - Decision Trees (DT)
   - Bayesian Network (BN)

2. **Deep Learning Techniques**:
   - Denoising Stacked Auto-Encoder
   - Long Short-Term Memory Network (LSTM)
   - Self-Attentive Convolutional Neural Networks

### Evaluation

1. **Metrics**: Precision, recall, F1-score, accuracy.
2. **Cross-Validation**: Validate model robustness.

### Deployment

Integrate the trained model into an industrial setting for real-time fault detection and isolation.

## References

- [Denoising Stacked Auto-Encoders and LSTM](https://arxiv.org/pdf/2006.13380.pdf)
- [Self-Attentive Convolutional Neural Networks](https://www.sciencedirect.com/science/article/abs/pii/S0020025520308422)
- [Deep Learning for Fault Detection](https://reader.elsevier.com/reader/sd/pii/S0306261920308114?token=1675928516A34730661B0C6A35207B4AB4BECC82512AC9C5A4F09E0D5395594AA636FF55A3BDE3206452AE185E61951B)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/fault-detection.git
    ```

2. Navigate to the project directory:
    ```bash
    cd fault-detection
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Preprocess Data**: Run `preprocess.py` to clean and prepare the dataset.
2. **Train Models**: Use `train_models.py` to train various machine learning models.
3. **Evaluate Models**: Execute `evaluate_models.py` to assess model performance.
4. **Deploy**: Integrate the model into an industrial system using `deploy.py`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes


