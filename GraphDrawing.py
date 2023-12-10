import pandas as pd
import matplotlib.pyplot as plt

# Function to load and parse CSV data
def load_csv_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to plot bar graph
def plot_bar_graph(data, x_column, y_column, title):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.show()

# Function to plot line graph
def plot_line_graph(data, x_column, y_column, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_column], data[y_column], marker='o')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.show()

# Function to plot scatter plot
def plot_scatter_plot(data, x_column, y_column, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.show()

# Function to plot stacked bar graph
def plot_stacked_bar_graph(data, x_column, y_columns, title):
    plt.figure(figsize=(12, 8))
    data[y_columns].plot(kind='bar', stacked=True)
    plt.xlabel(x_column)
    plt.ylabel('Number of Deaths')
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.show()

# Function to plot pie chart
def plot_pie_chart(data, labels, sizes, title):
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()

# Example usage
file_path = "US Deaths - Sheet1.csv"
csv_data = load_csv_data(file_path)

# Plot bar graph for COVID-19 deaths by age group
plot_bar_graph(csv_data, 'Age Group', 'COVID-19 Deaths', 'COVID-19 Deaths by Age Group')

# Plot line graph for AllCause Deaths by age group
plot_line_graph(csv_data, 'Age Group', 'AllCause Deaths', 'AllCause Deaths by Age Group')

# Plot scatter plot for Avg age in age group and COVID-19 deaths
plot_scatter_plot(csv_data, 'Avg age in age group', 'COVID-19 Deaths', 'Avg Age vs. COVID-19 Deaths')

# Plot stacked bar graph for COVID-19, AllCause, and Non-Covid deaths by age group
plot_stacked_bar_graph(csv_data, 'Age Group', ['COVID-19 Deaths', 'AllCause Deaths', 'Non-Covid (AllCause-C19)'], 'Deaths by Age Group')

# Plot pie chart for the distribution of COVID-19 deaths by age group
plot_pie_chart(csv_data, csv_data['Age Group'], csv_data['COVID-19 Deaths'], 'Distribution of COVID-19 Deaths by Age Group')
