# name=Worlde Panda 61

import transport

def OnControlChange(event):
    # Play: 119, Stop: 118, Record: 117, Loop: 114, Forward: 116, Rewind: 115
    
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
