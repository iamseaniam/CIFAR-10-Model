#!/usr/bin/env python3
""" Runs hyperparameter tuning """
from keras import layers, models


def build_model(hp):
    