import QiskitConfig
import qiskit as qk
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, IBMQ


qk.IBMQ.enable_account(QiskitConfig.ApiToken)
ibmprocessor = qk.IBMQ.get_backend('ibmqx4')


Qr1 = qk.QuantumRegister(1)
Cr1 = qk.ClassicalRegister(1)
Cir1 = qk.QuantumCircuit(Qr1,Cr1)


Cir1.measure(Qr1,Cr1)

Job = execute(Cir1,ibmprocessor)
res = Job.result()

print(res)
