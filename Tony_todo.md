## Tasks to delegate ##  
- function to return stat tiers given a loadout  
- function to return loadouts given a specific set of tier criteria for each stat  
	- Break down into a smaller function that looks at a single stat and determines if it fits a set of criteria  
		- Max tier, min tier, exotic allowed 

## TODO ##  

- add_modifier function: perform the addition on the total as well
- given a list of armor pieces, calculate the stat values, totals, and tiers
- Generate all possible loadouts given a class' armor set  
- Obj rep of a loadout to be stored in a file  
- Armor: exotic attribute  
- Set up tests for test driven development for Sif's pieces

## Done  ##  
- Loadout class stubbed out  
- given a stat obj, perform all updates to the loadout (loop add_modifier)
- Stub tier function for loadout  
    - 0 <= tier_value <= 10
