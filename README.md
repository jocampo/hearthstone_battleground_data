# hearthstone_battleground_data
uploads hearthstone match data to a google spreadsheet (initially anyway)

Reads from a local text file (template included) that contains battlegrounds match information. This information is later parsed and stored in a db (for now in a simple docker container) and then uploads the data into a google spreadsheet so it can be leveraged in other ways (easy graphs, simple calculations.


TODO List (eventually):
- Set up a centralized logger
- Client app that writes match data into file (look into hooking onto unity events)
- Move data dump file into s3
- Deploy db on a private instance
- Setup a chron job to process the match logs every 24h
- Deploy said service on a private instance
    - Fix less-than-happy scenarios and revert/not-commit db ops when upload fails?
    - Handle token expiring scenario
- Leverage stats. Generate insights from data stored
    - Win-rate per hero
    - Look into comments for comps with best results
- Add minion types per game (once data input is automated)
- Fix some bugs <_<
