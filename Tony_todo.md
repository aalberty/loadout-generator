## Tasks to delegate ##  
- function to return stat tiers given a loadout  
- function to return loadouts given a specific set of tier criteria for each stat  
	- Break down into a smaller function that looks at a single stat and determines if it fits a set of criteria  
		- Max tier, min tier, exotic allowed 

## TODO ##  
- Stub tier function for loadout  
    - 0 <= tier_value <= 10
- func to calc total
	- add_modifier: recalc total after each operation
- set_stat function
	- add_modifier: utilize the set stat function
- Generate all possible loadouts given a class' armor set  
- Obj rep of a loadout to be stored in a file  
- Armor: exotic attribute  

## Done  ##  
- Loadout class stubbed out  
- given a stat obj, perform all updates to the loadout (loop add_modifier)
