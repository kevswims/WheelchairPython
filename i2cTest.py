import smbus

bus = smbus.SMBus(1)

address = 0x48

#read adc values directly
# Pin 4 - FA
print("Pin 4 - FA")
print(bus.read_byte_data(address, 0x01))
# Pin 2 - LR
print("Pin 2 - LR")
print(bus.read_byte_data(address, 0x02))
# Pin 5 - FA
print("Pin 5 - FA")
print(bus.read_byte_data(address, 0x03))
# Pin 7 - LR
print("Pin 7 - LR")
print(bus.read_byte_data(address, 0x04))

# write scale factors
# write forward scale half
input("Forward scale half")
bus.write_byte_data(address, 0x05, 0x7F)
# write backward scale half
input("Backward scale half")
bus.write_byte_data(address, 0x06, 0x7F)
# write left scale half
input("Left scale half")
bus.write_byte_data(address, 0x07, 0x7F)
# write right scale half
input("Right scale half")
bus.write_byte_data(address, 0x08, 0x7F)
# write all scale full
input("Return scales to full")
bus.write_byte_data(address, 0x09, 0xFF)

# stops
# stop forward
input("Forward stop")
bus.write_byte_data(address, 0x0A, 0xFF)
# go forward
input("Forward go")
bus.write_byte_data(address, 0x0A, 0x00)

# stop backwards
input("Backward stop")
bus.write_byte_data(address, 0x0B, 0xFF)
# go backwards
input("Backward go")
bus.write_byte_data(address, 0x0B, 0x00)


# stop left
input("Stop left")
bus.write_byte_data(address, 0x0C, 0xFF)
# go left
input("Go left")
bus.write_byte_data(address, 0x0C, 0x00)


# stop right
input("Stop right")
bus.write_byte_data(address, 0x0D, 0xFF)
# go right
input("Go right")
bus.write_byte_data(address, 0x0D, 0x00)


# stop all
input("Stop all")
bus.write_byte_data(address, 0x0E, 0xFF)
# go all
input("Go all")
bus.write_byte_data(address, 0x0E, 0x00)