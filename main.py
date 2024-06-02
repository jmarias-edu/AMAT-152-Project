import numpy as np
import matplotlib.pyplot as plt
import constants
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def SIRModel(pop_size, S, I, R, contact_rate, recovery_rate):
    new_infected = contact_rate * S * I / pop_size
    new_recoveries = recovery_rate * I

    new_S = S - new_infected
    new_I = I + new_infected - new_recoveries
    new_R = R + new_recoveries

    return new_S, new_I, new_R

def SIRSimulation(pop_size, init_infected, contact_rate, recovery_rate, days):
    S = pop_size - init_infected
    I = init_infected
    R = 0

    S_hist = [S]
    I_hist = [I]
    R_hist = [R]

    for day in range(days):
        S, I, R = SIRModel(pop_size, S, I, R, contact_rate, recovery_rate)
        S_hist.append(S)
        I_hist.append(I)
        R_hist.append(R)
    
    return S_hist, I_hist, R_hist

def SIRMonteCarloSimulation(pop_size, init_infected, contact_rate_range, recovery_rate_range, days):
    S = pop_size - init_infected
    I = init_infected
    R = 0

    S_hist = [S]
    I_hist = [I]
    R_hist = [R]

    for day in range(days):
        contact_rate = np.random.uniform(*contact_rate_range)
        recovery_rate = np.random.uniform(*recovery_rate_range)
        S, I, R = SIRModel(pop_size, S, I, R, contact_rate, recovery_rate)
        S_hist.append(S)
        I_hist.append(I)
        R_hist.append(R)
    
    return S_hist, I_hist, R_hist

def plot_simulation(susceptible_list, infected_list, recovered_list, days):
    plt.plot(range(days + 1), susceptible_list, label='Susceptible')
    plt.plot(range(days + 1), infected_list, label='Infected')
    plt.plot(range(days + 1), recovered_list, label='Recovered')
    plt.xlabel('Days')
    plt.ylabel('Number of Individuals')
    plt.title('SIR Model Simulation')
    plt.legend()
    plt.show()

def getInt(prompt):
    while(True):
        try:
            return int(input(prompt))
        except:
            print("Invalid input (Integers only), try again")

def getFloat(prompt):
    while(True):
        try:
            return float(input(prompt))
        except:
            print("Invalid input (Floats only), try again")

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

    if(choice==1):
        S, I, R = SIRSimulation(pop, inf, constants.PERTUSSIS_CR, constants.PERTUSSIS_RR, days)
        plot_simulation(S, I, R, days)

    if(choice==2):
        print("Other Diseases")
        print("[1] COVID Delta Variant")
        print("[2] Rhinovirus (Common Cold)")
        choice1 = getInt("Choose Disease: ")
        if(choice1==1):
            S, I, R = SIRSimulation(pop, inf, constants.COVID_CR, constants.COVID_RR, days)
            plot_simulation(S, I, R, days)

    if(choice==3):
        cr = getFloat("Input Contact Rate: ")
        rr = getFloat("Input Recovery Rate: ")
        S, I, R = SIRSimulation(pop, inf, cr, rr, days)
        plot_simulation(S, I, R, days)

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

    if(choice==1):
        S, I, R = SIRMonteCarloSimulation(pop, inf, constants.PERTUSSIS_CR_RANGE, constants.PERTUSSIS_RR_RANGE, days)
        plot_simulation(S, I, R, days)
    if(choice==2):
        print("Other Diseases")
        print("[1] COVID Delta Variant")
        print("[2] Rhinovirus (Common Cold)")
        choice1 = getInt("Choose Disease: ")
        if(choice1==1):
            S, I, R = SIRMonteCarloSimulation(pop, inf, constants.COVID_CR_RANGE, constants.COVID_RR_RANGE, days)
            plot_simulation(S, I, R, days)
        
    if(choice==3):
        cr1 = getFloat("Input Contact Rate Range start: ")
        cr2 = getFloat("Input Contact Rate Range end: ")
        rr1 = getFloat("Input Recovery Rate start: ")
        rr2 = getFloat("Input Recovery Rate end: ")
        S, I, R = SIRMonteCarloSimulation(pop, inf, (cr1,cr2), (rr1,rr2), days)
        plot_simulation(S, I, R, days)

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