import numpy as np
import matplotlib.pyplot as plt
import constants
import os

# Accessory function to clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Accessory functionn to print menu logo
def printLogo():
    print(r"""  _____  ______ _____  ___   _____ _____ __  __ 
 |  __ \|  ____|  __ \|__ \ / ____|_   _|  \/  |
 | |__) | |__  | |__) |  ) | (___   | | | \  / |
 |  ___/|  __| |  _  /  / / \___ \  | | | |\/| |
 | |    | |____| | \ \ / /_ ____) |_| |_| |  | |
 |_|    |______|_|  \_\____|_____/|_____|_|  |_|                                    
    """)
    print("Welcome to the Pertussis Disease spread simulator!")
    print("What shall we do today?")

# Accessory function to get integers with input validation
def getInt(prompt):
    while(True):
        try:
            return int(input(prompt))
        except:
            print("Invalid input (Integers only), try again")

# Accessory function to get floats with input validation
def getFloat(prompt):
    while(True):
        try:
            return float(input(prompt))
        except:
            print("Invalid input (Floats only), try again")

# Sir Model Iteration
def SIRModel(pop_size, S, I, R, transmission_rate, recovery_rate):
    new_infected = transmission_rate * S * I / pop_size # Change in number of infected
    new_recoveries = recovery_rate * I # Change in number of recovered

    #Updating Values
    new_S = S - new_infected
    new_I = I + new_infected - new_recoveries
    new_R = R + new_recoveries

    return new_S, new_I, new_R

#SIR Model Simulation
def SIRSimulation(pop_size, init_infected, transmission_rate, recovery_rate, days):
    # Initial Values of SIR
    S = pop_size - init_infected
    I = init_infected
    R = 0

    # List of values per day of simulation
    S_hist = [S]
    I_hist = [I]
    R_hist = [R]

    # Main loop that simulates the SIR Model
    for day in range(days):
        S, I, R = SIRModel(pop_size, S, I, R, transmission_rate, recovery_rate)
        S_hist.append(S)
        I_hist.append(I)
        R_hist.append(R)
    
    return S_hist, I_hist, R_hist

# Modified SIR Model Modified Using the Monte Carlo Simulation
def SIRMonteCarloSimulation(pop_size, init_infected, transmission_rate_range, recovery_rate_range, days):
    # Initial Values of SIR
    S = pop_size - init_infected
    I = init_infected
    R = 0

    # List of values per day of simulation
    S_hist = [S]
    I_hist = [I]
    R_hist = [R]

    # Main loop that simulates the SIR Model
    for day in range(days):
        # Monte Carlo Simulation of contact rate and recovery 
        transmission_rate = np.random.uniform(*transmission_rate_range)
        recovery_rate = np.random.uniform(*recovery_rate_range)
        S, I, R = SIRModel(pop_size, S, I, R, transmission_rate, recovery_rate)
        S_hist.append(S)
        I_hist.append(I)
        R_hist.append(R)
    
    return S_hist, I_hist, R_hist

# Plots results of SIR Model
def plot_simulation(susceptible_list, infected_list, recovered_list, days, title):
    plt.plot(range(days + 1), susceptible_list, label='Susceptible')
    plt.plot(range(days + 1), infected_list, label='Infected')
    plt.plot(range(days + 1), recovered_list, label='Recovered')
    plt.xlabel('Days')
    plt.ylabel('Number of Individuals')
    plt.title(title)
    plt.legend()
    plt.show()

