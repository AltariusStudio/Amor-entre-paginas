### FOR DEVELOPERS:
### If you're launching your game with renedit intact, please make sure to add the following to the TOP of your
### distribution/archiving list in options.rpy

# build.classify('game/renedit/**.txt', "all")

# This will ensure your EditingLog will not be archived, and can easily be shared. Optionally, you can archive the rest of the files
# for a cleaner distribution.
# build.classify('game/renedit/**.**', "archive")
