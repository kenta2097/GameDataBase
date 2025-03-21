# GameDataBase

[Join GameDataBase on Patreon and consider supporting the project](https://www.patreon.com/GameDataBase)

GameDataBase project aims to provide the most detailed information about every videogame (console, computer and arcade) for sorting purposes. Goal is to unify in one place all available useful information for emulation projects like MiSTer, to make possible more efficient and specific searches. GameDataBase will be published in different files (by platform).

These lists are basically table files made of metadata fields separated by commas (CSV) as following:

- Screen title @ Exact (title in original character set, if applicable. This is particularly useful for Japanese titles usually transcribed in roman characters. Purist, curious and of course Japanese people will enjoy this)
- Cover Title @ Exact (if applicable)
- ID (to identify multiple versions of the same game)
- Date in format YYYY adding MM and DD if known (YYYY-MM-DD)
- Developer
- Publisher
- Tags with additional information about the game
- MAME filename
- MD5 hash
- SHA1 hash
- SHA256 hash
- SHA512 hash

# Guide for tags
GameDataBase uses a simple tag taxonomy to classify games in as many ways as possible. These tags main purpose is to improve sorting and searching. Of course this list will be updated as new ones emerge from darkness.

**Stand alone tags (#)**
This kind of tags defines useful uncommon attributes we can find in multiple games of multiple systems. They are intended to be visible. Let's imagine the following tags inside little color labels before (or after) the line of their respective titles in a list. These are:

**#mameparent** (MAME parent file)
**#bios** (BIOS game)
**#promo** (Promotion product)
**#qsound** (QSound)

**Group tags (#)+(:)+(>)**
This kind of tags uses subcategories to organize more complex things. There are three levels. The first (#) is for the main attribute, the second (:) is its value, and the third (>) is a subvalue. This subvalue is only specific information about their most immediate (:) value.

Several values and subvalues can be added for every main attribute. So, if we have **#genre:sports>wrestling:fighting**, we have two genre (_sports_ and _fighting_) and one subgenre only for the _sports_ tag (_wrestling_). There are:

**#input** (Input system)
**:joystick** (Joystick)
**:doublejoystick** (Double joystick)
**:rotary** (Rotary joystick)
**:stick** (Stick)
**:twinstick** (Twin Stick)
**:trackball** (Trackball)
**:paddle** (Paddle)
**:spinner** (Spinner)
**:wheel** (Wheel)
**:dial** (Dial)
**:lightgun** (Lightgun)
**:optical** (Optical device)
**:puncher** (Puncher)
**:motion** (Motion detection)
**:buttons** (In-game buttons)
**:keys** (Keyboard keys)
**:pedals** (Pedals)

**#input:joystick** / **#input:doublejoystick**
**\>2h** (2-way horizontal)
**\>2v** (2-way vertical)
**\>3** (3-way)
**\>4** (4-way)
**\>8** (8-way)

**#input:buttons** = **#input:pedals** = **#input:keys**
**\>1** (1)
**\>2** (2)
**\>3** (3)
**\>4** (4)
**\>6** (6)
**\>11** (11)
**\>12** (12)
**\>19** (19)
**\>23** (23)
**\>pneumatic** (Pneumatic buttons)

**#players** (Maximum number of players)
**:1** (1 player)
**:2** (2 players)
**:3** (3 players)
**:4** (4 players)
**:6** (6 players)
**:8** (8 players)
**:10** (10 players)
**:coop** (Cooperative)
**:vs** (Versus)
**:alt** (Alternating)

**#tate** (Vertical screen)
**:cw** (Clockwise)
**:ccw** (Counter clockwise)

**#multigame** (Multigame)
**:compilation** (Compilation)

**#unlicensed** (Unlicensed)
**:bootleg** (Bootleg/Pirate)
**:hack** (Hack)
**:translation** (Fan translation)
**:aftermarket** (Aftermarket)

**#genre** (Genre)
**:action** (Action)
**:platformer** (Platformer)
**:fighting** (Fighting)
**:brawler** (Beat'em up)
**:rpg** (RPG)
**:sports** (Sports)
**:shmup** (Shoot'em up)
**:puzzle** (Puzzle)
**:racing** (Racing)
**:rhythm** (Rhythm)
**:railshooter** (Rail shooter)
**:blockbreaker** (Block breaker)
**:maze** (Maze)
**:adventure** (Adventure)
**:pointandclick** (Point and click)
**:shooting** (Shooting gallery)
**:shooter** (Shooter)
**:runandgun** (Run and gun)
**:hackandslash** (Hack and slash)
**:survivalhorror** (Survival Horror)
**:dungeoncrawler** (Dungeon crawler)
**:pinball** (Pinball)
**:strategy** (Strategy)
**:roguelite** (Roguelite)
**:sim** (Simulation)
**:flightsim** (Flight simulator)
**:trainsim** (Train simulator)
**:datesim** (Date simulator)
**:lifesim** (Life simulator)
**:farmsim** (Farm simulator)
**:petsim** (Pet simulator)
**:board** (Board game)
**:quiz** (Quiz game)
**:fishing** (Fishing)
**:cooking** (Cooking)
**:cardgame** (Card game)
**:cards** (Classic cards)
**:hanafuda** (Hanafuda)
**:billiard** (Billiard)
**:jackpot** (Jackpot)
**:pachinko** (Pachinko)
**:minigames** (Mini games)
**:jankenpon** (Rock paper scissors)
**:kiddieride** (Kiddie ride)
**:bowling** (Bowling)
**:darts** (Darts)
**:mogurataiji** (Whac-A-Mole)
**:visualnovel** (Visual novel)
**:god** (God game)
**:building** (Building)
**:derby** (Derby horse ride)
**:strip** (Strip)
**:vending** (Vending machine)
**:redemption** (Redemption)
**:mechanical** (Mechanical)
**:educational** (Educational)
**:marketing** (Marketing)
**:media** (Non-game media)
**:drawing** (Drawing)
**:karaoke** (Karaoke)
**:application** (Application)
**:test** (Test)
**:sdk** (Software Development Kit)
**:slideshow** (Picture slideshow)
**:sound** (Only sound)

**#genre:sports**
**\>soccer** (Soccer)
**\>basketball** (Basketball)
**\>baseball** (Baseball)
**\>volleyball** (Volleyball)
**\>rugby** (Rugby)
**\>football** (American football)
**\>dodgeball** (Dodgeball)
**\>hockey** (Ice Hockey)
**\>skiing** (Skiing)
**\>skateboarding** (Skateboarding)
**\>snowboarding** (Snowboarding)
**\>tennis** (Tennis)
**\>pingpong** (Ping Pong)
**\>paddle** (Paddle)
**\>squash** (Squash)
**\>badminton** (Badminton)
**\>cycling** (Cycling)
**\>formula1** (Formula 1)
**\>rally** (Rally)
**\>nascar** (NASCAR)
**\>motogp** (Moto GP)
**\>motocross** (Motocross)
**\>golf** (Golf)
**\>cricket** (Cricket)
**\>boxing** (Boxing)
**\>kickboxing** (Kick Boxing)
**\>wrestling** (Wrestling)
**\>sumo** (Sumo)
**\>karate** (Karate)
**\>judo** (Judo)
**\>kendo** (Kendo)
**\>decathlon** (Decathlon)
**\>archery** (Archery)
**\>swimming** (Swimming)
**\>rowing** (Rowing)
**\>kayak** (Kayak)

**#genre:board**
**\>chess** (Chess)
**\>shougi** (Shōgi)
**\>go** (Go)
**\>mahjong** (Mahjong)
**\>reversi** (Reversi)
**\>othello** (Othello)

**#genre:rpg**
**\>a** (Action RPG)
**\>j** (JRPG)
**\>s** (Strategy RPG)

**#genre:shmup**
**\>h** (Horizontal shoot'em up)
**\>v** (Vertical shoot'em up)
**\>i** (Isometric shoot'em up)
**\>danmaku** (Bullet hell)

**#genre:puzzle**
**\>drop** (Drop pieces puzzle)

**#genre:racing**
**\>combat** (Combat racing)

**#genre:shooter**
**\>3p** (Third person shooter)

**#genre:vending**
**\>popcorn** (Popcorn)
**\>purikura** (Photo stickers)

**#disc** (Disc)
**\:1** (1, 2, 3, etc)
**\>2** (2, 3, 4, etc)

**#lang** (Language)
**:ja** (Japanese)
**:en** (English)
**:es** (Spanish)
**:fr** (French)
**:pt** (Portuguese)
**:de** (German)
**:it** (Italian)
**:sv** (Swedish)
**:nl** (Dutch)
**:no** (Norwegian)
**:fi** (Finnish)
**:cs** (Czech)
**:sl** (Slovenian)
**:ru** (Russian)
**:kh** (Simplified Chinese)
**:ch** (Chinese)
**:ko** (Korean)
**:fremen** (Fremen)

**#based** (Coming from another media)
**:movie** (Movie)
**:manganime** (Manga and/or anime)

**#official** (Official sealed)
**:sports** (Sports license)

**#endorsed** (Endorsed)
**:celeb** (Famous people)
**:company** (Company or brand)

**#port** (Ported from another system)
**#remake** (Remake from another system)
**:arcade** (Arcade)
**:c64** (Commodore 64)
**:amiga** (Commodore Amiga)
**:apple2** (Apple II)
**:mac** (Apple Macintosh)
**:bbcmicro** (Acorn BBC Micro)
**:dragon32** (Dragon 32)
**:elektronika60** (Elektronika 60 / Электроника 60)
**:atari400** (Atari 400)
**:atarist** (Atari ST)
**:lynx** (Atari Lynx)
**:pc88** (NEC PC-8801)
**:pc98** (NEC PC-9801)
**:pcengine** (NEC PC Engine)
**:cdrom2** (NEC CD-ROM²)
**:msx** (MSX)
**:x1** (Sharp X1)
**:pc** (PC)
**:sg1000** (SEGA SG-1000)
**:gamegear** (SEGA Game Gear)
**:mark3** (SEGA Mark III / Master System)
**:megadrive** (SEGA MegaDrive / Genesis)
**:saturn** (SEGA Saturn)
**:famicom** (Nintendo Famicom / NES)
**:superfamicom** (Nintendo Super Famicom / SNES)
**:gameboy** (Nintendo GameBoy)
**:playstation** (Sony PlayStation)
**:laseractive** (Pioneer LaserActive)
**:fmtowns** (Fujitsu FM Towns)

**#rerelease** (Re-release)
**:virtualconsole** (Nintendo Virtual Console)
**:virtualconsole>wii** (Nintendo Wii Virtual Console)
**:virtualconsole>wiiu** (Nintendo Wii-U Virtual Console)
**:virtualconsole>3ds** (Nintendo 3DS Virtual Console)
**:switchonline** (Nintendo Switch Online)
**:ereader** (Nintendo e-Reader)
**:animalcrossing** (Nintendo Dōbutsu no Mori+ / どうぶつの森+ / Animal Crossing)
**:capcomtown** (CAPCOM Town)
**:namcoanthology>1** (NAMCO Anthology 1)
**:namcoanthology>2** (NAMCO Anthology 2)
**:namcot** (NAMCOT Collection / ナムコットコレクション)
**:namcot>1** (NAMCO Museum Archives Volume 1)
**:namcot>2** (NAMCO Museum Archives Volume 2)
**:castlevaniaanniversary** (Akumajō Dracula Anniversary Collection / 悪魔城ドラキュラ Anniversary Collection / Castlevania Anniversary Collection)
**:contraanniversary** (Contra Anniversary Collection / 魂斗羅 Anniversary Collection)
**:cowabunga** (Teenage Mutant Ninja Turtles: The Cowabunga Collection)
**:dariuscozmic** (Darius Cozmic Collection)
**:disneyclassic** (Disney Classic Games Collection)
**:limitedrun** (Limited Run Games)
**:iam8bit** (iam8bit)
**:sonicclassic** (Sonic Classic Collection)
**:sonicmegacollection** (Sonic Mega Collection / Sonic Mega Collection+)
**:mdclassics** (SEGA MegaDrive Classics / SEGA Genesis Classics)
**:smashpack** (SEGA Smash Pack)
**:3dfukkoku** (SEGA 3D Fukkoku Archives / セガ3D復刻アーカイブス / SEGA 3D Classics Collection)
**:mdmini** (SEGA MegaDrive Mini / SEGA Genesis Mini)
**:gamenokanzume>1** (Game no Kanzume Vol.1 / ゲームのかんづめ Vol.1)
**:gamenokanzume>2** (Game no Kanzume Vol.2 / ゲームのかんづめ Vol.2)

**#addon** (Specific external hardware recommended or required)
**:bikehandle** (SEGA Bike Handle)
**:graphicboard** (SEGA Graphic Board)
**:3dglasses** (SEGA 3-D Glasses)
**:fmsoundunit** (SEGA FM Sound Unit)
**:lightphaser** (SEGA Light Phaser)
**:paddlecontrol** (SEGA Paddle Control)
**:sportspad** (SEGA Sports Pad)
**:6button** (SEGA Six Button Control Pad)
**:menacer** (SEGA Menacer)
**:segavr** (SEGA VR Headset)
**:megamodem** (SEGA Mega Modem)
**:megaanser** (SEGA Mega Anser)
**:toshokan** (SEGA Game Toshokan / ゲーム図書館)
**:segachannel** (SEGA Channel)
**:xband** (Catapult XB∀ND)
**:meganet* (Tec Toy MegaNet)
**:teleplay** (Baton Teleplay System)
**:linkup** (Technopop Link-up Cable)
**:justifier** (Konami The Justifier / サ・ジャスティファイアー)
**:gamegun** (American Laser GameGun)
**:teevgolf** (Sports Sciences TeeVGolf)
**:catalyst** (HeartBeat Catalyst)
**:segatap** (SEGA Tap / Multiplayer / Team Player / セガタップ)
**:4wayplay** (Electronic Arts 4 Way Play)
**:backupramcart** (Mega-CD Back Up RAM Cartridge / バックアップRAMカートリッジ)
**:megacd** (SEGA Mega-CD / SEGA-CD)
**:super32x** (SEGA Super 32X / MegaDrive 32X / Genesis 32X)
**:taisencable** (SEGA Game Gear Taisen Cable / Gear-to-Gear Cable)
**:xe1ap** (Dempa Micomsoft XE-1 AP)
**:smash** (Realtec Smash Controller)
**:comcable** (NEC COM Cable / TurboExpress)
**:illustbooster** (NEC Illust Booster)
**:printbooster** (NEC Print Booster)
**:photoreader** (NEC Photo Reader)
**:avenuepad3** (NEC Avenue Pad 3)
**:avenuepad6** (NEC Avenue Pad 6)
**:pcemultitap** (Hudson Multitap / NEC TurboTap)
**:tennokoe** (Hudson Ten no Koe 1&2 / NEC Backup Booster I&II / NEC TurboBooster-Plus)
**:memorybase128** (NEC Memory Base 128)
**:megald** (Pioneer LaserActive PAC-S Mega-LD)
**:ldrom2** (Pioneer LaserActive PAC-N LD-ROM²)
**:mouse>md** (SEGA Mouse)
**:mouse>pce** (NEC PC Engine Mouse)
**:mouse>pcfx** (NEC PC-FX Mouse)
**:mouse>n64** (Nintendo 64 Mouse)
**:10key** (NEC 10 Key Controller Pad)
**:pachinkocontroller** (Coconuts Pachinko Controller / パチンココントローラー)
**:cdromrom** (NEC CD-ROM² / Super CD-ROM² / Arcade CD-ROM² / PC Engine Duo / TurboGrafx-CD / TurboDuo)
**:supersystemcard** (NEC PC Engine Super System Card CD-ROM²)
**:arcadecard (NEC PC Engine Arcade Card Pro CD-ROM² / NEC PC Engine Arcade Card Duo CD-ROM²)
**:gamesexpresscard** (Games Express CD Card)
**:rss** (Roland Sound Space)
**:develobox** (Tokuma Shoten Develo Box)
**:teststation** (Nintendo NES Test Station)
**:disksystem** (Nintendo Famicom Disk System)
**:zapper** (Nintendo Zapper)
**:rob>gyro** (Nintendo Family Computer Robot Gyro Set / R.O.B. / Robotic Operating Buddy)
**:rob>block** (Nintendo Family Computer Robot Block Set)
**:turbofile** (ASCII Turbo File / Turbo File II / Turbo File GB / Turbo File Adapter / Turbo File Twin)
**:datarecorder** (Panasonic Famicom Data Recorder)
**:arkanoid** (Taito Arkanoid controller)
**:battlebox** (IGS Battle Box)
**:taptapmat** (IGS Tap-Tap Mat + Tonkachi / タップタップマット + トンカチ)
**:datach** (Bandai Datach Joint ROM System)
**:familytrainer** (Bandai Family Trainer / Power Pad / Family Fun Fitness)
**:karaokestudio** (Bandai Karaoke Studio)
**:oekakids** (Bandai Oekakids / おえかキッズ)
**:bandaihypershot** (Bandai Hyper Shot / ハイパーショット)
**:deckenhancer** (Camerica Aladdin Deck Enhancer)
**:oyagame** (Sunsoft Oyagame / 親ガメ)
**:powerglove** (Mattel Power Glove)
**:3dsystem** (Nintendo Famicom 3D System)
**:networksystem** (Nintendo Family Computer Network System)
**:4playersadaptor** (Hori 4 Player Adaptor / Nintendo Four Score)
**:horitrack** (Hori Track / ホリトラック)
**:miracle** (The Miracle MIDI Keyboard)
**:pianokeyboard** (Konami MIDI Keyboard)
**:hypershot** (Konami HyperShot)
**:qtai** (Konami QTai / Q太)
**:taikanfamicom** (Konami Taikan Famicom / 大汗ファミコン)
**:laserscope** (Konami LaserScope)
**:mahjongcontroller** (CAPCOM Mahjong Controller / Mahjong Controller II)
**:climberstick** (Nichibutsu Climber Stick)
**:partytap** (PR21 Party Tap)
**:hardwarebike** (Varie Hardware Bike / ハードウーアバイク)
**:uforce** (Brøderbund UForce Controller)
**:supergameboy** (Nintendo Super GameBoy 1&2)
**:superturbofile** (ASCII Super Turbo File)
**:supermultitap** (Hudson Super Multitap)
**:samegame** (Hudson SameGame Cassette / 鮫亀カセット)
**:gamelinkcable** (Nintendo Tsūshin Cable / Game Link Cable)
**:fourplayeradapter** (Nintendo Four Player Adapter)
**:pocketcamera** (Nintendo Pocket Camera / GameBoy Camera)
**:pocketprinter** (Nintendo Pocket Printer / GameBoy Printer)
**:controllerpak** (Nintendo Controller Pak)
**:transferpak** (Nintendo 64GB Pak / Transfer Pak)
**:rumblepak** (Nintendo Shindō Pak / Rumble Pak)
**:expansionpak** (Nintendo Memory Kakuchō Pak / Expansion Pak)
**:64dd** (Nintendo 64DD)
**:randnetmodem** (Randnet Modem)
**:capturecassette** (Nintendo 64 Capture Cassette)
**:n64mic** (Nintendo 64 Mic)
**:keyboard>fc (Famicom Keyboard)
**:keyboard>n64 (Nintendo 64 Keyboard)
**:biosensor** (SETA Bio Sensor)
**:smartmediacard** (Hagiwara Syscom SmartMedia Card)
**:vrs** (VRS / Onseininshiki System / Voice Recognition Unit)
**:ddr** (Konami Dance Dance Revolution controller)
**:tsurikon64** (ASCII Tsurikon 64)
**:barcodeboy** (NAMCOT Barcode Boy)
**:reeladapter** (Bandai Reel Adapter)
**:workboy** (Fabtek WorkBoy)
**:ngplink** (SNK NeoGeo Pocket Link Cable)
**:radiounitwireless** (SNK Musen Unit / Radio Unit Wireless Adaptor)
**:setsuzoku** (SNK NeoGeo Pocket-Dreamcast Setsuzoku Cable)
**:barcodebattler2** (Epoch Barcode Battler II + Sen'yō Setsuzoku Cord)

**#addon:fmsoundunit**
**\>hidden** (Hidden FM Sound Unit)

**#addon:3dglasses**
**\>hidden** (Hidden 3-D Glasses)

**#sg1000** (SEGA SG-1000)
**:sc3000** (SEGA SC-3000)
**:othello** (Tsukuda Original Othello Multivision)

**#gb** (GameBoy)
**:mono** (Monochrome)
**:color** (Color)
**:sgb** (Nintendo Super GameBoy / Super GameBoy 2)
**:np** (Nintendo Power GB-Memory Cartridge)

**#fds** (Famicom Disk System)
**:dw** (Disk Writer)

**#sfc** (Super Famicom)
**:np** (Nintendo Power SF-Memory Cassette)
**:soundlink** (SoundLink support)

**#pce** (PC Engine)
**:pcsg** (PC SuperGrafx)

**#ngp** (NeoGeo Pocket)
**:mono** (Monochrome)
**:color** (Color)

**#rev** (Revision)
**:1** (1)
**:2** (2)
**:a** (A)
**:b** (B)
**:c** (C)
**:g** (G)

**#set** (Set)
**:1** (1)
**:2** (2)

**#unfinished** (Unfinished)
**:beta** (Beta)
**:proto** (Prototype)
**:demo** (Demo)
**:sample** (Sample)
**:debug** (Debug)
**:competition (Competition)

**#unfinished:beta**
**\>1**
**\>2**
**\>3**
**\>alt** (Alternative)

**#unfinished:demo**
**\>1**
**\>2**
**\>auto** (Automatic)
**\>kiosk** (Kiosk)

**#clone** (Clone)
**:mario** (Mario)
**:sonic** (Sonic)
**:sf2** (Street Fighter II)
**:tetris** (Tetris)

**#embed** (Embed extra hardware)
**:battery** (Battery)
**:flashram** (Flash RAM)
**:feram** (Ferroelectric RAM)
**:eeprom** (EEPROM)
**:ram** (Extra RAM)
**:led** (LED)
**:rtc** (Real-Time Clock chip)
**:svp** (SEGA Virtua Processor / SVP)
**:lockon** (SEGA Sonic & Knuckles Lock-On Technology)
**:mmc5** (Nintendo MMC5 chip)
**:vrc6** (Konami VRC VI chip)
**:vrc7** (Konami VRC VII chip)
**:n163** (NAMCO 163 chip)
**:5b** (Sunsoft 5B chip)
**:m50805** (Mitsubishi M50805 chip)
**:7755** (NEC µPD7755C chip)
**:7756** (NEC µPD7756C chip)
**:kogame** (Sunsoft Kogame Cassette Slot / 子ガメカセット)
**:rj11** (RJ-11 port)
**:gbkiss** (Hudson GB Kiss)
**:pocketsonar** (Bandai Pocket Sonar)
**:smartmedia** (Tokyo Electron SmartMedia Double Slot)
**:jcart** (Codemasters J-Cart)

**#save** (The way you can save your progress)
**:password** (Password)
**:backup** (Backup)

**#3d** (Game uses some kind of 3D effect)
**:stereoscopic** (Stereoscopic 3D)
**:anaglyph** (Anaglyph 3D)

**#arcadeboard** (Arcade board)
**:capcom** (All CAPCOM boards)
**:sega** (All SEGA boards)
**:irem** (All Irem boards)
**:toaplan** (All Toaplan boards)
**:jaleco** (All Jaleco boards)
**:snk** (All SNK boards)
**:taito** (All Taito boards)

**#arcadeboard:capcom**
**\>cps** (CAPCOM CP System)
**\>cpsdash** (CAPCOM CP System Dash)
**\>cpschanger** (CAPCOM CP System Changer)
**\>cps2** (CAPCOM CP System II)
**\>cps3** (CAPCOM CP System III)

**#arcadeboard:sega**
**\>vco** (SEGA VCO Object)
**\>1** (SEGA System 1)
**\>2** (SEGA System 2)
**\>16** (SEGA System 16)
**\>16a** (SEGA System 16A)
**\>16b** (SEGA System 16B)
**\>16c** (SEGA System 16C)
**\>18** (SEGA System 18)
**\>24** (SEGA System 24)
**\>32** (SEGA System 32)
**\>m32** (SEGA System Multi 32)
**\>c** (SEGA System C)
**\>c2** (SEGA System C-2)
**\>e** (SEGA System E)
**\>x** (SEGA X Board)
**\>y** (SEGA Y Board)
**\>stv** (SEGA Titan Video)

**#arcadeboard:irem**
**\>m10** (Irem M10)
**\>m15** (Irem M15)
**\>m27** (Irem M27)
**\>m52** (Irem M52)
**\>m57** (Irem M57)
**\>m58** (Irem M58)
**\>m62** (Irem M62)
**\>m63** (Irem M63)
**\>m72** (Irem M72)
**\>m75** (Irem M75)
**\>m81** (Irem M81)
**\>m82** (Irem M82)
**\>m84** (Irem M84)
**\>m90** (Irem M90)
**\>m92** (Irem M92)
**\>m97** (Irem M97)
**\>m107** (Irem M107)

**#arcadeboard:snk**
**\>mvs** (MVS / Multi Video System)

**#arcadeboard:taito**
**\>xsystem** (X System)
**\>bsystem** (B System)
**\>hsystem** (H System)
**\>lsystem** (L System)
**\>zsystem** (Z System)
**\>osystem** (O System)
**\>f1** (F1 System / F2 System Extended)
**\>f2** (F2 System)
**\>lg** (LG System)

**#arcadeboard:toaplan**
**>1** (Toaplan Version 1)
**>2** (Toaplan Version 2)

**arcadeboard:jaleco**
**\>ms1** (Jaleco Mega System 1)

**#format**
**:mycard** (SEGA My Card)
**:thesegacard** (The SEGA Card)
**:themegacartridge** (The Mega Cartridge Japan version)
**:silvercartridge** (Silver Cartridge)
**:goldcartridge** (Gold Cartridge)

**#format:goldcartridge**
**\>1m**
**\>2m**
**\>4m**

**#reboxed** (Reboxed)
**:bluebox** (Blue Box)
**:purplebox** (Purple Box)
**:classicedition** (Classic Edition)
**:segaclassic** (SEGA Classic)
**:kixxedition** (Kixx Edition)
**:segaages** (SEGA Ages)
**:megadrive4** (Tec Toy MegaDrive 4)
**:reactor** (AtGames Reactor)
**:gopher** (AtGames Gopher)
**:meisaku** (Meisaku Collection)
**:majesco** (Majesco)
**:megahit** (Mega Hit Series)
**:konamiclassics** (Konami Classics)
**:eaclassics** (Console Classics)
**:videogameclassics** (Accolade Video Game Classics)
**:gamenokanzume>o** (Game no Kanzume Otokuyō / ゲームのかんづめ お徳用)
**:soundware** (Koei SoundWare audio CD)
**:playerschoice** (Players Choice / Million Seller)
**:classicserie** (NES / Game Boy Classic Serie)
**:kousenjuu** (Kōsenjū Series / 光線銃シリーズ)
**:disneysclassic** (Disney's Classic Video Games)
**:snkbestcollection** (Best Collection)
**:xeye** (JVC X'Eye)

**Searching tags ($)**
The goal of this kind of tags is just for searching purposes. They are designed to be internal (invisible) to provide additional information we can unlock when we search for it.

**Commercial tags for searching purposes**
This kind of tags provides us information about famous franchises and characters. For example, if we search for games based on Alien movie franchise and just write "alien", we probably get a huge list of games that have nothing to do with the franchise like _Alien Soldier_, _Alien Storm_ or _Alien Syndrome_. However, this tag unlocks the "did you mean" feature. This can be used as an additional useful search tool.

These tags even allow us to search for famous characters like Dracula. If we were to write "dracula" in a regular game search engine, we would only get games which contains the word _Dracula_, but there would be no _Castlevania_ or _Master of Darkness_. This tag can solve that. More tags will be added as soon new interesting franchises appeared in the process. At the end they will be a lot. For now, take a look to these ones:

**$alien** (Alien)
**$asterix** (Astérix & Obélix)
**$batman** (Batman)
**$castlevania** (Castlevania/Akumajō Dracula/悪魔城ドラキュラ)
**$compatihero** (Compati Hero)
**$disney** (Walt Disney)
**$donald** (Donald Duck)
**$dracula** (Dracula)
**$dragonslayer** (Dragon Slayer)
**$dnd** (Dungeons & Dragons)
**$gundam** (Gundam)
**$jurassicpark** (Jurassic Park)
**$kuniokun** (Kunio-kun/くにおくん)
**$looneytunes** (Looney Tunes)
**$mario** (Mario)
**$marvel** (Marvel Comics)
**$mickey** (Mickey Mouse)
**$pacman** (Pac-Man)
**$sherlock** (Sherlock Holmes)
**$simpsons** (The Simpsons)
**$smurfs** (The Smurfs/Les Schtroumpfs/Los Pitufos/Die Schlümpfe)
**$sonic** (Sonic The Hedgehog)
**$spiderman** (Spider-Man)
**$starwars** (Star Wars)
**$superman** (Superman)
**$wonderboy** (Wonder Boy)
**$xmen** (X-Men)

**Keyword tags**
In the same way, these tags are just for searching purposes based on keywords. If we look for games based on a movie or a manga, this kind of tags allow you to find more easier if implemented. Values of the right are like synonyms. Infinite possibilities. We can add tags like _ninja_, _cute_, _gore_ or, don't know, _rockandroll_. But for now, there's only these:

**$lightgun**
**$spinner**

Please, be welcome and enjoy. Thank you very much for coming. Pretty nice things to come.
