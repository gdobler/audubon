#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

def see_images(flist):
    """ View a list of images. """

    cnt = [0]

    def next_img(event):
        if event.key == "right":
            cnt[0] += 1
        elif event.key == "left":
            cnt[0] -= 1

        cnt[0] %= len(flist)
        im.set_data(np.rot90(imread(flist[cnt[0]]), 3)[1::2, 1::2])
        tt.set_text("{0} : {1}".format(cnt[0], flist[cnt[0]]))
        fig.canvas.draw()

        return

    fig, ax = plt.subplots(figsize=(6, 8))
    ax.axis("off")
    im = ax.imshow(np.rot90(imread(flist[cnt[0]]), 3)[1::2, 1::2], 
                   clim=[0, 50])
    tt = ax.set_title("{0} : {1}".format(cnt[0], flist[cnt[0]]))
    fig.canvas.draw()
    fig.canvas.mpl_connect("key_press_event", next_img)

    return
