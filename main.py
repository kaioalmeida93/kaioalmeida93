# Faz tudo
from numpy.core.defchararray import upper
import os

# Digite os dados
print("Os dados abaixo são em relação à característica do chassis e, portanto, está vinculada ao CRLV")
print("Em todas as entradas o caracter tem que estar em maiúsculo")
chassis = str(upper(input("Digite o número do chassis: ")))
marca = str(upper(input("Digite a Marca/Modelo da forma como aparece no documento: ")))
FAB = str(upper(input("Digite o ANO FABRICAÇÃO como aparece no documento - Formato AAAA: ")))
MOD = str(upper(input("Digite o ANO MODELO como aparece no documento - Formato AAAA: ")))
POT = str(upper(input("Digite a POTÊNCIA da forma como aparece no documento - somente número: ")))
print("Os dados abaixo são em relação à característica da carroceria e, portanto, não está vinculada ao CRLV")
PTS = str(upper(input("Digite o número de portas do veículo: ")))
BRT = str(upper(input("O veículo pertence ao Sistema BRT Move? Digite S para Sim e N para Não: ")))
Linha = int(upper(input("Qual é a linha planejada para operação do veículo? ")))

#Define Carroceria
if marca == 'AGRALE/INDUSCAR FOZ R': ModCar = str('INDUSCAR FOZ R')
if marca == 'M.BENZ/INDUSCAR FOZ R': ModCar = str('INDUSCAR FOZ R')
if marca == 'MBB/INDUSCAR FOZ R': ModCar = str('INDUSCAR FOZ R')
if marca == 'MBENZ/INDUSCAR FOZ R': ModCar = str('INDUSCAR FOZ R')
if marca == 'VOLVO/INDUSCAR FOZ R': ModCar = str('INDUSCAR FOZ R')
if marca == 'VW/INDUSCAR FOZ R': ModCar = str('INDUSCAR FOZ R')
if marca == 'M. BENZ/MPOLO IDEALE R': ModCar = str('MPOLO IDEALE R')
if marca == 'M. BENZ/INDUSCAR PICCO O': ModCar = str('INDUSCAR PICCO O')
if marca == 'AGRALE/MASCA GRANMICRO O': ModCar = str('MASCA GRANMICRO O')
if marca == 'M.BENZ/MASCA GRANMICRO O': ModCar = str('MASCA GRANMICRO O')
if marca == 'MBB/MASCA GRANMICRO O': ModCar = str('MASCA GRANMICRO O')
if marca == 'MBENZ/MASCA GRANMICRO O': ModCar = str('MASCA GRANMICRO O')
if marca == 'VOLVO/MASCA GRANMICRO O': ModCar = str('MASCA GRANMICRO O')
if marca == 'VW/MASCA GRANMICRO O': ModCar = str('MASCA GRANMICRO O')
if marca == 'MARCOPOLO/VOLARE V8 MO': ModCar = str('VOLARE V8')
if marca == 'AGRALE/NEOBUS TH O': ModCar = str('NEOBUS TH O')
if marca == 'M.BENZ/NEOBUS TH O': ModCar = str('NEOBUS TH O')
if marca == 'MBB/NEOBUS TH O': ModCar = str('NEOBUS TH O')
if marca == 'MBENZ/NEOBUS TH O': ModCar = str('NEOBUS TH O')
if marca == 'VOLVO/NEOBUS TH O': ModCar = str('NEOBUS TH O')
if marca == 'VW/NEOBUS TH O': ModCar = str('NEOBUS TH O')
if marca == 'AGRALE/BUSSCAR URBANUSS U': ModCar = str('BUSSCAR URBANUSS U')
if marca == 'AGRALE/BUSSCAR URBPLUS U': ModCar = str('BUSSCAR URBPLUS U')
if marca == 'AGRALE/BUSSCAR VIS BUSS R': ModCar = str('BUSSCAR VIS BUSS R')
if marca == 'AGRALE/CIFERAL CITIMAX U': ModCar = str('CIFERAL CITIMAX U')
if marca == 'AGRALE/CIFERAL CITMAX U': ModCar = str('CIFERAL CITMAX U')
if marca == 'AGRALE/COMIL CAMPIONE R': ModCar = str('COMIL CAMPIONE R')
if marca == 'AGRALE/COMIL DOPPIO A': ModCar = str('COMIL DOPPIO A')
if marca == 'AGRALE/COMIL SVELTO U': ModCar = str('COMIL SVELTO U')
if marca == 'AGRALE/COMIL VERSATILE R': ModCar = str('COMIL VERSATILE R')
if marca == 'AGRALE/INDUCAR APACHE U': ModCar = str('INDUCAR APACHE U')
if marca == 'AGRALE/INDUSCAR APACHE A': ModCar = str('INDUSCAR APACHE A')
if marca == 'AGRALE/INDUSCAR APACHE U': ModCar = str('INDUSCAR APACHE U')
if marca == 'AGRALE/INDUSCAR FOZ O LO': ModCar = str('INDUSCAR FOZ O LO')
if marca == 'AGRALE/INDUSCAR FOZ U': ModCar = str('INDUSCAR FOZ U')
if marca == 'AGRALE/INDUSCAR GI R': ModCar = str('INDUSCAR GI R')
if marca == 'AGRALE/INDUSCAR MILLE H U': ModCar = str('INDUSCAR MILLE H U')
if marca == 'AGRALE/INDUSCAR MILLEN U': ModCar = str('INDUSCAR MILLEN U')
if marca == 'AGRALE/INDUSCAR SOLAR R': ModCar = str('INDUSCAR SOLAR R')
if marca == 'AGRALE/MA150 NEOBUS SPEC': ModCar = str('MA150 NEOBUS SPEC')
if marca == 'AGRALE/MASCA GRANMIDI O': ModCar = str('MASCA GRANMIDI O')
if marca == 'AGRALE/MASCA GRANVIA': ModCar = str('MASCA GRANVIA')
if marca == 'AGRALE/MASCA GRANVIA LO': ModCar = str('MASCA GRANVIA LO')
if marca == 'AGRALE/MASCA GRANVIA O': ModCar = str('MASCA GRANVIA LO')
if marca == 'AGRALE/MPOLO SEM MIDI ON': ModCar = str('MPOLO SEM MIDI ON')
if marca == 'AGRALE/MPOLO SEN MIDI ON': ModCar = str('MPOLO SEN MIDI ON')
if marca == 'AGRALE/MPOLO SENIOR ON': ModCar = str('MPOLO SENIOR ON')
if marca == 'AGRALE/MPOLO SENIOR R': ModCar = str('MPOLO SENIOR R')
if marca == 'AGRALE/MPOLO TORINO GVU': ModCar = str('MPOLO TORINO GVU')
if marca == 'AGRALE/MPOLO TORINO U': ModCar = str('MPOLO TORINO U')
if marca == 'AGRALE/MPOLO VIAGGIO R': ModCar = str('MPOLO VIAGGIO R')
if marca == 'AGRALE/MPOLO VIALE A': ModCar = str('MPOLO VIALE A')
if marca == 'AGRALE/NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'AGRALE/NEOBUS MEGA U': ModCar = str('NEOBUS MEGA U')
if marca == 'AGRALE/NEOBUS MEGABRT A': ModCar = str('NEOBUS MEGABRT A')
if marca == 'AGRALE/NEOBUS SP U': ModCar = str('NEOBUS SP U')
if marca == 'AGRALE/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'AGRALE/OF 1722M NEOBUS MG': ModCar = str('OF 1722M NEOBUS MG')
if marca == 'AGRALE/OF01722M NEOBUS MG': ModCar = str('OF01722M NEOBUS MG')
if marca == 'AGRALE/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'AGRALE/OF1722M NEOBUS MG': ModCar = str('OF1722M NEOBUS MG')
if marca == 'AGRALE/POLO TORINO GVU': ModCar = str('POLO TORINO GVU')
if marca == 'M.BENZ/BUSSCAR URBANUSS U': ModCar = str('BUSSCAR URBANUSS U')
if marca == 'M.BENZ/BUSSCAR URBPLUS U': ModCar = str('BUSSCAR URBPLUS U')
if marca == 'M.BENZ/BUSSCAR VIS BUSS R': ModCar = str('BUSSCAR VIS BUSS R')
if marca == 'M.BENZ/CIFERAL CITIMAX U': ModCar = str('CIFERAL CITIMAX U')
if marca == 'M.BENZ/CIFERAL CITMAX U': ModCar = str('CIFERAL CITMAX U')
if marca == 'M.BENZ/COMIL CAMPIONE R': ModCar = str('COMIL CAMPIONE R')
if marca == 'M.BENZ/COMIL DOPPIO A': ModCar = str('COMIL DOPPIO A')
if marca == 'M.BENZ/COMIL SVELTO U': ModCar = str('COMIL SVELTO U')
if marca == 'M.BENZ/COMIL VERSATILE R': ModCar = str('COMIL VERSATILE R')
if marca == 'M.BENZ/INDUCAR APACHE U': ModCar = str('INDUCAR APACHE U')
if marca == 'M.BENZ/INDUSCAR APACHE A': ModCar = str('INDUSCAR APACHE A')
if marca == 'M.BENZ/INDUSCAR APACHE U': ModCar = str('INDUSCAR APACHE U')
if marca == 'M.BENZ/INDUSCAR FOZ O LO': ModCar = str('INDUSCAR FOZ O LO')
if marca == 'M.BENZ/INDUSCAR FOZ U': ModCar = str('INDUSCAR FOZ U')
if marca == 'M.BENZ/INDUSCAR GI R': ModCar = str('INDUSCAR GI R')
if marca == 'M.BENZ/INDUSCAR MILLE H U': ModCar = str('INDUSCAR MILLE H U')
if marca == 'M.BENZ/INDUSCAR MILLEN U': ModCar = str('INDUSCAR MILLEN U')
if marca == 'M.BENZ/INDUSCAR SOLAR R': ModCar = str('INDUSCAR SOLAR R')
if marca == 'M.BENZ/MASCA GRANMIDI O': ModCar = str('MASCA GRANMIDI O')
if marca == 'M.BENZ/MASCA GRANVIA': ModCar = str('MASCA GRANVIA')
if marca == 'M.BENZ/MASCA GRANVIA LO': ModCar = str('MASCA GRANVIA LO')
if marca == 'M.BENZ/MASCA GRANVIA O': ModCar = str('MASCA GRANVIA LO')
if marca == 'M.BENZ/MPOLO SEM MIDI ON': ModCar = str('MPOLO SEM MIDI ON')
if marca == 'M.BENZ/MPOLO SEN MIDI ON': ModCar = str('MPOLO SEN MIDI ON')
if marca == 'M.BENZ/MPOLO SENIOR ON': ModCar = str('MPOLO SENIOR ON')
if marca == 'M.BENZ/MPOLO SENIOR R': ModCar = str('MPOLO SENIOR R')
if marca == 'M.BENZ/MPOLO TORINO GVU': ModCar = str('MPOLO TORINO GVU')
if marca == 'M.BENZ/MPOLO TORINO U': ModCar = str('MPOLO TORINO U')
if marca == 'M.BENZ/MPOLO VIAGGIO R': ModCar = str('MPOLO VIAGGIO R')
if marca == 'M.BENZ/MPOLO VIALE A': ModCar = str('MPOLO VIALE A')
if marca == 'M.BENZ/NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'M.BENZ/NEOBUS MEGA U': ModCar = str('NEOBUS MEGA U')
if marca == 'M.BENZ/NEOBUS MEGABRT A': ModCar = str('NEOBUS MEGABRT A')
if marca == 'M.BENZ/NEOBUS SP U': ModCar = str('NEOBUS SP U')
if marca == 'M.BENZ/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'M.BENZ/OF 1722M NEOBUS MG': ModCar = str('OF 1722M NEOBUS MG')
if marca == 'M.BENZ/OF01722M NEOBUS MG': ModCar = str('OF01722M NEOBUS MG')
if marca == 'M.BENZ/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'M.BENZ/OF1722M NEOBUS MG': ModCar = str('OF1722M NEOBUS MG')
if marca == 'M.BENZ/POLO TORINO GVU': ModCar = str('POLO TORINO GVU')
if marca == 'MBB/BUSSCAR URBANUSS U': ModCar = str('BUSSCAR URBANUSS U')
if marca == 'MBB/BUSSCAR URBPLUS U': ModCar = str('BUSSCAR URBPLUS U')
if marca == 'MBB/BUSSCAR VIS BUSS R': ModCar = str('BUSSCAR VIS BUSS R')
if marca == 'MBB/CIFERAL CITIMAX U': ModCar = str('CIFERAL CITIMAX U')
if marca == 'MBB/CIFERAL CITMAX U': ModCar = str('CIFERAL CITMAX U')
if marca == 'MBB/COMIL CAMPIONE R': ModCar = str('COMIL CAMPIONE R')
if marca == 'MBB/COMIL DOPPIO A': ModCar = str('COMIL DOPPIO A')
if marca == 'MBB/COMIL SVELTO U': ModCar = str('COMIL SVELTO U')
if marca == 'MBB/COMIL VERSATILE R': ModCar = str('COMIL VERSATILE R')
if marca == 'MBB/INDUCAR APACHE U': ModCar = str('INDUCAR APACHE U')
if marca == 'MBB/INDUSCAR APACHE A': ModCar = str('INDUSCAR APACHE A')
if marca == 'MBB/INDUSCAR APACHE U': ModCar = str('INDUSCAR APACHE U')
if marca == 'MBB/INDUSCAR FOZ O LO': ModCar = str('INDUSCAR FOZ O LO')
if marca == 'MBB/INDUSCAR FOZ U': ModCar = str('INDUSCAR FOZ U')
if marca == 'MBB/INDUSCAR GI R': ModCar = str('INDUSCAR GI R')
if marca == 'MBB/INDUSCAR MILLE H U': ModCar = str('INDUSCAR MILLE H U')
if marca == 'MBB/INDUSCAR MILLEN U': ModCar = str('INDUSCAR MILLEN U')
if marca == 'MBB/INDUSCAR SOLAR R': ModCar = str('INDUSCAR SOLAR R')
if marca == 'MBB/MASCA GRANMIDI O': ModCar = str('MASCA GRANMIDI O')
if marca == 'MBB/MASCA GRANVIA': ModCar = str('MASCA GRANVIA')
if marca == 'MBB/MASCA GRANVIA LO': ModCar = str('MASCA GRANVIA LO')
if marca == 'MBB/MASCA GRANVIA O': ModCar = str('MASCA GRANVIA LO')
if marca == 'MBB/MPOLO SEM MIDI ON': ModCar = str('MPOLO SEM MIDI ON')
if marca == 'MBB/MPOLO SEN MIDI ON': ModCar = str('MPOLO SEN MIDI ON')
if marca == 'MBB/MPOLO SENIOR ON': ModCar = str('MPOLO SENIOR ON')
if marca == 'MBB/MPOLO SENIOR R': ModCar = str('MPOLO SENIOR R')
if marca == 'MBB/MPOLO TORINO GVU': ModCar = str('MPOLO TORINO GVU')
if marca == 'MBB/MPOLO TORINO U': ModCar = str('MPOLO TORINO U')
if marca == 'MBB/MPOLO VIAGGIO R': ModCar = str('MPOLO VIAGGIO R')
if marca == 'MBB/MPOLO VIALE A': ModCar = str('MPOLO VIALE A')
if marca == 'MBB/NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'MBB/NEOBUS MEGA U': ModCar = str('NEOBUS MEGA U')
if marca == 'MBB/NEOBUS MEGABRT A': ModCar = str('NEOBUS MEGABRT A')
if marca == 'MBB/NEOBUS SP U': ModCar = str('NEOBUS SP U')
if marca == 'MBB/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'MBB/OF 1722M NEOBUS MG': ModCar = str('OF 1722M NEOBUS MG')
if marca == 'MBB/OF01722M NEOBUS MG': ModCar = str('OF01722M NEOBUS MG')
if marca == 'MBB/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'MBB/OF1722M NEOBUS MG': ModCar = str('OF1722M NEOBUS MG')
if marca == 'MBB/POLO TORINO GVU': ModCar = str('POLO TORINO GVU')
if marca == 'MBENZ/BUSSCAR URBANUSS U': ModCar = str('BUSSCAR URBANUSS U')
if marca == 'MBENZ/BUSSCAR URBPLUS U': ModCar = str('BUSSCAR URBPLUS U')
if marca == 'MBENZ/BUSSCAR VIS BUSS R': ModCar = str('BUSSCAR VIS BUSS R')
if marca == 'MBENZ/CIFERAL CITIMAX U': ModCar = str('CIFERAL CITIMAX U')
if marca == 'MBENZ/CIFERAL CITMAX U': ModCar = str('CIFERAL CITMAX U')
if marca == 'MBENZ/COMIL CAMPIONE R': ModCar = str('COMIL CAMPIONE R')
if marca == 'MBENZ/COMIL DOPPIO A': ModCar = str('COMIL DOPPIO A')
if marca == 'MBENZ/COMIL SVELTO U': ModCar = str('COMIL SVELTO U')
if marca == 'MBENZ/COMIL VERSATILE R': ModCar = str('COMIL VERSATILE R')
if marca == 'MBENZ/INDUCAR APACHE U': ModCar = str('INDUCAR APACHE U')
if marca == 'MBENZ/INDUSCAR APACHE A': ModCar = str('INDUSCAR APACHE A')
if marca == 'MBENZ/INDUSCAR APACHE U': ModCar = str('INDUSCAR APACHE U')
if marca == 'MBENZ/INDUSCAR FOZ O LO': ModCar = str('INDUSCAR FOZ O LO')
if marca == 'MBENZ/INDUSCAR FOZ U': ModCar = str('INDUSCAR FOZ U')
if marca == 'MBENZ/INDUSCAR GI R': ModCar = str('INDUSCAR GI R')
if marca == 'MBENZ/INDUSCAR MILLE H U': ModCar = str('INDUSCAR MILLE H U')
if marca == 'MBENZ/INDUSCAR MILLEN U': ModCar = str('INDUSCAR MILLEN U')
if marca == 'MBENZ/INDUSCAR SOLAR R': ModCar = str('INDUSCAR SOLAR R')
if marca == 'MBENZ/MASCA GRANMIDI O': ModCar = str('MASCA GRANMIDI O')
if marca == 'MBENZ/MASCA GRANVIA': ModCar = str('MASCA GRANVIA')
if marca == 'MBENZ/MASCA GRANVIA LO': ModCar = str('MASCA GRANVIA LO')
if marca == 'MBENZ/MASCA GRANVIA O': ModCar = str('MASCA GRANVIA LO')
if marca == 'MBENZ/MPOLO SEM MIDI ON': ModCar = str('MPOLO SEM MIDI ON')
if marca == 'MBENZ/MPOLO SEN MIDI ON': ModCar = str('MPOLO SEN MIDI ON')
if marca == 'MBENZ/MPOLO SENIOR ON': ModCar = str('MPOLO SENIOR ON')
if marca == 'MBENZ/MPOLO SENIOR R': ModCar = str('MPOLO SENIOR R')
if marca == 'MBENZ/MPOLO TORINO GVU': ModCar = str('MPOLO TORINO GVU')
if marca == 'MBENZ/MPOLO TORINO U': ModCar = str('MPOLO TORINO U')
if marca == 'MBENZ/MPOLO VIAGGIO R': ModCar = str('MPOLO VIAGGIO R')
if marca == 'MBENZ/MPOLO VIALE A': ModCar = str('MPOLO VIALE A')
if marca == 'MBENZ/NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'MBENZ/NEOBUS MEGA U': ModCar = str('NEOBUS MEGA U')
if marca == 'MBENZ/NEOBUS MEGABRT A': ModCar = str('NEOBUS MEGABRT A')
if marca == 'MBENZ/NEOBUS SP U': ModCar = str('NEOBUS SP U')
if marca == 'MBENZ/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'MBENZ/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'MBENZ/OF 1722M NEOBUS MG': ModCar = str('OF 1722M NEOBUS MG')
if marca == 'MBENZ/OF01722M NEOBUS MG': ModCar = str('OF01722M NEOBUS MG')
if marca == 'MBENZ/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'MBENZ/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'MBENZ/OF1722M NEOBUS MG': ModCar = str('OF1722M NEOBUS MG')
if marca == 'MBENZ/POLO TORINO GVU': ModCar = str('POLO TORINO GVU')
if marca == 'VOLVO/BUSSCAR URBANUSS U': ModCar = str('BUSSCAR URBANUSS U')
if marca == 'VOLVO/BUSSCAR URBPLUS U': ModCar = str('BUSSCAR URBPLUS U')
if marca == 'VOLVO/BUSSCAR VIS BUSS R': ModCar = str('BUSSCAR VIS BUSS R')
if marca == 'VOLVO/CIFERAL CITIMAX U': ModCar = str('CIFERAL CITIMAX U')
if marca == 'VOLVO/CIFERAL CITMAX U': ModCar = str('CIFERAL CITMAX U')
if marca == 'VOLVO/COMIL CAMPIONE R': ModCar = str('COMIL CAMPIONE R')
if marca == 'VOLVO/COMIL DOPPIO A': ModCar = str('COMIL DOPPIO A')
if marca == 'VOLVO/COMIL SVELTO U': ModCar = str('COMIL SVELTO U')
if marca == 'VOLVO/COMIL VERSATILE R': ModCar = str('COMIL VERSATILE R')
if marca == 'VOLVO/INDUCAR APACHE U': ModCar = str('INDUCAR APACHE U')
if marca == 'VOLVO/INDUSCAR APACHE A': ModCar = str('INDUSCAR APACHE A')
if marca == 'VOLVO/INDUSCAR APACHE U': ModCar = str('INDUSCAR APACHE U')
if marca == 'VOLVO/INDUSCAR FOZ O LO': ModCar = str('INDUSCAR FOZ O LO')
if marca == 'VOLVO/INDUSCAR FOZ U': ModCar = str('INDUSCAR FOZ U')
if marca == 'VOLVO/INDUSCAR GI R': ModCar = str('INDUSCAR GI R')
if marca == 'VOLVO/INDUSCAR MILLE H U': ModCar = str('INDUSCAR MILLE H U')
if marca == 'VOLVO/INDUSCAR MILLEN U': ModCar = str('INDUSCAR MILLEN U')
if marca == 'VOLVO/INDUSCAR SOLAR R': ModCar = str('INDUSCAR SOLAR R')
if marca == 'VOLVO/MASCA GRANMIDI O': ModCar = str('MASCA GRANMIDI O')
if marca == 'VOLVO/MASCA GRANVIA': ModCar = str('MASCA GRANVIA')
if marca == 'VOLVO/MASCA GRANVIA LO': ModCar = str('MASCA GRANVIA LO')
if marca == 'VOLVO/MASCA GRANVIA O': ModCar = str('MASCA GRANVIA LO')
if marca == 'VOLVO/MPOLO SEM MIDI ON': ModCar = str('MPOLO SEM MIDI ON')
if marca == 'VOLVO/MPOLO SEN MIDI ON': ModCar = str('MPOLO SEN MIDI ON')
if marca == 'VOLVO/MPOLO SENIOR ON': ModCar = str('MPOLO SENIOR ON')
if marca == 'VOLVO/MPOLO SENIOR R': ModCar = str('MPOLO SENIOR R')
if marca == 'VOLVO/MPOLO TORINO GVU': ModCar = str('MPOLO TORINO GVU')
if marca == 'VOLVO/MPOLO TORINO U': ModCar = str('MPOLO TORINO U')
if marca == 'VOLVO/MPOLO VIAGGIO R': ModCar = str('MPOLO VIAGGIO R')
if marca == 'VOLVO/MPOLO VIALE A': ModCar = str('MPOLO VIALE A')
if marca == 'VOLVO/NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'VOLVO/NEOBUS MEGA U': ModCar = str('NEOBUS MEGA U')
if marca == 'VOLVO/NEOBUS MEGABRT A': ModCar = str('NEOBUS MEGABRT A')
if marca == 'VOLVO/NEOBUS SP U': ModCar = str('NEOBUS SP U')
if marca == 'VOLVO/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'VOLVO/OF 1722M NEOBUS MG': ModCar = str('OF 1722M NEOBUS MG')
if marca == 'VOLVO/OF01722M NEOBUS MG': ModCar = str('OF01722M NEOBUS MG')
if marca == 'VOLVO/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'VOLVO/OF1722M NEOBUS MG': ModCar = str('OF1722M NEOBUS MG')
if marca == 'VOLVO/POLO TORINO GVU': ModCar = str('POLO TORINO GVU')
if marca == 'VW/17230EOD NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'VW/BUSSCAR URBANUSS U': ModCar = str('BUSSCAR URBANUSS U')
if marca == 'VW/BUSSCAR URBPLUS U': ModCar = str('BUSSCAR URBPLUS U')
if marca == 'VW/BUSSCAR VIS BUSS R': ModCar = str('BUSSCAR VIS BUSS R')
if marca == 'VW/CIFERAL CITIMAX U': ModCar = str('CIFERAL CITIMAX U')
if marca == 'VW/CIFERAL CITMAX U': ModCar = str('CIFERAL CITMAX U')
if marca == 'VW/COMIL CAMPIONE R': ModCar = str('COMIL CAMPIONE R')
if marca == 'VW/COMIL DOPPIO A': ModCar = str('COMIL DOPPIO A')
if marca == 'VW/COMIL SVELTO U': ModCar = str('COMIL SVELTO U')
if marca == 'VW/COMIL VERSATILE R': ModCar = str('COMIL VERSATILE R')
if marca == 'VW/INDUCAR APACHE U': ModCar = str('INDUCAR APACHE U')
if marca == 'VW/INDUSCAR APACHE A': ModCar = str('INDUSCAR APACHE A')
if marca == 'VW/INDUSCAR APACHE U': ModCar = str('INDUSCAR APACHE U')
if marca == 'VW/INDUSCAR FOZ O LO': ModCar = str('INDUSCAR FOZ O LO')
if marca == 'VW/INDUSCAR FOZ U': ModCar = str('INDUSCAR FOZ U')
if marca == 'VW/INDUSCAR GI R': ModCar = str('INDUSCAR GI R')
if marca == 'VW/INDUSCAR MILLE H U': ModCar = str('INDUSCAR MILLE H U')
if marca == 'VW/INDUSCAR MILLEN U': ModCar = str('INDUSCAR MILLEN U')
if marca == 'VW/INDUSCAR SOLAR R': ModCar = str('INDUSCAR SOLAR R')
if marca == 'VW/MASCA GRANMIDI EOD O': ModCar = str('MASCA GRANMIDI O')
if marca == 'VW/MASCA GRANMIDI O': ModCar = str('MASCA GRANMIDI O')
if marca == 'VW/MASCA GRANVIA': ModCar = str('MASCA GRANVIA')
if marca == 'VW/MASCA GRANVIA LO': ModCar = str('MASCA GRANVIA LO')
if marca == 'VW/MASCA GRANVIA O': ModCar = str('MASCA GRANVIA LO')
if marca == 'VW/MPOLO SEM MIDI ON': ModCar = str('MPOLO SEM MIDI ON')
if marca == 'VW/MPOLO SEN MIDI ON': ModCar = str('MPOLO SEN MIDI ON')
if marca == 'VW/MPOLO SENIOR ON': ModCar = str('MPOLO SENIOR ON')
if marca == 'VW/MPOLO SENIOR R': ModCar = str('MPOLO SENIOR R')
if marca == 'VW/MPOLO TORINO GVU': ModCar = str('MPOLO TORINO GVU')
if marca == 'VW/MPOLO TORINO U': ModCar = str('MPOLO TORINO U')
if marca == 'VW/MPOLO VIAGGIO R': ModCar = str('MPOLO VIAGGIO R')
if marca == 'VW/MPOLO VIALE A': ModCar = str('MPOLO VIALE A')
if marca == 'VW/NEOBUS MEGA': ModCar = str('NEOBUS MEGA')
if marca == 'VW/NEOBUS MEGA U': ModCar = str('NEOBUS MEGA U')
if marca == 'VW/NEOBUS MEGABRT A': ModCar = str('NEOBUS MEGABRT A')
if marca == 'VW/NEOBUS SP U': ModCar = str('NEOBUS SP U')
if marca == 'VW/OF 1418 NEOBUS SPEC': ModCar = str('OF 1418 NEOBUS SPEC')
if marca == 'VW/OF 1722M NEOBUS MG': ModCar = str('OF 1722M NEOBUS MG')
if marca == 'VW/OF01722M NEOBUS MG': ModCar = str('OF01722M NEOBUS MG')
if marca == 'VW/OF1418 NEOBUS SPEC': ModCar = str('OF1418 NEOBUS SPEC')
if marca == 'VW/OF1722M NEOBUS MG': ModCar = str('OF1722M NEOBUS MG')
if marca == 'VW/POLO TORINO GVU': ModCar = str('POLO TORINO GVU')

