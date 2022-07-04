#!/bin/sh
tmux kill-session -a
cd /Users/sandradelgado/Documents/GitHub/portfolio-Katherine
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -d -s portfolio-Delgado
tmux send-keys -t portfolio-Delgado "python3 -m venv python3-virtualenv" ENTER
tmux send-keys -t portfolio-Delgado "source python3-virtualenv/bin/activate" ENTER
tmux send-keys -t portfolio-Delgado "pip install -r requirements.txt" ENTER
tmux send-keys -t portfolio-Delgado "export FLASK_ENV=development" ENTER
tmux send-keys -t portfolio-Delgado "flask run --host=0.0.0.0" ENTER

tmux a -t portfolio-Delgado
