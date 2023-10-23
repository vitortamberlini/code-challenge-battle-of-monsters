# 🚀 The Coding Challenge: Battle of the Monsters Edition!

🐉 **Scenario**: Think of this as a Pokémon game, but a bit more... wild. You've got monsters with stats like attack, defense, and perhaps a penchant for afternoon tea. Oh, and they battle each other. Let's build and fix it together!

**🎯 What's already there**: 
- The CRUD for our battle arena.
- A nifty endpoint to see all the battles that have taken place (For those who love keeping score).

## 🥇 Goals

1. **Implement the missing pieces**:
    - Endpoints to view our fierce monsters 🐲.
    - Starting a battle, because... well, it's a battle app 🥊.
    - Deleting a battle, for those "Oops, didn't mean to do that!" moments.
    
2. **TODO or not TODO?** That is the question.
    - Work on tests marked with `TODO`.

3. **🎨 Picasso Moment**: Make sure your code is art - the code style check script should paint a pretty picture.

## 🔍 Important Notes (or "Stuff to Not Break")

- 🚫 Please, no tinkering with already set tests. If your code is pure gold, those tests should pass without drama.
- Oh, by the way, expect some bumps along the way while getting the app to run. But hey, debugging is part of the fun, right? 😜 We believe in you!

## 📖 Battle Mechanics (or "How to Ensure Your Monster Doesn't Get a Boo-boo")

- Fast and Furious: The monster with the *jet-like* speed attacks first. If speeds tie, the stronger attacker takes the lead.
  
- 🧮 Math Time: To figure out the damage, it's `attack - defense`. If the attack feels... meek, and is equal to or lower than the defense, damage is a humble 1.

- 🩹 Ouch! Subtract the damage from the HP `(HP = HP - damage)`.
  
- Quick Battles: The monsters go back and forth until one emerges victorious. The battle endpoint should spill the beans about the winner in just one call.

- And the winner is... whoever gets the enemy's HP down to zero. Simple, right?

## 🛠 Setting Up the Project

1. **Clone and Own**: Get that repository onto your machine. 
   
2. **Let's Go Virtual**: Set up the Python venv.
    ```bash
    python -m venv venv
    ```

3. **Grab All The Goodies**: Install dependencies.
    ```bash
    pip install -r requirements/requirements.txt
    ```

4. **DB Magic**: Handle database migrations and seeds.
    ```bash
    make migrate
    ```

## 💡 How to Use

- **Lint It Up**: Keep things tidy with:
    ```bash
    make lint
    ```

- **Beautify**: Automagically make most of your lint errors vanish:
    ```bash
    make black
    ```

- **Kickstart the App**: Because you want to see the magic:
    ```bash
    make runserver
    ```

- **Test Time**: See if your code is the hero we deserve:
    ```bash
    make test
    ```

- **Module-specific Tests**: Because sometimes you only want to study one chapter:
    ```bash
    make test_module
    ```

## 🏆 Acceptance Criteria (or "How to Win this Challenge")

1. Monster endpoints: Up, running, and roaring.
2. Battle endpoints: Perfectly set for action.
3. The old tests should now be beaming with green ticks.
4. The `TODO` tests? Nailed them!
5. A test coverage that boasts at least 80% (wear it like a badge!).
6. The code style check? It should be giving you a standing ovation by the end.

