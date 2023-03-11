# Command Line ASCII Chess
A chess game/utility that runs entirely in a terminal using ASCII characters to display game states. Will include support for single (vs AI) and multiplayer gamemodes, along with swapping between the two during games. AI will be implemented using minimax and alpha-beta pruning to reduce computation. Multiplayer will be implemented first and will simply switch between prompting inputs from player 1 and from player 2.

Will include support options for piece animations and AI delay. Piece animations will show each step of a given move as opposed to just the final result of the move. AI delay will be a minimum time that the AI has to wait before displaying its results (if computation takes too long, it may go over that time, but never under). These are both pureply QoL features.

Will also make use of threads and file IO to include support for save files and error logging.


# Note
Coding aside, this project is an experiment of sorts for myself in regards to organization. In general for any kind of project, whether it is coding, writing a paper, or something else, I have some strange combination of a Notion page, a Word Doc, possibly Notepad, and way too many Chrome tabs (and of course the project file(s) itself).
Regarding school coding projects, in some cases I am required to use a specific development environment, and in other cases I don't use Github for academic integrity purposes, which in turn leads to me using multiple services for each project. So for this I am experimenting with having everything project-related in this repo in order to a) have an opportunity to actually use Github and b) to try out new organization methods.
