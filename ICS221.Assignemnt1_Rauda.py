import numpy as np
import time
import matplotlib.pyplot as plt

# Chocolate Distribution Algorithm
def distribute_chocolates_iter(chocolates, students):
    distribution = {}
    for student, chocolate in zip(students, chocolates):
        distribution[student] = chocolate
    return distribution

def distribute_chocolates_rec(chocolates, students, index=0):
    if index >= len(students) or index >= len(chocolates):
        return {}
    else:
        distribution = {students[index]: chocolates[index]}
        distribution.update(distribute_chocolates_rec(chocolates, students, index + 1))
        return distribution

# Sorting Algorithms
def sort_by_weight(chocolates):
    return sorted(chocolates, key=lambda x: x[0])

def sort_by_price(chocolates):
    return sorted(chocolates, key=lambda x: x[1])

# Searching Algorithm
def search_chocolate(chocolates, target):
    for chocolate in chocolates:
        if chocolate[0] == target or chocolate[1] == target:
            return chocolate
    return None

# Time Complexity Functions
def linear(n):
    return n

def nlogn(n):
    return n * np.log(n)

# Define the range of input values
n_values = np.arange(1, 100)

# Sensitivity analysis for each algorithm
execution_times = {'Iterative Distribution': [], 'Recursive Distribution': [], 'Sorting by Weight': [], 'Sorting by Price': [], 'Linear Search': []}
min_threshold = 0.001  # Set a minimum threshold for execution time

for n in n_values:
    # Chocolate Distribution Algorithm - Iterative
    chocolates = [(np.random.randint(10, 100), np.random.uniform(1.0, 5.0), 'Milk') for _ in range(n)]
    students = ["Student" + str(i) for i in range(n)]
    start_time = time.time()
    distribute_chocolates_iter(chocolates, students)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Iterative Distribution'].append(max(exec_time, min_threshold))

    # Chocolate Distribution Algorithm - Recursive
    start_time = time.time()
    distribute_chocolates_rec(chocolates, students)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Recursive Distribution'].append(max(exec_time, min_threshold))

    # Sorting Algorithm - Weight
    start_time = time.time()
    sort_by_weight(chocolates)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Sorting by Weight'].append(max(exec_time, min_threshold))

    # Sorting Algorithm - Price
    start_time = time.time()
    sort_by_price(chocolates)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Sorting by Price'].append(max(exec_time, min_threshold))

    # Searching Algorithm - Linear Search
    start_time = time.time()
    search_chocolate(chocolates, 40)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Linear Search'].append(max(exec_time, min_threshold))

# Plotting the Time Complexities
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Set minimum y-axis limit
y_min_limit = 0.001

# Plotting Chocolate Distribution Algorithm
axs[0, 0].plot(n_values, linear(n_values), label='Iterative Distribution', color='blue')
axs[0, 0].scatter(n_values, execution_times['Iterative Distribution'], color='blue')
axs[0, 0].set_title('Iterative Distribution')
axs[0, 0].set_xlabel('Input Size (n)')
axs[0, 0].set_ylabel('Time (T)')
axs[0, 0].set_ylim(ymin=y_min_limit)  # Set minimum y-axis limit
axs[0, 0].grid(True)
axs[0, 0].legend()

axs[0, 1].plot(n_values, linear(n_values), label='Recursive Distribution', color='green')
axs[0, 1].scatter(n_values, execution_times['Recursive Distribution'], color='green')
axs[0, 1].set_title('Recursive Distribution')
axs[0, 1].set_xlabel('Input Size (n)')
axs[0, 1].set_ylabel('Time (T)')
axs[0, 1].set_ylim(ymin=y_min_limit)  # Set minimum y-axis limit
axs[0, 1].grid(True)
axs[0, 1].legend()

# Plotting Sorting Algorithm
axs[1, 0].plot(n_values, nlogn(n_values), label='Sorting by Weight', color='red')
axs[1, 0].scatter(n_values, execution_times['Sorting by Weight'], color='red')
axs[1, 0].set_title('Sorting by Weight')
axs[1, 0].set_xlabel('Input Size (n)')
axs[1, 0].set_ylabel('Time (T)')
axs[1, 0].set_ylim(ymin=y_min_limit)  # Set minimum y-axis limit
axs[1, 0].grid(True)
axs[1, 0].legend()

axs[1, 1].plot(n_values, nlogn(n_values), label='Sorting by Price', color='purple')
axs[1, 1].scatter(n_values, execution_times['Sorting by Price'], color='purple')
axs[1, 1].set_title('Sorting by Price')
axs[1, 1].set_xlabel('Input Size (n)')
axs[1, 1].set_ylabel('Time (T)')
axs[1, 1].set_ylim(ymin=y_min_limit)  # Set minimum y-axis limit
axs[1, 1].grid(True)
axs[1, 1].legend()

# Plotting Searching Algorithm
axs[2, 0].plot(n_values, linear(n_values), label='Linear Search', color='orange')
axs[2, 0].scatter(n_values, execution_times['Linear Search'], color='orange')
axs[2, 0].set_title('Linear Search')
axs[2, 0].set_xlabel('Input Size (n)')
axs[2, 0].set_ylabel('Time (T)')
axs[2, 0].set_ylim(ymin=y_min_limit)  # Set minimum y-axis limit
axs[2, 0].grid(True)
axs[2, 0].legend()

# Hide the empty subplot
axs[2, 1].axis('off')

plt.tight_layout()
plt.show()
