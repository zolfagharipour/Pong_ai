### Pong AI Game 🏓🤖

A Python-based **Pong game** where a human player competes against an **AI opponent** that predicts ball trajectory. The AI only sees the game **once per second**, making strategic decisions based on ball physics.

## Features 

- **Real-Time Pong Gameplay** – Classic Pong with enhanced physics.
- **AI Opponent with Ball** Trajectory Prediction – The AI calculates where the ball will land and moves accordingly.
- **Dynamic Ball Speed** – The ball's speed increases based on where it hits the paddle, making the game more unpredictable.
- **AI Vision Limitation** – The AI can only "see" the game state every 1 second, adding a unique challenge.
- **Configurable Settings** – Modify AI behavior, physics, and game parameters in config.py.
## Installation & Setup
### Prerequisites

Ensure you have Python 3.8+ installed.

### 1. Install Dependencies

The game requires **pygame** and **numpy**. Install them using:
```bash

pip3 install pygame numpy
```
###2. Clone the Repository
```bash
git clone https://github.com/zolfagharipour/Pong_ai
cd Pong_ai
```

## Running the Game

Navigate to the project directory and run:
```bash

python3 src/main.py
```
## How the AI Works 

- The AI **only "sees" the game state every 1 second**.
- When it sees the ball, it predicts its trajectory and moves to the expected impact position.
- The AI **does not control the paddle** — it follows the same movement rules as a human player by stimulation keys **up** and **down**.
- The **ball speed changes dynamically** based on where it hits the paddle, making trajectory prediction harder.

## Game Controls 

| Action | Player 1 |
| --- | --- |
| Move **Up**   | ARROW KEY UP `↑` |
| Move **Down** | ARROW KEY DOWN `↓` |
| Quit **Game** | `Esc` or Close Window |


The AI controls Player 2 automatically.
## Modifying Game Settings

Customize the game in ``src/config.py``:

- **AI vision frequency** (``AI_WAIT = 1``) – Adjust AI wait time in seconds.
- **Ball speed modifiers** – Modify the initial speed of the ball.
- **Screen size**, **paddle speed**, and other game physics.

To experiment with different **difficulty levels**, tweak these parameters!