# Transforma entrada doc em resultado
if ModCar == 'INDUSCAR PICCO O': CarMod = str('23 - INDUSCAR PICCOLO')
if ModCar == 'INDUSCAR FOZ R': CarMod = str('41 - INDUSCAR FOZ R')
if ModCar == 'VOLARE V8': CarMod = str('36 - VOLARE V8')
if ModCar == 'VOLARE W9': CarMod = str('04 - VOLARE W9')
if ModCar == 'MASCA GRANMICRO O': CarMod = str('42 - MASCARELLO GRANMICRO')
if ModCar == 'BUSSCAR URBANUSS U': CarMod = str('17 - BUSSCAR URBANUSS U')
if ModCar == 'BUSSCAR URBPLUS U': CarMod = str('18 - BUSSCAR URBANUSS PLUSS U')
if ModCar == 'BUSSCAR VIS BUSS R': CarMod = str('19 - BUSSCAR VISSTA BUSS R')
if ModCar == 'CIFERAL CITIMAX U': CarMod = str('24 - CIFERAL CITMAX U')
if ModCar == 'CIFERAL CITMAX U': CarMod = str('24 - CIFERAL CITMAX U')
if ModCar == 'COMIL CAMPIONE R': CarMod = str('06 - COMIL CAMPIONE R')
if ModCar == 'COMIL DOPPIO A': CarMod = str('02 - COMIL DOPPIO A')
if ModCar == 'COMIL SVELTO U': CarMod = str('01 - COMIL SVELTO U')
if ModCar == 'COMIL VERSATILE R': CarMod = str('14 - COMIL VERSATILE R')
if ModCar == 'INDUCAR APACHE U': CarMod = str('38 - INDUSCAR APACHE U')
if ModCar == 'INDUSCAR APACHE A': CarMod = str('38 - INDUSCAR APACHE U')
if ModCar == 'INDUSCAR APACHE U': CarMod = str('38 - INDUSCAR APACHE U')
if ModCar == 'INDUSCAR FOZ U': CarMod = str('21 - INDUSCAR FOZ U')
if ModCar == 'INDUSCAR FOZ O LO': CarMod = str('21 - INDUSCAR FOZ U')
if ModCar == 'INDUSCAR GI R': CarMod = str('20 - INDUSCAR GIRO')
if ModCar == 'INDUSCAR MILLE H U': CarMod = str('37 - INDUSCAR MILLENNIUM U')
if ModCar == 'INDUSCAR MILLEN U': CarMod = str('37 - INDUSCAR MILLENNIUM U')
if ModCar == 'INDUSCAR SOLAR R': CarMod = str('22 - INDUSCAR SOLAR')
if ModCar == 'MASCA GRANMIDI O': CarMod = str('39 - MASCARELLO GRANMIDI')
if ModCar == 'MASCA GRANMIDI EOD O': CarMod = str('39 - MASCARELLO GRANMIDI')
if ModCar == 'MASCA GRANVIA LO': CarMod = str('30 - MASCARELLO GRANVIA')
if ModCar == 'MASCA GRANVIA': CarMod = str('30 - MASCARELLO GRANVIA')
if ModCar == 'MPOLO SEM MIDI ON': CarMod = str('27 - MARCOPOLO SENIOR MIDI')
if ModCar == 'MPOLO SEN MIDI ON': CarMod = str('27 - MARCOPOLO SENIOR MIDI')
if ModCar == 'MPOLO SENIOR ON': CarMod = str('26 - MARCOPOLO SENIOR R')
if ModCar == 'MPOLO IDEALE R': CarMod = str('25 - MARCOPOLO IDEALE R')
if ModCar == 'MPOLO SENIOR R': CarMod = str('26 - MARCOPOLO SENIOR R')
if ModCar == 'MPOLO TORINO GVU': CarMod = str('05 - MARCOPOLO TORINO U')
if ModCar == 'MPOLO TORINO U': CarMod = str('05 - MARCOPOLO TORINO U')
if ModCar == 'MPOLO VIAGGIO R': CarMod = str('09 - MARCOPOLO VIAGGIO R')
if ModCar == 'MPOLO VIALE A': CarMod = str('29 - MARCOPOLO VIALE A')
if ModCar == 'NEOBUS MEGA': CarMod = str('10 - NEOBUS MEGA U')
if ModCar == 'NEOBUS MEGA U': CarMod = str('10 - NEOBUS MEGA U')
if ModCar == 'NEOBUS MEGABRT A': CarMod = str('11 - NEOBUS MEGABRT A')
if ModCar == 'NEOBUS SPECTRUM R': CarMod = str('12 - NEOBUS SPECTRUM 320')
if ModCar == 'NEOBUS TH O': CarMod = str('34 - NEOBUS THUNDER')
if ModCar == 'NEOBUS SP U': CarMod = str('32 - NEOBUS SPECTRUM CITY')
if ModCar == 'MA150 NEOBUS SPEC': CarMod = str('33 - NEOBUS SPECTRUM INTERCITY')
if ModCar == 'OF 1418 NEOBUS SPEC': CarMod = str('32 - NEOBUS SPECTRUM CITY')
if ModCar == 'OF 1722M NEOBUS MG': CarMod = str('10 - NEOBUS MEGA U')
if ModCar == 'OF01722M NEOBUS MG': CarMod = str('10 - NEOBUS MEGA U')
if ModCar == 'OF1418 NEOBUS SPEC': CarMod = str('32 - NEOBUS SPECTRUM CITY')
if ModCar == 'OF1722M NEOBUS MG': CarMod = str('10 - NEOBUS MEGA U')
if ModCar == 'POLO TORINO GVU': CarMod = str('05 - MARCOPOLO TORINO U')

