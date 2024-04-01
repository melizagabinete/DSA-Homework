import matplotlib.pyplot as plt
from file_util import FileUtil
import math

# Read x values from file
with open('x_values.txt', 'r') as x_file: 
    x_values = [int(x) for x in x_file.read().split()]

# Define functions
def prob1():
    return [(x**2 + 7*x + 2) for x in x_values]

def prob2():
    return [(3*x + 2) for x in x_values]

def prob3():
    return [(x**2) for x in x_values]

def prob4():
    return [(x**3) for x in x_values]

def prob5():
    return [(x**5) for x in x_values]

def prob6():
    return [(x**3 + 2*x**2 + x + 10) for x in x_values]

def prob7():
    return [(x**4 - 3*x**3 + 2*x**2 - x + 11) for x in x_values]

def prob8():
    return [math.sin(x) for x in x_values]

def prob9():
    return [math.cos(x) for x in x_values]

def prob10():
    return [(x**5 + 4*x**4 + x**3 - 2*x**2 + 100) for x in x_values]

# Plotting
# Plot graphs for all problems
def plot_all():
    plt.figure()
    plt.title('Graphs of Problems')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.plot(x_values, prob1(), 'r', label="Problem 1")
    plt.plot(x_values, prob2(), 'b', label="Problem 2")
    plt.plot(x_values, prob3(), 'y', label="Problem 3")
    plt.plot(x_values, prob4(), 'c', label="Problem 4")
    plt.plot(x_values, prob5(), 'm', label="Problem 5")
    plt.plot(x_values, prob6(), 'k', label="Problem 6")
    plt.plot(x_values, prob7(), 'g', label="Problem 7")
    plt.plot(x_values, prob8(), 'skyblue', label="Problem 8")
    plt.plot(x_values, prob9(), 'lightcoral', label="Problem 9")
    plt.plot(x_values, prob10(), 'lime', label="Problem 10")
    plt.legend(loc='best')
    plt.show()

#Plot graph for Problem 1
def plot1():
    plt.figure()
    plt.title("Problem 1 Graph")
    plt.plot(x_values, prob1())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 2
def plot2():
    plt.figure()
    plt.title("Problem 2 Graph")
    plt.plot(x_values, prob2())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 3
def plot3():
    plt.figure()
    plt.title("Problem 3 Graph")
    plt.plot(x_values, prob3())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 4
def plot4():
    plt.figure()
    plt.title("Problem 4 Graph")
    plt.plot(x_values, prob4())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 5
def plot5():
    plt.figure()
    plt.title("Problem 5 Graph")
    plt.plot(x_values, prob5())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 6
def plot6():
    plt.figure()
    plt.title("Problem 6 Graph")
    plt.plot(x_values, prob6())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 7
def plot7():
    plt.figure()
    plt.title("Problem 7 Graph")
    plt.plot(x_values, prob7())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 8
def plot8():
    plt.figure()
    plt.title("Problem 8 Graph")
    plt.plot(x_values, prob8())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 9
def plot9():
    plt.figure()
    plt.title("Problem 9 Graph")
    plt.plot(x_values, prob9())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
# Plot graph for Problem 10
def plot10():
    plt.figure()
    plt.title("Problem 10 Graph")
    plt.plot(x_values, prob10())
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
# Main function to run the program
def main():
    while True: 
        with open('menu.txt', 'r') as menu_file:
            menu = [line.strip() for line in menu_file]
            for option in menu:
                print(option)
            choice = int(input("Enter your choice: "))
        
        with open('outputAss.txt', 'w') as output_file:
            output_file.write("RESULTS:\n")
            if choice == 11:
                plot_all()   
                problem_functions = [prob1, prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10]
                for prob_num, problem in enumerate(problem_functions, start=1):
                    problem_points = problem()
                    output_file.write(f"X and Y values for Problem {prob_num}:\n")
                    for i in range(len(x_values)):
                        output_file.write(f"{x_values[i]}, {problem_points[i]}\n")
                    output_file.write("\n") 
                
            elif 1 <= choice <= 10:
                output_file.write(f"X and Y Values for problem {choice}\n")
                plots = [plot1, plot2, plot3, plot4, plot5, plot6, plot7, plot8, plot9, plot10]
                plots[choice - 1]()
                problem_functions = [prob1, prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10] 
                problem = problem_functions[choice - 1]  # Adjusting for 0-based indexing
                with open('outputAss.txt', 'a') as output_file:
                    problem_points = problem()
                    for i in range(len(x_values)):
                        output_file.write(f"{x_values[i]}, {problem_points[i]}\n")
            else:
                output_file.write("Invalid choice!\n")
                
        choice2 = input("Try Again?[Y/N]")
        if choice2.upper() == 'N':
            break

if __name__ == "__main__":
    main()