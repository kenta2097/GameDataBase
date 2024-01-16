# GameDataBase

GameDataBase project aims to provide the most detailed information about every videogame (console, computer and arcade) for sorting purposes. Goal is to unify in one place all available useful information for emulation projects like MiSTer, to make possible more efficient and specific searchs. GameDataBase will be published in different files (by platform).

These lists are basically table files made of metadata fields separated by commas (CSV) as following:

1. Full title
2. Title in original character set, if applicable. This is particulary useful for Japanese titles usually transcribed in roman characters. Purist, curious and of course Japanese people will enjoy this.
3. ID (to identify multiple versions of the same game)
4. Date in format YYYY adding MM and DD if known (YYYY-MM-DD)
5. Developer
6. Tags with additional information about the game
7. MAME filename
8. MD5 hash
9. SHA1 hash
10. SHA256 hash
11. SHA512 hash

Tags (#):
  - Maximum players available = #1P, #2P...
  - Joystick ways = #0W, #2W, #4W, #8W... (#0W means there's no stick)
  - Number of buttons = #1B, #2B...
  - Non-common control system = #spinner, #lightgun (specific lightgun shows as #lightgun:lightphaser)
  - Non-common screen = #tate, #triple
  - Two or more players mode = #coop (cooperative), #vs (versus), #alternating (when players play one after another)
  - Genre tags are: #shmup (shoot'em up; joined to :danmaku is a bullet-hell), #brawler (AKA beat'em up), #puzzle, #fighting, #platformer, #runandgun, #hackandslash, #kiddieride, #quiz, #mogurataiji (AKA whack-a-mole), #datesim (date simulator), #maze, #adventure, #sports (:soccer, :basketball, :tennis, :football (American), :formula1, :boxing, :wrestling, :baseball, :golf)
  - System tags are: #cps (all CAPCOM CP System boards) joined with :cps1 (CAPCOM CP System), :cpsdash (CAPCOM CP System Dash), :cpschanger (CAPCOM CP System Changer), :cps2 (CAPCOM CP System II) and :cps3 (CAPCOM CP System III)
  - #licence = Game is based on a commercial licence
  - #celeb = Game uses famous name
  - #multigame = Game includes a selection of different games to play
  - #mameparent = Parent arcade game in MAME por specific ID
  - #prototype = Game never released but a WIP file were dumped
  - More to come.
