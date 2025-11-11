#NPRE 200 computer project 1: Main program
#V 3.1
#Coded by: Pete Zimmerman
#Requests JSON file names, extracts data, produces graphs and doc in Output folder

import ProjectLibrary as pl
import matplotlib.pyplot as plt
import numpy as np
import os

Energies = pl.Energies_eV
fluxes = pl.Fluxes_per_m2s
#getting data with project library
name235 = input('Enter "enriched" isotope json file Name: ')
#massEnriched = input('Enter Molar mass (g/mol) of "enriched" isotope: ')
name238 = input("Enter remainder isotope json file Name: ")
#massRemain = input('Enter Molar mass (g/mol) of "enriched" isotope: ')

#massEnriched = float(massEnriched)
#massRemain = float(massRemain)

en235 , xs235 , en238 , xs238 , xs235_e , xs238_e , arrXS235 , arrXS238, nameEnrich , nameRemain , massEnrich , massRemain = pl.dataExtractorF(name235 , name238)

#begin producing output
#check for Ouput file
os.makedirs("Output", exist_ok=True)

#cross section plotting
plt.loglog(en235, xs235, label = nameEnrich)
plt.loglog(en238, xs238, label = nameRemain)
plt.xlabel("Energy (eV)")
plt.ylabel("Cross Section (Barns)")
plt.grid()
plt.legend()
plt.savefig("Output/crossSection.png", dpi=300)
plt.close()
print("Cross Section")

#flux plotting
#uses given data
#interpolation to be used for all future math dependent on flux
plt.loglog(pl.x , pl.y)
plt.xlabel("Energy (eV)")
plt.ylabel("Flux (n/cm²·s·eV)")
plt.title("PWR Flux Distribution vs Energy")
plt.grid()
plt.savefig("Output/flux.png", dpi=300)
plt.close()
print("Flux")

#reaction Rates
#Given enrichments expressed as decimals
enrichments = np.array([0 , .03 , .2 , .5 , 1])

#calculate rate by enrichment, store array as key value pair in dict below
rr_results = pl.reactionRate_Enrich(enrichments , xs235_e , xs238_e , massEnrich , massRemain)

#graphing nonsense
plt.loglog(Energies , rr_results[0] , label = "0%")
plt.loglog(Energies , rr_results[.03] , label = "3%")
plt.loglog(Energies , rr_results[.2] , label = "20%")
plt.loglog(Energies , rr_results[.5] , label = "50%")
plt.loglog(Energies , rr_results[1] , label = "100%")
plt.xlabel("Energy (eV)")
plt.ylabel("Reaction Rate")
plt.title("Reaction Rate by Enrichment")
plt.grid()
plt.legend()
plt.savefig("Output/reactionRate.png", dpi=300)
plt.close()
print("Reaction Rate")

#power plot and write
#calculate rate by enrichment, store array as key value pair in dict below
pwResults = pl.powerPerVol_Enrich(enrichments , xs235_e , xs238_e , massEnrich , massRemain)

#write power integral in doc
pwInts = pl.powerInt_Enrich(enrichments , xs235_e , xs238_e , massEnrich , massRemain)

outpath = os.path.join("Output", "power_per_vol.txt")

with open(outpath, "w") as f:
    f.write("Power Produced per unit volume (W/cm^3)\n")
    for enr, val in pwInts.items():
        f.write(f"enrichment= {enr:.2f}:  {val:.4f}\n")

#graphing nonsense
plt.loglog(Energies , pwResults[0] , label = "0%")
plt.loglog(Energies , pwResults[.03] , label = "3%")
plt.loglog(Energies , pwResults[.2] , label = "20%")
plt.loglog(Energies , pwResults[.5] , label = "50%")
plt.loglog(Energies , pwResults[1] , label = "100%")
plt.xlabel("Neutron Energy (eV)")
plt.ylabel("Power per cm^3 (Watts)")
plt.title("Power Produced in 1 cm^3 as Function of Neutron Energy")
plt.grid()
plt.legend()
plt.savefig("Output/powerPerVolume.png", dpi=300)
plt.close()
print("Power")