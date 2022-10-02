#! /usr/bin/python3

from turtle import back
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
from time import sleep
import pygame
from pygame.locals import *
import requests
import sys
import threading
import matplotlib
from pathlib import Path


ENDPOINT_URL = 'http://localhost:8080/mock-api.json'
BACKGROUND = (Path(__file__).parent / 'background.png').resolve()
TITLE = 'Live Committee Signups'
SLEEP_BETWEEN = 5
TEXT_SIZE = 16
BLACK = (0, 0, 0)

data = dict()

def quit(status=0):
    pygame.quit()
    sys.exit(status)

def get_data():
    try:
        req = requests.get(ENDPOINT_URL, allow_redirects=True)
        _data = req.json()['data']
        return dict([(k.split('(')[0].strip(), v) for k, v in _data.items()])
    except:
        print('Error getting data (check ENDPOINT_URL)', file=sys.stderr)
        quit(1)


class Watcher(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop = threading.Event()
        threading.Thread.__init__(self, target=self.watch)

    def watch(self):
        global data
        try:
            while not self.stop.wait(1):
                _data = get_data()
                if len(_data.items()) > 0:
                    data = _data
                self.stop.wait(SLEEP_BETWEEN)
        except:
            pass

    def terminate(self):
        self.stop.set()


matplotlib.use('Agg')
matplotlib.rc('font', size=TEXT_SIZE)
pygame.init()
windowSurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(TITLE)
infoObject = pygame.display.Info()
size = (infoObject.current_w, infoObject.current_h)
background = None if BACKGROUND is None else pygame.image.load(BACKGROUND)

def white_to_transparent(image):
    pixels = pygame.PixelArray(image.convert_alpha())
    for v in [255, 241, 227, 225, 205, 193]:
        pixels.replace((v, v, v), (0, 0, 0, 0))
    return pixels.make_surface()

def draw():
    windowSurface.fill(BLACK)
    if len(data.items()) > 0:
        if background is not None:
            windowSurface.blit(pygame.transform.scale(background, size), (0, 0))
        figure = plt.figure(figsize=[size[0] / 100, size[1] / 100], dpi=100)
        figure.patch.set_facecolor('None')
        ax = figure.gca()
        max_signups = max(data.values())
        color = ['indianred' if v == max_signups else 'lightblue' for (
            _, v) in data.items()]
        ax.bar(data.keys(), data.values(), color=color, edgecolor='black')
        plt.xlim([-0.5, len(data.items()) - 0.5])
        plt.title(TITLE)
        plt.tight_layout()
        canvas = agg.FigureCanvasAgg(figure)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        plt.close(figure)
        image = pygame.image.fromstring(raw_data, size, 'RGB')
        if background is not None:
            image = white_to_transparent(image)
        windowSurface.blit(image, (0, 0))
    pygame.display.update()


quitting = False
w = Watcher()
w.start()
while True:
    try:
        draw()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                w.terminate()
                windowSurface.fill(BLACK)
                pygame.display.update()
                w.join()
                quit()
    except:
        break