#Define Euro
Ano = int(FAB)

# Monta o armazenamento em caso
if Ano >= 1996:
    if Ano <= 2003:
        Euro = 'EII'
    elif Ano <= 2011:
        Euro = 'EIII'
    elif Ano <= 2023:
        Euro = 'EV'
    elif Ano >= 2024:
        Euro = 'EVI'
else:
    print("ErroEuro")

#Define Chassis
baumus=str(chassis[3:9])
procv=str(baumus+"_"+POT+"_"+Euro)

#Qual é o modelo?
if procv == 'C51A1A_185_EIII':
    ModCha=str("01 - Agrale MA15.0")
elif procv == "C51A1A_190_EV":
    ModCha=str("01 - Agrale MA15.0 EURO V")
elif procv == "384073_211_EII":
    ModCha=str("03 - MBB OF1721")
elif procv == "384076_238_EV":
    ModCha=str("04 - MBB OF1724 EURO V")
elif procv == "382154_354_EV":
    ModCha=str("05 - MBB O500MA/2836 EURO V")
elif procv == "384065_238_EV":
    ModCha=str("07 - MBB OF1724L EURO V")
elif procv == "382176_305_EIII":
    ModCha=str("08 - MBB O500R/1830")
elif procv == "T5T720_270_EV" or "T5T721_270_EV" or "T5T722_270_EV" or "T5T723_270_EV" or "T5T724_270_EV":
    ModCha=str("09 - VOLVO B270F EURO V")
