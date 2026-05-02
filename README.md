# Flight Price Prediction Using Machine Learning

A machine learning project that predicts flight ticket prices based on factors like airline, route, travel class, departure time, and how many days are left before the flight. Built as part of the Machine Learning programme at the National Skill Training Institute, Bangalore.

---

## Background

Anyone who has tried to book a flight knows the frustration of watching prices change almost daily. A ticket that costs a certain amount today might be significantly more expensive tomorrow, or cheaper if you wait — except sometimes it goes up instead. The pricing logic is rarely obvious to the traveller.

This project tries to make that logic a bit more transparent. Using a dataset of around 300,000 flight records, it builds a regression model that takes the key variables affecting price and produces a numerical prediction for what a ticket is likely to cost. The model reaches an R-squared score of 0.90 on the test set, meaning it explains about 90% of the price variation in unseen data.

---

## Dataset

The dataset comes from Kaggle and contains roughly 300,000 rows with around 10 columns covering both economy and business class flights.

| Feature | Description | Type |
|---|---|---|
| Airline | Airline company name | Categorical |
| Source | Departure city | Categorical |
| Destination | Arrival city | Categorical |
| Departure Time | Time of day the flight departs | Categorical |
| Arrival Time | Time of day the flight arrives | Categorical |
| Duration | Total flight duration in hours | Numerical |
| Days Left | Number of days before departure | Numerical |
| Class | Economy or Business | Categorical |
| Price | Ticket price in rupees — this is the target | Numerical |

The dataset was clean with no missing values, which made preprocessing straightforward.

---

## What the Data Shows

A few things stand out clearly from the exploratory analysis.

The biggest driver of price is how many days are left before departure. Tickets bought within a week of the flight are dramatically more expensive than those bought a month out. This is the strongest single predictor in the dataset.

Travel class is the second biggest factor. Business class tickets are on average four to five times more expensive than economy on the same route. This creates a clear separation in the price distribution that the model has to account for.

Price distribution across the full dataset is right-skewed. Most tickets fall in the 5,000 to 30,000 rupee range, but there is a long tail of expensive last-minute business class bookings that pulls the mean upward.

Airline choice and route also matter, though less dramatically. Some airlines consistently price higher than others on the same routes, and some routes are simply more competitive than others.

Departure time has a moderate effect. Early morning and late-night flights tend to be cheaper, likely because they are less convenient and see lower demand.

---

## How It Works

**Preprocessing**

Categorical columns like airline name, source city, destination city, travel class, and time of day were encoded into numerical values using label encoding and one-hot encoding. Columns that were identifiers or otherwise not useful for prediction were dropped. The data was then split 80% for training and 20% for testing.

**Model**

The algorithm used is Linear Regression. It was chosen because it is interpretable, trains quickly on large datasets, and serves as a strong baseline for a regression problem. With 300,000 records and well-engineered features, it performs well enough to be genuinely useful.

**Evaluation**

The model was evaluated using three metrics:

- R-squared: 0.90, meaning the model explains 90% of the variance in ticket prices
- MAE (Mean Absolute Error): measures the average size of prediction errors in rupees
- MSE (Mean Squared Error): penalises larger errors more heavily, useful for catching systematic mistakes

An R-squared of 0.90 on held-out test data indicates the model is not just memorising the training set and should generalise reasonably well to new flights.

---

## Running the Project

**Requirements**

```
pip install pandas numpy scikit-learn flask gradio matplotlib seaborn
```

**Running the notebook**

Open the main notebook in Jupyter or Colab and run the cells in order. The preprocessing, training, and evaluation steps are all sequential.

**Running the web app**

```
python app.py
```

This starts the Flask backend. The Gradio interface for interactive predictions is either embedded or launched alongside it depending on your setup.

---

## Web Application

The project includes an interactive UI built with Flask and Gradio where you can enter your own flight details and get a price prediction in real time. The inputs are:

- Flight duration in hours
- Number of days before departure
- Airline name
- Source and destination city
- Travel class (Economy or Business)

The output is a predicted ticket price in rupees, along with a price chart and airline comparison visualisation.

---

## Project Structure

```
flight-price-prediction/
|
|-- notebook/
|   |-- FlightPricePrediction.ipynb    EDA, preprocessing, model training
|
|-- app.py                             Flask web application
|-- model.pkl                          Saved trained model
|-- requirements.txt
|-- README.md
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| pandas | Data loading and manipulation |
| numpy | Numerical operations |
| scikit-learn | Model training and evaluation |
| matplotlib / seaborn | Visualisations |
| Flask | Web backend |
| Gradio | Interactive prediction UI |

---

## Results

| Metric | Value |
|---|---|
| R-squared | 0.90 |
| Training split | 80% |
| Test split | 20% |
| Dataset size | ~300,000 rows |

The model performs well for a linear approach. The 10% unexplained variance is partly due to the inherent unpredictability of airline pricing. Airlines use proprietary dynamic pricing algorithms that respond to real-time demand signals not captured in a static dataset.

---

## What Could Be Improved

Linear Regression treats all relationships as linear, which is a simplification. The relationship between days left and price is actually non-linear — prices spike steeply in the last few days rather than rising at a constant rate. Switching to Random Forest or XGBoost would likely improve accuracy meaningfully and handle these non-linear patterns better.

The dataset is a static snapshot from Kaggle. A production version would need to pull from a live flight pricing API to reflect current market prices rather than historical patterns.

Multi-stop routes are not currently handled. The model assumes direct or single-connection flights. Adding layover information would make it more realistic for international bookings.

A price alert system — where a user sets a target price and gets notified when a route drops below it — would be a natural extension of the prediction functionality.

---

## Author
Vinitha Abhinashree M

Vinitha Abhinashree M
Machine Learning Trainee, National Skill Training Institute, Bangalore
March 2026
