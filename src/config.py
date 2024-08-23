# base data directory (from root)
data_dir = 'data'
# name of the transcript database csv file
db_file  = 'transcript_database.csv'

# info about the primary cast members
cast = {
    'MATT':     {'name': 'Matthew Mercer',    'speakerno': 0, 'color': '#9f6701'}, #brown
    'LAURA':    {'name': 'Laura Bailey',      'speakerno': 1, 'color': '#209bc7'}, #cerulean blue
    'SAM':      {'name': 'Sam Riegel',        'speakerno': 2, 'color': '#971287'}, #royal purple
    'MARISHA':  {'name': 'Marisha Ray',       'speakerno': 3, 'color': '#228B22'}, #forest green
    'TRAVIS':   {'name': 'Travis Willingham', 'speakerno': 4, 'color': '#bcbcbc'}, #grey
    'TALIESIN': {'name': 'Taliesin Jaffe',    'speakerno': 5, 'color': '#2020a0'}, #navy blue
    'LIAM':     {'name': "Liam O'Brien",      'speakerno': 6, 'color': '#333333'}, #charcoal
    'ASHLEY':   {'name': 'Ashley Johnson',    'speakerno': 7, 'color': '#ffd700'}, #gold
}

# sections of the show that have role-playing
rp_sections = ['Part I', 'Part II']

# episodes to remove (not actual episodes)
episodes_to_remove = [
    {'campaign_no': 1, 'arc_no': 1, 'episode_no': 12}
]

# colors to use for campaigns
campaign_colors = {
    'background': ['#59627d', '#5d7a5f', '#7d5959'],
    'color':      ['#1037ad', '#0ca816', '#ab1515']
}

# colors to use for arcs within campaigns (each sublist is a separate campaign)
arc_colors = [
    ['#bfb5b2', '#83b58e', '#5e3c58', '#ba9a74', '#2e4045']
]