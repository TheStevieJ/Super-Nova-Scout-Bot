  ____                        _   _                 ____            _         _____               _             
 / ___| _   _ _ __   ___ _ __| \ | | _____   ____ _/ ___|  ___ _ __(_)_ __ __|_   _| __ __ _  ___| | _____ _ __ 
 \___ \| | | | '_ \ / _ \ '__|  \| |/ _ \ \ / / _` \___ \ / __| '__| | '_ ` _ \| || '__/ _` |/ __| |/ / _ \ '__|
  ___) | |_| | |_) |  __/ |  | |\  | (_) \ V / (_| |___) | (__| |  | | | | | | | || | | (_| | (__|   <  __/ |   
 |____/ \__,_| .__/ \___|_|  |_| \_|\___/ \_/ \__,_|____/ \___|_|  |_|_| |_| |_|_||_|  \__,_|\___|_|\_\___|_|   
             |_|                                                                                                

HOW TO SETUP:
1. Download Python 3 (https://www.python.org/downloads/).
	IMPORTANT: Be sure to check box labeled "Add Python 3.8 to PATH at frist window.
2. Make sure the SNIntern folder is unzipped.
	If downloaded from github website/other form folder should come zipped.
	If pulled from github repo folder should come unzipped.
3. Double click "Install.bat" in the main folder to install required libraries.
4. Scrim Tracker is now ready to use.

HOW TO RUN:
1. Ensure that the "Input" page of the SNInfo Google Sheet is properly filled out.
	If ProDraft is used, be sure to select "YES" in row 14 and fill out rows 15-19 accordingly.
	If ProDraft is not used, select "NO" in row 14 and continue.
	IMPORTANT: fill in the ENTIRE match history URL in cell C21, not just the ID number.
2. Double click "ScrimTracker.bat" in the main folder to run the program.
3. Once "FINISHED" is displayed in the CMD, program has finished running.

POTENTIAL ERRORS/HOW TO FIX:
1. "IndexError: list out of range": A non URL has been entered in cell C21, be sure to copy/paste the url from web browser
2. "Riot API Request Forbidden":  Either...
	A. Summoner name is inproperly entered in the "Input" page.
	B. Riot API key is out of date, contact Stephen for new key.
3. "'Some Number' match was already entered": A match of the same Match ID has already been uploaded, check "IndvMatchReport" to verify, if in error contact Stephen.

If any other issues occur, feel free to contact Stephen Through discord (Returned#6422).