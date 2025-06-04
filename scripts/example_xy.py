#!/usr/bin/env python3
# Example of LinuxCNC control with Python
# See the LinucCNC user manual, section 13.5 - Python Interface

import sys
import linuxcnc


def program_robot(c: linuxcnc.command) -> None:
    def set_feed_rate(v: float):
        # set robot feed rate
        c.mdi(f"F{v}")
        c.wait_complete()

    def go_to(x: float, y: float):
        # go to position (x, y)
        print(f"Going to ({x}, {y})...", end="", flush=True)
        c.mdi(f"G1 X{x} Y{y}")
        while (ret := c.wait_complete(1)) == -1:
            continue
        print(" done")
        if ret == linuxcnc.RCS_ERROR:
            print("RCS_ERROR")

    # Put your robot commands here
    set_feed_rate(400)

    x, y = 0, 0

    for i in range(1, 22):
        go_to(x * 5, y * 5)

        x += -1 if (i % 4 == 0) else 1
        y += -1 if ((i - 2) % 4 == 0) else 1

    go_to(0, 0)


def main():
    s = linuxcnc.stat()  # connect to the status channel
    c = linuxcnc.command()  # connect to the command channel

    def ok_for_mdi() -> bool:
        s.poll()
        return (
            not s.estop
            and s.enabled
            and (s.homed.count(1) == s.joints)
            and (s.interp_state == linuxcnc.INTERP_IDLE)
        )

    if ok_for_mdi():
        c.mode(linuxcnc.MODE_MDI)
        c.wait_complete()  # wait until mode switch executed
        print("OK, running...")
        try:
            program_robot(c)
        except KeyboardInterrupt:
            c.abort()
            sys.exit(1)
    else:
        print("Not OK for running. Check that the robot is homed and idle.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except linuxcnc.error as e:
        print("error: ", e)
        print("is LinuxCNC running?")
        sys.exit(1)
