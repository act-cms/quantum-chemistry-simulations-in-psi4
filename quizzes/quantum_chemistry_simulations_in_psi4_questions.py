bo_energy = [
    {
        "question": "Within the Born-Oppenheimer approximation, the exact energy of molecular hydrogen is -1.17425 Hartree. What is a reasonable value for the exact energy of molecular hydrogen obtained by solving the Schroedinger equation using the full molecular Hamiltonian $\hat{H}_{molecular}$?",
        "type": "many_choice",
        "answers": [
            {"answer": "-1.17477 Hartree", "correct": False, "feedback": "Think about what term are neglected in the Born-Oppenheimer approximation and whether or not they raise or lower the energy?"},
            {"answer": "-1.17425 Hartree", "correct": False, "feedback": "Think about it. If the energies are  the same, then the Born-Oppenheimer and full Hamiltonians should also be the same. Is that so?"},
            {"answer": "-1.17373 Hartree", "correct": True, "feedback": "That is correct. Including the kinetic energy contributions from nuclear motion raises the energy."},
            {"answer": "I have no idea.", "correct": False, "feedback": "Maybe you should read the section on the Born-Oppenheimer approximation given above."}
        ]
    }
]

pople_diagram = [
    {
        "question": "Which combination of eletron correlation treatment and basis set would result in the most accurate solution of the Schroedinger equation within the Born-Oppenheimer approximation?",
        "type": "many_choice",
        "answers": [
            {"answer": "HF / cc-pVDZ", "correct": False, "feedback": "If you look at the Pople diagram, you will see that this calculation uses a relatively small basis set and treatment of electron correlation is rather crude."},
            {"answer": "HF / cc-pVQZ", "correct": False, "feedback": "If you look at the Pople diagram, you will see that this calculation uses a large basis set but treatment of electron correlation is rather crude."},
            {"answer": "CCSD(T) / cc-pVDZ", "correct": False, "feedback": "If you look at the Pople diagram, you will see that this calculation uses a relatively small basis set but treatment of electron correlation is sophisticated."},
            {"answer": "CCSD(T) / cc-pVQZ", "correct": True, "feedback": "If you look at the Pople diagram, you will see that this calculation use a relatively large basis set and treatment of electron correlation is sophisticated."}
        ]
    }
]

number_AOs = [
    {
        "question": "In the cc-pVTZ basis set, the number of AOs included for Cl is",
        "type": "many_choice",
        "answers": [
            {"answer": "4", "correct": False, "feedback": "Not quite. Looking at the table above, you seem to have picked the number of types of AOs included for Cl."},
            {"answer": "10", "correct": False, "feedback": "Not quite. Looking at the table above, you do not seem to have considered the number of AOs in a subshell (i.e. there are 3 p orbitals in a p subshell)"},
            {"answer": "14", "correct": False, "feedback": "Not quite. Looking at the table above, you seem to be on the right track, but you did not correctly identify what period Cl is in."},
            {"answer": "30", "correct": True, "feedback": "That is correct!"}
        ]
    }
]

correlation_energy = [
    {
        "question": "At $R_{HF} = 100$ pm, the RHF energy in a cc-pVTZ basis set is -100.048 Hartree. At the same bond distance and using the same basis set, which of the following is a reasonable value for the CISD energy?",
        "type": "many_choice",
        "answers": [
            {"answer": "-99.768 Hartree", "correct": False, "feedback": "Not quite. Does including the effects of instantaneous electron repulsion raise or lower the energy?"},
            {"answer": "-100.048 Hartree", "correct": False, "feedback": "Not quite. This result would imply that RHF and CISD treat electron-electron repulsion at the same level."},
            {"answer": "-100.328 Hartree", "correct": True, "feedback": "Not quite. Including the effects of the instantaneous repulsion between electrons lowers the energy relative to RHF."},
            {"answer": "I have no clue!", "correct": False, "feedback": "It is best if you go back and read the above section on how including the effects of the instantaneous repulsion between electrons affects the energy."}
        ]
    }
]

#QUIZZES = {"num_q": num_q , "many_q": many_q}
