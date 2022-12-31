# Lighthouse Pong

This is a simple pong game for the lighthouse project at our university CAU in Kiel.

## Connecting to lighthouse

To connect the game to the lighthouse 
create a file named `cred.txt` in game directory with following content:

```
username "your_username"
token "api_token" 
```

## Requirements

For running this you need the the libraries `pyghthouse` and `pynput`.

```
pip install pynput;
pip install pyghthouse
```

## Keyboard controls

- `G` - start game

### Player 1
- `A` - move left
- `D` - move right
- `S` - stop movement

### Player 2
- `J` - move left
- `L` - move right
- `K` - stop movement
