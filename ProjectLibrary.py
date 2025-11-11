#NPRE 200 computer project 1: Project Library
#V 3.0
#Coded by: Pete Zimmerman

import numpy as np
from scipy.interpolate import interp1d
import json
import sys


#given in doc
energyPerFission = 200 #MeV
fuelDensity = 10.97 #g/cm^3

#declaring pwr Flux Distribution Arrays
x = np.array([1.21009173e-10, 1.38723745e-10, 1.48530984e-10, 1.76190584e-10, 1.95201017e-10, 2.23776556e-10, 2.84214661e-10, 3.14880567e-10, 3.86495661e-10, 4.43074884e-10, 4.74398587e-10, 6.02525287e-10, 6.45121525e-10, 7.39561070e-10, 8.19357482e-10, 8.77282929e-10, 1.07680842e-09, 1.15293466e-09, 1.32171314e-09, 1.51519914e-09, 1.73700963e-09, 2.06047743e-09, 2.36211137e-09, 2.89933992e-09, 3.43925812e-09, 3.68240054e-09, 4.51991003e-09, 5.18158109e-09, 5.94011439e-09, 7.04628889e-09, 8.94936737e-09, 1.02594681e-08, 1.21699973e-08, 1.39515671e-08, 1.39515671e-08, 1.77196395e-08, 2.17497188e-08, 2.95768414e-08, 4.16181782e-08, 5.28585149e-08, 6.48804302e-08, 6.94672290e-08, 9.77487581e-08, 1.04659222e-07, 1.04659222e-07, 1.37544276e-07, 1.37544276e-07, 1.42323183e-07, 1.52384889e-07, 1.80762167e-07, 1.87042659e-07, 2.72336009e-07, 3.01720244e-07, 4.70365116e-07, 6.39636519e-07, 9.00045623e-07, 1.40312118e-06, 1.72224108e-06, 2.34202803e-06, 2.87468891e-06, 3.18485918e-06, 3.29551553e-06, 3.41001657e-06, 3.65109173e-06, 3.65109173e-06, 4.04503353e-06, 4.79830403e-06, 4.79830403e-06, 4.79830403e-06, 5.13752582e-06, 5.13752582e-06, 5.88960985e-06, 5.88960985e-06, 6.09424141e-06, 6.30598279e-06, 6.98637934e-06, 8.28739043e-06, 1.01722392e-05, 1.24857699e-05, 1.48108834e-05, 1.81794076e-05, 2.15647965e-05, 2.47216739e-05, 3.24894899e-05, 3.47863728e-05, 3.98787610e-05, 5.61142199e-05, 6.88765989e-05, 1.03769380e-04, 1.27370245e-04, 1.79225276e-04, 2.60953820e-04, 3.67193455e-04, 4.50706370e-04, 6.56233046e-04, 8.05483893e-04, 1.05857560e-03, 1.48954337e-03, 1.76692774e-03, 2.24414379e-03, 3.15778061e-03, 4.29417856e-03, 5.27082822e-03, 6.69438606e-03, 6.69438606e-03, 7.67437936e-03, 1.00857519e-02, 1.51951786e-02, 2.21243342e-02, 3.00862705e-02, 4.23350063e-02, 5.75702049e-02, 8.38228023e-02, 1.10160829e-01, 1.39913327e-01, 1.77701452e-01, 2.10793208e-01, 2.67724739e-01, 3.28614913e-01, 4.31869254e-01, 4.95090731e-01, 6.50653566e-01, 8.26383630e-01, 9.15547936e-01, 1.04957529e+00, 1.20322295e+00, 1.58128854e+00, 1.75190482e+00, 2.22506344e+00, 2.22506344e+00, 3.13093226e+00, 3.13093226e+00, 3.46875042e+00, 4.25766823e+00, 4.40559879e+00, 4.88094963e+00, 5.05053580e+00, 5.40758940e+00, 5.78988534e+00, 6.19920813e+00, 6.63746849e+00, 7.35363135e+00, 7.60912961e+00, 8.14706603e+00, 8.14706603e+00, 8.72303250e+00, 8.72303250e+00, 8.72303250e+00, 9.02610992e+00, 9.33971761e+00, 1.00000000e+01, 1.00000000e+01, 1.00000000e+01, 1.00000000e+01, 1.03474450e+01, 1.03474450e+01, 1.07069618e+01, 1.10789699e+01, 1.10789699e+01, 1.14639032e+01, 1.18622108e+01, 1.18622108e+01, 1.22743574e+01, 1.31421076e+01, 1.31421076e+01, 1.35987236e+01, 1.40712044e+01, 1.40712044e+01, 1.40712044e+01, 1.40712044e+01, 1.40712044e+01, 1.40712044e+01, 1.40712044e+01, 1.40712044e+01, 1.50659849e+01, 1.50659849e+01, 1.55894450e+01, 1.61310925e+01, 1.61310925e+01, 1.61310925e+01, 1.66915593e+01, 1.84925283e+01])*1e6
y = np.array([4.73887961e+07, 6.07832313e+07, 7.79636013e+07, 1.00000000e+08, 1.36500781e+08, 1.92213454e+08, 2.38989257e+08, 3.36532512e+08, 5.36697695e+08, 6.27042962e+08, 9.10876420e+08, 1.13254132e+09, 1.36500781e+09, 1.80616223e+09, 2.24569800e+09, 2.79219629e+09, 3.93182876e+09, 4.05609490e+09, 5.36697695e+09, 7.32596543e+09, 9.69363106e+09, 1.28264983e+10, 1.80616223e+10, 2.46542555e+10, 3.26222201e+10, 4.45295851e+10, 5.71158648e+10, 8.04276548e+10, 1.03160518e+11, 1.36500781e+11, 1.75082703e+11, 2.46542555e+11, 3.36532512e+11, 3.69460121e+11, 4.73887961e+11, 5.36697695e+11, 6.67304916e+11, 9.10876420e+11, 1.13254132e+12, 1.13254132e+12, 9.39664831e+11, 8.82969996e+11, 5.89210219e+11, 4.73887961e+11, 7.32596543e+11, 3.06539530e+11, 2.46542555e+11, 1.69718713e+11, 1.36500781e+11, 8.55918537e+10, 7.32596543e+10, 8.82969996e+10, 8.29695852e+10, 8.29695852e+10, 8.55918537e+10, 9.10876420e+10, 8.04276548e+10, 8.04276548e+10, 7.32596543e+10, 7.55750387e+10, 5.04315949e+10, 6.07832313e+10, 4.05609490e+10, 2.38989257e+10, 3.16227766e+10, 1.64519059e+10, 1.86324631e+10, 1.13254132e+10, 2.17689678e+10, 2.97148110e+10, 1.45265393e+10, 5.36697695e+10, 4.18428851e+10, 6.07832313e+10, 7.79636013e+10, 8.82969996e+10, 9.39664831e+10, 8.55918537e+10, 9.10876420e+10, 8.29695852e+10, 8.82969996e+10, 9.10876420e+10, 8.82969996e+10, 8.82969996e+10, 8.82969996e+10, 8.29695852e+10, 8.29695852e+10, 7.32596543e+10, 7.32596543e+10, 6.88395207e+10, 6.88395207e+10, 6.67304916e+10, 7.10152060e+10, 6.67304916e+10, 6.88395207e+10, 7.32596543e+10, 7.32596543e+10, 7.32596543e+10, 7.32596543e+10, 6.88395207e+10, 7.10152060e+10, 7.32596543e+10, 7.32596543e+10, 7.32596543e+10, 7.32596543e+10, 8.29695852e+10, 8.29695852e+10, 8.29695852e+10, 8.29695852e+10, 8.29695852e+10, 8.55918537e+10, 8.55918537e+10, 8.55918537e+10, 8.55918537e+10, 9.10876420e+10, 9.10876420e+10, 9.69363106e+10, 9.39664831e+10, 9.39664831e+10, 9.69363106e+10, 1.20526094e+11, 1.49856531e+11, 1.75082703e+11, 2.11020343e+11, 2.70665207e+11, 3.26222201e+11, 3.93182876e+11, 4.45295851e+11, 4.18428851e+11, 4.05609490e+11, 3.69460121e+11, 3.69460121e+11, 2.97148110e+11, 2.54334576e+11, 2.04555335e+11, 1.69718713e+11, 1.40814912e+11, 1.09784377e+11, 9.39664831e+10, 7.55750387e+10, 5.53660121e+10, 3.81136974e+10, 3.16227766e+10, 2.79219629e+10, 1.32318821e+10, 2.04555335e+10, 2.17689678e+10, 1.69718713e+10, 1.24335342e+10, 1.16833549e+10, 1.00000000e+10, 8.55918537e+09, 6.27042962e+09, 1.69718713e+10, 4.59369506e+09, 3.16227766e+09, 2.70665207e+09, 3.47168682e+09, 1.59478706e+09, 1.98288395e+09, 1.75082703e+09, 1.36500781e+09, 9.69363106e+08, 4.45295851e+08, 7.79636013e+08, 3.47168682e+08, 1.20526094e+08, 1.92213454e+08, 2.79219629e+08, 6.07832313e+07, 8.29695852e+07, 9.10876420e+07, 6.07832313e+08, 1.36500781e+08, 4.73887961e+07, 7.79636013e+07, 5.89210219e+07, 3.36532512e+07, 2.38989257e+07, 4.05609490e+07, 1.80616223e+07, 2.31667368e+07])

