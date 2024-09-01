# slot-machine-game program overview

The goal of this project is to create a somewhat realistic virtual slot machine game. This will be an inspired version of the video slot machines that appear in GTA V. The slot machine will have 3 reels with 9 possible symbols that can appear. There will be a betting system that alters how much you can win. The game will also take advantage of basic gambling psychology, using a payline to leverage the Near-Miss Effect, along with others.
_Please note: This program is purely a coding exercise and is not intended to promote gambling or the use of psychological manipulation._

### General Game Elements
- Start screen.
- Rules, Info, Credits, Stats, etc.
- User money.
- Ability to choose different slot machines.
- A goal to winning the game (example: to win you must earn 1 million dollars, if you run out of money then you lose).
- Cheat Codes. (unlimited money, etc)
- Basic AI Players.

### Slot Machine Design 
- Title and simplistic text based graphical user interface.
- Simple user interface that shows a big button to 'Pull The Lever' with. 
- 3 reels with 9 possible symbols on each.
- Single vertical payline running across the reels. 
- Display that shows the payout amount.
- Betting system that changes the possible payout amount.
- Display that generates a random message to encourage the user to continue playing.

### Psychological Elements 
- [NEUROBEHAVIORAL EVIDENCE FOR THE ‘‘NEAR-MISS’’ EFFECT IN
PATHOLOGICAL GAMBLERS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2861872/pdf/jeab-93-03-313.pdf)
- [The Effect of Losses Disguised as Wins and Near Misses
in Electronic Gaming Machines: A Systematic Review
](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5663799/pdf/10899_2017_Article_9688.pdf)
- [GENERATING VARIABLE AND RANDOM SCHEDULES OF
REINFORCEMENT USING MICROSOFT EXCEL MACROS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2408339/pdf/jaba-41-02-227.pdf)
- Illusion of Control
- Betting Options and Complexity
- Sound/Visual Effects

### Backend Infrastructure 
- Visual Data Analysis (graph plot).
- Statistics (Wins, Spins, Losses, Money Earned, etc).
- Import/Export stats via text file
