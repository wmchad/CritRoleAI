def BuildCampaignDatabase(
    transcript_db,
    drop_cols = [],
    remove_episodes = []
):
    """Builds the campaign database.
    
    Args:
        transcript_db (DataFrame): the episode transcripts database (from [GetTranscriptDatabase]).
        drop_cols (string[]): a list of columns to drop from the transcript data. Defaults to an empty list.
        remove_episodes (list): a list of episodes to remove.
            Each entry in the list must be a dictionary with the following keys:
                - campaign_no: the campaign number of the episode to remove
                - arc_no: the arc number of the episode to remove
                - episode_no: the episode number of the episode to remove
            Defaults to an empty list.
        
    Returns:
        A pandas DataFrame with only entries for the campaigns.
        Renames columns to use campaign/arc rather than section/subsection.
        Cleans up the 'episode' column by replacing underscores ('_') with spaces.
        Adds an 'episode_index' column that orders the episodes sequentially.
        Adds an 'episode_label' column as a shorthand readable identifier in the format <campaign_no>-<arc_no>-<episode_no>.
    """
    campaign_db = transcript_db \
    .loc[transcript_db['section_no'].isin([1, 2, 3])] \
    .drop(drop_cols, axis = 1) \
    .rename(columns = {
        'section_no': 'campaign_no',
        'section': 'campaign',
        'subsection_no': 'arc_no',
        'subsection': 'arc'
    })
    for x in remove_episodes:
        campaign_db = campaign_db.loc[
            ~((campaign_db['campaign_no'] == x['campaign_no']) &
            (campaign_db['arc_no'] == x['arc_no']) &
            (campaign_db['episode_no'] == x['episode_no'])),
            :]
    campaign_db['episode'] = [x.replace('_', ' ') for x in campaign_db['episode']]
    campaign_db['episode_index'] = (
        campaign_db['campaign_no'] * 1000 +
        campaign_db['arc_no'] * 100 +
        campaign_db['episode_no']
    ).rank(method = 'dense')
    campaign_db['episode_label'] = campaign_db['campaign_no'].astype(str) + \
        '-' + campaign_db['arc_no'].astype(str) + \
        '-' + campaign_db['episode_no'].apply('{:02d}'.format)
    return campaign_db