def loglog_interpolation(xmin, xmax, interval, x, y):
    sorted_idx = np.argsort(x)
    x = x[sorted_idx]
    y = y[sorted_idx]
    logx = np.log10(x)
    logy = np.log10(y)
    log_interp = interp1d(logx, logy, kind='linear', fill_value='extrapolate')
    def loglog_interpolate(x_query):
        return 10**log_interp(np.log10(x_query))
    x_query = np.logspace(np.log10(xmin), np.log10(xmax), interval)
    y_query = loglog_interpolate(x_query)
    return x_query, y_query

#Interpolations of Energy and fluxes per energy
Energies_eV, Fluxes_per_m2s = loglog_interpolation(1e-4, 20E6, 1000, x, y)

#other constants
NA = 6.02214076e23 # 1/mol
barn2cm2 = 1e-24 # cm^2
rho = 10.97 # g/cm^3 (given)

def cleanXsE(ener , xs):
    #sort, ascending E
    idx = np.argsort(ener)
    ener = ener[idx]
    xs   = xs[idx]

    #remove dups
    ener, unique_idx = np.unique(ener, return_index=True)
    xs = xs[unique_idx]
    return ener, xs

#returns a lot of stuff
# to use when called
# en235 , xs235 , en238 , xs238 , xs235_e , xs238_e , arrXS235 , arrXS238 = dataExtractorF()
def dataExtractorF(loc235 , loc238):
    ener235 = []
    xs235 = []
    with open(loc235, 'r') as f235:
        data235 = json.load(f235)
    
    nameEnrich = data235["datasets"][0]["TARGET"]


    for point in (data235["datasets"][0]["pts"]):
        ener235.append(point["E"])  
        xs235.append(point["Sig"])

    #238 
    ener238 = []
    xs238 = []
    with open(loc238, 'r') as f238:
        data238 = json.load(f238)

    for point in (data238["datasets"][0]["pts"]):
        ener238.append(point["E"]) 
        xs238.append(point["Sig"])

    nameRemain = data238["datasets"][0]["TARGET"]

    #Contvert to numpy arrays
    ener235 = np.array(ener235)
    xs235 = np.array(xs235)

    ener238 = np.array(ener238)
    xs238 = np.array(xs238)

    ener235, xs235 = cleanXsE(ener235, xs235)
    ener238, xs238 = cleanXsE(ener238, xs238)

    #interpolation functions
    #create interpolation functions
    xs235_e = interp1d(ener235, xs235, kind='linear', fill_value='extrapolate')
    xs238_e = interp1d(ener238, xs238, kind='linear', fill_value='extrapolate')

    #create array of xs corresponding to E array w/ interp funcs
    arrXS235 = xs235_e(Energies_eV)
    arrXS238 = xs238_e(Energies_eV)

    massEnrich = nameEnrich.split('-')[1]
    massEnrich = float(massEnrich)
    massRemain = nameRemain.split('-')[1]
    massRemain = float(massRemain)

    return ener235 , xs235 , ener238 , xs238 , xs235_e , xs238_e , arrXS235 , arrXS238, nameEnrich , nameRemain , massEnrich , massRemain

