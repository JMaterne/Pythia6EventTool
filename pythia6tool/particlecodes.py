# -*- coding: utf-8 -*-

#Non exhaustive dictionary for particle codes created with the help of a LLM. Better to be checked again against Pythia6 Manual.
particle_codes_dict = {
    1: "d",
    2: "u",
    3: "s",
    4: "c",
    5: "b",
    6: "t",
    7: "b'",
    8: "t'",
    11: "e-",
    12: "νe",
    13: "μ-",
    14: "νμ",
    15: "τ-",
    16: "ντ",
    17: "τ'",
    18: "ν'τ",
    21: "g",
    22: "γ",
    23: "Z0",
    24: "W+",
    25: "h0",
    26: None,  # KF 26 without name
    27: None,  # KF 27 without name
    28: None,  # KF 28 without name
    29: None,  # KF 29 without name
    30: None,  # KF 30 without name
    31: None,  # KF 31 without name
    32: "Z′0",
    33: "Z′′0",
    34: "W′+",
    35: "H0",
    36: "A0",
    37: "H+",
    38: None,  # KF 38 without name
    39: "G",
    40: None,  # KF 40 without name
    41: "R0",
    42: "LQ",
    81: "specflav",  # Spectator flavour; used in decay-product listings
    82: "rndmflav",  # A random u, d, or s flavour; possible decay product
    83: "phasespa",  # Simple isotropic phase-space decay
    84: "c-hadron",  # Information on decay of generic charm hadron
    85: "b-hadron",  # Information on decay of generic bottom hadron
    86: None,  # KF 86 without name
    87: None,  # KF 87 without name
    88: None,  # KF 88 without name
    89: "(internal use for unspecified resonance data)",  # KF 89
    90: "system",  # Intermediate pseudoparticle in external process
    91: "cluster",  # Parton system in cluster fragmentation
    92: "string",  # Parton system in string fragmentation
    93: "indep.",  # Parton system in independent fragmentation
    94: "CMshower",  # Four-momentum of time-like showering system
    95: "SPHEaxis",  # Event axis found with PYSPHE
    96: "THRUaxis",  # Event axis found with PYTHRU
    97: "CLUSjet",  # Jet (cluster) found with PYCLUS
    98: "CELLjet",  # Jet (cluster) found with PYCELL
    99: "table",  # Tabular output from PYTABU
    1103: "dd1",  # dd 1
    2101: "ud0",  # ud 0
    2103: "ud1",  # ud 1
    2203: "uu1",  # uu 1
    3101: "sd0",  # sd 0
    3103: "sd1",  # sd 1
    3201: "su0",  # su 0
    3203: "su1",  # su 1
    3303: "ss1",  # ss 1
    211: "π+",  # pi+
    213: "ρ+",  # rho+
    311: "K0",  # K0
    313: "K∗0",  # K*0
    321: "K+",  # K+
    323: "K∗+",  # K*+
    411: "D+",  # D+
    413: "D∗+",  # D*+
    421: "D0",  # D0
    423: "D∗0",  # D*0
    431: "D+s",  # D s+
    433: "D∗+s",  # D*+ s
    511: "B0",  # B0
    513: "B∗0",  # B*0
    521: "B+",  # B+
    523: "B∗+",  # B*+
    531: "B0s",  # B s0
    533: "B∗0s",  # B*0 s
    541: "B+",  # B+
    543: "B∗+",  # B*+
    111: "π0",  # pi0
    113: "ρ0",  # rho0
    221: "η",  # eta
    223: "ω",  # omega
    331: "η′",  # eta'
    333: "φ",  # phi
    441: "ηc",  # eta c
    443: "J/ψ",  # J/psi
    551: "ηb",  # eta b
    553: "Υ",  # Upsilon
    130: "K0L",  # K L0
    310: "K0S",  # K S0
    10213: "b1",  # b 1+
    10211: "a+",  # a+
    0: "a",  # a 0+
    10313: "K0",  # K0
    10311: "K∗0",  # K*0
    10323: "K+",  # K+
    10321: "K∗+",  # K*+
    10413: "D+",  # D+
    10411: "D∗+",  # D*+
    10423: "D0",  # D0
    10421: "D∗0",  # D*0
    10433: "D+s",  # D s+
    10431: "D∗+s",  # D*+ s
    10113: "b0",  # b0
    10111: "a0",  # a0
    10223: "h0",  # h0
    10221: "f0",  # f0
    10333: "h′0",  # h'0
    10331: "f′0",  # f'0
    10443: "h0",  # h0
    10441: "χ0",  # chi 0
    20213: "a+",  # a+ 1+
    215: "a+",  # a+ 2+
    20313: "K∗0",  # K*0 1+
    315: "K∗0",  # K*0 2+
    20323: "K∗+",  # K*+ 1+
    325: "K∗+",  # K*+ 2+
    20413: "D∗+",  # D*+ 1+
    415: "D∗+",  # D*+ 2+
    20423: "D∗0",  # D*0 1+
    425: "D∗0",  # D*0 2+
    20433: "D∗+s",  # D*+ s 1+
    435: "D∗+s",  # D*+ s 2+
    20113: "a0",  # a0 1+
    115: "a0",  # a0 2+
    20223: "f0",  # f0 1+
    225: "f0",  # f0 2+
    20333: "f′0",  # f'0 1+
    335: "f′0",  # f'0 2+
    20443: "χ0",  # χ0 1+
    445: "χ0",  # χ0 2+
    100443: "ψ′",  # psi'
    100553: "Υ′",  # Upsilon'
    1114: "∆−",  # Delta-
    2112: "n",  # n0
    2114: "∆0",  # Delta0
    2212: "p",  # p+
    2214: "∆+",  # Delta+
    2224: "∆++",  # Delta++
    3112: "Σ−",  # Sigma-
    3114: "Σ∗−",  # Sigma*- 
    3122: "Λ0",  # Lambda0
    3212: "Σ0",  # Sigma0
    3214: "Σ∗0",  # Sigma*0
    3222: "Σ+",  # Sigma+
    3224: "Σ∗+",  # Sigma*+
    3312: "Ξ−",  # Xi-
    3314: "Ξ∗−",  # Xi*-
    3322: "Ξ0",  # Xi0
    3324: "Ξ∗0",  # Xi*0
    3334: "Ω−",  # Omega-
    4112: "Σ0c",  # Sigma c0
    4114: "Σ∗0c",  # Sigma* c0
    4122: "Λ+c",  # Lambda c+
    4212: "Σ+c",  # Sigma c+
    4214: "Σ∗+c",  # Sigma* c+
    4222: "Σ++c",  # Sigma++ c
    4224: "Σ∗++c",  # Sigma*++ c
    4232: "Ξ+c",  # Xi c+
    4322: "Ξ′+c",  # Xi’ c+
    4324: "Ξ∗+c",  # Xi* c+
    4332: "Ω0c",  # Omega c0
    4334: "Ω∗0c",  # Omega* c0
    110: "reggeon",
    990: "pomeron",
    9900110: "rho",
    9900210: "pi",
    9900220: "omega",
    9900330: "phi",
    9900440: "J/psi",
    9902110: "n",
    9902210: "p"
}

def getParticleName(particlecode):
    if particlecode < 0:
        return 'anti ' + particle_codes_dict[-particlecode]
    else:
        return particle_codes_dict[particlecode]
