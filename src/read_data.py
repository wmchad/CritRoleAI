import pandas as pd

GetTranscriptDatabase(db_file):
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

def GetEpisodeTranscript(arc_no, ep_no, transcript_file):
    """Gets an episode transcript.
    
    Args:
        arc_no (int):             the arc number of the episode.
        ep_no (int):              the episode number of the episode within the arc.
        transcript_file (string): the filename for the transcript of the episode.
    
    Returns:
        A pandas DataFrame with the full transcript and some calculated columns.
        Contains the following columns:
        - arc_no:     the arc number of the episode.
        - episode_no: the episode number of the episode within the arc.
        - section_no: the section number of the line.
        - line_no:    the line number of the line within the section.
        - section:    the name of the section.
        - speaker:    the speaker of the line.
        - line:       the text of the line that was spoken.
        - linelength: the length of the line in characters.
        - nwords:     the number of words in the line.
    """
    df = pd.read_csv(transcript_file)
    df.insert(0, 'arc_no', arc_no)
    df.insert(1, 'episode_no', ep_no)
    df.loc[:, 'linelength'] = [len(x) for x in df['line']]
    df.loc[:, 'nwords'] = [len(x.split()) for x in df['line']]
    return df

# .rename(columns = {'subsection_no': 'arc_no', 'subsection': 'arc_name'})