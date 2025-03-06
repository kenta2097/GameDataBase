# GameDataBase

[Join GameDataBase on Patreon and consider supporting the project](https://www.patreon.com/GameDataBase)

GameDataBase project aims to provide the most detailed information about every videogame (console, computer and arcade) for sorting purposes. Goal is to unify in one place all available useful information for emulation projects like MiSTer, to make possible more efficient and specific searchs. GameDataBase will be published in different files (by platform).

## CSV Fields

| Field | Description |
|-------|-------------|
| Screen title @ Exact | Title in original character set |
| Cover Title @ Exact | If applicable |
| ID | To identify multiple versions |
| Date | Format YYYY-MM-DD |
| Developer | Game developer |
| Publisher | Game publisher |
| Tags | Additional information |
| MAME filename | MAME ROM name |
| MD5 hash | MD5 checksum |
| SHA1 hash | SHA1 checksum |
| SHA256 hash | SHA256 checksum |
| SHA512 hash | SHA512 checksum |

## Guide for tags

GameDataBase uses a simple tag taxonomy to classify games in as many ways as possible. These tags main purpose is to improve sorting and searching. Of course this list will be updated as new ones emerge from darkness.

**Stand Alone Tags**

| Tag | Description |
|-----|-------------|
| #mameparent | MAME parent file |
| #bios | BIOS game |
| #promo | Promotion product |
| #qsound | QSound |

**Group tags (#)+(:)+(>)**
This kind of tags uses subcategories to organize more complex things. There are three levels. The first (#) is for the main attribute, the second (:) is its value, and the third (>) is a subvalue. This subvalue is only specific information about their most inmediate (:) value.

Several values and subvalues can be added for every main attribute. So, if we have **#genre:sports>wrestling:fighting**, we have two genre (_sports_ and _fighting_) and one subgenre only for the _sports_ tag (_wrestling_). There are:

## Input System Tags

| Tag | Description | Subvalues |
|-----|-------------|-----------|
| #input:joystick | Joystick | >2h (2-way horizontal)<br>>2v (2-way vertical)<br>>3 (3-way)<br>>4 (4-way)<br>>8 (8-way) |
| #input:doublejoystick | Double joystick | Same as joystick |
| #input:buttons | In-game buttons | >1 to >23<br>>pneumatic |
| #input:keys | Keyboard keys | >1 to >23 |
| #input:pedals | Pedals | >1 to >23 |

## Players Tags

| Tag | Description |
|-----|-------------|
| #players:1 | 1 player |
| #players:2 | 2 players |
| #players:3 | 3 players |
| #players:4 | 4 players |
| #players:6 | 6 players |
| #players:8 | 8 players |
| #players:10 | 10 players |
| #players:coop | Cooperative |
| #players:vs | Versus |
| #players:alt | Alternating |

## Screen Tags

| Tag | Description |
|-----|-------------|
| #tate | Vertical screen |
| #tate:cw | Vertical screen (clockwise) |
| #tate:ccw | Vertical screen (counter clockwise) |

## Game Collection Tags

| Tag | Description |
|-----|-------------|
| #multigame | Multiple games in one cartridge/disk |
| #multigame:compilation | Official compilation of games |

## License Tags

| Tag | Description |
|-----|-------------|
| #unlicensed | Unlicensed game |
| #unlicensed:bootleg | Bootleg/pirated game |
| #unlicensed:hack | Hacked game |
| #unlicensed:translation | Fan translation |
| #unlicensed:aftermarket | Made after original market cycle |


## Genre Tags

| Main Tag | Description | Subgenres | Subgenre Names |
|----------|-------------|-----------|----------------|
| #genre:action | Action | - | - |
| #genre:adventure | Adventure | :pointandclick<br>:shooting<br>:shooter<br>:runandgun<br>:hackandslash<br>:survivalhorror<br>:dungeoncrawler | Point and click<br>Shooting gallery<br>Shooter<br>Run and gun<br>Hack and slash<br>Survival Horror<br>Dungeon crawler |
| #genre:platformer | Platformer | - | - |
| #genre:fighting | Fighting | - | - |
| #genre:brawler | Beat'em up | - | - |
| #genre:rpg | RPG | >a<br>>j<br>>s | Action RPG<br>JRPG<br>Strategy RPG |
| #genre:sports | Sports | >soccer<br>>basketball<br>>baseball<br>>volleyball<br>>rugby<br>>football<br>>dodgeball<br>>hockey<br>>skiing<br>>skateboarding<br>>snowboarding<br>>tennis<br>>pingpong<br>>paddle<br>>squash<br>>badminton<br>>cycling<br>>formula1<br>>rally<br>>nascar<br>>motogp<br>>motocross<br>>golf<br>>cricket<br>>boxing<br>>kickboxing<br>>wrestling<br>>sumo<br>>karate<br>>judo<br>>kendo<br>>decathlon<br>>archery<br>>swimming<br>>rowing<br>>kayak | Soccer<br>Basketball<br>Baseball<br>Volleyball<br>Rugby<br>American football<br>Dodgeball<br>Ice Hockey<br>Skiing<br>Skateboarding<br>Snowboarding<br>Tennis<br>Ping Pong<br>Paddle<br>Squash<br>Badminton<br>Cycling<br>Formula 1<br>Rally<br>NASCAR<br>Moto GP<br>Motocross<br>Golf<br>Cricket<br>Boxing<br>Kick Boxing<br>Wrestling<br>Sumo<br>Karate<br>Judo<br>Kendo<br>Decathlon<br>Archery<br>Swimming<br>Rowing<br>Kayak |
| #genre:shmup | Shoot'em up | >h<br>>v<br>>i<br>>danmaku | Horizontal<br>Vertical<br>Isometric<br>Bullet hell |
| #genre:puzzle | Puzzle | >drop | Drop pieces puzzle |
| #genre:racing | Racing | >combat | Combat racing |
| #genre:rhythm | Rhythm | - | - |
| #genre:shooter | Shooter | >3p | Third person |
| #genre:board | Board game | >chess<br>>shougi<br>>go<br>>mahjong<br>>reversi<br>>othello | Chess<br>Shōgi<br>Go<br>Mahjong<br>Reversi<br>Othello |
| #genre:sim | Simulation | :flightsim<br>:trainsim<br>:datesim<br>:lifesim<br>:farmsim<br>:petsim | Flight simulator<br>Train simulator<br>Date simulator<br>Life simulator<br>Farm simulator<br>Pet simulator |
| #genre:arcade | Arcade | :pinball<br>:jackpot<br>:pachinko<br>:darts<br>:bowling<br>:kiddieride | Pinball<br>Jackpot<br>Pachinko<br>Darts<br>Bowling<br>Kiddie ride |
| #genre:other | Other | :quiz<br>:fishing<br>:cooking<br>:cardgame<br>:cards<br>:hanafuda<br>:billiard<br>:minigames<br>:jankenpon<br>:mogurataiji<br>:visualnovel<br>:god<br>:building<br>:derby<br>:strip<br>:vending<br>:redemption<br>:mechanical<br>:educational<br>:marketing<br>:media<br>:drawing<br>:karaoke<br>:application<br>:test<br>:sdk<br>:slideshow<br>:sound | Quiz game<br>Fishing<br>Cooking<br>Card game<br>Classic cards<br>Hanafuda<br>Billiard<br>Mini games<br>Rock paper scissors<br>Whac-A-Mole<br>Visual novel<br>God game<br>Building<br>Derby horse ride<br>Strip<br>Vending machine<br>Redemption<br>Mechanical<br>Educational<br>Marketing<br>Non-game media<br>Drawing<br>Karaoke<br>Application<br>Test<br>Software Development Kit<br>Picture slideshow<br>Only sound |

## Language Tags

| Tag | Description |
|-----|-------------|
| #lang:ja | Japanese |
| #lang:en | English |
| #lang:es | Spanish |
| #lang:fr | French |
| #lang:pt | Portuguese |
| #lang:de | German |
| #lang:it | Italian |
| #lang:sv | Swedish |
| #lang:nl | Dutch |
| #lang:no | Norwegian |
| #lang:fi | Finnish |
| #lang:cs | Czech |
| #lang:sl | Slovenian |
| #lang:kh | Simplified Chinese |
| #lang:ch | Chinese |
| #lang:ko | Korean |

## Media Source Tags

| Tag | Description |
|-----|-------------|
| #based:movie | Based on a movie |
| #based:manganime | Based on manga/anime |
| #official:sports | Official sports license |
| #endorsed:celeb | Celebrity endorsed |
| #endorsed:company | Company/brand endorsed |

## System Port Tags

| Original System | Tag | Description |
|----------------|-----|-------------|
| Arcade | #port:arcade | Arcade port |
| Commodore | #port:c64<br>#port:amiga | Commodore 64<br>Commodore Amiga |
| Apple | #port:apple2<br>#port:mac | Apple II<br>Apple Macintosh |
| SEGA | #port:sg1000<br>#port:gamegear<br>#port:mark3<br>#port:megadrive<br>#port:saturn | SG-1000<br>Game Gear<br>Mark III / Master System<br>MegaDrive / Genesis<br>Saturn |
| Nintendo | #port:famicom<br>#port:superfamicom<br>#port:gameboy | Famicom / NES<br>Super Famicom / SNES<br>GameBoy |
| NEC | #port:pc88<br>#port:pc98<br>#port:pcengine | PC-8801<br>PC-9801<br>PC Engine |

## Re-release Collection Tags

| Publisher | Tag | Description |
|-----------|-----|-------------|
| Nintendo | #rerelease:virtualconsole<br>#rerelease:switchonline<br>#rerelease:ereader | Virtual Console (Wii/WiiU/3DS)<br>Switch Online<br>e-Reader |
| SEGA | #rerelease:segaclassic<br>#rerelease:segaages<br>#rerelease:mdclassics | SEGA Classic<br>SEGA Ages<br>MegaDrive/Genesis Classics |
| Konami | #rerelease:castlevaniaanniversary<br>#rerelease:contraanniversary | Castlevania Collection<br>Contra Collection |
| NAMCO | #rerelease:namcoanthology<br>#rerelease:namcot | NAMCO Anthology<br>NAMCOT Collection |

## Hardware Add-on Tags

### SEGA Hardware

| Tag | Description | Hidden Features |
|-----|-------------|----------------|
| #addon:bikehandle | SEGA Bike Handle | - |
| #addon:graphicboard | SEGA Graphic Board | - |
| #addon:3dglasses | SEGA 3-D Glasses | >hidden |
| #addon:fmsoundunit | SEGA FM Sound Unit | >hidden |
| #addon:lightphaser | SEGA Light Phaser | - |
| #addon:paddlecontrol | SEGA Paddle Control | - |
| #addon:sportspad | SEGA Sports Pad | - |
| #addon:6button | SEGA Six Button Control Pad | - |
| #addon:menacer | SEGA Menacer | - |
| #addon:segavr | SEGA VR Headset | - |
| #addon:megamodem | SEGA Mega Modem | - |
| #addon:megaanser | SEGA Mega Anser | - |
| #addon:mouse>md | SEGA Mouse | - |

### Nintendo Hardware

| Tag | Description | Subtype |
|-----|-------------|---------|
| #addon:rob | R.O.B. | >gyro (Gyro Set)<br>>block (Block Set) |
| #addon:zapper | Nintendo Zapper | - |
| #addon:powerglove | Power Glove | - |
| #addon:supergameboy | Super GameBoy | 1 & 2 |
| #addon:64dd | Nintendo 64DD | - |
| #addon:transferpak | Transfer Pak | - |
| #addon:rumblepak | Rumble Pak | - |
| #addon:expansionpak | Expansion Pak | - |
| #addon:keyboard | Keyboard | >fc (Famicom)<br>>n64 (Nintendo 64) |

### NEC Hardware

| Tag | Description |
|-----|-------------|
| #addon:mouse>pce | PC Engine Mouse |
| #addon:mouse>pcfx | PC-FX Mouse |
| #addon:10key | 10 Key Controller Pad |
| #addon:pcemultitap | Multitap / TurboTap |
| #addon:cdromrom | CD-ROM² / Super CD-ROM² |
| #addon:arcadecard | Arcade Card Pro/Duo |

### Storage & Memory

| Tag | Description |
|-----|-------------|
| #addon:backupramcart | Mega-CD Backup RAM Cart |
| #addon:memorybase128 | Memory Base 128 |
| #addon:controllerpak | N64 Controller Pak |
| #addon:turbofile | Turbo File Series |
| #addon:superturbofile | Super Turbo File |

### Communication Devices

| Tag | Description |
|-----|-------------|
| #addon:gamelinkcable | Game Link Cable |
| #addon:taisencable | Taisen/Gear-to-Gear Cable |
| #addon:ngplink | NeoGeo Pocket Link |
| #addon:radiounitwireless | Radio Unit Wireless |
| #addon:setsuzoku | NGP-Dreamcast Link |

### Specialized Controllers

| Tag | Description |
|-----|-------------|
| #addon:ddr | Dance Dance Revolution |
| #addon:mahjongcontroller | Mahjong Controller |
| #addon:pachinkocontroller | Pachinko Controller |
| #addon:arkanoid | Arkanoid Controller |
| #addon:justifier | The Justifier |
| #addon:gamegun | Laser GameGun |

### Audio & Visual

| Tag | Description |
|-----|-------------|
| #addon:karaokestudio | Karaoke Studio |
| #addon:pocketcamera | GameBoy Camera |
| #addon:pocketprinter | GameBoy Printer |
| #addon:printbooster | Print Booster |
| #addon:photoreader | Photo Reader |

## System Enhancement Tags

| Tag | Description |
|-----|-------------|
| #addon:megacd | SEGA Mega-CD / SEGA-CD |
| #addon:super32x | SEGA 32X |
| #addon:disksystem | Famicom Disk System |
| #addon:biosensor | Bio Sensor |
| #addon:smartmediacard | SmartMedia Card |

## Arcade Board Tags

### CAPCOM Boards

| Tag | Description |
|-----|-------------|
| #arcadeboard:capcom>cps | CAPCOM CP System |
| #arcadeboard:capcom>cpsdash | CAPCOM CP System Dash |
| #arcadeboard:capcom>cpschanger | CAPCOM CP System Changer |
| #arcadeboard:capcom>cps2 | CAPCOM CP System II |
| #arcadeboard:capcom>cps3 | CAPCOM CP System III |

### SEGA Boards

| Tag | Description |
|-----|-------------|
| #arcadeboard:sega>vco | SEGA VCO Object |
| #arcadeboard:sega>1 | SEGA System 1 |
| #arcadeboard:sega>2 | SEGA System 2 |
| #arcadeboard:sega>16 | SEGA System 16 |
| #arcadeboard:sega>16a | SEGA System 16A |
| #arcadeboard:sega>16b | SEGA System 16B |
| #arcadeboard:sega>16c | SEGA System 16C |
| #arcadeboard:sega>18 | SEGA System 18 |
| #arcadeboard:sega>24 | SEGA System 24 |
| #arcadeboard:sega>32 | SEGA System 32 |
| #arcadeboard:sega>m32 | SEGA System Multi 32 |
| #arcadeboard:sega>c | SEGA System C |
| #arcadeboard:sega>c2 | SEGA System C-2 |
| #arcadeboard:sega>e | SEGA System E |
| #arcadeboard:sega>x | SEGA X Board |
| #arcadeboard:sega>y | SEGA Y Board |
| #arcadeboard:sega>stv | SEGA Titan Video |

### IREM Boards

| Tag | Description |
|-----|-------------|
| #arcadeboard:irem>m10 | Irem M10 |
| #arcadeboard:irem>m15 | Irem M15 |
| #arcadeboard:irem>m27 | Irem M27 |
| #arcadeboard:irem>m52 | Irem M52 |
| #arcadeboard:irem>m57 | Irem M57 |
| #arcadeboard:irem>m58 | Irem M58 |
| #arcadeboard:irem>m62 | Irem M62 |
| #arcadeboard:irem>m72 | Irem M72 |
| #arcadeboard:irem>m92 | Irem M92 |
| #arcadeboard:irem>m107 | Irem M107 |

### TAITO Boards

| Tag | Description |
|-----|-------------|
| #arcadeboard:taito>xsystem | X System |
| #arcadeboard:taito>bsystem | B System |
| #arcadeboard:taito>hsystem | H System |
| #arcadeboard:taito>lsystem | L System |
| #arcadeboard:taito>zsystem | Z System |
| #arcadeboard:taito>osystem | O System |
| #arcadeboard:taito>f1 | F1/F2 System |
| #arcadeboard:taito>f2 | F2 System |
| #arcadeboard:taito>lg | LG System |

### Other Manufacturers

| Tag | Description |
|-----|-------------|
| #arcadeboard:toaplan>1 | Toaplan Version 1 |
| #arcadeboard:toaplan>2 | Toaplan Version 2 |
| #arcadeboard:snk>mvs | SNK Multi Video System |
| #arcadeboard:jaleco>ms1 | Jaleco Mega System 1 |

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
**:meganet** (Tec Toy MegaNet)
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

These tags even allow us to search for famous characters like Dracula. If we were to write "dracula" in a regular game search engine, we would only get games which contans the word _Dracula_, but there would be no _Castlevania_ or _Master of Darkness_. This tag can solve that. More tags will be added as soon new interesting franchises appeared in the process. At the end they will be a lot. For now, take a look to these ones:

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