# Menu for default SIR Model
def SIRMenu():
    print("SIR Model Menu")
    print("[1] Use Pertussis Data")
    print("[2] Use Other Data")
    print("[3] Use Own Inputted Data")
    print("[0] Go Back")
    choice = getInt("Choose data option: ")
    clear()

    pop = getInt("Input initial population: ")
    days = getInt("Input number of days: ")
    inf = getInt("Input initial number of infected: ")

    # SIR Simulation for Pertussis
    if(choice==1):
        S, I, R = SIRSimulation(pop, inf, constants.PERTUSSIS_TR, constants.PERTUSSIS_RR, days)
        plot_simulation(S, I, R, days, "Pertussis SIR Model Simulation")


    # SIR Simulation for Other Diseases
    if(choice==2):
        print("Other Diseases")
        print("[1] COVID Delta Variant")
        print("[2] Rhinovirus (Common Cold)")
        choice1 = getInt("Choose Disease: ")
        if(choice1==1):
            S, I, R = SIRSimulation(pop, inf, constants.COVID_TR, constants.COVID_RR, days)
            plot_simulation(S, I, R, days, "COVID Delta Variant SIR Model Simulation")
        if(choice1==2):
            S, I, R = SIRSimulation(pop, inf, constants.COLD_TR, constants.COLD_RR, days)
            plot_simulation(S, I, R, days, "Rhinovirus (Common Cold) SIR Model Simulation")

    # SIR Simulation for own data
    if(choice==3):
        title = input("Disease name: ")
        tr = getFloat("Input Contact Rate: ")
        rr = getFloat("Input Recovery Rate: ")
        S, I, R = SIRSimulation(pop, inf, tr, rr, days)
        plot_simulation(S, I, R, days, title+" SIR Monte Carlo Model Simulation")

# Menu for default SIR Monte Carlo model
def SIRMCMenu():
    print("SIR Monte Carlo Model Menu")
    print("[1] Use Pertussis Data")
    print("[2] Use Other Data")
    print("[3] Use Own Inputted Data")
    print("[0] Go Back")
    choice = getInt("Choose data option: ")
    clear()

    pop = getInt("Input initial population: ")
    days = getInt("Input number of days: ")
    inf = getInt("Input initial number of infected: ")

    # SIR Monte Carlo Simulation for Pertussis
    if(choice==1):
        S, I, R = SIRMonteCarloSimulation(pop, inf, constants.PERTUSSIS_TR_RANGE, constants.PERTUSSIS_RR_RANGE, days)
        plot_simulation(S, I, R, days, "Pertussis SIR Monte Carlo Model Simulation")
    
    # SIR Monte Carlo Simulation for Other Diseases
    if(choice==2):
        print("Other Diseases")
        print("[1] COVID Delta Variant")
        print("[2] Rhinovirus (Common Cold)")
        choice1 = getInt("Choose Disease: ")
        if(choice1==1):
            S, I, R = SIRMonteCarloSimulation(pop, inf, constants.COVID_TR_RANGE, constants.COVID_RR_RANGE, days)
            plot_simulation(S, I, R, days, "COVID Delta Variant SIR Monte Carlo Model Simulation")
        if(choice1==2):
            S, I, R = SIRMonteCarloSimulation(pop, inf, constants.COLD_TR_RANGE, constants.COLD_RR_RANGE, days)
            plot_simulation(S, I, R, days, "Rhinovirus (Common Cold) SIR Monte Carlo Model Simulation")
    
    # SIR Monte Carlo Simulation for Own Data
    if(choice==3):
        title = input("Disease name: ")
        tr1 = getFloat("Input Contact Rate Range start: ")
        tr2 = getFloat("Input Contact Rate Range end: ")
        rr1 = getFloat("Input Recovery Rate start: ")
        rr2 = getFloat("Input Recovery Rate end: ")
        S, I, R = SIRMonteCarloSimulation(pop, inf, (tr1,tr2), (rr1,rr2), days)
        plot_simulation(S, I, R, days, title)

# Main menu for program
def main():
    while True:
        clear()
        printLogo()
        print("[1] Default SIR Model")
        print("[2] SIR Monte Carlo Model")
        print("[0] Exit")
        choice = getInt("Pick an option: ")
        clear()

        if(choice==1):
            SIRMenu()

        if(choice==2):
            SIRMCMenu()

        elif(choice == 0):
            print("Thank you for using our program!")
            break

main()