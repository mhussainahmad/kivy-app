# Importing kivy dependencies
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Import kivy UX components
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

# Import other kivy stuff
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

# Import other dependencies
import cv2
import tensorflow as tf
from layers import L1Dist
import os
import numpy as np


# Build app and layout
class CamApp(App):

    def __init__(self, **kwargs):
        super().__init__()
        self.capture = None
        self.verification = None
        self.button = None
        self.webcam = None

    # Main layout components
    def build(self):
        self.webcam = Image(size_hint=(1, 0.8))
        self.button = Button(text='Verify', size_hint=(1, 0.1))
        self.verification = Label(text='Verification Uninitiated', size_hint=(1, 0.1))

        # Add items to Layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.webcam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification)

        # Setup video capture device
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 33.0)

        return layout

    # Run continuously to get video feed
    def update(self, *args):
        # Read frame from opencv
        ret, frame = self.capture.read()
        frame = frame[120:120 + 250, 200:200 + 250, :]

        # Flip horizontal and convert image to texture
        buf = cv2.flip(frame, 0).tostring()
        img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.webcam.texture = img_texture


if __name__ == '__main__':
    CamApp().run()
