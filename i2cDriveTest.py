import smbus

bus = smbus.SMBus(1)

address = 0x48

input("Enable Drive")
bus.write_byte_data(address, 0x13, 0xA7)
input("Drive forward")
bus.write_byte_data(address, 0x11, 0xFF)
input("Stop")
bus.write_byte_data(address, 0x11, 0x7F)
input("Drive backwards")
bus.write_byte_data(address, 0x11, 0x00)
input("Stop")
bus.write_byte_data(address, 0x11, 0x7F)

input("Drive left")
bus.write_byte_data(address, 0x12, 0xFF)
input("Stop")
bus.write_byte_data(address, 0x12, 0x7F)
input("Drive right")
bus.write_byte_data(address, 0x12, 0x00)
input("Stop")
bus.write_byte_data(address, 0x12, 0x7F)

input("Disable Drive")
bus.write_byte_data(address, 0x13, 0x00)