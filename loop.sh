#!/bin/bash
for (( i = 0; i < 1; i++ )); do
  python3 twitter-bot-enhanced.py
  sudo cyberghostvpn --traffic --country-code DE --connect
done