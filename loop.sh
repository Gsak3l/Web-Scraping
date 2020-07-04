#!/bin/bash
for (( i = 0; i < 10; i++ )); do
  sudo cyberghostvpn --traffic --country-code DE --connect
  python3 twitter-bot-enhanced.py
  python3 twitter-bot-enhanced.py
done