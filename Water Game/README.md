A solver for the water game you see so much in ads. It uses recursive backtracking to find a path to a solved state.

The bottles are encoded with 0 indexing, and each color is assigned a number (examples below)
We basically try every possible move from bottle i to bottle j, while tracking the current state to ensure that we don't enter a duplicate state.
Initial attempts at the solver led to some inefficient moves, like passing back and forth between empty bottles before carrying on, but we prune these with the following optimizations:
 - If the target bottle is empty, make sure that the current bottle is not all one color
 - If the target bottle is not empty, make sure that you can shift all of the top color of the current bottle

I also explored a BFS to try to find the shortest path to a valid solution, but the solution space grew intractably large.

![image](https://github.com/nickyfoo/game-stuff/assets/67411893/fd848421-574d-42b1-a2c3-d5281c2a7808)
![image](https://github.com/nickyfoo/game-stuff/assets/67411893/1c524455-98d4-4d1c-bf82-293f5cded6f9)

![image](https://github.com/nickyfoo/game-stuff/assets/67411893/13606262-d467-4bfd-8e42-ad5207ccc701)
![image](https://github.com/nickyfoo/game-stuff/assets/67411893/320296a0-ca8a-4296-bab4-3c75d04bf0ea)
