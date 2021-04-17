from circuit_components import ParallelResistor
from PySpice.Spice.Netlist import Circuit, SubCircuit
from PySpice.Unit import *

circuit = Circuit('Test')

circuit.subcircuit(ParallelResistor(R2=3@u_Ω))
circuit.X('1', 'parallel_resistor', 1, circuit.gnd)

print(circuit)