def findRegion(input_region):
    searchRegion = str(input_region)
    states_info = []

    with open('Economic_Data_2010.txt', 'r') as file:

        for line in file:
            fields = line.split(",")
            states_info.append(fields)

        i = 0
        regions = []
        for state in states_info:
            region = states_info[i][1].lower()
            if region not in regions:
                regions.append(region)
            i += 1

        if searchRegion not in regions:
            print(f'"{searchRegion.title()}" was not found in the list! Please enter a valid region.')
            exit(1)
        else:
            data = gatherData(searchRegion, states_info)
            region_pop = data[0]
            region_gdp = data[1]
            region_income = data[2]

            output = formatOutput(searchRegion, region_pop, region_gdp, region_income)
            for items in range(len(output)):
                print(output[items])

def gatherData(searchState, states_info):
    region_pop = {}
    region_gdp = {}
    region_income = {}

    i = 0
    for state in range(len(states_info)):
        if str(states_info[i][1]).lower() == searchState:
            if str(states_info[i][0]).lower() not in region_pop.keys():
                region_pop[str(states_info[i][0]).lower()] = states_info[i][2]
            if str(states_info[i][0]).lower() not in region_gdp.keys():
                region_gdp[str(states_info[i][0]).lower()] = states_info[i][3]
            if str(states_info[i][0]).lower() not in region_income.keys():
                region_income[str(states_info[i][0]).lower()] = states_info[i][4]
        i += 1
    return region_pop, region_gdp, region_income

def calc_total_pop(population):
    sum_pop = 0

    for k in population:
        sum_pop += float(population.get(k))
    return round(sum_pop, 2)

def calc_total_gdp(gdp):
    sum_gdp = 0

    for k in gdp:
        sum_gdp += float(gdp.get(k))
    return round(sum_gdp, 2)

def calc_total_pi(income):
    sum_income = 0

    for k in income:
        sum_income += float(income.get(k))
    return round(sum_income, 2)

def formatOutput(state, pop, gdp, income):
    sum_pop = calc_total_pop(pop)
    avg_pop = round(sum_pop / len(pop), 2)
    sum_gdp = calc_total_gdp(gdp)
    sum_income = calc_total_pi(income)
    avg_income = round((sum_income * 1000000000) / (sum_pop * 1000000), 2)

    region_states = []
    for key in pop:
        region_states.append(key.title())
    region_states_string = ', '.join(region_states)

    stats = str(f"Economic statistics for the {state.title()} region:")
    regionStates = str(f"\tStates in Region:\t{region_states_string}")
    regionPop = str(f"\tTotal Population:\t{sum_pop} million")
    regionAvgPop = str(f"\tAverage Population:\t{avg_pop} million")
    regionGDP = str(f"\tTotal GDP:\t\t\t${sum_gdp} billion")
    regionAvgIncome = str(f"\tAverage Income:\t\t${avg_income}")

    return stats, regionStates, regionPop, regionAvgPop, regionGDP, regionAvgIncome

requestRegion = input("Enter the region to query: ").lower()

findRegion(requestRegion)
