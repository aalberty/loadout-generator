- Given an input csv generated from DIM, determine possible "tier" values for each stat as calculated from combining armor pieces for every possible combination of armor pieces.   

- Give a user the ability to find a loadout that hits certain criteria  
	- Suggest the closest loadout if no loadouts fit the user defined criteria  
	- Enable the user to require a specific exotic  


## Tasks to delegate ##  
- function to return stat tiers given a loadout  
- function to return loadouts given a specific set of tier criteria for each stat  
	- Break down into a smaller function that looks at a single stat and determines if it fits a set of criteria  
		- Max tier, min tier, exotic allowed 