elif procv ==  "T5T725_270_EV" or "T5T726_270_EV" or "T5T727_270_EV" or "T5T728_270_EV":
    ModCha=str("09 - VOLVO B270F EURO V")
elif procv ==   "T5T729_270_EV" or "T5T72X_270_EV" :
    ModCha=str("09 - VOLVO B270F EURO V")
elif procv == "R9F820_340_EIII" or "R9F821_340_EIII" or "R9F822_340_EIII" or "R9F824_340_EIII":
    ModCha=str("12 - VOLVO B12M")
elif procv == "R9F827_340_EIII" or "R9F829_340_EIII" :
    ModCha=str("12 - VOLVO B12M")
elif procv == "384067_185_EV":
    ModCha=str("14 - MBB OF1519 EURO V")
elif procv == "634011_354_EV":
    ModCha=str("15 - MBB O500RS/1836 EURO V")
elif procv == "382177_306_EV" or "382177_310_EV" :
    ModCha=str("16 - MBB O500R/1830 EURO V")
elif procv == "T2S820_370_EV" or "T2S821_370_EV" or "T2S822_370_EV" or "T2S823_370_EV" or "T2S824_370_EV":
    ModCha=str("17 - VOLVO B380R EURO V")
elif procv == "T2S825_370_EV" or "T2S826_370_EV" or "T2S827_370_EV" or "T2S828_370_EV":
    ModCha=str("17 - VOLVO B380R EURO V")
elif procv == "T2S829_370_EV" or "T2S82X_370_EV" :
    ModCha=str("17 - VOLVO B380R EURO V")
elif procv == "R9R320_340_EV" or "R9R321_340_EV" or "R9R322_340_EV" or "R9R323_340_EV" or "R9R324_340_EV":
    ModCha=str("18 - VOLVO B340M EURO V")
elif procv == "R9R325_340_EV" or "R9R326_340_EV" or "R9R327_340_EV" or "R9R328_340_EV" or "R9R329_340_EV":
    ModCha=str("18 - VOLVO B340M EURO V")
elif procv == "R9R32X_340_EV" :
    ModCha=str("18 - VOLVO B340M EURO V")
elif procv == "384078_218_EIII":
    ModCha=str("20 - MBB OF1722M")
elif procv == "384067_177_EIII":
    ModCha=str("21 - MBB OF1418")
elif procv == "T5T510_260_EIII" or "T5T511_260_EIII" or "T5T512_260_EIII" or "T5T513_260_EIII" or "T5T514_260_EIII":
    ModCha=str("22 - VOLVO B270F")
elif procv == "T5T515_260_EIII" or "T5T516_260_EIII" or "T5T517_260_EIII" or "T5T518_260_EIII" or "T5T519_260_EIII":
    ModCha=str("22 - VOLVO B270F")
elif procv == "T5T51X_260_EIII" or "T5T520_260_EIII" or "T5T521_260_EIII" or "T5T522_260_EIII" or "T5T523_260_EIII":
    ModCha=str("22 - VOLVO B270F")
elif procv == "T5T524_260_EIII" or "T5T525_260_EIII" or "T5T526_260_EIII" or "T5T527_260_EIII" or "T5T528_260_EIII":
    ModCha=str("22 - VOLVO B270F")
elif procv == "T5T529_260_EIII" or "T5T52X_260_EIII" :
    ModCha=str("22 - VOLVO B270F")
elif procv == "C22Y1S_150_EIII" or "C32Y1U_150_EIII" :
    ModCha=str("23 - Agrale MA9.2")
elif procv == "B40N31_165_EV":
    ModCha=str("26 - VOLARE W9")
elif procv == "B25M1M_152_EV":
    ModCha=str("27 - VOLARE V8 ESCOLAR")
elif procv == "634011_360_EIII":
    ModCha=str("28 - MBB O500RS/1836")
elif procv == "979277_156_EV":
    ModCha=str("29 - MBB LO916 EURO V")
elif procv == "688276_150_EIII" or "688277_150_EIII" :
    ModCha=str("30 - MBB LO915")
elif procv == "688276_136_EII":
    ModCha=str("31 - MBB LO914")
elif procv == "384078_208_EV":
    ModCha=str("32 - MBB OF1721 EURO V")
elif procv == "384065_208_EV":
    ModCha=str("35 - MBB OF1721L EURO V")
elif procv == "2882W0_185_EIII" or "2882W1_185_EIII" or "2882W2_185_EIII" or "2882W3_185_EIII" or "2882W4_185_EIII":
    ModCha=str("37 - VOLKSWAGEN 15.190EOD")
elif procv == "2882W5_185_EIII" or "2882W6_185_EIII" or "2882W7_185_EIII" or "2882W8_185_EIII" or "2882W9_185_EIII":
    ModCha=str("37 - VOLKSWAGEN 15.190EOD")
elif procv == "2882WX_185_EIII" or "R882W0_185_EIII" or "R882W1_185_EIII" or "R882W2_185_EIII" or "R882W3_185_EIII":
    ModCha=str("37 - VOLKSWAGEN 15.190EOD")
elif procv == "R882W4_185_EIII" or "R882W5_185_EIII" or "R882W6_185_EIII" or "R882W7_185_EIII" or "R882W8_185_EIII":
    ModCha=str("37 - VOLKSWAGEN 15.190EOD")
elif procv == "R882W9_185_EIII" or "R882WX_185_EIII" :
    ModCha=str("37 - VOLKSWAGEN 15.190EOD")
elif procv == "RE82W0_186_EV" or "RE82W1_186_EV" or "RE82W2_186_EV" or "RE82W3_186_EV" or "RE82W4_186_EV":
    ModCha=str("38 - VOLKSWAGEN 15.190OD EURO V")
elif procv == "RE82W5_186_EV" or "RE82W6_186_EV" or "RE82W7_186_EV" or "RE82W8_186_EV" or "RE82W9_186_EV":
    ModCha=str("38 - VOLKSWAGEN 15.190OD EURO V")
elif procv == "RE82WX_186_EV" :
    ModCha=str("38 - VOLKSWAGEN 15.190OD EURO V")
elif procv == "R682W9_180_EIII":
    ModCha=str("39 - VOLKSWAGEN 15.180EOD")
elif procv == "2L82W0_225_EIII" or "2L82W1_225_EIII" or "2L82W2_225_EIII" or "2L82W3_225_EIII" or "2L82W4_225_EIII":
    ModCha=str("40 - VOLKSWAGEN 17.230EOD")
