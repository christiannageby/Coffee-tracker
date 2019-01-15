#!/bin/bash

cd ~/
git clone https://github.com/christiannageby/Coffee-tracker.git coffeeTracker

ln -s ~/coffeeTracker/add_cup_today.py /add_cup
ln -s ~/coffeeTracker/coffee_stats.py /stats

echo "Coffee-Tracker istalled"

