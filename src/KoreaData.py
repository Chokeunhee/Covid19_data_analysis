import pandas as pd
import matplotlib.pyplot as plt

k = pd.read_csv(r'Kordata.csv')
j = pd.read_csv(r'Japdata.csv')
u = pd.read_csv(r'Usdata.csv')
i = pd.read_csv(r'Isrdata.csv')
e = pd.read_csv(r'Eudata.csv')

#Korea
k_case = k["new_cases_smoothed_per_million"]
k_death = k["total_deaths_per_million"]
k_vac = k["people_fully_vaccinated_per_hundred"]
k_Stringency = k["stringency_index"]
k_Reproduction = k["reproduction_rate"]

#Japan
j_case = j["new_cases_smoothed_per_million"]
j_death = j["total_deaths_per_million"]
j_vac = j["people_fully_vaccinated_per_hundred"]
j_Stringency = j["stringency_index"]
j_Reproduction = j["reproduction_rate"]

#Us
u_case = u["new_cases_smoothed_per_million"]
u_death = u["total_deaths_per_million"]
u_vac = u["people_fully_vaccinated_per_hundred"]
u_Stringency = u["stringency_index"]
u_Reproduction = u["reproduction_rate"]

#Isreal
i_case = i["new_cases_smoothed_per_million"]
i_death = i["total_deaths_per_million"]
i_vac = i["people_fully_vaccinated_per_hundred"]
i_Stringency = i["stringency_index"]
i_Reproduction = i["reproduction_rate"]

#Eu
e_case = e["new_cases_smoothed_per_million"]
e_death = e["total_deaths_per_million"]
e_vac = e["people_fully_vaccinated_per_hundred"]
e_Stringency = e["stringency_index"]
e_Reproduction = e["reproduction_rate"]


#TotalVac = k["total_vaccinations"]
#TotalVacprime = TotalVac.diff()
'''
plt.title("New case per million")
plt.plot(k_case, label="Korea")
plt.plot(j_case, label="Japan")
plt.plot(u_case, label="US")
plt.plot(i_case, label="Israel")
plt.plot(e_case, label="EU")
'''

'''
plt.title("Total death per million")
plt.plot(k_death, label="Korea")
plt.plot(j_death, label="Japan")
plt.plot(u_death, label="US")
plt.plot(i_death, label="Israel")
plt.plot(e_death, label="EU")



plt.title("People fully vaccinated per hundred")
plt.plot(k_vac, label="Korea")
plt.plot(j_vac, label="Japan")
plt.plot(u_vac, label="US")
plt.plot(i_vac, label="Israel")
plt.plot(e_vac, label="EU")



plt.title("Stringenct index")
plt.plot(k_Stringency, label="Korea")
plt.plot(j_Stringency, label="Japan")
plt.plot(u_Stringency, label="US")
plt.plot(i_Stringency, label="Israel")



plt.title("Reproduction rate")
plt.plot(k_Reproduction, label="Korea")
plt.plot(j_Reproduction, label="Japan")
plt.plot(u_Reproduction, label="US")
plt.plot(i_Reproduction, label="Israel")
plt.plot(e_Reproduction, label="EU")
'''


plt.legend()
plt.ticklabel_format(style = 'plain')

#plt.scatter(NewCase, Stringency, s=3)
#plt.scatter(TotalVacprime, NewCase, s=3)