elif procv == "2L82W5_225_EIII" or "2L82W6_225_EIII" or "2L82W7_225_EIII" or "2L82W8_225_EIII" or "2L82W9_225_EIII":
    ModCha=str("40 - VOLKSWAGEN 17.230EOD")
elif procv == "2L82WO_225_EIII" or "2L82WX_225_EIII" or "RL82W0_225_EIII" or "RL82W1_225_EIII" or "RL82W2_225_EIII":
    ModCha=str("40 - VOLKSWAGEN 17.230EOD")
elif procv == "RL82W3_225_EIII" or "RL82W4_225_EIII" or "RL82W5_225_EIII" or "RL82W6_225_EIII" or "RL82W7_225_EIII":
    ModCha=str("40 - VOLKSWAGEN 17.230EOD")
elif procv == "RL82W8_225_EIII" or "RL82W9_225_EIII" or "RL82WX_225_EIII" :
    ModCha=str("40 - VOLKSWAGEN 17.230EOD")
elif procv == "RP82W0_206_EIII" or "RP82W2_206_EIII" or "RP82W3_206_EIII" or "RP82W8_206_EIII" or "RP82W9_206_EIII":
    ModCha=str("41 - VOLKSWAGEN 17.210EOD")
elif procv == "RP82WX_206_EIII" :
    ModCha=str("41 - VOLKSWAGEN 17.210EOD")
elif procv == "RF82W0_206_EII" or "RF82W4_206_EII" or "RF82W6_206_EII" or "RF82W8_206_EII" :
    ModCha=str("42 - VOLKSWAGEN 17.210OD")
elif procv == "_225_EV":
    ModCha=str("43 - VOLKSWAGEN 17.230ODS")
elif procv == "2M62P1_160_EV" or "2M62P2_160_EV" or "2M62P3_160_EV" or "2M62P4_160_EV" or "2M62P5_160_EV":
    ModCha=str("45 - VOLKSWAGEN 9.160OD EURO V")
elif procv == "2M62P6_160_EV" or "2M62P7_160_EV" or "2M62P8_160_EV" or "2M62P9_160_EV" or "2M62PX_160_EV" :
    ModCha=str("45 - VOLKSWAGEN 9.160OD EURO V")
elif procv == "384063_305_EIII":
    ModCha=str("46 - MBB OF1730")
elif procv == "2K82W2_256_EV":
    ModCha=str("47 - VOLKSWAGEN 17.260OD EURO V")
elif procv == "C75A1A_165_EV":
    ModCha=str("Agrale MA9.2 EURO V")
elif procv == "634011_329_EIII":
    ModCha=str("MBB O500RS/1833")
elif procv == "2G82W1_225_EV" or "2G82W2_225_EV" or "2G82W4_225_EV" or "2G82W5_225_EV":
    ModCha=str("VER. SUSPENSÃO: 36 - VOLKSWAGEN 17.230OD EURO V (METÁLICA) /"
               "43 - VOLKSWAGEN 17.230ODS EURO V (PNEUMÁTICA)")
elif procv == "2G82W7_225_EV" or "2G82W8_225_EV" or "2G82WX_225_EV" :
    ModCha=str("VER. SUSPENSÃO: 36 - VOLKSWAGEN 17.230OD EURO V (METÁLICA) /"
               "43 - VOLKSWAGEN 17.230ODS EURO V (PNEUMÁTICA)")
elif procv == "2Y82Z2_330_EV":
    ModCha=str("VOLKSWAGEN 26.330OTA EURO V")
elif procv == "T2T820_300_EV" or "T2T821_300_EV" or "T2T822_300_EV" or "T2T823_300_EV" or "T2T824_300_EV":
    ModCha=str("VOLVO B310R EURO V")
elif procv == "T2T825_300_EV" or "T2T826_300_EV" or "T2T827_300_EV" or "T2T828_300_EV" or "T2T829_300_EV" or "T2T82X_300_EV" :
    ModCha=str("VOLVO B310R EURO V")
elif procv == "T2T620_330_EV" or "T2T621_330_EV" or "T2T622_330_EV":
    ModCha=str("VOLVO B340R EURO V")
elif procv == "T2T623_330_EV" or "T2T624_330_EV" or "T2T625_330_EV" or "T2T626_330_EV" or "T2T627_330_EV":
    ModCha=str("VOLVO B340R EURO V")
elif procv == "T2T628_330_EV" or "T2T629_330_EV" or "T2T62X_330_EV" :
    ModCha=str("VOLVO B340R EURO V")
elif procv == "(vazio)":
    ModCha=str("(vazio)")

#Qual é a Suspensão
if ModCha == '01 - Agrale MA15.0' :
    Susp = str('Metálica')
if ModCha == '01 - Agrale MA15.0 EURO V' :
    Susp = str('Metálica')
if ModCha == '03 - MBB OF1721' :
    Susp = str('Metálica')
if ModCha == '04 - MBB OF1724 EURO V' :
    Susp = str('Metálica')
if ModCha == '05 - MBB O500MA/2836 EURO V' :
    Susp = str('Pneumática')
if ModCha == '07 - MBB OF1724L EURO V' :
    Susp = str('Pneumática')
if ModCha == '08 - MBB O500R/1830' :
    Susp = str('Pneumática')
if ModCha == '09 - VOLVO B270F EURO V' :
    Susp = str('Metálica ou Pneumática')
if ModCha == '12 - VOLVO B12M' :
    Susp = str('Pneumática')
if ModCha == '14 - MBB OF1519 EURO V' :
    Susp = str('Metálica')
if ModCha == '15 - MBB O500RS/1836 EURO V' :
    Susp = str('Pneumática')
if ModCha == '16 - MBB O500R/1830 EURO V' :
    Susp = str('Pneumática')
if ModCha == '17 - VOLVO B380R EURO V' :
    Susp = str('Pneumática')
if ModCha == '18 - VOLVO B340M EURO V' :
    Susp = str('Pneumática')
if ModCha == '20 - MBB OF1722M' :
    Susp = str('Metálica')
if ModCha == '21 - MBB OF1418' :
    Susp = str('Metálica')
if ModCha == '22 - VOLVO B270F' :
    Susp = str('Metálica')
if ModCha == '23 - Agrale MA9.2' :
    Susp = str('Metálica')
if ModCha == '26 - VOLARE W9' :
    Susp = str('Metálica')
if ModCha == '27 - VOLARE V8 ESCOLAR' :
    Susp = str('Metálica')
if ModCha == '28 - MBB O500RS/1836' :
    Susp = str('Pneumática')
if ModCha == '29 - MBB LO916 EURO V' :
    Susp = str('Metálica ou Pneumática')
if ModCha == '30 - MBB LO915' :
    Susp = str('Metálica')
if ModCha == '31 - MBB LO914' :
    Susp = str('Metálica')
if ModCha == '32 - MBB OF1721 EURO V' :
    Susp = str('Metálica')
if ModCha == '35 - MBB OF1721L EURO V' :
    Susp = str('Pneumática')
if ModCha == '37 - VOLKSWAGEN 15.190EOD' :
    Susp = str('Metálica')
if ModCha == '38 - VOLKSWAGEN 15.190OD EURO V' :
    Susp = str('Metálica')
if ModCha == '39 - VOLKSWAGEN 15.180EOD' :
    Susp = str('Metálica')
if ModCha == '40 - VOLKSWAGEN 17.230EOD' :
    Susp = str('Metálica')
if ModCha == '41 - VOLKSWAGEN 17.210EOD' :
    Susp = str('Metálica')
if ModCha == '42 - VOLKSWAGEN 17.210OD' :
    Susp = str('Metálica')
if ModCha == '43 - VOLKSWAGEN 17.230ODS' :
    Susp = str('Pneumática')
if ModCha == '45 - VOLKSWAGEN 9.160OD EURO V' :
    Susp = str('Metálica')
if ModCha == '46 - MBB OF1730' :
    Susp = str('Metálica')
if ModCha == '47 - VOLKSWAGEN 17.260OD EURO V' :
    Susp = str('Metálica / Pneumática')
if ModCha == 'Agrale MA9.2 EURO V' :
    Susp = str('Metálica')
if ModCha == 'MBB O500RS/1833' :
    Susp = str('Pneumática')
if ModCha == 'VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / ' \
             'VOLKSWAGEN 17.230ODS EURO V - 43 (SUSPENSÃO PNEUMÁTICA)' :
    Susp = str('Metálica / Pneumática')
if ModCha == 'VOLKSWAGEN 26.330OTA EURO V' :
    Susp = str('Mista')
if ModCha == 'VOLVO B270F' :
    Susp = str('Metálica')
if ModCha == 'VOLVO B310R EURO V' :
    Susp = str('Pneumática')
if ModCha == 'VOLVO B340R EURO V' :
    Susp = str('Pneumática')
if ModCha == '(vazio)' :
    Susp = str('(vazio)')

#Qual é o Câmbio
if ModCha == '01 - Agrale MA15.0' :
    Cambio = str('MANUAL')
if ModCha == '01 - Agrale MA15.0 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '03 - MBB OF1721' :
    Cambio = str('MANUAL')
if ModCha == '04 - MBB OF1724 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '05 - MBB O500MA/2836 EURO V' :
    Cambio = str('AUTOMÁTICO')
if ModCha == '07 - MBB OF1724L EURO V' :
    Cambio = str('MANUAL')
if ModCha == '08 - MBB O500R/1830' :
    Cambio = str('MANUAL')
if ModCha == '09 - VOLVO B270F EURO V' :
    Cambio = str('MANUAL')
if ModCha == '12 - VOLVO B12M' :
    Cambio = str('AUTOMÁTICO')
if ModCha == '14 - MBB OF1519 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '15 - MBB O500RS/1836 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '16 - MBB O500R/1830 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '17 - VOLVO B380R EURO V' :
    Cambio = str('MANUAL')
if ModCha == '18 - VOLVO B340M EURO V' :
    Cambio = str('AUTOMÁTICO')
if ModCha == '20 - MBB OF1722M' :
    Cambio = str('MANUAL')
if ModCha == '21 - MBB OF1418' :
    Cambio = str('MANUAL')
if ModCha == '22 - VOLVO B270F' :
    Cambio = str('MANUAL')
if ModCha == '23 - Agrale MA9.2' :
    Cambio = str('MANUAL')
if ModCha == '26 - VOLARE W9' :
    Cambio = str('MANUAL')
if ModCha == '27 - VOLARE V8 ESCOLAR' :
    Cambio = str('MANUAL')
if ModCha == '28 - MBB O500RS/1836' :
    Cambio = str('MANUAL')
if ModCha == '29 - MBB LO916 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '30 - MBB LO915' :
    Cambio = str('MANUAL')
