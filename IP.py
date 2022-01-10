#!/usr/bin/env python3
import matplotlib.pyplot as plt
import sys
import re

def harvester(file):
    d = {}
    ipsa = []
    ipsp = []
    i = file.read()
    count = 0
    ips = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', i)
    if ips:
        for ip in ips:
            count += 1
            if ip in d:
                d[ip] += 1
            else:
                d[ip] = 1
    for key, value in sorted(d.items()):
        perc = ((value / count) * 100)
        print(key + " - " + str(round(perc, 2))+ "%")
        ipsa.append(key)
        ipsp.append(perc)
    
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.barh(ipsa, ipsp)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.grid(visible = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
    ax.invert_yaxis()
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.6,
                str(round((i.get_width()), 2)) + "%",
                fontsize = 10, fontweight ='bold',
                color ='grey')
    ax.set_title('Harvested IP Addresses',
                loc ='left', )
    plt.show()
    print("Number of IP Addresses: " + str(count))

def main():
    args = sys.argv[1]
    with open(args) as open_file:
        harvester(open_file)

if __name__ == "__main__":
    main()