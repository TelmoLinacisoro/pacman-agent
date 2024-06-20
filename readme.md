# Eutopia AI Pacman Capture-the-Flag

This project was developed for the Eutopia Pacman contest.

We considered the following factors:

1. **Successor Score**: Potential gains from reaching a specific state (collecting food).
2. **Distance to Key Points**: How far the agent is from important locations (food and opponents).
3. **Enemy Position and State**: Whether an opponent is nearby and whether they are vulnerable or dangerous.

### Agent Design

Each agent evaluates actions based on a heuristic evaluation function:

1. **Offensive Agent**: Focuses on maximizing score by aggressively collecting food items and evading ghosts.
2. **Defensive Agent**: Concentrates on guarding its territory and intercepting enemy Pacman.

The agents anticipate and react to opponents’ actions. For example, predicting where an opponent will move next based on their current position and potential actions, and adjusting strategies dynamically based on the changing game state and opponent behavior.