if ModCha == '31 - MBB LO914' :
    Cambio = str('MANUAL')
if ModCha == '32 - MBB OF1721 EURO V' :
    Cambio = str('MANUAL')
if ModCha == '35 - MBB OF1721L EURO V' :
    Cambio = str('MANUAL')
if ModCha == '37 - VOLKSWAGEN 15.190EOD' :
    Cambio = str('MANUAL')
if ModCha == '38 - VOLKSWAGEN 15.190OD EURO V' :
    Cambio = str('MANUAL')
if ModCha == '39 - VOLKSWAGEN 15.180EOD' :
    Cambio = str('MANUAL')
if ModCha == '40 - VOLKSWAGEN 17.230EOD' :
    Cambio = str('MANUAL')
if ModCha == '41 - VOLKSWAGEN 17.210EOD' :
    Cambio = str('MANUAL')
if ModCha == '42 - VOLKSWAGEN 17.210OD' :
    Cambio = str('MANUAL')
if ModCha == '43 - VOLKSWAGEN 17.230ODS' :
    Cambio = str('MANUAL')
if ModCha == '45 - VOLKSWAGEN 9.160OD EURO V' :
    Cambio = str('MANUAL')
if ModCha == '46 - MBB OF1730' :
    Cambio = str('MANUAL')
if ModCha == '47 - VOLKSWAGEN 17.260OD EURO V' :
    Cambio = str('MANUAL')
if ModCha == 'Agrale MA9.2 EURO V' :
    Cambio = str('MANUAL')
if ModCha == 'MBB O500RS/1833' :
    Cambio = str('MANUAL')
if ModCha == 'VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / ' \
             'VOLKSWAGEN 17.230ODS EURO V - 43 (SUSPENSÃO PNEUMÁTICA)' :
    Cambio = str('MANUAL')
if ModCha == 'VOLKSWAGEN 26.330OTA EURO V' :
    Cambio = str('AUTOMÁTICO')
if ModCha == 'VOLVO B270F' :
    Cambio = str('MANUAL')
if ModCha == 'VOLVO B310R EURO V' :
    Cambio = str('MANUAL')
if ModCha == 'VOLVO B340R EURO V' :
    Cambio = str('MANUAL')
if ModCha == '(vazio)' :
    Cambio = str('(vazio)')

#Qual é o Tipo
if ModCha == '01 - Agrale MA15.0' :
    TipoV = str('MEDIO')
if ModCha == '01 - Agrale MA15.0 EURO V' :
    TipoV = str('MEDIO')
if ModCha == '03 - MBB OF1721' :
    TipoV = str('PESADO')
if ModCha == '04 - MBB OF1724 EURO V' :
    TipoV = str('PESADO')
if ModCha == '05 - MBB O500MA/2836 EURO V' :
    TipoV = str('ARTICULADO')
if ModCha == '07 - MBB OF1724L EURO V' :
    TipoV = str('PESADO')
if ModCha == '08 - MBB O500R/1830' :
    TipoV = str('RODOVIARIO')
if ModCha == '09 - VOLVO B270F EURO V' :
    TipoV = str('PESADO')
if ModCha == '12 - VOLVO B12M' :
    TipoV = str('ARTICULADO')
if ModCha == '14 - MBB OF1519 EURO V' :
    TipoV = str('MEDIO')
if ModCha == '15 - MBB O500RS/1836 EURO V' :
    TipoV = str('RODOVIARIO')
if ModCha == '16 - MBB O500R/1830 EURO V' :
    TipoV = str('RODOVIARIO')
if ModCha == '17 - VOLVO B380R EURO V' :
    TipoV = str('RODOVIARIO')
if ModCha == '18 - VOLVO B340M EURO V' :
    TipoV = str('ARTICULADO')
if ModCha == '20 - MBB OF1722M' :
    TipoV = str('PESADO')
if ModCha == '21 - MBB OF1418' :
    TipoV = str('MEDIO')
if ModCha == '22 - VOLVO B270F' :
    TipoV = str('PESADO')
if ModCha == '23 - Agrale MA9.2' :
    TipoV = str('LEVE')
if ModCha == '26 - VOLARE W9' :
    TipoV = str('LEVE')
if ModCha == '27 - VOLARE V8 ESCOLAR' :
    TipoV = str('LEVE')
if ModCha == '28 - MBB O500RS/1836' :
    TipoV = str('RODOVIARIO')
if ModCha == '29 - MBB LO916 EURO V' :
    TipoV = str('LEVE')
if ModCha == '30 - MBB LO915' :
    TipoV = str('LEVE')
if ModCha == '31 - MBB LO914' :
    TipoV = str('LEVE')
if ModCha == '32 - MBB OF1721 EURO V' :
    TipoV = str('PESADO')
if ModCha == '35 - MBB OF1721L EURO V' :
    TipoV = str('PESADO')
if ModCha == '37 - VOLKSWAGEN 15.190EOD' :
    TipoV = str('MEDIO')
if ModCha == '38 - VOLKSWAGEN 15.190OD EURO V' :
    TipoV = str('MEDIO')
if ModCha == '39 - VOLKSWAGEN 15.180EOD' :
    TipoV = str('MEDIO')
if ModCha == '40 - VOLKSWAGEN 17.230EOD' :
    TipoV = str('PESADO')
if ModCha == '41 - VOLKSWAGEN 17.210EOD' :
    TipoV = str('PESADO')
if ModCha == '42 - VOLKSWAGEN 17.210OD' :
    TipoV = str('PESADO')
if ModCha == '43 - VOLKSWAGEN 17.230ODS' :
    TipoV = str('PESADO')
if ModCha == '45 - VOLKSWAGEN 9.160OD EURO V' :
    TipoV = str('LEVE')
if ModCha == '46 - MBB OF1730' :
    TipoV = str('PESADO')
if ModCha == '47 - VOLKSWAGEN 17.260OD EURO V' :
    TipoV = str('PESADO')
if ModCha == 'Agrale MA9.2 EURO V' :
    TipoV = str('LEVE')
if ModCha == 'MBB O500RS/1833' :
    TipoV = str('RODOVIARIO')
if ModCha == 'VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / ' \
             'VOLKSWAGEN 17.230ODS EURO V - 43 (SUSPENSÃO PNEUMÁTICA)' :
    TipoV = str('PESADO')
if ModCha == 'VOLKSWAGEN 26.330OTA EURO V' :
    TipoV = str('ARTICULADO')
if ModCha == 'VOLVO B270F' :
    TipoV = str('PESADO')
if ModCha == 'VOLVO B310R EURO V' :
    TipoV = str('PESADO')
if ModCha == 'VOLVO B340R EURO V' :
    TipoV = str('PESADO')
if ModCha == '(vazio)' :
    TipoV = str('(vazio)')

#Local Motor
if ModCha == '01 - Agrale MA15.0' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '01 - Agrale MA15.0 EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '03 - MBB OF1721' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '04 - MBB OF1724 EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '05 - MBB O500MA/2836 EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == '07 - MBB OF1724L EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '08 - MBB O500R/1830' :
    LocalMotor = str('TRASEIRO')
if ModCha == '09 - VOLVO B270F EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '12 - VOLVO B12M' :
    LocalMotor = str('ENTRE EIXOS')
if ModCha == '14 - MBB OF1519 EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '15 - MBB O500RS/1836 EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == '16 - MBB O500R/1830 EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == '17 - VOLVO B380R EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == '18 - VOLVO B340M EURO V' :
    LocalMotor = str('ENTRE EIXOS')
if ModCha == '20 - MBB OF1722M' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '21 - MBB OF1418' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '22 - VOLVO B270F' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '23 - Agrale MA9.2' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '26 - VOLARE W9' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '27 - VOLARE V8 ESCOLAR' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '28 - MBB O500RS/1836' :
    LocalMotor = str('TRASEIRO')
if ModCha == '29 - MBB LO916 EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '30 - MBB LO915' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '31 - MBB LO914' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '32 - MBB OF1721 EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '35 - MBB OF1721L EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '37 - VOLKSWAGEN 15.190EOD' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '38 - VOLKSWAGEN 15.190OD EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '39 - VOLKSWAGEN 15.180EOD' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '40 - VOLKSWAGEN 17.230EOD' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '41 - VOLKSWAGEN 17.210EOD' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '42 - VOLKSWAGEN 17.210OD' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '43 - VOLKSWAGEN 17.230ODS' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '45 - VOLKSWAGEN 9.160OD EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '46 - MBB OF1730' :
    LocalMotor = str('DIANTEIRO')
if ModCha == '47 - VOLKSWAGEN 17.260OD EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == 'Agrale MA9.2 EURO V' :
    LocalMotor = str('DIANTEIRO')
if ModCha == 'MBB O500RS/1833' :
    LocalMotor = str('TRASEIRO')
if ModCha == 'VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / ' \
             'VOLKSWAGEN 17.230ODS EURO V - 43 (SUSPENSÃO PNEUMÁTICA)' :
    LocalMotor = str('DIANTEIRO')
if ModCha == 'VOLKSWAGEN 26.330OTA EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == 'VOLVO B270F' :
    LocalMotor = str('DIANTEIRO')
if ModCha == 'VOLVO B310R EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == 'VOLVO B340R EURO V' :
    LocalMotor = str('TRASEIRO')
if ModCha == '(vazio)' :
    LocalMotor = str('(vazio)')
#Padrão Veículo
if ModCha == '01 - Agrale MA15.0' :
    PadraoVeiculo = str('MEDIO')
if ModCha == '01 - Agrale MA15.0 EURO V' :
    PadraoVeiculo = str('MEDIO')
if ModCha == '03 - MBB OF1721' :
    PadraoVeiculo = str('PADRON')
if ModCha == '04 - MBB OF1724 EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '05 - MBB O500MA/2836 EURO V' :
    PadraoVeiculo = str('ARTICULADO')
if ModCha == '07 - MBB OF1724L EURO V' :
    if BRT == "n" or "N" or "NÃO" or "NAO" or "Não" or "Nao" or "não" or "nao":
        PadraoVeiculo = str('PADRON')
    else:
        PadraoVeiculo = str('PADRON 2')
if ModCha == '08 - MBB O500R/1830' :
    PadraoVeiculo = str('PADRON')
if ModCha == '09 - VOLVO B270F EURO V' :
    if BRT == "n" or "N" or "NÃO" or "NAO" or "Não" or "Nao" or "não" or "nao":
        PadraoVeiculo = str('PADRON')
    elif PTS == "2":
            PadraoVeiculo = str("PADRON 3")
    else:
        PadraoVeiculo = str('PADRON 4')
if ModCha == '12 - VOLVO B12M' :
    PadraoVeiculo = str('ARTICULADO')
