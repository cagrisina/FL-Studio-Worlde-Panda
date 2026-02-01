# name=Worlde Panda 61

import transport
import channels

def OnControlChange(event):
    if event.controlNum == 119:
        transport.start()
        event.handled = True
    elif event.controlNum == 118:
        transport.stop()
        event.handled = True
    elif event.controlNum == 117:
        transport.record()
        event.handled = True
    elif event.controlNum == 114:
        transport.setLoopMode()
        event.handled = True
    elif event.controlNum == 116:
        transport.fastForward(2)
        event.handled = True
    elif event.controlNum == 115:
        transport.rewind(2)
        event.handled = True
    else:
        event.handled = False

def OnPitchBend(event):
    event.handled = True
    selected_channel = channels.selectedChannel()
    if selected_channel == -1:
        return
    pitch_value = event.data1 | (event.data2 << 7)
    normalised_pitch = (pitch_value - 8192) / 8192.0
    channels.setChannelPitch(selected_channel, normalised_pitch)

def OnMidiMsg(event):
    event.handled = False
