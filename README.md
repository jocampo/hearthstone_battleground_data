# Hearthstone Battleground Data
I created this very simple app to parse and upload my bg data. It still has a LONG way to go for it to have a smooth workflow, but for the time being, I've stopped development on it.

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