if ModCha == '14 - MBB OF1519 EURO V' :
    PadraoVeiculo = str('MEDIO')
if ModCha == '15 - MBB O500RS/1836 EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '16 - MBB O500R/1830 EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '17 - VOLVO B380R EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '18 - VOLVO B340M EURO V' :
    PadraoVeiculo = str('ARTICULADO')
if ModCha == '20 - MBB OF1722M' :
    PadraoVeiculo = str('PADRON')
if ModCha == '21 - MBB OF1418' :
    PadraoVeiculo = str('MIDI')
if ModCha == '22 - VOLVO B270F' :
    PadraoVeiculo = str('PADRON')
if ModCha == '23 - Agrale MA9.2' :
    PadraoVeiculo = str('MINI')
if ModCha == '26 - VOLARE W9' :
    PadraoVeiculo = str('MINI')
if ModCha == '27 - VOLARE V8 ESCOLAR' :
    PadraoVeiculo = str('MINI')
if ModCha == '28 - MBB O500RS/1836' :
    PadraoVeiculo = str('PADRON')
if ModCha == '29 - MBB LO916 EURO V' :
    PadraoVeiculo = str('MINI')
if ModCha == '30 - MBB LO915' :
    PadraoVeiculo = str('MINI')
if ModCha == '31 - MBB LO914' :
    PadraoVeiculo = str('MINI')
if ModCha == '32 - MBB OF1721 EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '35 - MBB OF1721L EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '37 - VOLKSWAGEN 15.190EOD' :
    PadraoVeiculo = str('MEDIO')
if ModCha == '38 - VOLKSWAGEN 15.190OD EURO V' :
    PadraoVeiculo = str('MEDIO')
if ModCha == '39 - VOLKSWAGEN 15.180EOD' :
    PadraoVeiculo = str('MEDIO')
if ModCha == '40 - VOLKSWAGEN 17.230EOD' :
    PadraoVeiculo = str('PADRON')
if ModCha == '41 - VOLKSWAGEN 17.210EOD' :
    PadraoVeiculo = str('PADRON')
if ModCha == '42 - VOLKSWAGEN 17.210OD' :
    PadraoVeiculo = str('PADRON')
if ModCha == '43 - VOLKSWAGEN 17.230ODS' :
    PadraoVeiculo = str('PADRON')
if ModCha == '45 - VOLKSWAGEN 9.160OD EURO V' :
    PadraoVeiculo = str('MINI')
if ModCha == '46 - MBB OF1730' :
    PadraoVeiculo = str('PADRON')
if ModCha == '47 - VOLKSWAGEN 17.260OD EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == 'Agrale MA9.2 EURO V' :
    PadraoVeiculo = str('MINI')
if ModCha == 'MBB O500RS/1833' :
    PadraoVeiculo = str('PADRON')
if ModCha == 'VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / ' \
             'VOLKSWAGEN 17.230ODS EURO V - 43 (SUSPENSÃO PNEUMÁTICA)' :
    if BRT == "n" or "N" or "NÃO" or "NAO" or "Não" or "Nao" or "não" or "nao":
        PadraoVeiculo = str('PADRON')
    else:
        PadraoVeiculo = str('PADRON 2')
if ModCha == 'VOLKSWAGEN 26.330OTA EURO V' :
    PadraoVeiculo = str('ARTICULADO')
if ModCha == 'VOLVO B270F' :
    PadraoVeiculo = str('PADRON')
if ModCha == 'VOLVO B310R EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == 'VOLVO B340R EURO V' :
    PadraoVeiculo = str('PADRON')
if ModCha == '(vazio)' :
    PadraoVeiculo = str('(vazio)')
    
#Define Medidas
proc = str(BRT + "_" + PTS + "_" + ModCha)
if proc == 'N_1_01 - Agrale MA15.0':
    CAR = str('0')
    CDR = str('6.209')
if proc == 'N_1_23 - Agrale MA9.2':
    CAR = str('0.5')
    CDR = str('3.6')
if proc == 'N_1_39 - VOLKSWAGEN 15.180EOD':
    CAR = str('0')
    CDR = str('6.209')
if proc == 'N_1_31 - MBB LO914':
    CAR = str('0')
    CDR = str('3.6')
if proc == 'N_1_30 - MBB LO915':
    CAR = str('0')
    CDR = str('6.209')
if proc == 'N_1_29 - MBB LO916 EURO V':
    CAR = str('0')
    CDR = str('6.209')
if proc == 'N_1_08 - MBB O500R/1830':
    CAR = str('0')
    CDR = str('9.2')
if proc == 'N_1_16 - MBB O500R/1830 EURO V':
    CAR = str('0')
    CDR = str('9.2')
if proc == 'N_1_28 - MBB O500RS/1836':
    CAR = str('0')
    CDR = str('9.2')
if proc == 'N_1_14 - MBB OF1519 EURO V':
    CAR = str('0')
    CDR = str('6.209')
if proc == 'N_1_32 - MBB OF1721 EURO V':
    CAR = str('0')
    CDR = str('8.224')
if proc == 'N_1_20 - MBB OF1722M':
    CAR = str('0')
    CDR = str('8.224')
if proc == 'N_1_04 - MBB OF1724 EURO V':
    CAR = str('0')
    CDR = str('8.224')
if proc == 'N_1_27 - VOLARE V8 ESCOLAR':
    CAR = str('1.27')
    CDR = str('3.21')
if proc == 'N_1_37 - VOLKSWAGEN 15.190EOD':
    CAR = str('0')
    CDR = str('6.209')
if proc == 'N_1_17 - VOLVO B380R EURO V':
    CAR = str('0')
    CDR = str('10')
if proc == 'N_2_01 - Agrale MA15.0':
    CAR = str('1')
    CDR = str('5.209')
if proc == 'N_2_21 - MBB OF1418':
    CAR = str('1')
    CDR = str('5.209')
if proc == 'N_2_03 - MBB OF1721':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_32 - MBB OF1721 EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_35 - MBB OF1721L EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_20 - MBB OF1722M':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_04 - MBB OF1724 EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_07 - MBB OF1724L EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_37 - VOLKSWAGEN 15.190EOD':
    CAR = str('0.9')
    CDR = str('5.309')
if proc == 'N_2_46 - MBB OF1730':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_14 - MBB OF1519 EURO V':
    CAR = str('1')
    CDR = str('5.209')
if proc == 'N_2_26 - VOLARE W9':
    CAR = str('1.68')
    CDR = str('3.5')
if proc == 'N_2_42 - VOLKSWAGEN 17.210OD':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_41 - VOLKSWAGEN 17.210EOD':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_40 - VOLKSWAGEN 17.230EOD':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_36 - VOLKSWAGEN 17.230OD EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / ' \
           'VOLKSWAGEN 17.230ODS EURO V - 43 (SUSPENSÃO PNEUMÁTICA)':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_45 - VOLKSWAGEN 9.160OD EURO V':
    CAR = str('0')
    CDR = str('2.95')
if proc == 'N_2_22 - VOLVO B270F':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_VOLVO B270F 15 METROS':
    CAR = str('1')
    CDR = str('9.034')
if proc == 'S_2_VOLVO B270F 15 METROS':
    CAR = str('1')
    CDR = str('9.034')
if proc == 'N_2_09 - VOLVO B270F EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_2_47 - VOLKSWAGEN 17.260OD EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_47 - VOLKSWAGEN 17.260OD EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_21 - MBB OF1418':
    CAR = str('1.3')
    CDR = str('5.859')
if proc == 'N_3_32 - MBB OF1721 EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_35 - MBB OF1721L EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_20 - MBB OF1722M':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_04 - MBB OF1724 EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_07 - MBB OF1724L EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'S_3_07 - MBB OF1724L EURO V':
    CAR = str('1')
    CDR = str('8.91')
if proc == 'N_3_41 - VOLKSWAGEN 17.210EOD':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_40 - VOLKSWAGEN 17.230EOD':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_36 - VOLKSWAGEN 17.230OD EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_22 - VOLVO B270F':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_3_09 - VOLVO B270F EURO V':
    CAR = str('1')
    CDR = str('8.224')
if proc == 'N_4_09 - VOLVO B270F EURO V':
    CAR = str('1')
    CDR = str('9.034')
if proc == 'S_4_09 - VOLVO B270F EURO V':
    CAR = str('1')
    CDR = str('9.034')
if proc == 'N_5_09 - VOLVO B270F EURO V':
    CAR = str('1')
    CDR = str('9.034')
if proc == 'S_5_09 - VOLVO B270F EURO V':
    CAR = str('1')
    CDR = str('9.034')
if proc == 'S_5_07 - MBB OF1724L EURO V':
    CAR = str('1')
    CDR = str('8.91')
if proc == 'S_6_12 - VOLVO B12M':
    CAR = str('0')
    CDR = str('16.06')
if proc == 'S_6_18 - VOLVO B340M EURO V':
    CAR = str('0')
    CDR = str('16.96')
if proc == 'S_4_05 - MBB O500MA/2836 EURO V':
    CAR = str('0')
    CDR = str('16.145')
if proc == 'S_6_05 - MBB O500MA/2836 EURO V':
    CAR = str('0')
    CDR = str('16.145')
if proc == 'S_7_05 - MBB O500MA/2836 EURO V':
    CAR = str('0')
    CDR = str('16.145')

# Largura
# Pegar carroceria e vincular

if CarMod == '23 - INDUSCAR PICCOLO' :
    CarL=str('0')
    CarC=str('0,3')
if CarMod == '41 - INDUSCAR FOZ R' :
    CarL=str('RODOV')
    CarC=str('RODOV')
if CarMod == '36 - VOLARE V8' :
    CarL=str('MANTER')
    CarC=str('MANTER')
if CarMod == '04 - VOLARE W9' :
    CarL=str('MANTER')
    CarC=str('MANTER')
if CarMod == '42 - MASCARELLO GRANMICRO' :
    CarL=str('0,6')
    CarC=str('0,6')
if CarMod == '17 - BUSSCAR URBANUSS U' :
    CarL=str('0,93')
    CarC=str('0,6')
if CarMod == '18 - BUSSCAR URBANUSS PLUSS U' :
    CarL=str('0,65')
    CarC=str('0,6')
if CarMod == '19 - BUSSCAR VISSTA BUSS R' :
    CarL=str('0')
    CarC=str('0,6')
if CarMod == '24 - CIFERAL CITMAX U' :
    CarL=str('0,6')
    CarC=str('0,65')
if CarMod == '06 - COMIL CAMPIONE R' :
    CarL=str('0')
    CarC=str('0,5')
if CarMod == '02 - COMIL DOPPIO A' :
    CarL=str('0,77')
    CarC=str('0,65')
