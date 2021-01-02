from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.side_channel.side_channel import (
    SideChannel,
    IncomingMessage,
    OutgoingMessage,
)
import numpy as np
import uuid


# Create the StringLogChannel class
class StringLogChannel(SideChannel):

    def __init__(self) -> None:
        super().__init__(uuid.UUID("621f0a70-4f87-11ea-a6bf-784f4387d1f7"))

    def on_message_received(self, msg: IncomingMessage) -> None:
        """
        Note: We must implement this method of the SideChannel interface to
        receive messages from Unity
        """
        # We simply read a string from the message and print it.
        print(msg.read_string())

    def send_string(self, data: str) -> None:
        # Add the string to an OutgoingMessage
        msg = OutgoingMessage()
        msg.write_string(data)
        # We call this method to queue the data we want to send
        super().queue_message_to_send(msg)



print('Start:')
# Create the channel
string_log = StringLogChannel()
print('.')
# We start the communication with the Unity Editor and pass the string_log side channel as input
env = UnityEnvironment(side_channels=[string_log])
print('.')
env.reset()
print('.')
string_log.send_string("The environment was reset")
string_log.send_string('hi')
print('Done.')
env.step()  # Move the simulation forward


for i in range(1000):
#    print(i)
    string_log.send_string('hi')
    env.step()  # Move the simulation forward

env.close()





































