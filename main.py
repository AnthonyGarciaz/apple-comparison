import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the start and end dates for data retrieval
start_date = "2004-01-01"
end_date = "2023-12-31"

# Retrieve historical data for Apple (BID) using yfinance
apple_data = yf.download("KO", start=start_date, end=end_date)

# Extract year from the date index to filter by year
apple_data['Year'] = apple_data.index.year

# Create a figure for plotting
plt.figure(figsize=(14, 8))

# Get unique years from 2004 to 2023
years_to_plot = range(2004, 2024)

# Iterate through each year and plot the cumulative price changes starting from zero
for year in years_to_plot:
    data = apple_data[apple_data['Year'] == year]
    # Normalize closing prices to start from zero
    normalized_prices = data['Close'] - data['Close'].iloc[0]
    plt.plot(data.index, normalized_prices, label=str(year))

# Add titles and labels
plt.title("Cumulative Apple Stock Price Changes (2004 - 2023) - Overlapping")
plt.xlabel("Date")
plt.ylabel("Cumulative Price Change ($)")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Adding a line at y=0 for reference
plt.legend(loc="upper left", fontsize="small")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