if CarMod == '01 - COMIL SVELTO U' :
    CarL=str('0,9')
    CarC=str('0,65')
if CarMod == '14 - COMIL VERSATILE R' :
    CarL=str('0')
    CarC=str('0,35')
if CarMod == '38 - INDUSCAR APACHE U' :
    CarL=str('0,6')
    CarC=str('0,65')
if CarMod == '21 - INDUSCAR FOZ U' :
    CarL=str('1')
    CarC=str('0,6')
if CarMod == '20 - INDUSCAR GIRO' :
    CarL=str('0')
    CarC=str('0,6')
if CarMod == '37 - INDUSCAR MILLENNIUM U' :
    CarL=str('0,9')
    CarC=str('0,75')
if CarMod == '22 - INDUSCAR SOLAR' :
    CarL=str('0')
    CarC=str('0,4')
if CarMod == '39 - MASCARELLO GRANMIDI' :
    CarL=str('0,95')
    CarC=str('0,6')
if CarMod == '30 - MASCARELLO GRANVIA' :
    CarL=str('0,92')
    CarC=str('0,6')
if CarMod == '27 - MARCOPOLO SENIOR MIDI' :
    CarL=str('1')
    CarC=str('0,8')
if CarMod == '26 - MARCOPOLO SENIOR R' :
    CarL=str('0')
    CarC=str('0')
if CarMod == '25 - MARCOPOLO IDEALE R' :
    CarL=str('0')
    CarC=str('0')
if CarMod == '05 - MARCOPOLO TORINO U' :
    CarL=str('0,85')
    CarC=str('0,65')
if CarMod == '09 - MARCOPOLO VIAGGIO R' :
    CarL=str('0')
    CarC=str('0,5')
if CarMod == '29 - MARCOPOLO VIALE A' :
    CarL=str('0,72')
    CarC=str('0,8')
if CarMod == '10 - NEOBUS MEGA U' :
    CarL=str('0,84')
    CarC=str('0,6')
if CarMod == '11 - NEOBUS MEGABRT A' :
    CarL=str('0,67')
    CarC=str('0,74')
if CarMod == '12 - NEOBUS SPECTRUM 320' :
    CarL=str('0')
    CarC=str('0,38')
if CarMod == '34 - NEOBUS THUNDER' :
    CarL=str('0')
    CarC=str('0,55')
if CarMod == '32 - NEOBUS SPECTRUM CITY' :
    CarL=str('0,7')
    CarC=str('0,6')
if CarMod == '33 - NEOBUS SPECTRUM INTERCITY' :
    CarL=str('0')
    CarC=str('0,38')

# PBT

if ModCha == '01 - Agrale MA15.0':
    PBT = str('15000')
if ModCha == '01 - Agrale MA15.0 EURO V':
    PBT = str('15000')
if ModCha == '03 - MBB OF1721':
    PBT = str('17000')
if ModCha == '04 - MBB OF1724 EURO V':
    PBT = str('17000')
if ModCha == '05 - MBB O500MA/2836 EURO V':
    PBT = str('28000')
if ModCha == '07 - MBB OF1724L EURO V':
    PBT = str('17000')
if ModCha == '08 - MBB O500R/1830':
    PBT = str('18500')
if ModCha == '09 - VOLVO B270F EURO V':
    PBT = str('17000')
if ModCha == '12 - VOLVO B12M':
    PBT = str('30000')
if ModCha == '14 - MBB OF1519 EURO V':
    PBT = str('15000')
if ModCha == '15 - MBB O500RS/1836 EURO V':
    PBT = str('18500')
if ModCha == '16 - MBB O500R/1830 EURO V':
    PBT = str('18500')
if ModCha == '17 - VOLVO B380R EURO V':
    PBT = str('19500')
if ModCha == '18 - VOLVO B340M EURO V':
    PBT = str('30000')
if ModCha == '20 - MBB OF1722M':
    PBT = str('17000')
if ModCha == '21 - MBB OF1418':
    PBT = str('14000')
if ModCha == '22 - VOLVO B270F':
    PBT = str('17000')
if ModCha == '23 - Agrale MA9.2':
    PBT = str('9200')
if ModCha == '26 - VOLARE W9':
    PBT = str('9200')
if ModCha == '27 - VOLARE V8 ESCOLAR':
    PBT = str('7850')
if ModCha == '28 - MBB O500RS/1836':
    PBT = str('18500')
if ModCha == '29 - MBB LO916 EURO V':
    PBT = str('9400')
if ModCha == '30 - MBB LO915':
    PBT = str('8500')
if ModCha == '31 - MBB LO914':
    PBT = str('8500')
if ModCha == '32 - MBB OF1721 EURO V':
    PBT = str('17000')
if ModCha == '35 - MBB OF1721L EURO V':
    PBT = str('17000')
if ModCha == '37 - VOLKSWAGEN 15.190EOD':
    PBT = str('15000')
if ModCha == '38 - VOLKSWAGEN 15.190OD EURO V':
    PBT = str('15000')
if ModCha == '39 - VOLKSWAGEN 15.180EOD':
    PBT = str('15000')
if ModCha == '40 - VOLKSWAGEN 17.230EOD':
    PBT = str('16000')
if ModCha == '41 - VOLKSWAGEN 17.210EOD':
    PBT = str('16000')
if ModCha == '42 - VOLKSWAGEN 17.210OD':
    PBT = str('16000')
if ModCha == '43 - VOLKSWAGEN 17.230ODS':
    PBT = str('16000')
if ModCha == '45 - VOLKSWAGEN 9.160OD EURO V':
    PBT = str('9200')
if ModCha == '46 - MBB OF1730':
    PBT = str('17000')
if ModCha == '47 - VOLKSWAGEN 17.260OD EURO V':
    PBT = str('16000')
if ModCha == 'Agrale MA9.2 EURO V':
    PBT = str('9200')
if ModCha == 'MBB O500RS/1833':
    PBT = str('18500')
if ModCha == 'VER: VOLKSWAGEN 17.230OD EURO V - 36 (SUSPENSÃO METÁLICA) / VOLKSWAGEN 17.230ODS EURO V - 43 (' \
                     'SUSPENSÃO PNEUMÁTICA)':
    PBT = str('16000')
if ModCha == 'VOLKSWAGEN 26.330OTA EURO V':
    PBT = str('26000')
if ModCha == 'VOLVO B310R EURO V':
    PBT = str('19500')
if ModCha == 'VOLVO B340R EURO V':
    PBT = str('19500')
if ModCha == '(vazio)':
    PBT = str('(vazio)')

# Area Def
if int(MOD) < 2008:
    DEFlar = str("0.6")
    DEFCom = str("0.8")
else:
    DEFlar = str("0.8")
    DEFCom = str("1.2")

# Digite a saída
print("")
print("")
print("")
sistema = int(input("Digite 1 para tela SGTM ou 2 para tela SIMETRO"))
if sistema == 1:
    # Saída sem leiaute
    os.system("")
    print("Padrão de Serviço: ")
    print("Padrão: ", PadraoVeiculo)
    print("Nro. Chassis: ", chassis)
    print("Modelo da Carroceria: ", CarMod)
    print("Ano Modelo da Carroceria: ", MOD)
    print("Modelo do chassis: ", ModCha)
    print("Ano Fabricação do Chassis: ", FAB)
    print("Tipo de Suspensão: ", Susp)
    print("Tipo de Câmbio: ", Cambio)
    print("Tipo de Veículo: ", TipoV)
    print("Localização do Motor: ", LocalMotor)
    print("Potência do Motor: ", POT)
    # Colocar instrução de É move? Se sim, ART = 4, P2 e P4 = 2, se não, 0
    if BRT == "n" or "N" or "NÃO" or "NAO" or "Não" or "Nao" or "não" or "nao":
        print("Qt de portas: ", PTS)
        print("Qt de portas esquerda: 0")
    elif BRT == "s" or "S" or "SIM" or "Sim" or "sim":
        if PadraoVeiculo == "PADRON 2" or "PADRON 4":
            print("Qt de portas: ", int(PTS) - 2)
            print("Qt de portas esquerda: 2")
        elif PadraoVeiculo == "ARTICULADO":
            print("Qt de portas: ", int(PTS) - 4)
            print("Qt de portas esquerda: 4")
    else:
            print("Qt de portas: ERRO PORTA")
            print("Qt de portas esquerda: ERRO PORTA")
    print("Peso do veículo: ", PBT)
    print("Largura antes da Roleta(cm): ", CarL)
    print("Comprimento antes da Roleta(cm): ", CAR)
    print("Largura após a Roleta(cm): ", CarC)
    print("Comprimento após a Roleta(cm): ", CDR)
    print("Largura da área para deficientes (cm): ", DEFlar)
    print("Comprimento da área para deficientes (cm): ", DEFCom)
elif sistema == 2:
    # Exportar em Leiaute SIMETRO

    print("Aba: PRINCIPAL")
    print("Data de Entrada: O que indicarem no sistema")
    print("Serviço: ")
    print("Placa: O que indicarem no sistema")
    print("Número de Ordem: O que indicarem no sistema")
    print("Renavam: O que indicarem no sistema")
    print("Padrão: ", PadraoVeiculo)
    print("Cor: O que indicarem no sistema")
    print("Tipo de Veículo: ", TipoV)
    print("")  # Isso aqui é pra dar linha
    print("Aba: CARROCERIA")
    print("Número de Chassi: ")
    print("Modelo de Chassi: ")
    print("Ano do Chassi: ")
    print("Modelo da Carroceria: ")
    print("Ano da Carroceria: ")
    print("Suspensão: ")
    print("Câmbio: ")
    print("LocalMotor: ")
    print("Potência do Motor: ")
    print("Tipo de assento: O que indicarem no sistema")
    print("")  # Isso é para dar linha
    print("Aba: Medidas")
    print("Peso: ")
    print("Comp. Antes Roleta: ")
    print("Comp. Após Roleta: ")
    print("Larg. Antes Roleta: ")
    print("Larg. Após Roleta: ")
    print("Larg. Porta Dianteira (LD)")
    print("Larg. Porta Central (LD 1)")
    print("Larg. Porta Central (LD 2)")
    print("Larg. Porta Traseira (LD)")
    print("Larg. Porta Dianteira (LE)")
    print("Larg. Porta Central (LE 1)")
    print("Larg. Porta Central (LE 2)")
    print("Larg. Porta Traseira (LE):")
    print("Comp. Area Deficientes: ")
    print("Larg. Area Deficientes: ")
    print("Tanque 1: O que indicarem")
    print("Tanque 2: O que indicarem")
    print("Número de assentos: O que indicarem")
    print("")
else:
    print("Erro Sistema")