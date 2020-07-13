This is the client side part of the valorant colour aimbot - runs on the same pc as valorant. To make use of this you would need to write the other part which takes the positions and performs mouse movements - this could be a raspberry pi as a hid device.

This wasn't written to be readable in the case that vanguard inspects the file whilst it's running. It's not doing anything majorly suspicious (debatable). I think I've named things to throw said readers off, like "checksum" is the actual pixel positions transmitted and pretending as if this was meant for some "special streaming software".

There isn't much code to it - simply capturing the screen as fast as possible and checking where the topmost pixel of a given type can be found (not a hardcoded hex).
