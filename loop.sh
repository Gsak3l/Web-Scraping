#!/bin/bash
for (( i = 0; i < 20; i++ )); do
  sudo cyberghostvpn --traffic --country-code DE --connect
  python3 twitter-bot-enhanced.py
done