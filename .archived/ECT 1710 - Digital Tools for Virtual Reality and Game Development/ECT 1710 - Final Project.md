# ECT 1710 - Final Project

Reverend Guarino

## Proposal / Disclaimer

For my final project, I took my ECT 3401 - Game Development project and implemented a stat system with upgrades in addition to making improvements to the holster system. The base project I worked off of was developed by Eric Popp and myself, but the additions I've made to I completed solo. I did have some of the stat system written prior to this project, but it was incomplete and had yet to be implemented.

## The Stat System

My stat system is made up of two primary parts, found in the Rogue namespace, the Rogue.StatBlock and the Rogue.UpgradeManager.

The Rogue.StatBlock is the base unit of the system and is used by almost every entity. It is a wrapper for a Dictionary that is made up of key/value pairs, the keys being pulled from an Enum called Rogue.StatKey, and the values being floats.

Rogue.StatKey is essentially a list of stats that appear in the game, it includes everything from Health to Damage to Speed.

Inside Rogue.StatBlock are also several helper functions such as Rogue.StatBlock.Sum which is a static function that returns the result of combining two Rogue.StatBlocks.

Rogue.UpgradeManager is the point of truth for all entities when referencing the Player.

## Stat System Usage

As mentioned previously, all entities use Rogue.StatBlock for their data. Objects controlled by the player use a pattern of base stats + player's current stats. The base stats are typically a ScriptableObject prefab that is representative of the default or starting values of an object. The player's current stats are pulled from the Rogue.UpgradeManager.

Additionally, the stats of the enemies in the game also use Rogue.StatBlock except they currently only have values for Health and Speed.

In game, the way it works is that the Player collects some number of upgrades. When they shoot a bullet, the weapon gets the sum of its base stats and the player's current stats and adds them together. It then passes that sum to the bullet as in snapshot form, this is just so bullets don't live check the player's stats every frame. On contact with an enemy, the enemy subtracts the bullet's damage value from its health value.

## The "So What"

Though the interaction described is pretty straightforward and can be completed without a generalized system, the power of the Stat System is that any features added in the future will use the same class and can be added/subtracted/etc the same way.

A good example use case would be adding an effect like bullets that slow enemies. On contact the enemy would simply subtract the negative speed value on the bullet from its speed value.

Furthermore, the system is not locked to this specific game. It could be used for any and all future RPGs, FPS, strategy games, etc.

## Additional Work

In addition to implementing the Stat System, I made several improvements to some core mechanics, specifically our holster system. Our game uses a "Reload Like Reaper" system where you throw your guns away and new ones appear at your hips.

Note: In the submitted build, the holsters are placed ahead of the player due to development with the XR Device Simulator.

Previously, we had to track what hand was holding a weapon so that we could spawn a new weapon in the appropriate holster. In this project, I made it so that when a weapon is grabbed, it creates a inactive copy of itself in the holster through my Combat.ControllerEventHandler and attaches a listener to a Unity Event named OnWeaponDestroy. When the weapon is destroyed, after a delay whose value is also using Rogue.StatBlock, it invokes that event on its OnDestroy hook. The Combat.ControllerEventHandler then triggers a new, active weapon to spawn in its corresponding holster.

This removes a lot of issues with tracking right or left hand and making sure Unity events lined up so that an object reference to the previous weapon was always available.
