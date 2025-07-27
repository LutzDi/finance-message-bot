# STRATEGY PARAMETERS

# ********************************** SPY TIPS COOL STRATEGY **********************************
SPY_SMA = 150
TIPS_SMA = 200
COOLDOWN_DAYS = 15

# number of attempts to download data
TRY_COUNT = 3
DAILY_NOTIFICATION = True # Write True to send a daily notification, False to only send notifications when the signal changes

# main subjects
MAIN_SIGNAL_CHANGE_LONG = f"Halten (Cooldown ist aktiv seit {0} Tagen)"
MAIN_SIGNAL_CHANGE_SHORT = f"In Cash wechseln (Cooldown ist aktiv seit {0} Tagen)"
COOLDOWN_WARNINGS = [1]
COOLDOWN_WARNINGS_TEXT = ["Cooldown Warnung: Letzter Tag der Cooldown-Phase!"]

# sub subjects
INDICATOR_CHANGE_TITLE = "Einige Indikatoren haben sich geändert"
assert len(COOLDOWN_WARNINGS) == len(COOLDOWN_WARNINGS_TEXT), "COOLDOWN_WARNINGS and COOLDOWN_WARNINGS_TEXT must have the same length"

# ********************************** END SPY TIPS COOL STRATEGY **********************************






# DO NOT CHANGE THESE
BUY = "BUY"
SELL = "SELL"
HISTORY_FILENAME = "history"
