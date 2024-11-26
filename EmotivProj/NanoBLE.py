import asyncio
from bleak import BleakClient

# Replace with your Arduino's advertised name or MAC address
DEVICE_NAME = "78:21:84:7A:9E:12"  # Use the MAC address instead
CHARACTERISTIC_UUID = "87654321-4321-4321-4321-abcdefabcdef"

# Function to send a command to the Arduino
async def send_command(command):
    # Connect to the BLE device
    async with BleakClient(DEVICE_NAME) as client:
        print("Connected to Nano33Control")

        # Send the command as a single byte
        await client.write_gatt_char(CHARACTERISTIC_UUID, bytes([command]))
        print(f"Command {command} sent")

# Run the send_command function with the desired command
# For example, to send command 0x01
command_to_send = 0x01  # Change this to the command you want to send
asyncio.run(send_command(command_to_send))