def nDense(enrich , massEn , massRe):
    num = fuelDensity * NA
    denom = (float(massEn) * float(enrich)) + (float(massRe) * (1 - float(enrich)))
    return num / denom

#requires interpolated Functions
def reactionRate_Enrich(enrichments , xs235_e , xs238_e , massEn , massRe):
    rr_results = {}
    for enrich in enrichments:
        Ntot = nDense(enrich , massEn , massRe)
        N235 = Ntot * enrich
        N238 = Ntot * (1-enrich)

        rr = np.empty_like(Energies_eV, dtype=float)
        for ind, Ei in enumerate(Energies_eV):
            sig235 = xs235_e(Ei)
            sig238 = xs238_e(Ei)
            macroXS = (N235*sig235 + N238*sig238)* barn2cm2
            rr[ind] = macroXS * (Fluxes_per_m2s[ind] * 1e-4)  # convert flux to cm^2)
        rr_results[enrich] = rr
    return rr_results

#power per unit volume as function of energy
#unit of volume = 1cm^3
def powerPerVol_Enrich(enrichments , xs235_e , xs238_e, massEn , massRe):
    sol = reactionRate_Enrich(enrichments , xs235_e , xs238_e, massEn , massRe)
    enPerReact = energyPerFission * (1.60218e-13)

    for k in sol:
        sol[k] = sol[k] * enPerReact
    return sol

def powerInt_Enrich(enrichments , xs235_e , xs238_e, massEn , massRe):
    pwrDict = powerPerVol_Enrich(enrichments , xs235_e , xs238_e , massEn , massRe)
    
    powers = {}
    lnE = np.log(Energies_eV)
    for i in pwrDict:
        pw = np.trapz(pwrDict[i] * Energies_eV , lnE)
        powers[i] = pw
    return powers
#It's finally over