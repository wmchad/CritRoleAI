import pandas as pd

def GetTranscriptDatabase(db_file):
    """Gets the transcript database.
    
    Args:
        db_file (string): the filename for the transcript database.
        
    Returns:
        A pandas DataFrame with the episode transcript information.
        Contains the following columns:
        - section_no:      the section number of the episode.
        - subsection_no:   the subsection number of the episode within the section.
        - episode_no:      the number of the episode within the subsection.
        - section:         the section name (e.g. Campaign 1: Vox Machina).
        - subsection       the subsection name (e.g. Arc 2: The Briarwoods).
        - episode          the episode name (e.g. Desperate_Measures).
        - link             the url of the episode transcript page.
        - download_date    the date that the transcript was last downloaded, or NaT if never downloaded.
        - transcript_file: the path to the downloaded and processed transcript file, relative to the base data directory.
    """
    return pd.read_csv(
        db_file,
        parse_dates = ['download_date']
    )

def GetEpisodeTranscript(transcript_file):
    """Gets an episode transcript.
    
    Args:
        transcript_file (string): the filename for the transcript of the episode.
    
    Returns:
        A pandas DataFrame with the full transcript and some calculated columns.
        Contains the following columns:
        - section_no: the section number of the line.
        - line_no:    the line number of the line within the section.
        - section:    the name of the section.
        - speaker:    the speaker of the line.
        - line:       the text of the line that was spoken.
        - linelength: the length of the line in characters.
        - nwords:     the number of words in the line.
    """
    df = pd.read_csv(transcript_file)
    df.loc[:, 'linelength'] = [len(x) for x in df['line']]
    df.loc[:, 'nwords'] = [len(x.split()) for x in df['line']]
    return df

def CollectTranscripts(transcript_df, data_dir, addl_columns = {}):
    """Collects a set of transcripts.
    
    Args:
        transcript_df (DataFrame): the episode transcripts to retrieve, with one row per transcript.
            Must include the transcript_file column, along with any specified in <addl_columns>.
        data_dir (string): the base directory for the transcript files.
        addl_columns (dictionary): a dictionary of additional fields to add to the transcript data.
            Keys are the column name in <transcript_df>, and values are the target column name in the transcript data.
            All new fields are added as the first columns of the data.
            Defaults to an empty dictionary.
        
    Returns:
        A pandas DataFrame with the data from all the transcripts.
        See [GetEpisodeTranscript] for more information.
    """

    transcripts = pd.DataFrame()
    for index, row in transcript_df.iterrows():
        episode_transcript = GetEpisodeTranscript(f'{data_dir}/{row["transcript_file"]}')
        for k, v in reversed(addl_columns.items()):
            episode_transcript.insert(0, v, row[k])
        transcripts = pd.concat([
            transcripts,
            episode_transcript
        ])
    transcripts.reset_index(inplace = True)
    transcripts.drop('index', axis = 1, inplace = True)
    return transcripts
# .rename(columns = {'subsection_no': 'arc_no', 'subsection': 'arc_name'})