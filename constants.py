# Constants file for rates of diseases
# Gamma (Recovery Rate) = 1/Days people are infectious
# Beta (Contact/Transmission Rate) = Ro (Average number of people infected per person) * Gamma
# https://www.futurelearn.com/info/courses/pandemics-modelling-and-policy/0/steps/144957

# Pertussis
# 6-21 Days Infectious
# 11 Days Average
# 15-17 People on average infected

# Pertussis Constants
PERTUSSIS_TR = 1.5
PERTUSSIS_RR = 0.1
PERTUSSIS_TR_RANGE = (0.8, 2.72)
PERTUSSIS_RR_RANGE = (0.05, 0.17)

# COVID 
# 8-10 Days Infectious
# 9 Days Average Infectious
# 5 People on average infected

# COVID DELTA Variant Constants
COVID_TR = 0.9
COVID_RR = 0.11
COVID_TR_RANGE = (0.9, 1.17)
COVID_RR_RANGE = (0.1, 0.13)

# Rhinovirus (Common cold)
# 2-7 Days Infectious
# 5 Days Average Infectious
# 3 People on average infected

# Rhinovirus (Common cold)
COLD_TR = 0.6
COLD_RR = 0.2
COLD_TR_RANGE = (0.9, 1.17)
COLD_RR_RANGE = (0.1, 0.13)