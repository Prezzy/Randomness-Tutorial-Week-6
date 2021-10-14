import sys
import math
import struct


#float to bin function, but returns bin
#https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
def binary(num):
    return int(''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num)))


def main():

    time = []
    bitmask = 0x00001FFE


    with open(sys.argv[1]) as f:

        timingset = f.readlines()

        for timestamp in timingset:
            timestamp = timestamp.split(" ")[0]
            timestamp = float(timestamp)*1000

            time.append(timestamp)

        delta = [0] * len(time)
        delta2 = [0] * len(time)
        delta3 = [0] * len(time)

        entropy = [0] * len(time)

        for i in range(1,len(time)):
            delta[i] = time[i] - time[i-1]
            print(f"time : {time[i]}")
            print(f"delta: {delta[i]}")
            delta2[i] = delta[i] - delta[i-1]
            print(f"delta2: {delta2[i]}")
            delta3[i] = delta2[i] - delta2[i-1]
            print(f"delta3: {delta3[i]}")

            deltachoice = min(abs(binary(delta[i])&bitmask),abs(binary(delta2[i])&bitmask),abs(binary(delta3[i])&bitmask))
        

            
            if deltachoice == 0:
                entropy[i] = 0
            else:
                entropy[i] = math.log2(deltachoice)


        total = sum(entropy)
    
        average = total / len(entropy)

        print(f"{sys.argv[1]}, estimate entropy {average}")



main()








        

